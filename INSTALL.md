# How to install

<details>
<summary><strong>Antigravity (<code>agy</code>)</strong></summary>

### Install

```bash
agy plugin install https://github.com/jastfan/adhd
```

### Verify

```bash
agy plugin list
```

### Update

```bash
agy plugin uninstall adhd-mode
agy plugin install https://github.com/jastfan/adhd
```

### Uninstall

```bash
agy plugin uninstall adhd-mode
```

Or keep it installed and turn it off: `agy plugin disable adhd-mode`.

### Always-on (optional)

Add to `~/.gemini/GEMINI.md`:

```markdown
## Output style

The reader has ADHD. Shape every response so it can be acted on:

1. Lead with the answer or next action: command, path, or snippet first.
2. Number multi-step work; one bounded action per step.
3. End with one next action doable in under two minutes.
4. Finish the current issue before raising a new one.
5. Restate progress each turn ("step 3 of 5 done").
6. Give time estimates in concrete units, never "a bit".
7. After a change, show what now works.
8. Errors: state location, cause, and fix. No drama.
9. Cap lists to 5 items.
10. No preamble, no recaps, no closers.

Exceptions: explain fully when asked to explain. Confirm before destructive actions. After three failed fixes, stop and name the doubtful assumption. If the request is ambiguous, ask one short question.
```

</details>

<details>
<summary><strong>AstronClaw (custom skill)</strong></summary>

