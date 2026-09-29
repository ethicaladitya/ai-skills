---
name: linkedin-post
description: Write a LinkedIn post that shares a blog post or piece of work in the author's own voice, practical and credible rather than promotional. Use when drafting or rewriting a LinkedIn post, especially one promoting a new article.
---

# LinkedIn post from a piece of work

## Shape
- **Line 1 is the hook,** built on the most useful or surprising insight in the work, not "I just published...".
  It must make sense on its own, because LinkedIn truncates after about 2 lines.
- 150–250 words. Two or three short paragraphs, or a tight list of 3–5 points.
- One concrete takeaway the reader can use today (a command, a check, a decision rule).
- The link near the end, with one line on what they'll get from it.
- At most 3 specific hashtags (#WordPress #DevOps #SysAdmin), never a wall of tags.

## Voice
First person, the author talking to peers. Specific over grand. No hype ("game-changer", "excited
to announce"), no engagement bait ("Agree?"), no em dashes, no emoji strings. Claims only what the
work actually shows; no invented numbers or outcomes.

## Readability (checked by `readability.py --kind social` from runbook-to-blog-post)
First line 30 words or fewer and able to stand alone as the hook; paragraphs of 70 words or fewer (list items count
separately); average sentence around 16-20 words; reading ease 40 or more. At most one post a day, spaced about 20
hours apart, in working hours: more is noise, and the audience stops reading.

## Before posting
Run the post text through `clean_text.py` from the runbook-to-blog-post skill (it must exit 0) and
check the link opens. If the platform or agent that posts it has an approval step, respect it.
