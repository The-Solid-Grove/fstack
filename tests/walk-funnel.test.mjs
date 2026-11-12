import assert from 'node:assert/strict';
import { test } from 'node:test';
import { parseArgs, selectAnswers, screenshotName, decideAction, finalizeReport } from '../skills/qa-funnel/scripts/walk-funnel.mjs';

test('CLI defaults, validation, and payment implication', () => {
  const args = ['http://localhost:3000', '--dir', '.', '--out', 'artifacts'];
  const options = parseArgs(args);
  assert.deepEqual(options.viewport, { width: 375, height: 667 });
  assert.equal(options.until, 'paywall');
  assert.equal(parseArgs([...args, '--pay-test-card']).checkout, true);
  for (const extra of [['--viewport', '0x20'], ['--max-screens', '-1'], ['--until', 'unknown'], ['--oops']]) {
    assert.throws(() => parseArgs([...args, ...extra]));
  }
  assert.throws(() => parseArgs(['file:///tmp/test', '--dir', '.', '--out', '.']));
  assert.throws(() => parseArgs(['http://localhost']));
  assert.equal(parseArgs(['--help']).help, true);
});

test('answer labels, zero-based indices, defaults and multi-select', () => {
  const options = [{ label: 'One' }, { label: 'Two' }, { label: 'Three' }];
  assert.deepEqual(selectAnswers(options, 'first', 'q', true), options.slice(0, 2));
  assert.deepEqual(selectAnswers(options, 'last'), [options[2]]);
  assert.deepEqual(selectAnswers(options, { q: ['Three', 0] }, 'q', true), [options[2], options[0]]);
  assert.throws(() => selectAnswers(options, { q: 9 }, 'q'));
  assert.throws(() => selectAnswers(options, { q: [0, 1] }, 'q'));
  assert.equal(screenshotName(1, '/hello/../../world'), '01-hello-world.png');
  assert.equal(screenshotName(12, 'offer', '-full'), '12-offer-full.png');
});

test('action priority, modal options, primary preference and loaders', () => {
  const next = { id: 9, type: 'button', enabled: true, label: 'Continue', actionArea: true };
  const back = { id: 10, type: 'button', enabled: true, label: 'Back' };
  const option = { id: 2, type: 'radio', enabled: true, option: true, label: 'One' };
  const email = { id: 1, type: 'email', enabled: true };
  const required = { id: 3, type: 'number', required: true, enabled: true };
  const decide = controls => decideAction({ stepId: 'q', controls });
  assert.equal(decide([email, required, option, next]).rule, 'email');
  assert.equal(decide([required, option, next]).rule, 'required-inputs');
  assert.equal(decide([{ ...option, dialog: true }, next]).rule, 'dialog-options');
  assert.equal(decide([option, next]).rule, 'options');
  assert.equal(decide([next, back]).button.id, 9);
  assert.equal(decide([{ ...next, enabled: false }]).rule, 'loader');
  assert.equal(decide([]).rule, 'end');
  // A localized icon-only back button is never the primary action.
  const iconBack = { id: 10, type: 'button', label: 'Atgal', glyph: '←', enabled: true };
  assert.equal(decide([iconBack]).rule, 'loader');
  assert.equal(decide([iconBack, next]).button.id, 9);
});

test('only a reached stop condition without stuck screens or page errors succeeds', () => {
  const base = { until: 'end', screens: [{ consoleErrors: ['logged'], requests: [{ status: 500 }] }], pageErrors: [] };
  for (const reason of ['end', 'paywall', 'max-screens']) assert.equal(finalizeReport(base, reason, 'offer').exitCode, 0);
  assert.equal(finalizeReport(base, 'stuck', 'q').ok, false);
  assert.equal(finalizeReport({ ...base, until: 'paywall' }, 'max-screens', 'q').ok, false);
  assert.equal(finalizeReport({ ...base, pageErrors: ['uncaught'] }, 'paywall', 'offer').ok, false);
  assert.equal(finalizeReport({ ...base, screens: [{ status: 'stuck' }] }, 'end', 'q').ok, false);
});

import { createServer } from 'node:http';
import { mkdtemp, readFile, rm, symlink } from 'node:fs/promises';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadPlaywright, testPaymentAllowed } from '../skills/qa-funnel/scripts/walk-funnel.mjs';
const script = fileURLToPath(new URL('../skills/qa-funnel/scripts/walk-funnel.mjs', import.meta.url));

test('payment guard uses the current host or visible test mode', () => {
  assert.equal(testPaymentAllowed('https://example.com/?preview=1', 'Live checkout'), false);
  assert.equal(testPaymentAllowed('http://localhost:3000', ''), true);
  assert.equal(testPaymentAllowed('https://preview.example.com', ''), true);
  assert.equal(testPaymentAllowed('https://example.com', 'Test mode'), true);
});

