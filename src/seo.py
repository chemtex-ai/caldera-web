# -*- coding: utf-8 -*-
"""Structured data (JSON-LD), page metadata and llms.txt.

Runs after the pages exist: it rewrites <title>/description and injects JSON-LD
before </head>. Keeping it a separate stage means the schema is generated from the
built pages (the FAQ entries are scraped out of faq.html), so it cannot drift from
what the site actually says.
"""
import json, re, html as _html, pathlib, build_white as bw

SITE = bw.SITE_URL
W = bw.WHITE

ORG = {
    "@type": "Organization",
    "@id": f"{SITE}/#organization",
    "name": "Karnani FnB Specialities LLP",
    "alternateName": "Caldera",
    "url": SITE + "/",
    "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo_stack_black.png"},
    "email": "hello@caldera.beer",
    "telephone": "+91-1800-123-3415",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Haute Street Corporate Park, 86A Topsia Road (S)",
        "addressLocality": "Kolkata",
        "addressRegion": "West Bengal",
        "postalCode": "700046",
        "addressCountry": "IN",
    },
    "sameAs": ["https://instagram.com/caldera.craftbeer/",
               "https://facebook.com/caldera.craftbeer/"],
}

BRAND = {"@type": "Brand", "@id": f"{SITE}/#brand", "name": "Caldera",
         "slogan": "Calcutta's Finest Craft",
         "logo": f"{SITE}/assets/logo_stack_black.png",
         "parentOrganization": {"@id": ORG["@id"]}}

# style, flavour, ABV ceiling, serving temp, formats, hero image
BEERS = {
 "yellow": ("Caldera Witbier", "Belgian-Style Wheat Beer", "Citrusy & Spicy", "5",
            "4-6 °C", ["On Pint"], "witbier_travertine.jpg",
            "Bright citrus, gentle spice and soft wheat in an easygoing Belgian-style wheat beer."),
 "blue":   ("Caldera Blue", "German-Style Pilsner", "Crispy & Dry", "5",
            "4-6 °C", ["On Tap", "On Pint"], "blue_blue.jpg",
            "Clean malt, balanced hop bitterness and a refreshing dry finish."),
 "strong": ("Caldera Strong", "Strong Lager", "Smooth & Roasty", "8",
            "4-6 °C", ["On Tap", "On Pint"], "strong_red.jpg",
            "A fuller-bodied lager with rich malt character and a smooth finish."),
}

# title (aim 50-60 chars) and description (aim 140-155)
META = {
 "index.html": ("Caldera — Calcutta's Finest Craft Beer | Kolkata",
   "Caldera is a craft beer brand from Kolkata. Witbier, Pilsner, Strong Lager and Hefeweizen, served on tap and by the pint across the city."),
 "find.html": ("Where to Find Caldera — Craft Beer Near You in Kolkata",
   "Bars, clubs and stores across Kolkata serving Caldera on tap or by the pint. Search by name, or narrow it down to your part of the city."),
 "ontap.html": ("Caldera On Tap — Draught Craft Beer in Kolkata",
   "Three Caldera styles poured fresh from the keg: Hefeweizen, Blue and Strong. Find the bars and taprooms pouring Caldera on draught."),
 "yellow.html": ("Caldera Witbier — Belgian-Style Wheat Beer, Kolkata",
   "Bright citrus, gentle spice and soft wheat. A Belgian-style wheat beer under 5% ABV, brewed in Calcutta and available by the pint."),
 "blue.html": ("Caldera Blue — German-Style Pilsner | Craft Beer Kolkata",
   "Clean malt, balanced hop bitterness and a dry finish. A German-style pilsner under 5% ABV, on tap and by the pint across Kolkata."),
 "strong.html": ("Caldera Strong — Strong Lager | Craft Beer Kolkata",
   "A fuller-bodied lager with rich malt character and a smooth, rounded finish. Under 8% ABV, on tap and by the pint across Kolkata."),
 "about.html": ("About Caldera — Craft Beer Brewed in Calcutta",
   "Caldera is the craft beer brand of Karnani FnB Specialities LLP, Kolkata. Four styles, brewed for people who share a good moment over adda."),
 "faq.html": ("Craft Beer FAQ — Styles, Serving and Caldera",
   "What craft beer is, how lager and ale differ, how to serve each style, and how to enjoy Caldera at its best. Common questions answered."),
 "blog.html": ("The Cal Journal — Caldera Craft Beer Stories",
   "Notes on craft beer, brewing and Calcutta from the Caldera team — beer styles, serving, and where the city drinks."),
 "contact.html": ("Contact Caldera — Craft Beer in Kolkata",
   "Get in touch about stocking Caldera, serving it at your venue, or finding it near you. A Kolkata craft beer brand."),
 "privacy.html": ("Privacy Policy — Caldera Craft Beer",
   "How Karnani FnB Specialities LLP collects, uses and protects the information you share through the caldera.beer website."),
 "pubcrawl.html": ("The Pub Crawl — Caldera Craft Beer, Kolkata",
   "Register for the Caldera Pub Crawl. Join us as we head to Calcutta's best pubs and engage ourselves in adda. Free to enter, 21+."),
}

