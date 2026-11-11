#!/usr/bin/env node
import { createRequire } from 'node:module';
import { mkdir, readFile, realpath, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

export const usage = `Usage: node skills/qa-funnel/scripts/walk-funnel.mjs <url> --dir <funnel-folder> --out <dir>
     [--viewport 375x667] [--until paywall|end] [--answers first|last|<file.json>]
     [--email <address>] [--checkout] [--pay-test-card] [--max-screens 80]
     [--screen-timeout 45000] [--json]

Answer-file indices are zero-based. --pay-test-card implies --checkout.
`;

export function parseArgs(args) {
  if (args.includes('--help') || args.includes('-h')) return { help: true };
  const options = { viewport: '375x667', until: 'paywall', answers: 'first',
    email: `qa+walk${Date.now()}@example.com`, 'max-screens': '80', 'screen-timeout': '45000' };
  const values = new Set(['dir', 'out', 'viewport', 'until', 'answers', 'email', 'max-screens', 'screen-timeout']);
  const flags = new Set(['checkout', 'pay-test-card', 'json']);
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    const key = arg.slice(2);
    if (arg.startsWith('--') && flags.has(key)) options[key] = true;
    else if (arg.startsWith('--') && values.has(key) && args[i + 1] && !args[i + 1].startsWith('--')) options[key] = args[++i];
    else if (!arg.startsWith('-') && !options.url) options.url = arg;
    else throw new Error(`Unknown argument or missing value: ${arg}`);
  }
  for (const key of ['url', 'dir', 'out']) if (!options[key]) throw new Error(`${key === 'url' ? '<url>' : `--${key}`} is required.`);
  const url = new URL(options.url);
  if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password) throw new Error('Use an HTTP(S) URL without credentials.');
  if (!/^\d+x\d+$/.test(options.viewport)) throw new Error('--viewport must be WIDTHxHEIGHT.');
  const [width, height] = options.viewport.split('x').map(Number);
  if (!width || !height) throw new Error('Viewport dimensions must be positive.');
  options.viewport = { width, height };
  for (const key of ['max-screens', 'screen-timeout']) {
    if (!/^\d+$/.test(options[key]) || !Number.isSafeInteger(Number(options[key])) || Number(options[key]) < 1) throw new Error(`--${key} must be a positive integer.`);
    options[key] = Number(options[key]);
  }
  if (!['paywall', 'end'].includes(options.until)) throw new Error('--until must be paywall or end.');
  if (options['pay-test-card']) options.checkout = true;
  return options;
}

export function selectAnswers(options, answers = 'first', stepId = '', multi = false) {
  if (!options.length) return [];
  const choice = typeof answers === 'object' ? answers[stepId] ?? 'first' : answers;
  if (choice === 'first' || choice === 'last') {
    const ordered = choice === 'last' ? [...options].reverse() : options;
    return ordered.slice(0, multi ? 2 : 1);
  }
  const chosen = (Array.isArray(choice) ? choice : [choice]).map(value => {
    const option = typeof value === 'number' && Number.isInteger(value) ? options[value]
      : options.find(item => item.label === value);
    if (!option) throw new Error(`Answer for ${stepId} does not match an option: ${value}`);
    return option;
  });
  if (!multi && chosen.length > 1) throw new Error(`Multiple answers supplied for single-select step ${stepId}.`);
  return [...new Set(chosen)];
}

export function screenshotName(index, stepId, suffix = '') {
  const slug = String(stepId).replace(/[^a-zA-Z0-9_-]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 100) || 'screen';
  return `${String(index).padStart(2, '0')}-${slug}${suffix}.png`;
}

const secondary = /^(back|go back|close|skip|dismiss|cancel)(\b|$)/i;
function primaryButton(controls) {
  const buttons = controls.filter(c => c.type === 'button' && c.enabled && !c.option);
  const preferred = buttons.filter(c => !secondary.test(c.label));
  const candidates = preferred;
  return candidates.filter(c => c.actionArea).at(-1) ?? candidates.at(-1);
}

