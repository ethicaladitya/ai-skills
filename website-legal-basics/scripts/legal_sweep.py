#!/usr/bin/env python3
"""Read-only legal-basics sweep of a site's home page: policy links, trackers, consent tool,
forms without a privacy notice, images without alt, risky claims. Hints, not a verdict.
Usage: python3 legal_sweep.py example.com [other.com ...]"""
import re, sys, urllib.request

UA = {'User-Agent': 'Mozilla/5.0 (legal-sweep)'}


def get(url):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25)
        return r.status, r.read().decode('utf-8', 'replace')
    except Exception as e:
        return getattr(e, 'code', str(e)), ''


TRACKERS = ['googletagmanager', 'gtag(', 'adsbygoogle', 'ca-pub-', 'wordads', 'clarity.ms', 'connect.facebook.net',
            'hotjar', 'snap.licdn.com', 'youtube.com/embed', 'fonts.googleapis', 'recaptcha', 'challenges.cloudflare']
CMP = r'fundingchoices|cmplz|cookieyes|complianz|cookie-notice|moove_gdpr|onetrust|cookiebot|termly|iubenda'
CLAIMS = r'trusted by [^<]{0,40}|\b\d[\d,]*\+? (?:clients|customers|users|lawyers|advocates)\b|best in india|guaranteed?|no\.? ?1 '

for host in sys.argv[1:]:
    status, h = get(f'https://{host}/')
    low = h.lower()
    links = set(re.findall(r'href="([^"#]+)"', h))
    print(f'\n== {host} [{status}]')
    for label, pat in [('privacy', 'privacy'), ('terms', 'terms|conditions'), ('cookies', 'cookie'),
                       ('refund', 'refund|cancell'), ('contact', 'contact'), ('about', 'about')]:
        print(f'  link {label:8}', sorted(l for l in links if re.search(pat, l, re.I))[:3] or 'MISSING')
    print('  trackers   ', [t for t in TRACKERS if t in low] or 'none')
    print('  consent CMP', bool(re.search(CMP, low)))
    print('  DPDP/grievance mentioned', 'dpdp' in low or 'digital personal data' in low, '/', 'grievance' in low)
    imgs = re.findall(r'<img\b[^>]*>', h, re.I)
    print(f'  images {len(imgs)}, no alt attr {sum(1 for i in imgs if not re.search(r"alt=", i, re.I))}')
    for f in re.findall(r'<form\b.*?</form>', h, re.I | re.S):
        fields = re.findall(r'name="([^"_][^"]*)"', f)
        print('  form', fields[:8], 'privacy notice:', bool(re.search(r'privacy|consent', f, re.I)))
    print('  claims to verify', sorted({m.lower().strip() for m in re.findall(CLAIMS, h, re.I)})[:6] or 'none')
    for p in ['/error_log', '/debug.log', '/wp-content/debug.log', '/.env']:
        s, _ = get(f'https://{host}{p}')
        if s == 200:
            print('  PUBLIC FILE (block it)', p)
    for p in ['/privacy-policy/', '/privacy/', '/privacy.html', '/terms/', '/terms-of-service/', '/terms.html']:
        s, _ = get(f'https://{host}{p}')
        if s == 200:
            print('  page exists', p)
