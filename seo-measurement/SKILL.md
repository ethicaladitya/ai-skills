---
name: seo-measurement
description: Collect and interpret Google Search Console and GA4 data correctly (site totals, units, staleness, auth), and measure whether an individual SEO change worked with a before/after comparison. Use when building SEO reports, dashboards or collectors, or judging the effect of SEO work.
---

# SEO measurement that doesn't lie

## Search Console
- **Site totals come from a query with no dimensions:**
  `searchanalytics.query(siteUrl, {startDate, endDate, type: "web"})` returns one row with the real
  clicks, impressions, CTR and position. **Never sum query or page rows:** GSC drops anonymized and
  long-tail queries from rows and caps them at `rowLimit`. One site read 0 clicks this way when it had 27.
- Average CTR and position across rows are meaningless; use the dimensionless row.
- **Data lag:** the last 2–3 days are incomplete. End windows at least 3 days back when comparing.
- **Property type matters:** `sc-domain:example.com` covers every subdomain and protocol; `https://example.com/` does not.
- Sitemap status: `sitemaps.list(siteUrl)` shows errors per submitted sitemap. Look for junk submissions
  (typos, the homepage submitted as a sitemap) before blaming the generator.
- A read-only token (`webmasters.readonly`) can't resubmit sitemaps; that's a manual step.

## GA4
Sessions, users and engagement rate per 14-day window, with the previous window alongside. Track AI
referrals separately (chatgpt.com, perplexity.ai, gemini.google.com, copilot): on some sites they
outgrow Google clicks.

## Hygiene
- **Units at boundaries:** decide whether CTR is a fraction or a percent, and convert where data changes hands.
- **Missing is not zero.** Label stale data with its age; never report a failed collection as a drop.
- **Auth fails silently if you let it:** check auth first in the collector (`creds.refresh`); OAuth apps
  in Google Cloud "Testing" mode expire refresh tokens after about 7 days, so publish the consent screen.
- Keep collection deterministic (scripts on a schedule). Spend model tokens on interpretation only.

## Did this change work? (per page)
For each change, log the exact page URL and date. After at least 7 days of post-change data (plus 3 days of lag):
- **before** = the 14 days before the change; **after** = day+1 up to 28 days, ending 3 days ago.
- Compare **per-day** impressions and clicks (windows differ in length) and average position.
- Score +1 for more than 20% up (impressions, clicks) or position better by more than 1; −1 for the
  reverse. Positive is *improved*, negative *worse*, zero *flat*.
- Roll verdicts into a playbook weekly ("title rewrites on position 4–15 pages work on site X"), and
  revert or rethink changes that stay *worse* after 14+ days.
One page and one change is noisy; trust the pattern across several, not a single verdict.
