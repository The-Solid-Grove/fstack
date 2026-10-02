import assert from 'node:assert/strict';
import { execFile, spawnSync } from 'node:child_process';
import { mkdtemp, mkdir, readFile, realpath, rename, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { promisify } from 'node:util';
import { afterEach, test } from 'node:test';

const script = fileURLToPath(new URL('../scripts/funnel-workspace.mjs', import.meta.url));
const roots = [];
afterEach(async () => {
  await Promise.all(roots.splice(0).map(root => rm(root, { recursive: true, force: true })));
});

async function fixture() {
  const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'fstack-workspace-')));
  roots.push(root);
  const state = path.join(root, 'state');
  async function folder(name, workspaceId = 'workspace-one', funnelId = 'funnel-one') {
    const directory = path.join(root, name);
    await mkdir(directory, { recursive: true });
    await writeFile(path.join(directory, '.funnelsgrove-sync.json'), JSON.stringify({
      version: 1, workspaceId, funnelId, draftVersionId: 'draft-one', files: [],
    }));
    return directory;
  }
  function run(command, extra = [], overrides = {}) {
    const result = spawnSync(process.execPath, [script, command,
      '--api-url', overrides.api ?? 'https://api.example.com/trpc',
      '--workspace', overrides.workspace ?? 'workspace-one',
      '--funnel', overrides.funnel ?? 'funnel-one', '--state-dir', state, ...extra,
    ], { encoding: 'utf8' });
    return { ...result, json: result.status === 0 ? JSON.parse(result.stdout) : null };
  }
  return { root, state, folder, run };
}

test('remembers one physical folder across fresh processes and repeated registration', async () => {
  const f = await fixture();
  const directory = await f.folder('existing funnel');
  const missing = f.run('find');
  assert.equal(missing.status, 0, missing.stderr);
  assert.equal(missing.json.status, 'not_found');
  assert.match(missing.json.key, /^[a-f0-9]{64}$/);
  const remembered = f.run('remember', ['--dir', directory]);
  assert.equal(remembered.status, 0, remembered.stderr);
  assert.equal(remembered.json.status, 'remembered');
  assert.equal(remembered.json.key, missing.json.key);
  assert.equal(remembered.json.path, directory);
  assert.equal(f.run('remember', ['--dir', directory]).status, 0);
  assert.deepEqual(f.run('find').json, { ...remembered.json, status: 'found' });
});

test('keeps different APIs and funnels separate while normalizing equivalent API URLs', async () => {
  const f = await fixture();
  const first = await f.folder('first');
  const second = await f.folder('second', 'workspace-one', 'funnel-two');
  const staging = await f.folder('staging');
  const a = f.run('remember', ['--dir', first], { api: 'https://API.example.com:443/trpc/' });
  assert.equal(a.status, 0, a.stderr);
  assert.equal(f.run('find').json.path, first);
  assert.equal(f.run('find', [], { funnel: 'funnel-two' }).json.status, 'not_found');
  assert.equal(f.run('remember', ['--dir', second], { funnel: 'funnel-two' }).status, 0);
  assert.equal(f.run('remember', ['--dir', staging], { api: 'https://staging.example.com/trpc' }).status, 0);
  assert.equal(f.run('find').json.path, first);
  assert.equal(f.run('find', [], { funnel: 'funnel-two' }).json.path, second);
  const otherApi = f.run('find', [], { api: 'https://staging.example.com/trpc' }).json;
  assert.equal(otherApi.path, staging);
  assert.notEqual(otherApi.key, a.json.key);
});

test('refuses mismatched or invalid manifests and revalidates identity on lookup', async () => {
  const f = await fixture();
  const directory = await f.folder('wrong', 'workspace-one', 'different-funnel');
  const wrong = f.run('remember', ['--dir', directory]);
  assert.equal(wrong.status, 1);
  assert.match(wrong.stderr, /identity mismatch/i);
  assert.equal(f.run('find').json.status, 'not_found');
  await f.folder('wrong');
  assert.equal(f.run('remember', ['--dir', directory]).status, 0);
  await f.folder('wrong', 'different-workspace');
  const drift = f.run('find');
  assert.equal(drift.status, 1);
  assert.match(drift.stderr, /identity mismatch/i);
  await writeFile(path.join(directory, '.funnelsgrove-sync.json'), '{bad json');
  assert.equal(f.run('remember', ['--dir', directory]).status, 1);
  assert.match(f.run('find').stderr, /invalid.*manifest/i);
  await writeFile(path.join(directory, '.funnelsgrove-sync.json'), JSON.stringify({
    version: 1, workspaceId: 'workspace-one', funnelId: 'funnel-one', draftVersionId: 123, files: [],
  }));
  assert.equal(f.run('find').status, 1);
});

test('reports moved folders and missing manifests as stale without forgetting their path', async () => {
  const f = await fixture();
  const directory = await f.folder('original');
  assert.equal(f.run('remember', ['--dir', directory]).status, 0);
  const moved = path.join(f.root, 'moved');
  await rename(directory, moved);
  const stale = f.run('find');
  assert.equal(stale.status, 0, stale.stderr);
  assert.equal(stale.json.status, 'stale');
  assert.equal(stale.json.reason, 'directory_missing');
  assert.equal(stale.json.path, directory);
  await rename(moved, directory);
  await rm(path.join(directory, '.funnelsgrove-sync.json'));
  const missingManifest = f.run('find');
  assert.equal(missingManifest.json.status, 'stale');
  assert.equal(missingManifest.json.reason, 'manifest_missing');
  assert.equal(f.run('remember', ['--dir', directory]).status, 1);
  await f.folder('original');
  assert.equal(f.run('find').json.status, 'found');
});

