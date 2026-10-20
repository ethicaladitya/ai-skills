---
name: website-legal-basics
description: Check and fix the legal and trust basics every business website needs, especially in India, covering privacy policy, terms, cookies and consent, refund policy, form notices, DPDP Act 2023 and Rules 2025, ad and analytics disclosures, accessibility, honest claims and image rights. Use when launching or auditing a business site, adding a form, ads, analytics or payments, or when someone asks "can my website get me sued".
---

# Website legal basics

This is a checklist and a set of defaults. It is not legal advice; a lawyer signs off the final policy text for
anything that takes payments or handles sensitive data. Never paste a generic template: every policy must
describe what **this** site actually collects and loads, and must match the live code.

## 1. Find what the site really does (before writing a word)
Run `scripts/legal_sweep.py <domain>` and then open the browser network tab on the home page, a post, the contact
page and checkout. List: forms and their fields, analytics (GA4, GTM, Clarity), ads (AdSense, WordAds),
pixels (LinkedIn Insight, Meta), embeds (YouTube, maps, fonts), captchas (reCAPTCHA, Turnstile), payment and
email processors. The policy is written from this list. A policy that says "no third-party cookies" while
AdSense loads is worse than no policy (we shipped exactly that once on courtsandcases.com).

## 2. Pages every business site needs, linked from the footer of every page
| Page | Required when | Must contain |
|---|---|---|
| Privacy policy | Always. IT (SPDI) Rules 2011 r.4 for any body corporate collecting personal data; AdSense and Google Analytics terms require it | What is collected (itemised), why, legal basis/consent, every processor and tracker by name, retention, rights and how to use them, grievance contact, cross-border transfers, children, last updated date |
| Terms of use | Always | Who runs the site (legal name), acceptable use, IP, disclaimers, liability, governing law and courts, last updated |
| Refund and cancellation | Anything is sold (Consumer Protection (E-Commerce) Rules 2020; Razorpay/Stripe onboarding checks it) | Linked **at the point of purchase**, not only inside the terms |
| Contact / business details | Always; mandatory for e-commerce | Legal entity name, address, email, phone or form, grievance officer name and contact |
| Cookie notice | Non-essential cookies; consent required for EU/UK visitors | Can be a section of the privacy policy |
| Disclaimer | Legal, medical, financial content | "Not legal advice" on explainers and guides |

## 3. India: DPDP Act 2023 and DPDP Rules 2025
Rules notified 13/14 Nov 2025. Consent-manager rule from ~Nov 2026; notice, security, breach and most
fiduciary duties from ~13 May 2027. Build to it now; retrofitting consent is harder than shipping it.
- **Notice** before or with collection: itemised data, purposes, how to withdraw consent, how to use rights,
  how to complain to the Data Protection Board. Plain language, standalone.
- **Consent** that is free, specific, informed, unambiguous, a clear affirmative act: no pre-ticked boxes.
  Withdrawing must be as easy as giving it.
- **Rights:** access, correction, erasure, grievance redressal, nomination. Give a working route (email or settings).
- **Grievance contact** published, and answer within the stated time.
- **Children (<18):** verifiable parental consent; no tracking, behavioural monitoring or targeted ads aimed at them.
- **Minimisation:** collect only what the purpose needs. A contact form needs name, email, message; phone,
  budget and URL are optional or gone. Delete data when the purpose is served.
- **Breach:** a written plan to inform the Board and affected people.

## 4. Forms
- One line under every submit button: what happens to the data and a link to the privacy policy.
- Marketing opt-in is a separate, unticked checkbox. Never bundle it with the enquiry.
- Labels on every field (not placeholder-only), errors announced, works with keyboard alone.
- Bot protection (Turnstile/reCAPTCHA) is named in the privacy policy.

## 5. Ads, analytics and consent
- AdSense: the privacy policy must disclose Google and third-party ad cookies and link Google's ad settings.
  For EEA, UK and Switzerland visitors Google requires a Google-certified CMP (TCF); without one those visitors
  get limited ads only. AdSense's own "Privacy & messaging" CMP is free.
- GA4: disclose it; enable Consent Mode v2 when EU/UK traffic matters.
- India has no GDPR-style cookie-banner rule, but DPDP consent covers personal data, so tie trackers to
  consent once the 2027 duties apply. A banner that sets cookies before the click is not consent.
- The whole stack (policy text, banner, tags) changes together. Re-run the sweep after adding any script.

## 6. Accessibility (WCAG 2.1 AA as the floor)
Alt text on meaningful images (`alt=""` for decorative), text contrast ≥ 4.5:1 (3:1 for large text), visible
focus, every control reachable by keyboard, buttons that say what they do ("Send enquiry", not "Submit"),
one `h1`, lang attribute, captions on video. Check with Lighthouse/axe on each template, not just the home page.

## 7. Claims, reviews and content rights
- Only real, attributed testimonials with consent on record (date and channel). Fake or invented reviews break
  the Consumer Protection Act 2019, BIS IS 19000:2022 on online reviews, and Google's spam policies.
- No unsupported numbers ("500+ clients", "#1", "saves 3 hours") without evidence on file. Use ranges or remove them.
- No dark patterns (CCPA Guidelines 2023): false urgency, basket sneaking, confirm-shaming, drip pricing, pre-ticked boxes.
- Images: own, licensed, or properly attributed; record the source. Stock "team" photos are not your team.
- Legal services: advocates may not solicit work (Bar Council of India Rule 36); keep legal-tech copy about the product.

## 8. Keep it true
Put "Last updated" on every policy and review it whenever a tracker, form, processor or price changes.
Log each policy change with what changed and why.