export function decideAction(screen, answers = 'first') {
  const controls = screen.controls ?? [];
  const enabled = controls.filter(c => c.enabled);
  const email = enabled.find(c => c.type === 'email');
  const required = enabled.filter(c => c.required && ['text', 'number'].includes(c.type));
  if (email) return { rule: 'email', inputs: [email, ...required], button: primaryButton(controls) };
  if (required.length) return { rule: 'required-inputs', inputs: required, button: primaryButton(controls) };
  const modal = enabled.filter(c => c.dialog && c.option);
  const options = modal.length ? modal : enabled.filter(c => c.option);
  if (options.length) {
    const multi = options.some(c => c.type === 'checkbox');
    return { rule: modal.length ? 'dialog-options' : 'options',
      options: selectAnswers(options, answers, screen.stepId, multi), button: primaryButton(controls), multi };
  }
  const button = primaryButton(controls);
  if (button) return { rule: 'primary', button };
  return { rule: controls.some(c => c.type === 'button') ? 'loader' : 'end' };
}

export function finalizeReport(report, reason, stoppedAt) {
  const ok = (['paywall', 'end'].includes(reason) || (reason === 'max-screens' && report.until === 'end'))
    && !report.screens.some(s => s.status === 'stuck') && !(report.pageErrors ?? []).length;
  return { ...report, ok, stoppedAt, reason, exitCode: ok ? 0 : 1 };
}

export function loadPlaywright(directory) {
  try { return createRequire(path.join(path.resolve(directory), 'package.json'))('playwright'); }
  catch { throw new Error(`Playwright is missing. Run npm install in ${path.resolve(directory)}, then npx playwright install chromium there.`); }
}

// This function runs in the browser; return only serialisable observations.
async function describe(page) {
  return page.evaluate(() => {
    const visible = el => !!el.getClientRects().length && getComputedStyle(el).visibility !== 'hidden' && getComputedStyle(el).display !== 'none';
    const step = [...document.querySelectorAll('[data-step-id]')].find(visible);
    const root = step ?? document.body;
    const dialog = [...document.querySelectorAll('[role=dialog],dialog[open]')].find(visible);
    const scope = dialog ?? root;
    document.querySelectorAll('[data-walk-control]').forEach(el => el.removeAttribute('data-walk-control'));
    const elements = [...scope.querySelectorAll('input,textarea,button,[role=button],[role=radio],[role=checkbox]')].filter(visible);
    const controls = elements.map((el, i) => {
      el.setAttribute('data-walk-control', String(i));
      const role = el.getAttribute('role');
      const type = ['radio', 'checkbox'].includes(role) ? role : el.tagName === 'INPUT' ? el.type : el.tagName === 'TEXTAREA' ? 'text' : 'button';
      const option = ['radio', 'checkbox'].includes(type)
        || (type === 'button' && (!!el.closest('[role=radiogroup],[role=group]') || el.hasAttribute('aria-checked') || el.hasAttribute('aria-pressed')));
      return { id: i, type, option, label: (el.getAttribute('aria-label') || el.innerText || el.labels?.[0]?.innerText || '').trim(),
        enabled: !el.matches(':disabled') && el.getAttribute('aria-disabled') !== 'true', required: el.required || el.getAttribute('aria-required') === 'true',
        checked: el.checked || el.getAttribute('aria-checked') === 'true', dialog: !!dialog,
        actionArea: !!el.closest('footer,[data-action-area],.actions,.action-area,.funnel-actions') };
    });
    return { stepId: step?.getAttribute('data-step-id') || location.pathname, pathname: location.pathname,
      kind: step?.closest('.funnel-shell')?.getAttribute('data-step-kind') ?? null,
      heading: [...root.querySelectorAll('h1,h2,h3,h4,h5,h6,[role=heading]')].find(visible)?.innerText?.trim() ?? '', controls };
  });
}
const changed = (a, b) => a.stepId !== b.stepId || a.pathname !== b.pathname;
const idle = rule => rule === 'loader' || rule === 'end';
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
async function waitFor(page, predicate, timeout) {
  const deadline = Date.now() + timeout;
  do {
    // A redirect (e.g. the checkout return URL) destroys the context mid-evaluate: keep polling.
    const state = await describe(page).catch(() => null);
    if (state && predicate(state)) return state;
    await pause(state ? 100 : 500);
  } while (Date.now() < deadline);
  return null;
}
function control(page, item) { return page.locator(`[data-walk-control="${item.id}"]`).filter({ visible: true }).first(); }
async function act(page, state, action, options) {
  for (const input of action.inputs ?? []) await control(page, input).fill(input.type === 'email' ? options.email : input.type === 'number' ? '30' : 'Test');
  for (const option of action.options ?? []) {
    if (!option.checked) await control(page, option).click();
    if (changed(state, await describe(page))) return;
  }
  // Selection can enable Continue or close a sheet without changing the step.
  const current = await waitFor(page, next => changed(state, next) || !!primaryButton(next.controls), options['screen-timeout']);
  if (!current || changed(state, current)) return;
  const button = primaryButton(current.controls);
  if (button) await control(page, button).click();
}

