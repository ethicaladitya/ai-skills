---
name: schema-markup
description: Choose, generate and validate Schema.org JSON-LD structured data (Organization, Person, WebSite, Article or BlogPosting, Service, LocalBusiness, BreadcrumbList) and avoid deprecated or pointless types. Use when adding or auditing structured data on a page or site.
---

# Schema markup

## Rules
- JSON-LD only, in the page head, **output by the SEO plugin or theme, never pasted into post content**.
- Every block needs `@context` and `@type`; URLs absolute; dates ISO 8601; no placeholder text.
- Only truthful, visible facts. Never mark up reviews you don't show, or fake or undisclosed incentivized reviews.
- Connect entities with `@id` (the WebSite `publisher` is the Organization; the Article `author` is the Person).
- Schema helps machines understand a page. It is not a ranking factor by itself; don't promise rankings.
- Verify after publishing: fetch the live page, parse every `application/ld+json` block with a JSON
  parser, list the `@type`s, then run Google's Rich Results Test on important templates.

## Pick by page type
| Page | Types |
|---|---|
| Home | `WebSite` (with `SearchAction` if the site has search), `Organization` (logo, `sameAs`) |
| Blog post | `BlogPosting` or `Article` (headline, author Person, datePublished, dateModified, image), `BreadcrumbList` |
| Author or About | `Person` with `sameAs` and `jobTitle`; `ProfilePage` for author pages |
| Service page | `Service` (`provider` = Organization, `areaServed`), `BreadcrumbList` |
| Business or agency | `Organization` or `ProfessionalService` / `LocalBusiness` subtype, with `areaServed` for service-area businesses |
| Legal services | `LegalService` (not the old `Attorney`) |
| Genuine user Q&A | `QAPage` / `DiscussionForumPosting` |
| Software tool | `SoftwareApplication` / `WebApplication` |

## Status as of mid-2026 (re-check Google's docs before relying on it)
- **FAQPage:** Google no longer shows FAQ rich results. Keep visible FAQ sections because they help readers
  and AI answers, but don't add FAQPage expecting a SERP feature.
- **Don't recommend:** `HowTo` (rich results removed 2023), `SpecialAnnouncement`, `CourseInfo`,
  `EstimatedSalary`, `LearningVideo`, `VehicleListing`, and `ClaimReview` for SERP features.
- `Dataset` is for Dataset Search only; `Book` actions are still supported.

## Minimal templates
```json
{"@context":"https://schema.org","@type":"Organization","@id":"https://example.com/#org",
 "name":"Example","url":"https://example.com/","logo":"https://example.com/logo.png",
 "sameAs":["https://www.linkedin.com/company/example"]}
```
```json
{"@context":"https://schema.org","@type":"BlogPosting","headline":"Title",
 "author":{"@type":"Person","name":"Name","url":"https://example.com/about/"},
 "publisher":{"@id":"https://example.com/#org"},
 "datePublished":"2026-09-29","dateModified":"2026-09-29","image":"https://example.com/cover.png"}
```
