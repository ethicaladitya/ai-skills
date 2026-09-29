#!/usr/bin/env python3
"""Pre-publish text gate. No AI.

  ops/clean_text.py FILE            clean FILE in place, report what changed
  ops/clean_text.py --check FILE    report only, change nothing

Removes invisible characters that AI tools and copy-paste leave behind
(zero-width spaces/joiners, BOM, soft hyphens, bidi controls, word joiners,
Mongolian vowel separator, variation selectors, tag characters) and turns
unusual spaces (narrow no-break, thin, hair, figure, ideographic...) into
normal spaces. Plain U+00A0 no-break spaces are kept only as the HTML entity.

Exit 1 if em dashes (U+2014) remain: blog style forbids them and the writer
must rephrase them, not the script.
Exit 2 if private details may be leaking (source notes are internal runbooks):
real IPv4 addresses outside documentation/private ranges, email addresses other
than example domains, or key/token-like strings. The writer must replace them
with placeholders (203.0.113.x, example.com).
"""
import re
import sys
from pathlib import Path

INVISIBLE = re.compile(
    "[​‌‍‎‏⁠⁡⁢⁣⁤﻿­"
    "‪-‮⁦-⁩᠎͏︀-️]"
    "|[\U000e0000-\U000e007f]"
)
ODD_SPACES = re.compile("[ -   　  ]")


def clean(text):
    report = {}
    found = INVISIBLE.findall(text)
    if found:
        report["invisible_removed"] = len(found)
        text = INVISIBLE.sub("", text)
    odd = ODD_SPACES.findall(text)
    if odd:
        report["odd_spaces_normalized"] = len(odd)
        text = ODD_SPACES.sub(" ", text)
    nbsp = text.count(" ")
    if nbsp:
        report["nbsp_to_entity"] = nbsp
        text = text.replace(" ", "&nbsp;")
    return text, report


DOC_IP = re.compile(r"^(192\.0\.2|198\.51\.100|203\.0\.113|10|127|0|255)\.|^192\.168\.|^172\.(1[6-9]|2\d|3[01])\.")
PUBLIC_EMAIL_OK = ("example.com", "example.org", "example.net", "adityashah.blog")


def privacy_flags(text):
    flags = []
    for ip in set(re.findall(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])", text)):
        if all(0 <= int(p) <= 255 for p in ip.split(".")) and not DOC_IP.match(ip) and not ip.startswith(("1.1.1.", "8.8.")):
            flags.append(f"real-looking IP {ip}")
    for email in set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)):
        if not email.lower().endswith(PUBLIC_EMAIL_OK):
            flags.append(f"email {email}")
    for tok in set(re.findall(r"\b(?:sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|ghp_[A-Za-z0-9]{30,}|xox[bp]-[A-Za-z0-9-]{20,})\b", text)):
        flags.append(f"secret-like string {tok[:6]}…")
    return flags


def main():
    args = sys.argv[1:]
    check = "--check" in args
    args = [a for a in args if a != "--check"]
    if len(args) != 1:
        sys.exit(__doc__)
    path = Path(args[0])
    original = path.read_text(encoding="utf-8")
    text, report = clean(original)
    dashes = [i + 1 for i, line in enumerate(text.splitlines()) if "—" in line or "&mdash;" in line]
    if not check and text != original:
        path.write_text(text, encoding="utf-8")
    private = privacy_flags(text)
    print(f"{path}: {report or 'clean'}" + (f"; em dashes on lines {dashes[:20]} (rephrase them)" if dashes else "")
          + (f"; PRIVACY: {', '.join(sorted(private)[:10])} (replace with placeholders)" if private else ""))
    return 2 if private else (1 if dashes else 0)


if __name__ == "__main__":
    sys.exit(main())
