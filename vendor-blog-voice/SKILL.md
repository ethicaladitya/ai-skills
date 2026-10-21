---
name: vendor-blog-voice
description: Write a product company's blog the way WPMU DEV and Elementor do it, with a warm, opinionated house voice, product posts that read as help, competitors named but never attacked, and customers, partners and the open-source community promoted as allies. Use when writing or editing posts for a company or product blog (launches, updates, experiments, roundups, newsletters, case studies), or when deciding how a post should talk about rivals and supporters.
---

# Vendor blog voice (WPMU DEV and Elementor, studied October 2026)

Twelve posts read on 2026-10-21: six from wpmudev.com/blog (Mail Canary, uncached hosting load test, Hub Tickets
vs helpdesk software, one month of EmDash hosting, OpenClaw hosting launch, the DEV newsletter) and six from
elementor.com/blog (WordPress born agent-ready, MCP for WordPress options, Webgate MCP case study, Elementor MCP launch,
two "10 best AI ..." roundups). Rules below name the post they come from. Our own house rules (no invented numbers,
no em dashes, dated competitor facts, `comparison-pages`, `runbook-to-blog-post`) win on any conflict.

## 1. The two voices, and when to use each

| | WPMU DEV | Elementor |
|---|---|---|
| Sounds like | A mate at the agency who runs the hosting, cracking jokes ("my friends", "you, know, look", one emoji per post) | A product company explaining the platform calmly; the founder-nerd voice appears only in op-eds |
| Byline | "Editorial Staff" for most; the CEO (James Farmer) signs launches and progress reports in first person | A named expert with a one-line credential, or a customer's own byline |
| Best at | Making a dry product update feel like news from a friend | Positioning: tying every feature to a bigger story (open source, the agentic web, the ecosystem) |

Pick one per post and keep it. The WPMU DEV register suits updates, experiments and newsletters. The Elementor
register suits launches, platform arguments, case studies and roundups.

## 2. Tone rules that both share
- **Open on the reader's pain, in a scene, not on the product.** Mail Canary opens with the Monday-morning client
  message "We haven't had a single inquiry all month"; Hub Tickets opens with requests spread across "inbox, forms,
  DMs, WhatsApp ... and that one ancient spreadsheet". The product enters only after the problem is felt.
