# -*- coding: utf-8 -*-
"""The Cal Journal — article pages, and the index cards that link to them.

Articles live at /blog/<slug> and use ROOT-ABSOLUTE asset paths, since they sit a
directory deeper than every other page.
"""
import re, html as _html, pathlib, datetime, json, build_white as bw

HERE = pathlib.Path(__file__).resolve().parent
SITE = bw.SITE_URL
PUB  = "2026-11-09"

POSTS = [
 dict(slug="the-art-of-the-adda", img="cheers_bridge.jpg", cat="The Cal Way",
      title="The art of the adda, in a glass",
      excerpt="Calcutta doesn't rush its conversations — and neither should its beer. "
              "A look at how the city's unhurried way of gathering shapes the way we brew and pour.",
      desc="Adda is Calcutta's unhurried way of gathering. What that asks of a beer, and why "
           "Caldera is brewed unfiltered for evenings that have nowhere to be."),
 dict(slug="why-your-witbier-is-cloudy", img="witbier_travertine.jpg", cat="Know Your Beer",
      title="Why your Witbier is cloudy — and proud of it",
      excerpt="Haze isn't a flaw. We unpack what makes a Belgian-style wheat beer naturally cloudy, "
              "and why unfiltered craft beer carries more character.",
      desc="Yeast, wheat protein and starch are what make a wheat beer cloudy. Why Caldera leaves "
           "them in, how to tell haze from spoilage, and how to pour the bottle."),
 dict(slug="lager-vs-ale", img="glasses_trio.jpg", cat="Know Your Beer",
      title="Lager vs ale: a quick guide for the curious",
      excerpt="Top-fermented or bottom-fermented? Warm or cool? A simple, no-jargon guide to the "
              "two great families of beer — and where Caldera's styles sit.",
      desc="The only real difference between lager and ale is the yeast and the temperature it "
           "works at. A plain-language guide, plus where each Caldera beer sits."),
]

# ---------- a very small markdown subset: ## , **b** , [text](url), > quote, tables ----------
def md(src):
    out, para, tbl = [], [], []
    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para.clear()
    def flush_tbl():
        if not tbl: return
        rows = [r.strip().strip("|").split("|") for r in tbl if not set(r.strip()) <= set("|-: ")]
        head, body = rows[0], rows[1:]
        out.append("<div class='jtable'><table><thead><tr>"
                   + "".join(f"<th>{inline(c.strip())}</th>" for c in head) + "</tr></thead><tbody>"
                   + "".join("<tr>" + "".join(f"<td>{inline(c.strip())}</td>" for c in r) + "</tr>" for r in body)
                   + "</tbody></table></div>")
        tbl.clear()
    for line in src.splitlines():
        s = line.strip()
        if s.startswith("|"):
            flush(); tbl.append(s); continue
        flush_tbl()
        if not s: flush()
        elif s.startswith("## "): flush(); out.append(f"<h2>{inline(s[3:])}</h2>")
        elif s.startswith("> "): flush(); out.append(f"<blockquote><p>{inline(s[2:])}</p></blockquote>")
        else: para.append(s)
    flush(); flush_tbl()
    return "\n".join(out)

def inline(t):
    t = _html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t.replace("—", "&mdash;").replace("–", "&ndash;")

def read_minutes(words): return max(2, round(words / 200))

