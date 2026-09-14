<p align="center">
  <img src="./logo.png" alt="ADHD Mode Logo" width="180" style="border-radius: 24px; box-shadow: 0 8px 30px rgba(0,0,0,0.5);" />
</p>

<h1 align="center">ADHD Mode</h1>

<p align="center">
  <strong>Action-first, zero-fluff AI assistant engine designed for developers with ADHD.</strong><br>
  <em>Never scroll past another "Great question! Let's dive in..." again.</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="#verification"><img src="https://img.shields.io/badge/Tests-51%2F51%20Passed-emerald.svg?style=flat-square" alt="Tests"></a>
  <a href="#quickstart"><img src="https://img.shields.io/badge/Platforms-Cursor%20%7C%20Claude%20%7C%20Gemini%20%7C%20Web-purple.svg?style=flat-square" alt="Platforms"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"></a>
</p>

<p align="center">
  <a href="#what-is-it">What It Is</a> •
  <a href="#the-10-rules">The 10 Rules</a> •
  <a href="#quickstart">Quickstart</a> •
  <a href="#visual-playground">Visual Playground</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#verification">Verification</a>
</p>

---

## What It Is

**ADHD Mode** is an open-source behavioral engine and skill plugin that intercepts AI coding assistants and forces them to deliver immediate, actionable answers.

Default AI responses overwhelm ADHD working memory with conversational pleasantries, lengthy background summaries, and unprompted sidebars. **ADHD Mode** enforces:
- **Line-1 Action Guarantee**: Executable command, file edit, or code snippet is always on line 1.
- **Numbered Bounded Steps**: Tasks broken down into atomic steps. No nested rabbit holes.
- **Working Memory Cap**: Lists capped at 5 items maximum.
- **Concrete Time Horizons**: Specific units ("about 3 minutes", "an afternoon") instead of vague estimates.
- **Zero Polite Noise**: Strips greetings, pleasantries, apologies, and closing summaries.

---

## Before vs. After

<table>
<tr>
<th width="50%">❌ Default AI Output (High Friction)</th>
<th width="50%">✅ ADHD Mode Output (Action First)</th>
</tr>
<tr>
<td>

> Great question! Let's think about this carefully. Your auth flow has a few moving pieces: the middleware, the token verification, and the cookie handling. Looking at `src/auth.ts`, the `verifyToken` function (around lines 42-58) seems to be using an older `jsonwebtoken` API where callbacks were required. One approach would be to update the package and rewrite that function to handle promises properly. After making the change, you'd want to run the auth tests to confirm nothing breaks. By the way, you might also want to look at your dependency versions overall. Hope this helps! Let me know if you want to dig deeper into JWT configuration!

</td>
<td>

> Run `npm install jsonwebtoken@latest`, then edit `src/auth.ts:42`.
>
> 1. Open `src/auth.ts`
> 2. Replace `verifyToken` (lines 42–58) with:
> ```ts
> export async function verifyToken(token: string) {
>   return jwt.verify(token, process.env.JWT_SECRET!);
> }
> ```
> 3. Run `npm test -- auth.spec.ts` (~1 minute)
>
> Next: paste the first failing line if any test fails.

</td>
</tr>
</table>

---

## The 10 Canonical Rules

The behavior is strictly governed by [skills/adhd-mode/SKILL.md](skills/adhd-mode/SKILL.md):

1. **Lead with the next action**: Line 1 is something executable (command, snippet, path). Prose comes after.
2. **Number multi-step tasks**: One bounded action per step. No double "and then".
3. **End with one concrete next action**: Exactly ONE task taking under 2 minutes.
4. **Suppress tangents**: Finish primary goal before offering secondary improvements.
5. **Restate state every turn**: Anchor progress ("Step 2 of 4 done: schema built") at the top.
6. **Specific time estimates**: Units in minutes or hours; never "a bit".
7. **Make completed work visible**: Show what now works immediately.
8. **Matter-of-fact errors**: State failure, root cause, and direct fix without emotional filler.
9. **Cap lists to 5 items**: Prevent working memory overload by grouping into sets of ≤ 5.
10. **Zero pleasantries / fluff**: Forbidden: "Great question!", "Sure thing!", "Hope this helps!".

---

## Quickstart: Use It Anywhere

### 1. Cursor IDE
Copy the skill folder into your workspace:
```bash
cp -r .cursor/skills/adhd-mode path/to/your-project/.cursor/skills/
```
Cursor auto-detects the skill on your next prompt.

### 2. Claude Code CLI
Install directly from your local clone or GitHub repository:
```bash
claude plugin install https://github.com/jastfan/adhd
```

### 3. Gemini / Antigravity IDE
Add this single import line to `GEMINI.md` in your project root:
```markdown
@skills/adhd-mode/SKILL.md
```

### 4. Web Browsers (ChatGPT, Claude.ai, Gemini Web)
Websites in Chrome/Edge cannot read local disk files. To use ADHD Mode in web browsers:
1. Copy this prompt snippet:
```text
Shape all responses for ADHD:
1. Lead with the executable command or code on line 1.
2. Number all multi-step tasks (one action per step).
3. End with exactly one concrete next step under 2 minutes.
4. Cap all lists at 5 items maximum.
5. Give specific time estimates (minutes/hours).
6. Cut all greetings, preambles ("Great question!"), and closing pleasantries ("Hope this helps!").
```
2. Paste into **Custom Instructions** (ChatGPT Settings -> Personalization -> Custom Instructions, or Claude.ai Account Settings).

---

## Visual Playground & Studio

Test prompt transformations and inspect before/after comparisons in an interactive browser dashboard:

```bash
python playground/server.py 8080
```
Open **[http://localhost:8080](http://localhost:8080)** in your browser. Includes live prompt comparisons, platform setup studio, and diagnostic proof matrix.

---

## Architecture & Repository Map

```
adhd/
├── skills/                     # Canonical prompt definition & agent profiles
│   └── adhd-mode/
│       ├── SKILL.md            # The source of truth for the 10 ADHD response rules
│       └── agents/             # Gemini and OpenAI agent definitions
├── .cursor/skills/adhd-mode/   # Cursor-compatible auto-discovery mirror
├── .claude-plugin/             # Claude Code plugin manifest and marketplace config
├── .codex-plugin/              # Codex plugin manifest
├── .opencode/                  # OpenCode plugin scripts and slash commands
├── hooks/                      # Always-on hook engine (Node.js, PowerShell, Bash)
├── extensions/                 # Native TypeScript agent extensions (Pi & OMP)
├── evals/                      # 14 evaluation benchmark scenarios & grading rubric
├── scripts/                    # Evaluation runner (run_evals.py) & LLM judge (judge.py)
├── tests/                      # 51 unit tests (100% passing on Windows, Linux, macOS)
└── playground/                 # Zero-dependency interactive web simulator & studio
```

---

## Verification

Run the automated test and evaluation suite locally:

```bash
# Run all 51 unit tests (Windows, Linux, macOS)
python -m unittest discover -s tests -v

# Validate evaluation cases catalog
python scripts/run_evals.py validate

# Verify context memory compatibility
npx -y tsx scripts/check_context_compat.ts
```

All 51 tests pass out of the box with zero external dependencies.

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) before submitting pull requests.

## License

[MIT](LICENSE) © 2026 [jastfan](https://github.com/jastfan). Built for focused, frictionless coding.
