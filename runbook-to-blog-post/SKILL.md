---
name: runbook-to-blog-post
description: Turn a real work note, runbook or incident write-up into an expert, publishable technical blog post in the author's own voice, with no invented experience, no private details and no AI tells. Use when writing or rewriting a technical blog post (sysadmin, DevOps, hosting, WordPress, AI), especially from internal notes.
---

# Runbook to blog post

The strongest technical posts are real work, explained well. This skill turns a note someone wrote
while doing the job into a post that builds their authority, without inventing anything.

## 1. Read the source like an editor
- List every command, config value, decision and warning in the note. All of them must survive.
- Work out the reader's real question (the search query) and what they need to act safely.
- Identify what is private: real IPs, hostnames, customer or employer names, emails, ticket IDs,
  internal tools and procedures, credentials. All of them get replaced (step 4).

## 2. Shape
- **Title:** under 60 characters, contains the query, promises the outcome.
- **First paragraph answers the query directly** (answer engines and busy readers both quote it).
- Then: when you need this · the steps (commands in `<pre><code>`, each explained: what it does,
  the risk, how to verify, how to roll back) · pitfalls · a quick-reference block · FAQ (3 real
  questions, short answers).
- 1,200–2,000 words. Depth over padding: every section must teach something.
- Internal links only where they genuinely help (2–3); one authoritative external link (official docs).

## 3. Voice
- Expert, direct, practical. Vary sentence length. Plain trade-offs, and say when something is uncertain.
- **First person only for what the note shows the author actually does** ("When I need to block a
  server's outbound traffic, I use REJECT, not DROP, because..."). Never invent incidents, clients,
  numbers, experiments or results.
- Add an AI angle only where it's genuine (AI for triage, automation, detection). Never force it.
- **Banned:** em dashes (U+2014); filler openers ("In today's digital landscape"); hype and AI-tell
  words (delve, tapestry, game-changer, seamless, robust, leverage, unlock, elevate, realm,
  ever-evolving, crucial); generic conclusions ("In conclusion...").

## 4. Sanitize
Replace every private detail with a placeholder: IPs with `203.0.113.x` / `198.51.100.x` /
`192.0.2.x`, domains with `example.com`, people and companies with roles ("the client", "a hosting
provider"). Remove internal-only procedures entirely.

## Quality bar (people-first content)
Before the gates, the draft must pass Google's Who / How / Why test:
- **Who** wrote it? A visible byline and an author page with real credentials.
- **How** was it made? First-hand evidence from the note: real commands, real decisions, real results.
  Disclose AI assistance where readers would reasonably want to know.
- **Why** does it exist? To help the reader do the task, not to fill a keyword or word count.

Signs of low-quality AI content to remove: generic phrasing, no original insight, the same structure as
every other post, missing author, factual errors. Show the publish and "updated" dates, and refresh posts
on fast-moving topics.

## 5. Review, then gate
1. Run the **technical-review** skill on the draft. In a blind test every draft from every model had
   real command or code errors until reviewed.
2. `python3 scripts/clean_text.py draft.html` must exit 0. It strips invisible characters (zero-width,
   BOM, soft hyphens, bidi controls, odd spaces) in place. Exit 1 means em dashes to rephrase; exit 2
   means likely private details (real IPs, non-example emails, key-like strings).

## 6. Publish checklist
SEO title and meta description (140–155 characters) set in the SEO plugin, not in the body. Never
paste `<meta>` or JSON-LD into post content. Canonical correct, indexable, in the sitemap, HTTP 200,
links resolve. Record which note became which post, so no note is used twice.

## Why these rules (evidence)
Blind comparison, 2026-09-29, same brief to Claude Opus, Claude Sonnet and gpt-5.6-luna, judged by
two different models: Opus scored 8.0, luna 6.7, Sonnet 6.0. None was publishable without the
technical review. No model produced invisible characters, but the gate stays: it's cheap and deterministic.