AstronClaw supports importing a Markdown file as a custom skill. This route uses
the existing `SKILL.md`; see its [official skills guide](https://github.com/iflytek/astronclaw-tutorial/blob/main/docs/guide/astronclaw/skills.md)
for the upload and management controls.

This procedure follows AstronClaw's documentation but has not been tested with
this skill. Check the exported instructions before enabling it.

### Install

1. Download the [canonical SKILL.md](https://raw.githubusercontent.com/jastfan/adhd/main/skills/adhd-mode/SKILL.md) and save it as `SKILL.md`. Review its contents before uploading.
2. In AstronClaw, open **我的技能 (My skills)**, choose **新建 (New)**, and upload that `.md` file.
3. Check that the imported skill is named `adhd-mode`. Use **启用/禁用 (Enable/Disable)** to control its availability.

Only the skill Markdown is needed. Uploading sends that file to AstronClaw;
the repository's plugin manifests and hooks are not part of this setup.

### Verify and activate

Confirm `adhd-mode` appears in **My skills**. Use **下载 (Download)** to review
the imported instructions against the original skill, then enable it and try:

```text
Use the adhd-mode skill for this conversation. Explain how to create an empty Git repository in a new folder.
```

Check that the reply leads with the action and numbers the steps. This is a
manual check of the imported skill; a successful upload alone does not verify
that its response rules are being applied.

### Activation note

AstronClaw supports both explicit requests and automatic skill invocation.
Its guide does not specify whether it honors `disable-model-invocation: true`,
so use **Disable** when you do not want the skill available. There is no need
to rely on a `/adhd-mode` slash command.

The skill instructs the assistant to keep the style for the conversation until
you say `stop adhd mode` or `normal mode`. That instruction does not change the
platform toggle; disable the skill and start a new conversation for a fresh
session without it.

### Update

Download the latest canonical `SKILL.md`. If you customized the imported copy,
use **下载 (Download)** to keep a backup first. For a clean replacement, delete
the old `adhd-mode` entry, repeat the import, and run the verification prompt
in a new conversation.

### Uninstall

In **My skills**, select `adhd-mode` and choose **删除 (Delete)**, then start a
new conversation. To keep the imported copy for later, choose **Disable** instead.

</details>

<details>
<summary><strong>Claude Code</strong></summary>

### Install

```bash
claude plugin marketplace add jastfan/adhd
claude plugin install adhd-mode@adhd-mode
```

Type `/adhd-mode`.

### Verify

```bash
claude plugin list
```

### Update

```bash
claude plugin marketplace update adhd-mode
```

### Uninstall

```bash
claude plugin uninstall adhd-mode
claude plugin marketplace remove adhd-mode
```

Or keep it installed and turn it off: `claude plugin disable adhd-mode`.

### Always-on (optional)

A `SessionStart` hook loads the full ruleset at the start of every session, no `/adhd-mode` needed:

```bash
touch ~/.claude/.adhd-mode-always
```

If you use a custom Claude configuration directory, create the flag there instead:

```bash
touch "$CLAUDE_CONFIG_DIR/.adhd-mode-always"
```

Back to on-demand:

```bash
rm ~/.claude/.adhd-mode-always
```

The hook only fires when the flag file exists, so installing the plugin changes nothing by itself. "stop adhd mode" still turns it off for the current session.

</details>


<details>
<summary><strong>Codex</strong></summary>

### Install

```bash
codex plugin marketplace add jastfan/adhd --ref main
codex plugin add adhd-mode@adhd-mode
```

Invoke the skill explicitly by typing `$adhd-mode`. Codex will not activate
it automatically.

### Verify

```bash
codex plugin list
```

### Update

```bash
codex plugin marketplace upgrade adhd-mode
codex plugin remove adhd-mode
codex plugin add adhd-mode@adhd-mode
```

### Uninstall

```bash
codex plugin remove adhd-mode
codex plugin marketplace remove adhd-mode
```

### Always-on (optional)

Add to `~/.codex/AGENTS.md`:

```markdown
## Output style

The reader has ADHD. Shape every response so it can be acted on:

1. Lead with the answer or next action: command, path, or snippet first.
2. Number multi-step work; one bounded action per step.
3. End with one next action doable in under two minutes.
4. Finish the current issue before raising a new one.
5. Restate progress each turn ("step 3 of 5 done").
6. Give time estimates in concrete units, never "a bit".
7. After a change, show what now works.
8. Errors: state location, cause, and fix. No drama.
9. Cap lists to 5 items.
10. No preamble, no recaps, no closers.

Exceptions: explain fully when asked to explain. Confirm before destructive actions. After three failed fixes, stop and name the doubtful assumption. If the request is ambiguous, ask one short question.
```

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

Gemini CLI has no plugin marketplace, so there are two native routes: a **custom command** (opt-in, off until you invoke it) or an **extension** (always-on once installed). The command route matches this skill's default posture; pick it unless you want the rules on every session.

### Install (command, opt-in)

```bash
mkdir -p ~/.gemini/commands
curl -fsSL https://raw.githubusercontent.com/jastfan/adhd/main/skills/adhd-mode/agents/gemini.toml \
  -o ~/.gemini/commands/adhd-mode.toml
```

Start a new session, type `/adhd-mode`. It stays on for that session.

### Install (extension, always-on)

```bash
gemini extensions install https://github.com/jastfan/adhd
```

The extension loads `GEMINI.md`, which imports the full skill, so the rules apply from message one. `git` must be installed.

### Verify

```bash
gemini extensions list          # extension route
ls ~/.gemini/commands           # command route: adhd-mode.toml present
```

Or type `/` in a session and confirm `adhd-mode` is listed.

### Update

```bash
gemini extensions update adhd-mode    # extension route
# command route: re-run the curl above
```

### Uninstall

```bash
gemini extensions uninstall adhd-mode    # extension route
rm ~/.gemini/commands/adhd-mode.toml     # command route
```

</details>

<details>
<summary><strong>GitHub Copilot (VS Code and Copilot CLI)</strong></summary>

Copilot reads Agent Skills natively: the same `SKILL.md`, no conversion. It scans `.github/skills/`, `.claude/skills/`, and `.agents/skills/` in the project, and `~/.copilot/skills/`, `~/.claude/skills/`, and `~/.agents/skills/` globally.

### Install

```bash
npx skills add jastfan/adhd -a github-copilot        # this project
npx skills add jastfan/adhd -a github-copilot -g     # all projects
```

Without the CLI, copy the skill folder into any directory Copilot scans:

```bash
git clone https://github.com/jastfan/adhd
mkdir -p ~/.copilot/skills
cp -R adhd-mode/skills/adhd-mode ~/.copilot/skills/
```

### Verify

Type `/` in the chat input and confirm `adhd-mode` appears. Or:

```bash
npx skills list
npx skills ls -g    # if installed globally
```

### Update

```bash
npx skills update adhd-mode
```

Or re-copy the folder after `git pull`.

### Uninstall

```bash
npx skills remove adhd-mode
```

Or delete the `adhd-mode` folder from the skills directory it landed in.

### Activation note

Copilot respects `disable-model-invocation`: nothing applies until you invoke the skill, same as Claude Code (tested in [#60](https://github.com/jastfan/adhd/pull/60)).

### Always-on (optional)

Add the block below to `.github/copilot-instructions.md` in the project (Copilot reads it into every chat):

```markdown
## Output style

The reader has ADHD. Shape every response so it can be acted on:

1. Lead with the answer or next action: command, path, or snippet first.
2. Number multi-step work; one bounded action per step.
3. End with one next action doable in under two minutes.
4. Finish the current issue before raising a new one.
5. Restate progress each turn ("step 3 of 5 done").
6. Give time estimates in concrete units, never "a bit".
7. After a change, show what now works.
8. Errors: state location, cause, and fix. No drama.
9. Cap lists to 5 items.
10. No preamble, no recaps, no closers.

Exceptions: explain fully when asked to explain. Confirm before destructive actions. After three failed fixes, stop and name the doubtful assumption. If the request is ambiguous, ask one short question.
```

</details>


<details>
<summary><strong>Hermes</strong></summary>

### Install

```bash
hermes skills install jastfan/adhd/skills/adhd-mode
```

Type `/adhd-mode`. The skill installs into `~/.hermes/skills/` and is exposed as a slash command at the next session start.

Prefer to browse first? Add this repo as a skill source (a "tap"), then search and install:

```bash
hermes skills tap add jastfan/adhd
hermes skills search adhd
hermes skills install jastfan/adhd/skills/adhd-mode
```

### Verify

```bash
hermes skills list
```

### Update

```bash
hermes skills update adhd-mode
```

### Uninstall

```bash
hermes skills uninstall adhd-mode
```

Or remove the tap too: `hermes skills tap remove jastfan/adhd`.

### Always-on (optional)

Add to the `AGENTS.md` in your working directory (Hermes loads it per workdir), or to your persona `SOUL.md` for every session:

```markdown
## Output style

The reader has ADHD. Shape every response so it can be acted on:

1. Lead with the answer or next action: command, path, or snippet first.
2. Number multi-step work; one bounded action per step.
3. End with one next action doable in under two minutes.
4. Finish the current issue before raising a new one.
5. Restate progress each turn ("step 3 of 5 done").
6. Give time estimates in concrete units, never "a bit".
7. After a change, show what now works.
8. Errors: state location, cause, and fix. No drama.
9. Cap lists to 5 items.
10. No preamble, no recaps, no closers.

Exceptions: explain fully when asked to explain. Confirm before destructive actions. After three failed fixes, stop and name the doubtful assumption. If the request is ambiguous, ask one short question.
```

</details>

<details>
<summary><strong>Kimi Code CLI</strong></summary>

### Install

Start a Kimi Code session, then:

1. Run `/plugins`.
2. Choose **Custom**.
3. Paste `https://github.com/jastfan/adhd` and press `Enter`.
4. Choose **Trust and install**.

Use slash command `/skill:adhd-mode` to invoke the skill explicitly.

### Update

`/plugins` in Kimi Code session, cursor to **I Have ADHD**, press `R`.

### Uninstall

`/plugins` in Kimi Code session, cursor to **I Have ADHD**, press `D`.


</details>

<details>
<summary><strong>OpenCode</strong></summary>

OpenCode loads this repository as a server plugin: `.opencode/plugins/adhd-mode.mjs` registers the `skills/` entry point and the `/adhd-mode` command, and injects the ruleset when always-on is enabled. OpenCode also reads `skills/` natively, so the skill still works even without the plugin — the plugin adds the `/adhd-mode` command and the always-on flag.

### Install

Clone the repo and point OpenCode at the plugin. An absolute path shares one checkout across every project:

```bash
git clone https://github.com/jastfan/adhd ~/.config/opencode/vendor/adhd-mode
```

Add to your `opencode.json` (global: `~/.config/opencode/opencode.json`):

```json
{ "plugin": ["/absolute/path/to/adhd-mode/.opencode/plugins/adhd-mode.mjs"] }
```

Or run OpenCode from the checkout — it ships a root `opencode.json` with the plugin already wired up.

Start a new session and turn on ADHD-friendly output for the session:

```text
/adhd-mode
```

Rules stay on until `stop adhd mode` or `normal mode`.

### Verify

Start OpenCode, type `/`, and confirm `adhd-mode` appears in the command list.

### Update

```bash
git -C ~/.config/opencode/vendor/adhd-mode pull
```

### Uninstall

Remove the `plugin` entry from `opencode.json`.

### Always-on (optional)

```bash
touch ~/.config/opencode/.adhd-mode-always
```

While the flag exists, the plugin appends the full ruleset to the system prompt every turn — the OpenCode equivalent of the Claude Code `SessionStart` hook. `stop adhd mode` or `normal mode` disables it for the current session; delete the flag to turn always-on off for good:

```bash
rm ~/.config/opencode/.adhd-mode-always
```

</details>


<details>
<summary><strong>Pi</strong></summary>

Pi discovers this repository as a native package: `extensions/` provides the session-persistent mode and `skills/` keeps the Agent Skills entry point available.

### Install

```bash
pi install https://github.com/jastfan/adhd
```

Start a new Pi session. Toggle ADHD-friendly output for the current session:

```text
/adhd-mode
```

The footer shows `● ADHD ON` while the mode is active. Run the command again to turn it off, or be explicit:

```text
/adhd-mode on
/adhd-mode off
stop adhd mode
```

Like the Claude Code hook, the extension adds the ruleset to the conversation once instead of rewriting the system prompt on every request, and adds it again after compaction drops it.

The existing Agent Skills command remains available as an alias:

```text
/skill:adhd-mode
```

Start a new Pi session with the mode enabled by default:

```bash
pi --adhd
```

### Verify

```bash
pi list
```

Confirm the GitHub package is listed, then type `/adhd-mode` and check that `● ADHD ON` appears in the footer.

### Update

```bash
pi update https://github.com/jastfan/adhd
```

Or update every unpinned Pi package with `pi update --extensions`.

### Uninstall

```bash
pi remove https://github.com/jastfan/adhd
```

### Always-on (optional)

Create a flag in Pi's agent configuration directory:

```bash
touch ~/.pi/agent/.adhd-mode-always
```

The extension checks the flag at every new, resumed, forked, or reloaded session. A saved choice for the current session wins over this default, so `stop adhd mode` keeps that session disabled.

Back to on-demand:

```bash
rm ~/.pi/agent/.adhd-mode-always
```

### Config file (optional)

Create `~/.pi/agent/adhd-mode.json` in Pi's agent configuration directory:

```json
{
  "alwaysOn": true,
  "hideStatus": true
}
```

- `alwaysOn`: start every session with the rules active — same as the `.adhd-mode-always` flag file, which still works
- `hideStatus`: keep the `● ADHD ON` status-bar entry hidden; the rules and the `/adhd-mode` command still work

Read once at extension startup, so restart Pi after changing it. A saved choice for the current session wins over `alwaysOn`, so `stop adhd mode` keeps that session disabled.

If `PI_CODING_AGENT_DIR` is set, put `.adhd-mode-always` in that directory instead. Run `/reload` or start a new session after changing the flag.

</details>


<details>
<summary><strong>Oh My Pi (OMP)</strong></summary>

### Install

```bash
omp plugin marketplace add jastfan/adhd
omp plugin install --scope user adhd-mode@adhd-mode
```

Start a new OMP session and run `/adhd-mode` to toggle the mode.

### Update

```bash
omp plugin marketplace update adhd-mode
omp plugin upgrade --scope user adhd-mode@adhd-mode
```

### Uninstall

```bash
omp plugin uninstall --scope user adhd-mode@adhd-mode
omp plugin marketplace remove adhd-mode
```

</details>


<details>
<summary><strong>Qwen Code</strong></summary>

### Install

```bash
qwen extensions install jastfan/adhd
```

Qwen Code supports the GitHub shorthand and installs the repository as a
native extension. The extension discovers the skill under `skills/`.

Type `/adhd-mode` to invoke the skill explicitly. Installing the extension
does not change output until the skill is invoked.

### Verify

```bash
qwen extensions list
```

Then start a new Qwen Code session and run:

```text
/skills
```

Confirm that `adhd-mode` appears in the list.

### Update

```bash
qwen extensions update adhd-mode
```

### Uninstall

```bash
qwen extensions uninstall adhd-mode
```

</details>

<details>
<summary><strong>Zed</strong></summary>

Zed's Agent reads Agent Skills natively using the same SKILL.md format without conversion. Note that Zed's older "Rules" have been replaced by Skills alongside AGENTS.md instructions.

### Install

In the Agent Panel, open the Skills manager and choose **Create skill from URL** (also in the command palette as `agent: create skill from url`), then paste:

```
https://github.com/jastfan/adhd/blob/main/skills/adhd-mode/SKILL.md
```

Save it in **User** scope for every project, or **Project** scope for one. Then type `/adhd-mode` in the Agent Panel.

Prefer the filesystem? Clone the repo and drop the skill folder into your user skills directory:

```bash
git clone https://github.com/jastfan/adhd
mkdir -p ~/.agents/skills
cp -R adhd-mode/skills/adhd-mode ~/.agents/skills/
```

### Verify

Open the Skills manager in the Agent Panel and confirm `adhd-mode` is listed. Or type `/` and confirm it appears.

### Update

Re-import from the same URL (overwrites), or re-copy the folder after `git pull`.

### Uninstall

Remove `adhd-mode` from the Skills manager, or delete `~/.agents/skills/adhd-mode`.

### Always-on (optional)

Add to your personal `~/.config/zed/AGENTS.md`:

```markdown
## Output style

The reader has ADHD. Shape every response so it can be acted on:

1. Lead with the answer or next action: command, path, or snippet first.
2. Number multi-step work; one bounded action per step.
3. End with one next action doable in under two minutes.
4. Finish the current issue before raising a new one.
5. Restate progress each turn ("step 3 of 5 done").
6. Give time estimates in concrete units, never "a bit".
7. After a change, show what now works.
8. Errors: state location, cause, and fix. No drama.
9. Cap lists to 5 items.
10. No preamble, no recaps, no closers.

Exceptions: explain fully when asked to explain. Confirm before destructive actions. After three failed fixes, stop and name the doubtful assumption. If the request is ambiguous, ask one short question.
```

</details>

<details>
<summary><strong>Cursor, Amp, and any other agent-skills harness</strong></summary>

Works with any harness that reads agent skills. Swap `-a <agent>` for yours.

### Install

```bash
npx skills add jastfan/adhd                  # this workspace
npx skills add jastfan/adhd -g               # all projects
npx skills add jastfan/adhd -a cursor -y     # one agent only
npx skills add jastfan/adhd -a opencode -y
```

New agent chat, type `/adhd-mode`.

Without the CLI, copy the skill folder into whatever path your agent scans:

```bash
git clone https://github.com/jastfan/adhd
mkdir -p ~/.cursor/skills     # Cursor. Use .agents/skills for OpenCode, or your agent's own path
cp -R adhd-mode/skills/adhd-mode ~/.cursor/skills/
```

### Verify

```bash
npx skills list
npx skills ls -g    # if installed globally
```

### Update

```bash
npx skills update adhd-mode
npx skills update -g    # if installed globally
```

### Uninstall

```bash
npx skills remove adhd-mode
npx skills remove adhd-mode -g    # if installed globally
```

### Always-on (optional)

Paste this into your agent's persistent rules file. Cursor: **Settings → Rules → User Rules**, or a project rule under `.cursor/rules/` with `alwaysApply: true`. OpenCode: `~/.config/opencode/AGENTS.md`.

```markdown
## Output style

The reader has ADHD. Shape every response so it can be acted on:

1. Lead with the answer or next action: command, path, or snippet first.
2. Number multi-step work; one bounded action per step.
3. End with one next action doable in under two minutes.
4. Finish the current issue before raising a new one.
5. Restate progress each turn ("step 3 of 5 done").
6. Give time estimates in concrete units, never "a bit".
7. After a change, show what now works.
8. Errors: state location, cause, and fix. No drama.
9. Cap lists to 5 items.
10. No preamble, no recaps, no closers.

Exceptions: explain fully when asked to explain. Confirm before destructive actions. After three failed fixes, stop and name the doubtful assumption. If the request is ambiguous, ask one short question.
```
</details>


## How activation works

1. **Installed, not invoked.** In Claude Code, Qwen Code, and Codex, nothing happens until you invoke the skill explicitly. Claude Code and Qwen Code honor `disable-model-invocation: true` in `SKILL.md`; Codex honors `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. Other harnesses may load every skill's description at startup and activate the skill themselves.
2. **You invoke it explicitly.** Type `/adhd-mode` in Claude Code or Qwen Code, or `$adhd-mode` in Codex. Rules stay on for that session. "stop adhd mode" or "normal mode" turns them off.
3. **You touch `~/.claude/.adhd-mode-always`** (Claude Code). A `SessionStart` hook loads the full ruleset from message one, every session.
4. **You add the always-on snippet above** (other harnesses). Keeps the core rules in your agent's persistent context.

In Claude Code, Qwen Code, and Codex, no middle ground: if you did not turn it on, it is off.

## Troubleshooting

**`/adhd-mode` not in autocomplete.** Restart the agent. The plugin index is read at startup.

**Always-on flag has no effect.** Update the plugin (`claude plugin marketplace update adhd-mode`) and restart. Hooks are read at startup, and the flag needs the plugin version that ships `hooks/hooks.json`.

**`claude plugin marketplace add` fails.** Use the `owner/repo` form. A local path must point at the repo root, not `.claude-plugin/`.

**Installed but replies still preamble.** Open a new session. If it still drifts, tighten the wording in `skills/adhd-mode/SKILL.md`.

**Want different rules.** Fork, edit `skills/adhd-mode/SKILL.md`, then swap your copy in:

```bash
claude plugin uninstall adhd-mode            # drop the upstream copy first:
claude plugin marketplace remove adhd-mode   # fork and upstream share both names
claude plugin marketplace add <jastfan>/adhd-mode
claude plugin install adhd-mode@adhd-mode
```

Restart, then re-invoke `/adhd-mode`.

**Skill missing after `npx skills add`.** Start a new agent chat. Skills are indexed at session start. Confirm the folder landed where your agent scans (`~/.cursor/skills/` for Cursor, `.agents/skills/` for OpenCode) and that the frontmatter `name` matches the folder name.
