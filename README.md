# ai-skills

Aditya Shah's reusable skills for AI agents (Claude Code, Hermes, or anything that reads
`SKILL.md` files). Each skill encodes what actually worked, and what went wrong, while running
adityashah.blog, courtsandcases.com and ariham.com.

| Skill | Use it for |
|---|---|
| [runbook-to-blog-post](runbook-to-blog-post/SKILL.md) | Turning real work notes into expert posts in the author's voice; includes `scripts/clean_text.py` (invisible characters, em dashes, privacy gate) |
| [technical-review](technical-review/SKILL.md) | Verifying every command, flag and snippet before publishing, with the error classes top models really make |
| [wordpress-safe-changes](wordpress-safe-changes/SKILL.md) | Changing live WordPress safely; debugging Rank Math and Yoast output; no plugin or theme file edits |
| [seo-measurement](seo-measurement/SKILL.md) | Correct GSC and GA4 numbers, and before/after measurement of individual SEO changes |
| [linkedin-post](linkedin-post/SKILL.md) | Sharing work on LinkedIn in a credible, non-promotional voice |
| [legal-content-india](legal-content-india/SKILL.md) | Accurate judgment explainers, process guides and fair legal-tech comparisons |
| [agent-ops-hygiene](agent-ops-hygiene/SKILL.md) | Cheap, observable, self-correcting agent loops, and the traps that break unattended runs |

## Install

```bash
git clone https://github.com/ethicaladitya/ai-skills.git ~/dev/Personal/ai-skills
~/dev/Personal/ai-skills/install.sh
```

`install.sh` symlinks every skill into `~/.claude/skills/` (Claude Code, all projects). Pass a
directory to install elsewhere, e.g. `./install.sh ~/.hermes/skills/aditya` or a project's
`.claude/skills`. Because they're symlinks, `git pull` updates every project at once.

## How skills are maintained
- Each skill is small, specific and evidence-based: rules come from real incidents and tests, noted
  with dates where useful.
- The portfolio agent (repo `aditya-hermes-setup`) keeps a `LESSONS.md`. Once a month it promotes
  general lessons into these skills, and records each change in [CHANGELOG.md](CHANGELOG.md).
- Site-specific details (hosts, IDs, brand rules) stay in that repo, never here.
- No secrets, hostnames or client data in this repo.

## Adding a skill
One folder, one `SKILL.md` with `name` and a `description` that says **when** to use it. Add scripts
only where a script is more reliable than instructions. Update the table above and `CHANGELOG.md`.
