---
name: ui-anti-slop
description: Avoid the visual and copy patterns that make a site look AI-generated ("vibe coded"), such as harsh gradients, Lucide and sparkle icons, purple-on-black, bento grids, three feature cards, three pricing tiers, Inter or Geist type, and emoji. Use when designing, building or reviewing any UI, landing page, component or page copy.
---

# UI without the AI-slop look

Readers now spot a generated site within seconds, and it costs trust. Source: a 30-item list
("30 reasons your site looks vibecoded", @abhijayarora_, 2026-09), reviewed and grouped here.

**The existing design system wins.** Where a site already has tokens, fonts or components, keep them
(on courtsandcases, design tokens are the Chair's call). Use this list to stop new defaults creeping in
and to review a change, not as a reason to redesign.

## Defaults to avoid (choose on purpose instead)

Colour
- Harsh or rainbow gradients, radial "orbs", neon accents, purple-and-black, generic pastels.
- A pure `#fff` page. Use a slightly tinted off-white and a palette taken from the brand, with one accent.

Type and icons
- Inter, Geist or Space Grotesk as the reflex choice. Pick a face that fits the brand and pair it deliberately.
- The stock Lucide set, sparkle/✨ "AI" icons, emoji as decoration, checkmark bullets on every list,
  animated arrows on every CTA.

Layout
- Hero, then 3 feature cards in a row, then bento grid, then 3 pricing tiers. Let the content decide the
  layout: varied rhythm, real hierarchy, asymmetry where it helps.
- Dot-grid or glassy ("liquid glass") backgrounds, soft drop shadows and the same large corner radius
  on everything, a coloured left stripe on cards, fake terminal windows.
- Hover animations on every element. Animate only what gives feedback.

Copy (also in copywriting / copy-editing skills)
- Em dashes, "it's not X, it's Y" reveals, fake or unattributed testimonials. Use real quotes or none.

## Missing pieces that also give it away

- **Real product demos:** actual screenshots, recordings or live examples of the product, not illustrations.
- **Skeleton loaders** for async content instead of spinners or layout jumps.
- **Terms of service and privacy policy** linked in the footer (see website-legal-basics).

## Review check

Before shipping a UI change, count how many of the items above it adds. Two or more new ones means it
will read as generated: replace them with choices that come from the brand and the content.