- **Short paragraphs, one or two sentences, lots of one-line paragraphs** that act as beats ("Lovely stuff." "Very
  civilized." "That last point matters."). Headings are sentences or questions, not labels.
- **Plain words, named things.** `wp_mail()`, `/wp-json/`, `show_in_rest`, "Elementor > Elementor MCP". Specifics
  carry the authority; the jokes carry the warmth. Never jokes without specifics.
- **Self-deprecation beats boasting.** The CEO admits he "doesn't do Terminal"; the load-test post says "we hate to
  toot our own horn... but" right before the trumpet. Admit limits before claiming wins.
- **Own the rough edges in public.** "I openly said it was going to be a bit Wild West", then a numbered list of
  what was fixed, each with the why. Progress reports build more trust than launch posts.
- **"The code is yours": give things away.** Free plugin plus skill on GitHub, "take it and make it better".
  Experiments are framed as "we tried something", not as features.
- **Close on the next action, lightly.** One link ("See how Unlimited Hosting works", "Set up Email Tickets"),
  then a sign-off with personality ("Happy Dashing", "no actual canaries were harmed"). No hard sell paragraph.

## 3. Product posts that read as help
- **Lead with the mechanism, then the three answers it gives.** Mail Canary explains why `wp_mail()` returning true
  proves nothing, then lists the three outcomes the tool distinguishes (site down, send refused, lost after handoff).
  A reader learns something even if they never install it.
- **Say what the product can't do or doesn't touch.** "OpenClaw doesn't get access to wp-admin"; "everything is saved
  as a draft rather than published"; "using the MCP is entirely optional". Boundaries are a selling point.
- **Qualify your own benchmark before anyone else does.** The load test states the method, says "simulated clients"
  are not visitors, and adds a "quick note about the test" that lists what it does not predict. Then the ratios.
- **Progress reports are numbered lists of fixed things, each with cause and effect**, plus "what's next" and an
  invitation to keep reporting problems.
- **Launch posts are short** (the OpenClaw launch is about 400 words): the founder's own frustration, what the team
  built, who gets it, how to start, "tell us what you think".

## 4. How they talk about competitors
- **Name them, in a list, with current prices, and say "nothing wrong with" them.** Hub Tickets lists HelpScout,
  Zendesk, Freshdesk, Groove, Gorgias and HelpDesk with entry prices "at the time of writing", then: "We're not here
  to dramatically flip a table at Zendesk." The argument is never "they are bad", it is "you are already paying for
  this twice" or "theirs lives outside the workflow where the work happens".
- **Compare on a dimension you chose and explain why that dimension matters.** The hosting test compares uncached
  load (where WPMU DEV wins) and spends a section on why uncached matters to agencies. Pick the honest dimension
  where you are strong; never pretend it is the only one.
- **Never a single-competitor hit piece.** Rivals appear in a set of five or six, or as a category ("unofficial
  MCP servers", "a separate helpdesk platform"). The reader compares categories, not two brands.
- **Frame the rival's weakness as a cost to the reader, in neutral words:** "more to keep updated", "manual setup that
  is on you", "vary in maintenance, permissions and what they expose". No adjectives about the rival itself.
- **Be generous to the platform's official option even when you compete with it.** Elementor calls the WordPress MCP
  Adapter "a good step for the whole ecosystem", explains what it does fairly, then shows its own as the easier
  path for its users. Praise first, then "if you build with Elementor, start with what you already have".
- **Roundups rank yourself first, then give real rivals real verdicts.** Elementor's "10 best" posts put Angie and
  Elementor at 1 and 2, but each rival gets Key features, Pricing, Pros, Cons and a verdict that says who it is
  for ("an easy call if you're inside the Elegant Themes ecosystem", "Hostinger's $2.99 entry point" for solo owners).
  A summary table and a "which should you choose" section hand different readers to different tools, including rivals.
- **Our tightening:** every competitor price and feature is checked live and dated, "not listed" is not "doesn't
  have", and the verdict for a rival must be one we would defend to them (see `comparison-pages`). We do not use
  unsourced market statistics ("73% of designers use AI") that pad the Elementor roundups.

## 5. How they talk about supporters (customers, partners, community)
- **Customers write in their own name and keep their doubts.** The Webgate case study is bylined by the agency's
  co-founder, keeps a "where the workflow still needs human supervision" section, and ends on the agency's own plans.
  The vendor's launch post then quotes the study in three neutral sentences and links it. Both posts link each other.
- **Users are "you good people" doing the testing:** feedback is thanked, bugs they found are listed as fixed, and
  the close asks for more ("keep telling us what you'd like to see"). Members are co-developers, not an audience.
- **Partners and the ecosystem are named generously:** WooCommerce, Yoast, WPForms, Jetpack, ACF as things the product
  reaches; Claude, Codex, Cursor and Figma as tools the reader already uses. Being compatible with a bigger name is
  a feature, so say the name.
- **The platform and its community get credit, even at the rival's expense.** Elementor's "born ready" post gives
  WordPress core the whole credit (REST API, Application Passwords, roles) and the company one closing line. The DEV
  newsletter covers WordCamp, core releases, Make blog debates and community posts by name, with links, and ends
  "share it with your favorite WordPress weirdo".
- **Community news uses a human calendar:** what happened this month, what shipped, what is being debated, three
  stats with sources, links worth reading, then "coffee break distractions". Product mentions are near zero.
- **Our tightening:** only real quotes and real customers, with permission; "customer language: unavailable" stays
  unavailable until we have interviews or reviews. No invented agencies.

## 6. Structure templates (copy the shape, not the words)
- **Experiment / small tool:** scene of the pain · why it happens · the thing everyone assumes that is wrong ·
  "so we tried something" · how it works (3 outcomes) · what it can't touch · what you hear from it · setup time ·
  take it and make it better · sign-off.
- **Benchmark:** what everyone knows (cache) · what we tested instead · result in one table and ratios · why this
  dimension matters for the reader · what the test does not say · one CTA.
- **Replace-a-tool:** where requests pile up · the tools people buy, named · "but wait, you already have this" ·
  what they charge for · what ours does, as a list · "either way" flexibility · CTA for members and non-members.
- **Progress report (founder):** what we said at launch · numbered fixes, each "what / why / done" · what's next ·
  ask for feedback · personal sign-off.
- **Platform argument:** the buzzword · "but first, what does it mean" · one plain requirement · "guess which platform
  did this already" · history by version number · the ecosystem credit · our one line at the end.
- **Options explainer:** TL;DR with three options and a bottom line · fair paragraph on the official option ·
  the cost of the others in reader terms · our path in a few steps · "start with what's already on your site".
- **Customer case study (their byline):** their setup list · first real use case · what the feature actually does
  in their words · numbered use cases with real prompts · what surprised them · where humans stay · their plan.
- **Roundup:** key takeaways · selection criteria · entries (features, pricing, pros, cons, verdict) · table ·
  "which should you choose", routing readers to rivals too · FAQ with real questions.

## 7. Checks before publishing a vendor post
1. First paragraph is a problem the reader has, not our product name.
2. Every competitor is named with a dated, live-checked fact, and no adjective judges the competitor itself.
3. At least one sentence says what our product does not do or cannot see.
4. Any benchmark states method, units and what it does not predict, before the ratios.
5. A customer or community member is credited by name only with permission and real words.
6. One CTA, one sign-off, no closing sales paragraph.
7. `clean_text.py` from `runbook-to-blog-post` exits 0 (no em dashes, no invisible characters).

## 8. What to adopt when you are small (one product, one expert blog, one agency)
Adopted 2026-10-21 for a portfolio of a legal-research product, a personal engineering blog and a small agency.
In priority order, because each costs almost nothing and compounds:
1. **Product posts as help.** Open on the user's pain scene, explain the mechanism, state what the product does
   not do. Readers learn something even if they never sign up, and the post earns links a feature page never will.
2. **A founder-signed "what we fixed this month" post** from the real changelog: numbered fixes with cause and
   effect, what's next, "keep telling us". It costs one weekly slot, builds more trust than any launch, and turns
   users into bug reporters.
3. **The "nothing wrong with them" line in every comparison,** plus a dated price list of all the rivals at once.
   Compare on a dimension you chose and say why it matters to the reader. The rival's weakness is always a cost to
   the reader ("a subscription you pay for twice"), never an adjective about the rival.
4. **Be generous to the official or open-source option you build on** (the government portal, the open-source core)
   before showing your easier path. Readers trust a vendor that praises what it depends on. A free rival is still a
   rival: it gets the fair-comparison treatment of point 3, not the ally treatment of this one or point 5.
5. **Name the bigger names you work with** as a feature (the platforms, tools and payment or hosting providers a
   reader already uses). Compatibility with a known name is a selling point, so say the name.
6. **Guest and customer posts under their own byline, doubts kept.** A case study that lists where humans still
   supervise is believed; a glowing one is not. Link both ways.
7. **Give code away.** Scripts and checks from your own work go on GitHub with "take it and make it better".
8. **Benchmarks only with method, units and a "what this does not say" note** before the ratios.

Leave behind: the emoji and in-jokes when the audience is professional (lawyers, buyers), unsourced market statistics
as filler, and ranking yourself first in a roundup without a reason the reader can check.
