# Changelog

## 2026-10-20
- schema-markup: SearchAction no longer earns a rich result (sitelinks search box retired Nov 2024).
- seo-measurement: two-round stop rule per page, kill criteria per initiative, compute-don't-eyeball and matching windows.
- ai-search-visibility: retrieved/cited/mentioned/recommended ladder, fixed question set with controls, one owning page per fact.
- comparison-pages: "not listed" is not "doesn't have", and a Current/Changed/Unverifiable/Overclaimed claim audit.
- authority-building: journalist-request triage and reply shape, moved and broken link reclamation, permission-first teardown offers.
- agent-ops-hygiene: separate check cadence from act condition; log checked=/acted= per run.
- linkedin-post: link stays in the body until a first-comment test wins; PDF document carousel format.

## 2026-10-18
- agent-ops-hygiene: reasoning-model token caps, claim a task before building, absolute worktree paths.

## 2026-10-03
- wordpress-safe-changes: Yoast redirects need both options, sitemap cache clear, generate FAQ block JSON with an encoder.

## 2026-09-29 (evening)
- runbook-to-blog-post: `scripts/readability.py` gate (answer-first, sentence and paragraph length, reading ease, question headings, FAQ, lists).
- linkedin-post: readability limits and posting cadence (one a day, about 20 hours apart).

## 2026-09-29 (later)
- Added ai-search-visibility, schema-markup, local-seo, comparison-pages, site-structure-at-scale,
  conversion-basics and authority-building, written from our own review of current practice and
  primary-source docs (crawler and schema facts from OpenAI, Google and Anthropic documentation).
- runbook-to-blog-post: people-first quality bar (Who / How / Why) and low-quality AI content markers.

## 2026-09-29
- First release: runbook-to-blog-post (with `clean_text.py`), technical-review, wordpress-safe-changes,
  seo-measurement, linkedin-post, legal-content-india, agent-ops-hygiene.
- Sources: the blind writer comparison (Opus 8.0, gpt-5.6-luna 6.7, Sonnet 6.0), the courts blog Rank Math
  fixes (registration gate, modules stored as a JSON string, head markup in post bodies), the GSC totals
  bug, and the unattended-run traps found while setting up the portfolio agent.