async function paywallDetails(page) {
  return page.evaluate(async () => {
    const scrollers = [document.scrollingElement, ...document.querySelectorAll('*')].filter(el => el && el.scrollHeight > el.clientHeight + 4
      && (el === document.scrollingElement || /auto|scroll/.test(getComputedStyle(el).overflowY)));
    const positions = scrollers.map(el => el.scrollTop);
    for (const el of scrollers) el.scrollTop = el.scrollHeight;
    await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    const visible = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth && getComputedStyle(el).visibility !== 'hidden'; };
    const sticky = [...document.querySelectorAll('*')].find(el => ['sticky', 'fixed'].includes(getComputedStyle(el).position) && visible(el));
    const plans = [...document.querySelectorAll('[role=radio]')];
    const result = { stickyBarVisible: !!sticky, stickyBarText: sticky ? sticky.innerText.replace(/\s+/g, ' ').trim().slice(0, 120) : null,
      pageScrolls: scrollers.some(el => el.scrollTop > 0), planOptionCount: plans.length,
      planOptions: plans.slice(0, 3).map(el => (el.innerText || el.getAttribute('aria-label') || '').trim()) };
    scrollers.forEach((el, i) => { el.scrollTop = positions[i]; });
    return result;
  });
}

export function testPaymentAllowed(url, visibleText) {
  const host = new URL(url).hostname;
  return host === 'localhost' || host === '127.0.0.1' || host === '[::1]' || host.includes('preview') || /\btest mode\b/i.test(visibleText);
}
async function checkout(page, state, options, record) {
  if (options['pay-test-card'] && !testPaymentAllowed(page.url(), await page.locator('body').innerText())) throw new Error('Refusing test card: page must show test mode or use localhost/a preview host.');
  const purchase = await page.evaluate(() => {
    const group = document.querySelector('[role=radiogroup]');
    if (!group) return false;
    for (const el of document.querySelectorAll('button,[role=button]')) {
      if (!(group.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING) || group.contains(el) || el.matches(':disabled') || el.getAttribute('aria-disabled') === 'true' || !el.getClientRects().length || getComputedStyle(el).visibility === 'hidden') continue;
      let sticky = false;
      for (let p = el; p; p = p.parentElement) if (['sticky', 'fixed'].includes(getComputedStyle(p).position)) sticky = true;
      if (!sticky && !/^(back|close|skip|cancel)\b/i.test(el.innerText.trim())) { el.setAttribute('data-walk-purchase', 'true'); return true; }
    }
    return false;
  });
  if (!purchase) throw new Error('No enabled non-sticky purchase button after the plan radiogroup.');
  await page.locator('[data-walk-purchase=true]').click();
  const dialog = page.locator('[role=dialog],dialog[open]').filter({ visible: true }).first();
  await dialog.waitFor({ timeout: options['screen-timeout'] });
  record.checkout = { screenshot: screenshotName(record.index, state.stepId, '-checkout') };
  await page.screenshot({ path: path.join(options.out, record.checkout.screenshot) });
  if (!options['pay-test-card']) return;
  // The card method opens only once the dialog has finished opening and its session is ready:
  // tap it until its submit button is no longer inside a collapsed (aria-hidden) block.
  const card = dialog.locator('button, [role=radio]').filter({ hasText: /card/i })
    .or(dialog.locator('button[aria-label*="card" i], [role=radio][aria-label*="card" i]')).first();
  const cardOpen = () => dialog.evaluate(el => [...el.querySelectorAll('button[type=submit]')]
    .some(b => b.getClientRects().length && !b.closest('[aria-hidden=true]')));
  const cardDeadline = Date.now() + options['screen-timeout'];
  while (await card.isVisible() && !await cardOpen() && Date.now() < cardDeadline) {
    await card.click().catch(() => {});
    await pause(1000);
  }
  const fields = { number: '4242424242424242', expiry: '12/34', cvc: '123' };
  for (const [name, value] of Object.entries(fields)) {
    const deadline = Date.now() + options['screen-timeout'];
    let filled = false;
    while (!filled && Date.now() < deadline) {
      for (const frame of page.frames().filter(f => f !== page.mainFrame())) {
        const input = frame.locator(`input[name="${name}"]`).first();
        if (await input.isVisible()) { await input.fill(value); filled = true; break; }
      }
      if (!filled) await pause(100);
    }
    if (!filled) throw new Error(`Stripe card field ${name} was not found.`);
  }
  for (const frame of page.frames()) {
    const postal = frame.locator('input[name=postalCode],input[name=postal],input[name=postal_code]').first();
    if (await postal.isVisible()) await postal.fill('10001');
  }
  const submit = dialog.locator('button[type=submit]').filter({ visible: true }).last();
  await (await submit.count() ? submit : dialog.getByRole('button', { name: /^(pay|subscribe|start|confirm|purchase)/i }).last()).click();
  const destination = await waitFor(page, next => changed(state, next), 90000);
  if (!destination) throw new Error('Test payment did not leave the paywall within 90 seconds.');
  record.checkout.destination = { stepId: destination.stepId, pathname: destination.pathname, url: page.url() };
}

