#!/usr/bin/env node
import { createHash, randomUUID } from 'node:crypto';
import { link, mkdir, readdir, readFile, realpath, rename, rm, rmdir, stat, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';

const usage = `Usage: node scripts/funnel-workspace.mjs find|remember
  --api-url URL --workspace ID --funnel ID [--dir PATH] [--replace] [--state-dir PATH]

Remember a verified local funnel folder; find reuses it across conversations.
Only remember accepts --dir and --replace. No funnel files or remote data change.
`;

function optionsFor(args) {
  if (args.includes('--help') || args.includes('-h')) {
    process.stdout.write(usage);
    process.exit(0);
  }
  const command = args.shift();
  if (!['find', 'remember'].includes(command)) throw new Error(usage);
  const options = { command };
  const values = new Set(['--api-url', '--workspace', '--funnel', '--dir', '--state-dir']);
  while (args.length) {
    const option = args.shift();
    if (option === '--replace') options.replace = true;
    else if (values.has(option) && args[0] && !args[0].startsWith('--')) options[option.slice(2)] = args.shift();
    else throw new Error(`Unknown option or missing value: ${option}`);
  }
  for (const option of ['api-url', 'workspace', 'funnel']) {
    if (!options[option]?.trim()) throw new Error(`--${option} is required.`);
  }
  if (command === 'remember' && !options.dir) throw new Error('--dir is required for remember.');
  if (command === 'find' && (options.dir || options.replace)) throw new Error('find does not accept --dir or --replace.');
  return options;
}

async function readRecord(filename) {
  let raw;
  try { raw = await readFile(filename, 'utf8'); }
  catch (error) { if (error.code === 'ENOENT') return null; throw error; }
  try {
    const record = JSON.parse(raw);
    const fields = ['apiUrl', 'workspaceId', 'funnelId', 'path'];
    if (!record || fields.some(field => typeof record[field] !== 'string' || !record[field].trim())
      || Object.keys(record).length !== fields.length || !path.isAbsolute(record.path)
      || normalizeApi(record.apiUrl) !== record.apiUrl
      || path.basename(filename) !== `${identityKey(record)}.json`) throw new Error('Invalid fields');
    return record;
  } catch { throw new Error(`Invalid workspace record at ${filename}. Preserve it for inspection.`); }
}

function identityKey(identity) {
  return createHash('sha256').update(JSON.stringify({
    apiUrl: identity.apiUrl, workspaceId: identity.workspaceId, funnelId: identity.funnelId,
  })).digest('hex');
}

function normalizeApi(value) {
  const message = '--api-url must be an HTTP(S) URL without credentials, query, or fragment.';
  let url;
  try { url = new URL(value); }
  catch { throw new Error(message); }
  if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password || /[?#]/.test(url.href)) {
    throw new Error(message);
  }
  return url.href.replace(/\/+$/, '');
}

async function validateFolder(directory, identity) {
  try {
    if (!(await stat(directory)).isDirectory()) throw new Error('The selected path is not a directory.');
    if (await realpath(directory) !== directory) throw new Error(`The remembered physical path changed at ${directory}. Reconcile the folder before replacing its mapping.`);
  } catch (error) { if (error.code === 'ENOENT') return 'directory_missing'; throw error; }
  let manifest;
  try { manifest = JSON.parse(await readFile(path.join(directory, '.funnelsgrove-sync.json'), 'utf8')); }
  catch (error) {
    if (error.code === 'ENOENT') return 'manifest_missing';
    throw new Error(`Invalid sync manifest in ${directory}. Preserve the folder and recover its baseline.`);
  }
  if (!manifest || manifest.version !== 1 || typeof manifest.draftVersionId !== 'string'
    || !manifest.draftVersionId.trim() || !Array.isArray(manifest.files)
    || manifest.files.some(file => !file || typeof file.path !== 'string' || typeof file.hash !== 'string')) {
    throw new Error(`Invalid sync manifest in ${directory}.`);
  }
  if (manifest.workspaceId !== identity.workspaceId || manifest.funnelId !== identity.funnelId) {
    throw new Error(`Manifest identity mismatch in ${directory}. Preserve the folder and select the correct funnel.`);
  }
}

async function main() {
  const options = optionsFor(process.argv.slice(2));
  const identity = {
    apiUrl: normalizeApi(options['api-url']), workspaceId: options.workspace.trim(), funnelId: options.funnel.trim(),
  };
  const key = identityKey(identity);
  const base = process.env.XDG_STATE_HOME;
  const state = options['state-dir'] ?? path.join(
    base && path.isAbsolute(base) ? base : path.join(os.homedir(), '.local', 'state'), 'fstack', 'funnels',
  );
  const filename = path.join(state, `${key}.json`);
  if (options.command === 'find') {
    const previous = await readRecord(filename);
    const reason = previous && await validateFolder(previous.path, identity);
    if (reason) return { status: 'stale', key, ...identity, path: previous.path, reason };
    return { status: previous ? 'found' : 'not_found', key, ...identity, ...(previous ? { path: previous.path } : {}) };
  }
  const directory = await realpath(options.dir);
  const reason = await validateFolder(directory, identity);
  if (reason) throw new Error(`Cannot remember ${directory}: ${reason}. Recover the folder before registering it.`);
  await mkdir(state, { recursive: true, mode: 0o700 });
  const lock = path.join(state, '.write-lock');
  try { await mkdir(lock, { mode: 0o700 }); }
  catch (error) {
    if (error.code === 'EEXIST') throw new Error(`Workspace registry is busy. Retry after the other writer finishes; preserve an unexplained lock at ${lock} for inspection.`);
    throw error;
  }
  const temporary = path.join(state, `.${key}-${randomUUID()}.tmp`);
  try {
    const previous = await readRecord(filename);
    if (previous && previous.path !== directory && !options.replace) {
      throw new Error(`This funnel is already remembered at ${previous.path}. Use --replace only for an intentional relocation.`);
    }
    for (const name of await readdir(state)) {
      if (!name.endsWith('.json') || name === `${key}.json`) continue;
      const record = await readRecord(path.join(state, name));
      let recordedPath = record.path;
      try { recordedPath = await realpath(record.path); }
      catch (error) { if (error.code !== 'ENOENT') throw error; }
      if (recordedPath === directory) throw new Error('This physical folder is already remembered for another API or funnel identity.');
    }
    if (previous?.path !== directory) {
      await writeFile(temporary, `${JSON.stringify({ ...identity, path: directory }, null, 2)}\n`, { mode: 0o600, flag: 'wx' });
      if (previous) await rename(temporary, filename);
      else await link(temporary, filename);
    }
  } finally {
    await rm(temporary, { force: true });
    await rmdir(lock);
  }
  return { status: 'remembered', key, ...identity, path: directory };
}

try { process.stdout.write(`${JSON.stringify(await main())}\n`); }
catch (error) { process.stderr.write(`funnel-workspace: ${error.message}\n`); process.exitCode = 1; }