def article(p):
    raw = (HERE / "journal" / f"{p['slug']}.md").read_text(encoding="utf-8")
    words = len(raw.split())
    body = md(raw)
    pretty_date = datetime.date.fromisoformat(PUB).strftime("%-d %B %Y")
    url = f"{SITE}/blog/{p['slug']}"
    inner = f'''<article class="jart">
  <header class="jhead"><div class="wrap jwrap">
    <a class="jback" href="/blog">&larr; The Cal Journal</a>
    <span class="blog-cat jcat">{p["cat"]}</span>
    <h1>{p["title"]}</h1>
    <p class="jmeta"><time datetime="{PUB}">{pretty_date}</time> &middot; {read_minutes(words)} min read</p>
  </div></header>
  <div class="jhero"><img src="/assets/{p["img"]}" alt="{_html.escape(p["title"],quote=True)}" width="1600" height="900"></div>
  <div class="wrap jwrap jbody">{body}</div>
  <div class="wrap jwrap jfoot">
    <p class="jlegal">Consumption of alcohol is injurious to health. Not for sale to persons below
    21 years. For sale in West Bengal only. Please enjoy responsibly.</p>
    <a class="btn btn-gold" href="/find">Where to Find Caldera</a>
  </div>
</article>'''
    html = bw.clean(bw.standalone_w(f'{p["title"]} — Caldera', p["desc"], inner, "blog", "", "blog.html"))
    # a directory deeper than everything else: make every local reference root-absolute
    html = re.sub(r'(href|src)="assets/', r'\1="/assets/', html)
    html = re.sub(r'(href|src)="(?!/|https?:|#|mailto:|tel:)([A-Za-z0-9_-]+)"', r'\1="/\2"', html)
    html = html.replace(f'<link rel="canonical" href="{SITE}/blog">',
                        f'<link rel="canonical" href="{url}">')
    html = html.replace(f'<meta property="og:url" content="{SITE}/blog">',
                        f'<meta property="og:url" content="{url}">')
    html = html.replace(f'{SITE}/assets/og_default.jpg', f'{SITE}/assets/{p["img"]}')
    ld = {"@context":"https://schema.org","@type":"BlogPosting","@id":url+"#post",
          "headline":p["title"], "description":p["desc"], "url":url,
          "image":f'{SITE}/assets/{p["img"]}',
          "datePublished":PUB, "dateModified":PUB, "inLanguage":"en-IN",
          "wordCount":words, "articleSection":p["cat"],
          "author":{"@type":"Organization","name":"Caldera","@id":f"{SITE}/#organization"},
          "publisher":{"@id":f"{SITE}/#organization"},
          "isPartOf":{"@type":"Blog","name":"The Cal Journal","@id":f"{SITE}/blog#blog"},
          "mainEntityOfPage":{"@type":"WebPage","@id":url}}
    html = html.replace("</head>",
        f'<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False,separators=(",",":"))}</script>\n</head>', 1)
    d = bw.WHITE / "blog"; d.mkdir(exist_ok=True)
    (d / f'{p["slug"]}.html').write_text(html, encoding="utf-8")
    return words

# ---------- articles ----------
counts = {p["slug"]: article(p) for p in POSTS}

# ---------- index: cards now link, and no longer say "Coming soon" ----------
idx = bw.WHITE / "blog.html"
h = idx.read_text(encoding="utf-8")
pretty_date = datetime.date.fromisoformat(PUB).strftime("%-d %b %Y")
for p in POSTS:
    h = h.replace(
      f'<article class="blog-card rv"><div class="blog-media"><img src="assets/{p["img"]}"',
      f'<article class="blog-card rv"><a class="blog-link" href="/blog/{p["slug"]}">'
      f'<div class="blog-media"><img src="assets/{p["img"]}"')
h = re.sub(r'<span class="blog-soon">Coming soon</span></div></article>',
           '__CARDEND__</div></a></article>', h)
for p in POSTS:
    h = h.replace('__CARDEND__',
        f'<span class="blog-soon">{pretty_date} &middot; {read_minutes(counts[p["slug"]])} min read</span>', 1)
h = h.replace("Fresh stories are on the way &mdash; here's a taste of what's brewing.",
              "Three to start with &mdash; on the city, on haze, and on the two families every beer belongs to.")
h = h.replace("Fresh stories are on the way — here's a taste of what's brewing.",
              "Three to start with — on the city, on haze, and on the two families every beer belongs to.")
idx.write_text(h, encoding="utf-8")

print(f"journal: {len(POSTS)} articles -> " + ", ".join(f'/blog/{s} ({w}w)' for s,w in counts.items()))
