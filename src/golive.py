# -*- coding: utf-8 -*-
"""Go-live extras for the Caldera white site: 404, robots.txt, sitemap.xml, _redirects."""
import datetime, pathlib, re, build_white as bw

W = bw.WHITE
SITE = bw.SITE_URL
TODAY = datetime.date.today().isoformat()

PAGES = ["index.html","ontap.html","yellow.html","blue.html","strong.html",
         "about.html","faq.html","find.html","blog.html","contact.html","privacy.html"]
PRIORITY = {"index.html":"1.0","ontap.html":"0.9","yellow.html":"0.9","blue.html":"0.9",
            "strong.html":"0.9","find.html":"0.8","about.html":"0.7","faq.html":"0.6",
            "contact.html":"0.6","blog.html":"0.5","privacy.html":"0.2"}

# ---------- sitemap ----------
urls = "\n".join(
  f'  <url>\n    <loc>{bw.canon(p)}</loc>\n    <lastmod>{TODAY}</lastmod>\n'
  f'    <changefreq>{"weekly" if p in ("index.html","find.html","blog.html") else "monthly"}</changefreq>\n'
  f'    <priority>{PRIORITY[p]}</priority>\n  </url>' for p in PAGES)
(W/"sitemap.xml").write_text(
  '<?xml version="1.0" encoding="UTF-8"?>\n'
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'\n</urlset>\n', encoding="utf-8")

# ---------- robots ----------
(W/"robots.txt").write_text(
  "User-agent: *\n"
  "Allow: /\n"
  "Disallow: /wp-admin/\n"
  "Disallow: /wp-content/\n"
  "Disallow: /wp-includes/\n"
  "Disallow: /wp-json/\n\n"
  f"Sitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

# ---------- _redirects ----------
clean = "\n".join(f"/{p[:-5]:<16} /{p:<16} 301!" for p in PAGES if p != "index.html")
(W/"_redirects").write_text(f"""# ---- one canonical host: send the netlify.app copy to the domain ----
http://caldera-beer.netlify.app/*   https://caldera.beer/:splat   301!
https://caldera-beer.netlify.app/*  https://caldera.beer/:splat   301!

# ---- the review URL now lives at the root ----
/white/*           /:splat           301!
/white             /                 301!

# ---- legacy WordPress pages -> new site ----
/find-us/*         /find.html        301!
/find-us           /find.html        301!
/contact-us/*      /contact.html     301!
/contact-us        /contact.html     301!
/apply/*           /contact.html     301!
/apply             /contact.html     301!
/home              /                 301!

# ---- clean URLs ----
{clean}

# ---- retired WordPress surface: gone, not moved ----
/wp-admin/*        /404.html         410
/wp-content/*      /404.html         410
/wp-includes/*     /404.html         410
/wp-json/*         /404.html         410
/xmlrpc.php        /404.html         410
/feed              /404.html         410
/comments/feed     /404.html         410
""", encoding="utf-8")

# ---------- 404 ----------
BODY404 = '''<section class="chero nf"><div class="wrap maxw">
  <div class="eyebrow">Error 404</div>
  <h1>This page has <em>gone flat.</em></h1>
  <p>The page you were after isn't here any more &mdash; but the beer still is.</p>
  <div class="hero-ctas nf-ctas">
    <a class="btn btn-gold" href="/">Back to Caldera</a>
    <a class="btn btn-ghost" href="/find.html">Where to Find Caldera</a>
  </div>
</div></section>'''

html = bw.clean(bw.standalone_w(
    "Page Not Found — Caldera",
    "That page isn't here any more. Head back to Caldera — Calcutta's Finest Craft.",
    BODY404, "", "", "404.html"))

# root-absolute paths so the page works at ANY depth Netlify serves it from
html = re.sub(r'(href|src)="assets/', r'\1="/assets/', html)
html = re.sub(r'(href|src)="(?!/|https?:|#|mailto:|tel:)([A-Za-z0-9_\-]+\.html)', r'\1="/\2', html)
html = html.replace('<meta name="robots" content="index,follow,max-image-preview:large">',
                    '<meta name="robots" content="noindex,follow">')
html = html.replace(f'<link rel="canonical" href="{SITE}/404.html">\n', '')
(W/"404.html").write_text(html, encoding="utf-8")

print("go-live files written: sitemap.xml, robots.txt, _redirects, 404.html")
