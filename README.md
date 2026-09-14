<p align="center">
  <img src="./logo.png" alt="ADHD" width="160" style="border-radius: 32px;" />
</p>

<h1 align="center">ADHD</h1>

<p align="center">
  <strong>Action-first cognitive accelerator for AI coding assistants.</strong><br>
  Built specifically for neurodivergent developers to eliminate conversational friction, information overload, and context drift.
</p>

<p align="center">
  <a href="https://github.com/jastfan/adhd/actions"><img src="https://img.shields.io/badge/Tests-51%2F51%20Passed-00E599.svg?style=flat-square" alt="Tests"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-7928CA.svg?style=flat-square" alt="License"></a>
  <a href="https://github.com/jastfan/adhd"><img src="https://img.shields.io/badge/Platform-Multi--Assistant-0070F3.svg?style=flat-square" alt="Platform"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square" alt="Contributions"></a>
</p>

---

## Why ADHD Exists

Default AI coding assistants write like polite essayists: long conversational greetings, winding explanations, and buried action items. For developers with ADHD, working memory is scarce and activation energy is the biggest obstacle to getting code written.

**ADHD** reshapes the assistant's behavior at the engine level:

- **Immediate Execution (Line 1)**: First line contains executable commands, code snippets, or target files. Prose comes last.
- **Micro-Step Chunking**: Multi-step operations are strictly broken down into sequential, atomic actions.
- **Cognitive Working-Memory Limits**: Output lists never exceed 5 items at a time to prevent cognitive overload.
- **Deterministic Time Estimations**: Exact units (minutes or hours) instead of vague generalities.
- **Zero Polite Overhead**: Completely strips pleasantries ("Sure!", "Great question!"), recaps, and conversational closures.

---

## Execution Contrast

<table>
<tr>
<th width="50%">Standard Assistant Output (High Cognitive Friction)</th>
<th width="50%">ADHD Engine Output (Action First)</th>
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

## Core Operational Rules

The assistant strictly complies with the specifications defined in [`skills/adhd-mode/SKILL.md`](skills/adhd-mode/SKILL.md):

1. **Lead with action**: Line 1 must be actionable immediately (command, diff, or file path).
2. **Atomic numbering**: Bounded single-action steps for any multi-step task.
3. **Single closure step**: End with exactly one concrete action that takes under 2 minutes.
4. **Suppress tangents**: Complete the active objective before introducing side observations.
5. **Continuous state grounding**: Restate step index and completed state every turn.
6. **Explicit time units**: Every estimate must be specified in minutes or hours.
7. **Make wins explicit**: Highlight completed milestones directly.
8. **Objective diagnostics**: Surface errors and fixes without conversational padding.
9. **5-item cognitive cap**: Group and cap working lists to prevent cognitive fatigue.
10. **Zero pleasantries**: Strip all greetings, acknowledgments, apologies, and valedictions.

---

## Quick Setup

### Cursor IDE
Link the skill into your project:
```bash
cp -r .cursor/skills/adhd-mode path/to/your-project/.cursor/skills/
```

### Claude Code CLI
Install directly via git URL:
```bash
claude plugin install https://github.com/jastfan/adhd
```

### Gemini / Antigravity IDE
Include in your root `GEMINI.md`:
```markdown
@skills/adhd-mode/SKILL.md
```

### ChatGPT / Claude.ai / Web LLMs
Paste the following into your system instructions or custom prompt:
```text
Shape all responses for ADHD:
1. Lead with the executable command or code on line 1.
2. Number all multi-step tasks (one action per step).
3. End with exactly one concrete next step under 2 minutes.
4. Cap all lists at 5 items maximum.
5. Give specific time estimates (minutes/hours).
6. Cut all greetings, preambles, and closing pleasantries.
```

---

## Verification & Testing

The repository includes a comprehensive zero-dependency test and validation harness:

```bash
# Run 51 automated unit tests
python -m unittest discover -s tests -v

# Validate benchmark evaluation cases
python scripts/run_evals.py validate

# Verify context-memory runtime compatibility
npx -y tsx scripts/check_context_compat.ts
```

All 51 test suites pass with 100% test coverage across Windows, macOS, and Linux.

---

## License

[MIT](LICENSE) © 2026 [jastfan](https://github.com/jastfan/adhd). Engineered for deep, uninterrupted flow.