CRUMB = {"index.html": None, "find.html": "Where to Find", "ontap.html": "On Tap",
         "yellow.html": "Witbier", "blue.html": "Blue", "strong.html": "Strong",
         "about.html": "About", "faq.html": "FAQ", "blog.html": "Journal",
         "contact.html": "Contact", "privacy.html": "Privacy Policy",
         "pubcrawl.html": "The Pub Crawl"}


def faq_pairs():
    """Pull the Q&A straight out of the built FAQ page so schema can't drift."""
    h = (W / "faq.html").read_text(encoding="utf-8")
    out = []
    for q, a in re.findall(r'<span class="faq-q">(.*?)</span>.*?<div class="faq-a">(.*?)</div>', h, re.S):
        q = _html.unescape(re.sub(r"<[^>]+>", "", q)).strip()
        a = _html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", a))).strip()
        if q and a:
            out.append({"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}})
    return out


def product(key):
    name, style, flavour, abv, serve, fmts, img, desc = BEERS[key]
    return {
        "@type": "Product", "@id": f"{SITE}/{key}#product", "name": name,
        "description": desc, "category": style,
        "image": f"{SITE}/assets/{img}",
        "brand": {"@id": BRAND["@id"]},
        "manufacturer": {"@id": ORG["@id"]},
        "url": f"{SITE}/{key}",
        "additionalProperty": [
            {"@type": "PropertyValue", "name": "Style", "value": style},
            {"@type": "PropertyValue", "name": "Tasting notes", "value": flavour},
            {"@type": "PropertyValue", "name": "Alcohol by volume", "value": f"under {abv}% ABV"},
            {"@type": "PropertyValue", "name": "Serving temperature", "value": serve},
            {"@type": "PropertyValue", "name": "Available as", "value": ", ".join(fmts)},
        ],
    }


def graph_for(slug):
    website = {"@type": "WebSite", "@id": f"{SITE}/#website", "url": SITE + "/",
               "name": "Caldera", "publisher": {"@id": ORG["@id"]},
               "inLanguage": "en-IN"}
    g = [ORG, BRAND, website]

    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    if CRUMB.get(slug):
        crumbs.append({"@type": "ListItem", "position": 2, "name": CRUMB[slug],
                       "item": SITE + bw.pretty(slug)})
    g.append({"@type": "BreadcrumbList", "itemListElement": crumbs})

    key = slug[:-5]
    if key in BEERS:
        g.append(product(key))
    if slug == "faq.html":
        pairs = faq_pairs()
        if pairs:
            g.append({"@type": "FAQPage", "@id": f"{SITE}/faq#faq", "mainEntity": pairs})
    if slug == "ontap.html":
        g.append({"@type": "ItemList", "name": "Caldera on tap",
                  "itemListElement": [
                      {"@type": "ListItem", "position": i + 1, "name": n}
                      for i, n in enumerate(["Caldera Hefeweizen", "Caldera Blue", "Caldera Strong"])]})
    return {"@context": "https://schema.org", "@graph": g}


def apply_to(slug):
    p = W / slug
    h = p.read_text(encoding="utf-8")
    title, desc = META[slug]
    h = re.sub(r"<title>.*?</title>", "<title>" + _html.escape(title) + "</title>", h, count=1, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">',
               '<meta name="description" content="' + _html.escape(desc, quote=True) + '">', h, count=1, flags=re.S)
    for prop in ("og:title", "twitter:title"):
        h = re.sub(r'(<meta (?:property|name)="%s" content=").*?(">)' % prop,
                   lambda m: m.group(1) + _html.escape(title, quote=True) + m.group(2), h, count=1)
    for prop in ("og:description", "twitter:description"):
        h = re.sub(r'(<meta (?:property|name)="%s" content=").*?(">)' % prop,
                   lambda m: m.group(1) + _html.escape(desc, quote=True) + m.group(2), h, count=1)
    ld = json.dumps(graph_for(slug), ensure_ascii=False, separators=(",", ":"))
    h = h.replace("</head>", f'<script type="application/ld+json">{ld}</script>\n</head>', 1)
    p.write_text(h, encoding="utf-8")
    return len(title), len(desc), ld.count('"@type"')


print("SEO stage:")
print(f"  {'page':14} {'title':>5} {'desc':>5} {'types':>6}")
for slug in META:
    if (W / slug).exists():
        t, d, n = apply_to(slug)
        flag = "" if 35 <= t <= 62 and 110 <= d <= 158 else "  <- check length"
        print(f"  {slug:14} {t:>5} {d:>5} {n:>6}{flag}")

# ---- llms.txt : a plain-language map for AI crawlers ----
(W / "llms.txt").write_text(f"""# Caldera

> Caldera is a craft beer brand from Kolkata (Calcutta), India, owned by
> Karnani FnB Specialities LLP. Four styles are produced: Witbier, Blue,
> Strong and Hefeweizen. Caldera is sold on draught ("on tap") at bars and
> restaurants, and in 330 ml bottles ("on pint") at licensed stores across
> Kolkata. Caldera does not sell alcohol online.

## Beers
- [Caldera Witbier]({SITE}/yellow): Belgian-style wheat beer, citrusy and spicy, under 5% ABV. Bottle only.
- [Caldera Blue]({SITE}/blue): German-style pilsner, crisp and dry, under 5% ABV. On tap and bottle.
- [Caldera Strong]({SITE}/strong): strong lager, smooth and roasty, under 8% ABV. On tap and bottle.
- [Caldera Hefeweizen]({SITE}/ontap): German-style wheat beer, fruity and smooth. On tap only, never bottled.

## Pages
- [Where to find Caldera]({SITE}/find): searchable list of bars, clubs and stores in Kolkata, filterable by area and by tap or bottle.
- [On tap]({SITE}/ontap): the styles poured on draught.
- [About]({SITE}/about): who Caldera is and where it comes from.
- [FAQ]({SITE}/faq): what craft beer is, how styles differ, how to serve them.
- [Contact]({SITE}/contact): enquiries, stocking Caldera, serving it at a venue.

## Facts
- Brand: Caldera. Tagline: Calcutta's Finest Craft.
- Owner: Karnani FnB Specialities LLP, Haute Street Corporate Park,
  86A Topsia Road (S), Kolkata 700046, West Bengal, India.
- Contact: hello@caldera.beer, 1800 123 3415.
- Caldera is a beer brand, not a visitable brewery or taproom.
- Legal drinking age applies. Not for sale to persons below 21 years.
""", encoding="utf-8")
print("  llms.txt written")
