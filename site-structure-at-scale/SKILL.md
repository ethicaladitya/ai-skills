---
name: site-structure-at-scale
description: Plan site hierarchy, URLs, hubs, internal linking and programmatic pages at scale (thousands to millions of template pages) without thin-content or doorway problems. Use when designing a site's structure, adding a section of service or location pages, or building or auditing templated pages such as case, product or directory pages.
---

# Site structure and pages at scale

## Hierarchy
- Every important page within about 3 clicks of the homepage. Go as flat as navigation allows.
- 4–7 items in the main navigation, with the primary call to action on the right. The footer groups the rest.
- Breadcrumbs mirror the URL path and carry `BreadcrumbList` schema.

## URLs
- Lowercase, hyphenated, readable, short; they reflect the hierarchy (`/services/wordpress-development/`).
- One trailing-slash policy. No dates in blog URLs, no IDs where a slug works, no content in query strings.
- **Subfolders over subdomains** when you want authority to be shared.
- Never change a URL without a 301 redirect from the old one.

## Internal linking
- **Hub and spoke:** a hub page links to every page in its cluster, each page links back to the hub,
  and related pages link to each other.
- No orphans: every page has inbound internal links. Important pages get the most.
- Descriptive anchor text, never "click here". Roughly 3–10 contextual links per 1,000 words.
- Related-content blocks at the end of posts and template pages.

## Pages at scale (programmatic SEO)
Templates plus data can rank for thousands of long-tail queries, or get a site demoted for thin content.
- **Every page must be worth visiting on its own:** unique data, conditional sections that appear only
  when data exists, and real analysis. Swapping one variable into identical text is a doorway page.
- **Data is the moat:** your own proprietary or product data beats public data that anyone can template.
- **Match intent:** the page must answer what the query asks, not just contain the words.
- **Indexation control:** index the pages with real content and demand; `noindex` thin or empty
  variants; split XML sitemaps by page type and watch the indexed-versus-submitted ratio in Search Console.
- **Hubs make pages discoverable:** category, court, statute or topic hubs link into the long tail, so
  crawlers and people reach it within a few clicks.
- **Keep request paths cheap:** precompute aggregates (counts, lists, stats) offline. Never compute them
  per request on a large dataset.
- **Common failures:** thin variants, cannibalization (several pages for one query), pages with no search
  demand, stale or wrong data, pages that exist only for crawlers.

## Before launching a new section
Unique titles and descriptions per page · one H1 · schema · in a sitemap · linked from a hub ·
a sample of 20 pages read by a human for usefulness · Search Console coverage checked 2–4 weeks later.