export async function walk(options) {
  await mkdir(options.out, { recursive: true });
  const report = { url: options.url, until: options.until, viewport: options.viewport, screens: [], pageErrors: [] };
  let browser, reason = 'error', stoppedAt = null;
  const pending = { consoleErrors: [], requests: [], pageErrors: [] };
  const drain = record => { for (const key of Object.keys(pending)) record[key].push(...pending[key].splice(0)); };
  try {
    let answers = options.answers;
    if (!['first', 'last'].includes(answers)) {
      answers = JSON.parse(await readFile(answers, 'utf8'));
      if (!answers || typeof answers !== 'object' || Array.isArray(answers)) throw new Error('Answer file must map step ids to labels or zero-based indices.');
    }
    const playwright = loadPlaywright(options.dir);
    try { browser = await playwright.chromium.launch({ headless: true }); }
    catch (error) { throw new Error(`Cannot launch Chromium. Run npx playwright install chromium in ${path.resolve(options.dir)}. ${error.message}`); }
    const page = await browser.newPage({ viewport: options.viewport, deviceScaleFactor: 2, isMobile: true, hasTouch: true,
      userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' });
    page.setDefaultTimeout(options['screen-timeout']);
    page.on('console', msg => { if (msg.type() === 'error') pending.consoleErrors.push(msg.text()); });
    page.on('pageerror', error => { report.pageErrors.push(error.message); pending.pageErrors.push(error.message); });
    page.on('requestfailed', request => pending.requests.push({ url: request.url(), error: request.failure()?.errorText }));
    page.on('response', response => { if (response.status() >= 400) pending.requests.push({ url: response.url(), status: response.status() }); });
    await page.goto(options.url, { waitUntil: 'domcontentloaded' });
    for (let index = 1; index <= options['max-screens']; index++) {
      const started = Date.now();
      reason = 'max-screens';
      await pause(250);
      const state = await describe(page);
      stoppedAt = state.stepId;
      const record = { index, stepId: state.stepId, pathname: state.pathname, heading: state.heading, kind: state.kind,
        rule: 'stop', status: 'visited', ms: 0, consoleErrors: [], requests: [], pageErrors: [], screenshots: [] };
      report.screens.push(record);
      const capture = async suffix => {
        const name = screenshotName(index, state.stepId, suffix);
        await page.screenshot({ path: path.join(options.out, name), fullPage: suffix === '-full' });
        record.screenshots.push(name);
      };
      try {
        await capture('');
        if (state.kind === 'paywall') {
          await capture('-full');
          record.paywall = await paywallDetails(page);
          if (options.checkout) { record.rule = options['pay-test-card'] ? 'pay-test-card' : 'checkout'; await checkout(page, state, options, record); }
          if (options.until === 'paywall') { reason = 'paywall'; break; }
          if (record.checkout?.destination) continue;
          if (options.checkout) await page.locator('[role=dialog],dialog[open]').filter({ visible: true }).first().getByRole('button', { name: /close/i }).click();
        }
        const deadline = Date.now() + options['screen-timeout'];
        const remaining = () => Math.max(1, deadline - Date.now());
        let action = decideAction(state, answers);
        record.rule = action.rule;
        if (idle(action.rule)) {
          // Nothing to press yet: a loader, a screen that advances by itself, or a page still rendering.
          const patience = action.rule === 'end' ? Math.min(remaining(), 20000) : remaining();
          const ready = await waitFor(page, next => changed(state, next) || !idle(decideAction(next, answers).rule), patience);
          if (!ready) {
            reason = action.rule === 'end' && options.until === 'end' ? 'end' : 'stuck';
            if (reason === 'stuck') record.status = 'stuck';
            break;
          }
          if (changed(state, ready)) { record.rule = 'auto-advance'; continue; }
          action = decideAction(ready, answers);
          record.rule = `${record.rule === 'end' ? 'wait' : 'loader'}→${action.rule}`;
        }
        await act(page, state, action, { ...options, 'screen-timeout': remaining() });
        if (!await waitFor(page, next => changed(state, next), remaining())) {
          record.status = 'stuck'; reason = 'stuck'; break;
        }
        reason = 'max-screens';
      } catch (error) {
        record.status = 'stuck';
        record.error = error.message;
        report.error = error.message;
        reason = 'stuck';
        break;
      } finally { record.ms = Date.now() - started; drain(record); }
    }
  } catch (error) { report.error = error.message; reason = 'error'; }
  finally {
    if (browser) await browser.close();
    if (report.screens.length) drain(report.screens.at(-1));
    else Object.assign(report, { consoleErrors: pending.consoleErrors, requests: pending.requests });
  }
  const result = finalizeReport(report, reason, stoppedAt);
  await writeFile(path.join(options.out, 'report.json'), `${JSON.stringify(result, null, 2)}\n`);
  return result;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) { process.stdout.write(usage); return; }
  const report = await walk(options);
  if (options.json) process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
  else {
    console.log(' #  step id                      rule                 ms  errors');
    for (const s of report.screens) console.log(`${String(s.index).padStart(2)}  ${s.stepId.padEnd(28)} ${s.rule.padEnd(20)} ${String(s.ms).padStart(6)}  ${s.consoleErrors.length + s.requests.length + s.pageErrors.length}`);
    console.log(`${report.ok ? 'OK' : 'FAIL'}: ${report.reason} (${report.stoppedAt ?? 'before first screen'})`);
  }
  if (report.error) console.error(`walk-funnel: ${report.error}`);
  process.exitCode = report.exitCode;
}
if (process.argv[1] && import.meta.url === pathToFileURL(await realpath(process.argv[1])).href) {
  main().catch(error => { console.error(`walk-funnel: ${error.message}`); process.exitCode = 1; });
}
