#!/usr/bin/env node
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

const usage = `Usage: node skills/writing-funnel-copy/scripts/reference-strip.mjs <funnel-id> [<funnel-id> ...]
       node skills/writing-funnel-copy/scripts/reference-strip.mjs --file journey.json

Print the rhythm strip of a recorded Funnel Screens journey.

Reads \`fgrove references show <funnel-id> --json\` (public, no login) or a saved
response, then prints the strip (Q question, E energy, P result/plan, L loading,
@ email, $ paywall), its pacing stats and one line per screen. The mapping is a
first pass from the library's recorded screen kinds: read the screens to tell a
profile mirror (M) from a plan reveal (P) before using the strip in an arc.
`;

const CODES = {
  'single-choice': 'Q', 'multi-choice': 'Q', 'image-choice': 'Q', scale: 'Q',
  'text-input': 'Q', 'first-step': 'Q', information: 'E', 'social-proof': 'E',
  result: 'P', loading: 'L', email: '@', paywall: '$', checkout: '$',
};
const ENERGY = new Set(['E', 'P', 'M']);

function fail(message) {
  process.stderr.write(`${message}\n`);
  process.exit(2);
}

function load(funnelId, file) {
  let data;
  if (file) {
    data = JSON.parse(readFileSync(file, 'utf8'));
  } else {
    // On Windows the npm-installed CLI is fgrove.cmd, which only a shell can start.
    if (!/^[\w.-]+$/.test(funnelId)) fail(`invalid funnel ID: ${funnelId}`);
    const result = spawnSync('fgrove', ['references', 'show', funnelId, '--json'], {
      encoding: 'utf8',
      shell: process.platform === 'win32',
      maxBuffer: 64 * 1024 * 1024,
    });
    if (result.error || result.status !== 0) {
      fail(`fgrove references show ${funnelId} failed: ${(result.stderr || result.error?.message || '').trim()}`);
    }
    data = JSON.parse(result.stdout);
  }
  return data.funnel ?? data;
}

function summarize(funnel) {
  const steps = funnel.steps ?? [];
  const codes = steps.map((step) => CODES[step.screenType ?? ''] ?? '?');
  const paywall = codes.indexOf('$');
  const body = paywall >= 0 ? codes.slice(0, paywall) : codes;
  const energy = body.filter((code) => ENERGY.has(code)).length;
  let run = 0;
  let longest = 0;
  let firstEnergy = null;
  body.forEach((code, index) => {
    if (code === 'Q') {
      run += 1;
      longest = Math.max(longest, run);
    } else if (ENERGY.has(code)) {
      run = 0;
      firstEnergy ??= index + 1;
    }
  });
  const lines = [
    `${funnel.name ?? ''} [${funnel.id ?? ''}] · ${funnel.industry ?? ''} · ${steps.length} screens`,
    `Strip: ${codes.join(' ')}`,
    `Before paywall: ${body.length} screens · energy share ${Math.round((energy / Math.max(1, body.length)) * 100)}% · ` +
      `longest question run ${longest} · first energy screen ${firstEnergy ?? 'none'}`,
  ];
  steps.forEach((step, index) => {
    const text = Array.from((step.content?.text ?? '').replaceAll('\n', ' / ')).slice(0, 90).join('');
    lines.push(`  ${String(step.position ?? '?').padStart(3)} ${codes[index]} ${step.screenType ?? ''}: ${text}`);
  });
  return lines.join('\n');
}

const args = process.argv.slice(2);
if (args.includes('--help') || args.includes('-h')) {
  process.stdout.write(usage);
  process.exit(0);
}
const fileIndex = args.indexOf('--file');
const file = fileIndex >= 0 ? args[fileIndex + 1] : undefined;
if (fileIndex >= 0 && !file) fail('--file needs a path');
const funnelIds = args.filter((_, index) => fileIndex < 0 || (index !== fileIndex && index !== fileIndex + 1));
if (!file && funnelIds.length === 0) {
  process.stderr.write(usage);
  fail('give at least one funnel ID or --file');
}
const sources = file ? [[undefined, file]] : funnelIds.map((id) => [id, undefined]);
process.stdout.write(`${sources.map(([id, path]) => summarize(load(id, path))).join('\n\n')}\n`);
