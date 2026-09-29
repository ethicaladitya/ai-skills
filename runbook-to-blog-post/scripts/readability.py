#!/usr/bin/env python3
"""Readability and answer-engine checks for posts. No AI.

  ops/readability.py FILE [--kind post|social] [--query "target query"]

Posts (HTML): answer-first opening (first paragraph <= 60 words, mentions the query), sentence and
paragraph length, Flesch reading ease (technical content allowed down to 30), H2/H3 structure with
some question-style headings, an FAQ section, lists or tables for scannability. Social: sentence and
paragraph length, reading ease, short first line (the hook). Exit 1 with problems listed, else 0.
Metrics are guides for humans and answer engines; the rules are deliberately loose so they catch
walls of text and buried answers, not style.
"""
import html
import json
import re
import sys
from pathlib import Path


def _syllables(word):
    w = word.lower()
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups) - (1 if w.endswith("e") and len(groups) > 1 else 0)
    return max(1, n)


def _plain(text):
    text = re.sub(r"<(pre|code|script|style)[^>]*>.*?</\1>", " ", text, flags=re.S | re.I)
    return html.unescape(re.sub(r"<[^>]+>", " ", text))


def score_text(text, kind="post", query=""):
    is_html = "<p" in text or "<h2" in text
    raw = text
    plain = _plain(text) if is_html else text
    plain = re.sub(r"https?://\S+", " ", plain)
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", plain) if len(s.split()) >= 3]
    words = re.findall(r"[A-Za-z][A-Za-z'’-]*", plain)
    wc, sc = len(words), max(1, len(sentences))
    syl = sum(_syllables(w) for w in words) or 1
    flesch = round(206.835 - 1.015 * (wc / sc) - 84.6 * (syl / max(1, wc)), 1)
    avg_sentence = round(wc / sc, 1)
    long_sentences = sum(1 for s in sentences if len(s.split()) > 35)
    if is_html:
        paras = [_plain(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", raw, re.S | re.I)]
    else:
        paras = []
        for block in (p for p in re.split(r"\n\s*\n", plain) if p.strip()):
            lines = [l for l in block.splitlines() if l.strip()]
            # list items ("- ", "* ", "1. ") are separate units, not one long paragraph
            if len(lines) > 1 and all(re.match(r"\s*([-*\u2022]|\d+[.)])\s", l) for l in lines[1:]):
                paras += lines
            else:
                paras.append(block)
    para_words = [len(p.split()) for p in paras]
    m = {"words": wc, "flesch": flesch, "avg_sentence_words": avg_sentence, "long_sentences": long_sentences,
         "max_paragraph_words": max(para_words or [0])}
    problems = []
    if avg_sentence > 24:
        problems.append(f"average sentence {avg_sentence} words (aim <= 20)")
    if long_sentences > max(2, sc // 10):
        problems.append(f"{long_sentences} sentences over 35 words")
    if flesch < (30 if kind == "post" else 40):
        problems.append(f"reading ease {flesch} (too dense)")
    if kind == "social":
        first = (text.strip().splitlines() or [""])[0]
        m["hook_words"] = len(first.split())
        if len(first.split()) > 30:
            problems.append("first line over 30 words (LinkedIn truncates the hook)")
        if max(para_words or [0]) > 70:
            problems.append("a paragraph over 70 words")
    else:
        if max(para_words or [0]) > 120:
            problems.append("a paragraph over 120 words")
        first = para_words[0] if para_words else 0
        m["first_paragraph_words"] = first
        if first > 60:
            problems.append(f"first paragraph {first} words: answer the query in <= 60")
        if query and paras and not any(w.lower() in paras[0].lower() for w in re.findall(r"[a-z0-9]{4,}", query.lower())[:3]):
            problems.append("first paragraph doesn't address the target query")
        h2 = re.findall(r"<h2[^>]*>(.*?)</h2>", raw, re.S | re.I)
        h3 = re.findall(r"<h3[^>]*>(.*?)</h3>", raw, re.S | re.I)
        m["h2"], m["h3"] = len(h2), len(h3)
        questions = sum(1 for h in h2 + h3 if _plain(h).strip().endswith("?"))
        m["question_headings"] = questions
        if wc > 600 and len(h2) < 3:
            problems.append("fewer than 3 H2 sections")
        if not re.search(r"<h2[^>]*>\s*(FAQ|Frequently)", raw, re.I):
            problems.append("no FAQ section")
        if questions < 2:
            problems.append("fewer than 2 question-style headings (answer engines match questions)")
        if wc > 600 and not re.search(r"<(ul|ol|table)\b", raw, re.I):
            problems.append("no list or table")
    return {"metrics": m, "problems": problems}


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    kind = a[a.index("--kind") + 1] if "--kind" in a else "post"
    query = a[a.index("--query") + 1] if "--query" in a else ""
    r = score_text(Path(a[0]).read_text(encoding="utf-8"), kind=kind, query=query)
    print(json.dumps(r, indent=1))
    return 1 if r["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
