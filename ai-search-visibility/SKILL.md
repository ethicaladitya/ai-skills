---
name: ai-search-visibility
description: Make pages citable in AI answers (Google AI Overviews and AI Mode, ChatGPT Search, Claude, Perplexity, Copilot) by checking crawler access per bot, answer-first structure, entity signals and AI referral tracking. Use when auditing or improving a site's visibility in AI search, or when AI assistants send traffic.
---

# AI search visibility

**Principle:** optimizing for AI search is still SEO. Google's AI Overviews and AI Mode are served
from the normal Googlebot index and ranking systems. Pages that rank and answer clearly get cited.
Be sceptical of "GEO hacks": chunking content for AI, rewriting for AI, `llms.txt` and mention-farming
have no confirmed effect on Google.

## 1. Crawler access: check the right bot for the claim
Read `robots.txt` and report each bot separately. Training bots and search bots are different things.

| To be citable in... | This bot must be allowed | Not this one (training only) |
|---|---|---|
| Google Search, AI Overviews, AI Mode | `Googlebot` | `Google-Extended` (Gemini/Vertex training and grounding) |
| ChatGPT Search | `OAI-SearchBot` | `GPTBot` |
| Claude's search features | `Claude-SearchBot` | `ClaudeBot` |
| Perplexity | `PerplexityBot` | (it doesn't train foundation models) |
| Bing, Copilot (and ChatGPT's Bing-based results) | `Bingbot` | |
| Siri, Spotlight, Safari | `Applebot` | `Applebot-Extended` (an opt-out label, not a crawler) |

User-triggered fetchers (`ChatGPT-User`, `Claude-User`, `Perplexity-User`, Google's user-triggered
agents) act for a person and may not follow `robots.txt`. Blocking training bots is a licensing choice,
not a visibility one. Sources: the OpenAI, Google and Anthropic crawler documentation pages.

Google Search Console also has a per-site "Search generative AI" setting (include, exclude or inherit)
for AI features. Check it before assuming a site is eligible.

## 2. Make pages quotable
- The answer comes first: a direct answer or definition in the first 40–60 words of the page and of
  each section ("X is...", "To do Y, ...").
- Self-contained passages: a paragraph should make sense quoted alone, with specific facts, not vague claims.
- Question-shaped H2 and H3 headings, one H1, short paragraphs, lists for steps, tables for comparisons.
- Primary sources cited inline; visible author, publish date and updated date.
- Key content in the server-rendered HTML. Many AI crawlers don't run JavaScript.
- Keep pages fresh: pages that answer changing questions need visible updates.

## 3. Entity signals (who you are)
AI systems recommend entities they can identify and see discussed elsewhere.
- Organization or Person schema with `sameAs` links to real profiles (LinkedIn, GitHub, Wikipedia or
  Wikidata if you qualify, the WordPress.org profile).
- A consistent name and description everywhere, and an About page that states expertise plainly.
- Genuine mentions on the places assistants read: community discussions, video, reputable directories,
  and "best of" roundups. Earn them; never fake them.

## 4. Measure
- GA4: sessions from `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`,
  `claude.ai`, tracked separately and trended. On some sites these outgrow Google clicks.
- Spot-check target questions in the assistants themselves and note who gets cited. Log the date; answers change.

## Optional extras (low priority)
`/llms.txt` costs little but has no confirmed effect on Google; don't spend real effort on it.
