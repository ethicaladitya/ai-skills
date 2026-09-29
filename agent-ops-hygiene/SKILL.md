---
name: agent-ops-hygiene
description: Run autonomous or scheduled AI agents cheaply and reliably, covering scripts over LLM calls, lessons files, stage logging, cost caps, and the shell, SSH and scheduler traps that break unattended runs. Use when designing agent loops, cron or launchd jobs, or debugging unattended agent runs.
---

# Agent operations hygiene

## Spend tokens only on judgment
- Anything countable or repeatable is a script: data collection, health checks, text cleanup, diffing,
  exporting. The model reads a compact brief (a few KB), not raw data.
- One deep-dive per run and a cap on actions (e.g. 3). Cap spend per run (`--max-budget-usd`).
- If you do the same manual check twice, turn it into a script.

## Make runs observable
- Log every stage with status `done | failed | skipped | waiting`, **including what didn't happen**
  and why. A missing report is an incident, not "healthy".
- Log scheduled skips ("not due") separately from misses, so dashboards can tell them apart.
- Keep each run's transcript (session id, cost, turns) where the owner can read it.

## Learn from mistakes
Keep a `LESSONS.md` that every run reads first. When a mistake is found and fixed, add the lesson in
the same commit: one line of what happened, one line of the rule. Promote general lessons into skills.

## Traps that break unattended runs
- **Bash:** `( cmd )` subshells swallow variables such as `errors+=()`; collect failures in the parent shell.
- **macOS launchd:** no ssh-agent, a minimal `PATH`, and a sleeping Mac runs jobs only during dark
  wakes. Use an explicit `ssh -F <config>` with a dedicated key, set `PATH` in the plist, and schedule a wake (`pmset repeat`).
- **Custom shells:** `grep` may be ugrep and `ls` may be eza (different output and regex limits). Parse
  with Python. In zsh, a bare `==` is a command.
- **Remote hosts** may lack Python; use the platform's own runtime (`wp eval-file` for PHP).
- **MySQL collations** treat invisible characters as equal. Search bytes with `LOCATE(UNHEX(..), BINARY col)`.
- **Cloudflare** blocks Python's default User-Agent (error 1010). Send a real one.
- **Scripted edits:** assert the anchor is unique before replacing; re-read a file right before rewriting it.
- **Secrets:** scripts read tokens themselves and never print them; the model sees statuses, not values.
- **Headless Claude Code:** `claude -p ... --model <m> --output-format json` gives `result`, `session_id`,
  `total_cost_usd` and `num_turns`. The transcript is at `~/.claude/projects/<cwd-with-dashes>/<session_id>.jsonl`.