test('CLI help and missing dependency guidance', async () => {
  const { stdout } = await promisify(execFile)(process.execPath, [script, '--help']);
  assert.match(stdout, /--pay-test-card/);
  const root = await mkdtemp(path.join(os.tmpdir(), 'walk-missing-'));
  try {
    const alias = path.join(root, 'installed-walker.mjs');
    await symlink(script, alias);
    const linked = await promisify(execFile)(process.execPath, [alias, '--help']);
    assert.match(linked.stdout, /Usage: node/);
    await assert.rejects(promisify(execFile)(process.execPath, [script, 'http://localhost', '--dir', root, '--out', root, '--json']), error => {
      assert.match(error.stderr, /npm install.*npx playwright install chromium/s);
      assert.equal(JSON.parse(error.stdout).ok, false);
      return true;
    });
  } finally { await rm(root, { recursive: true, force: true }); }
});

test('offline browser walk captures options, inputs, modal, loader, paywall, checkout and failures', async t => {
  const directory = process.env.WALK_FUNNEL_PLAYWRIGHT_DIR ?? process.cwd();
  let playwright;
  try { playwright = loadPlaywright(directory); }
  catch { t.skip('Playwright unavailable; set WALK_FUNNEL_PLAYWRIGHT_DIR to a funnel folder to enable.'); return; }
  try { const browser = await playwright.chromium.launch(); await browser.close(); }
  catch { t.skip('Chromium unavailable; run npx playwright install chromium.'); return; }
  const html = await readFile(new URL('./fixtures/walk-funnel/index.html', import.meta.url));
  const server = createServer((req, res) => {
    if (req.url.startsWith('/failure')) { res.writeHead(503); res.end('fixture error'); }
    else { res.setHeader('content-type', 'text/html'); res.end(html); }
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const root = await mkdtemp(path.join(os.tmpdir(), 'walk-fixture-'));
  const url = `http://127.0.0.1:${server.address().port}`;
  async function run(name, flags = []) {
    const out = path.join(root, name);
    let result;
    try { result = await promisify(execFile)(process.execPath, [script, `${url}/?mode=${name}`, '--dir', directory, '--out', out, '--screen-timeout', '2500', '--json', ...flags]); }
    catch (error) { result = error; }
    const report = JSON.parse(result.stdout);
    assert.deepEqual(JSON.parse(await readFile(path.join(out, 'report.json'), 'utf8')), report);
    return { report, out };
  }
  try {
    const { report, out } = await run('normal', ['--checkout']);
    assert.equal(report.ok, true, JSON.stringify(report));
    assert.deepEqual(report.screens.map(s => s.stepId), ['choice', 'multi', 'email', 'details', 'sheet', 'loader', 'offer']);
    assert.deepEqual(report.screens.slice(0, 5).map(s => s.rule), ['options', 'options', 'email', 'required-inputs', 'dialog-options']);
    assert.equal(report.screens[5].rule, 'loader→primary');
    const offer = report.screens.at(-1);
    assert.equal(offer.paywall.stickyBarVisible, true);
    assert.equal(offer.paywall.planOptionCount, 3);
    assert.deepEqual(offer.paywall.planOptions, ['Monthly', 'Quarterly', 'Annual']);
    assert.equal(offer.screenshots.length, 2);
    for (const s of report.screens) for (const name of s.screenshots) assert.ok((await readFile(path.join(out, name))).length > 100);
    assert.ok((await readFile(path.join(out, offer.checkout.screenshot))).length > 100);
    assert.ok(report.screens.some(s => s.consoleErrors.includes('fixture console error')));
    assert.ok(report.screens.some(s => s.requests.some(r => r.status === 503)));
    const stuck = (await run('stuck')).report;
    assert.equal(stuck.reason, 'stuck'); assert.equal(stuck.ok, false);
    const error = (await run('pageerror')).report;
    assert.equal(error.reason, 'paywall'); assert.equal(error.ok, false);
    assert.ok(error.pageErrors.some(e => e.includes('fixture uncaught')));
    assert.equal((await run('end', ['--until', 'end'])).report.reason, 'end');
    assert.equal((await run('limit', ['--max-screens', '1'])).report.reason, 'max-screens');
    const payment = (await run('payment', ['--pay-test-card'])).report;
    assert.equal(payment.ok, true, JSON.stringify(payment));
    assert.equal(payment.screens.at(-1).checkout.destination.stepId, '/done');
  } finally {
    server.closeAllConnections();
    await new Promise(resolve => server.close(resolve));
    await rm(root, { recursive: true, force: true });
  }
});