test('requires explicit replacement and changes only the saved mapping', async () => {
  const f = await fixture();
  const original = await f.folder('original');
  const replacement = await f.folder('replacement');
  await writeFile(path.join(original, 'local-work.txt'), 'unuploaded work');
  await writeFile(path.join(replacement, '.env'), 'PRIVATE_FIXTURE_SECRET');
  assert.equal(f.run('remember', ['--dir', original]).status, 0);
  const refused = f.run('remember', ['--dir', replacement]);
  assert.equal(refused.status, 1);
  assert.match(refused.stderr, /--replace/);
  assert.equal(f.run('find').json.path, original);
  assert.equal(f.run('remember', ['--dir', replacement, '--replace']).status, 0);
  assert.equal(f.run('find').json.path, replacement);
  assert.equal(await readFile(path.join(original, 'local-work.txt'), 'utf8'), 'unuploaded work');
  assert.equal(await readFile(path.join(replacement, '.env'), 'utf8'), 'PRIVATE_FIXTURE_SECRET');
});

test('rejects credential-bearing or ambiguous API URLs before remembering a folder', async () => {
  const f = await fixture();
  const directory = await f.folder('funnel');
  for (const api of [
    'https://user:PRIVATE_PASSWORD@api.example.com/trpc',
    'https://api.example.com/trpc?token=PRIVATE_QUERY',
    'https://api.example.com/trpc#different', 'file:///tmp/trpc', 'invalid',
  ]) {
    const result = f.run('remember', ['--dir', directory], { api });
    assert.equal(result.status, 1);
    assert.match(result.stderr, /HTTP\(S\).*credentials.*query.*fragment/i);
    assert.doesNotMatch(result.stderr, /PRIVATE_PASSWORD|PRIVATE_QUERY/);
  }
  assert.equal(f.run('find').json.status, 'not_found');
});

test('resolves folder aliases and refuses to assign one physical folder to another identity', async () => {
  const f = await fixture();
  const directory = await f.folder('funnel');
  const alias = path.join(f.root, 'alias');
  await symlink(directory, alias);
  assert.equal(f.run('remember', ['--dir', alias]).json.path, directory);
  assert.equal(f.run('remember', ['--dir', directory]).status, 0);
  const otherApi = f.run('remember', ['--dir', alias, '--replace'], { api: 'https://staging.example.com/trpc' });
  assert.equal(otherApi.status, 1);
  assert.match(otherApi.stderr, /already.*another.*identity/i);
  await f.folder('funnel', 'workspace-one', 'funnel-two');
  const otherFunnel = f.run('remember', ['--dir', directory], { funnel: 'funnel-two' });
  assert.equal(otherFunnel.status, 1);
  assert.equal(f.run('find', [], { funnel: 'funnel-two' }).json.status, 'not_found');
  await f.folder('funnel');
  const differentPhysicalFolder = await f.folder('different-physical-folder');
  await rename(directory, path.join(f.root, 'saved-original'));
  await symlink(differentPhysicalFolder, directory);
  assert.match(f.run('find').stderr, /physical.*changed/i);
});

test('rejects corrupt saved records instead of trusting or overwriting them', async () => {
  const f = await fixture();
  const directory = await f.folder('funnel');
  const remembered = f.run('remember', ['--dir', directory]).json;
  const filename = path.join(f.state, `${remembered.key}.json`);
  const valid = JSON.parse(await readFile(filename, 'utf8'));
  for (const corrupt of ['{broken', JSON.stringify({ ...valid, funnelId: 'another-funnel' }), JSON.stringify({ ...valid, path: 'relative/path' })]) {
    await writeFile(filename, corrupt);
    const found = f.run('find');
    assert.equal(found.status, 1);
    assert.match(found.stderr, /invalid.*record/i);
    assert.equal(f.run('remember', ['--dir', directory, '--replace']).status, 1);
    assert.equal(await readFile(filename, 'utf8'), corrupt);
  }
});

test('concurrent registrations choose one folder without silently replacing the winner', async () => {
  const f = await fixture();
  const directories = await Promise.all(Array.from({ length: 12 }, (_, i) => f.folder(`copy-${i}`)));
  const results = await Promise.allSettled(directories.map(directory => promisify(execFile)(process.execPath, [
    script, 'remember', '--api-url', 'https://api.example.com/trpc', '--workspace', 'workspace-one',
    '--funnel', 'funnel-one', '--state-dir', f.state, '--dir', directory,
  ])));
  const successes = results.filter(result => result.status === 'fulfilled');
  assert.equal(successes.length, 1);
  const winner = JSON.parse(successes[0].value.stdout);
  assert.equal(f.run('find').json.path, winner.path);
  for (const result of results.filter(result => result.status === 'rejected')) {
    assert.match(result.reason.stderr, /busy|--replace/i);
  }
});
