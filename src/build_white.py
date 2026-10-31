# -*- coding: utf-8 -*-
import pathlib, re, shutil, build

SITE   = build.SITE
WHITE  = SITE/"white"
ASSETS = WHITE/"assets"
HERE   = pathlib.Path(__file__).resolve().parent
WHITE.mkdir(exist_ok=True)

# ---- assets ----
shutil.copytree(SITE/"assets", ASSETS, dirs_exist_ok=True)
base = (SITE/"assets"/"caldera.css").read_text(encoding="utf-8")
ov   = (HERE/"white_overrides.css").read_text(encoding="utf-8")
(ASSETS/"caldera-white.css").write_text(base+"\n\n"+ov, encoding="utf-8")
(ASSETS/"caldera-white.js").write_text((HERE/"caldera-white.js").read_text(encoding="utf-8"), encoding="utf-8")

SITE_URL = "https://caldera.beer"

HEADBITS_W = '''<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta name="theme-color" content="#ffffff">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,500&family=Rock+Salt&display=swap">
<link rel="stylesheet" href="assets/caldera-white.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>'''

SOCIAL_W = '''<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Caldera">
<meta property="og:locale" content="en_IN">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{site}/assets/og_default.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Caldera - Calcutta\'s Finest Craft">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/assets/og_default.jpg">
<meta name="robots" content="index,follow,max-image-preview:large">'''

CARET = '<svg class="caret" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M6 9l6 6 6-6"/></svg>'

def nav_w(active=""):
    def a(href,label,key):
        cls=' class="active"' if key==active else ''
        return f'<a href="{href}"{cls}>{label}</a>'
    return f'''<header id="nav"><div class="wrap maxw nav-row">
  <a class="brand" href="index.html" aria-label="Caldera home"><img src="assets/logo_horiz_black.png" alt="Caldera — Calcutta's Finest Craft"></a>
  <div class="nav-right">
    <nav class="nav-links" aria-label="Primary">
      <div class="nav-drop">
        <a class="nav-droptrig{' active' if active=='beers' else ''}" href="index.html#beers">Our Beers {CARET}</a>
        <div class="nav-sub nav-sub-2">
          <div class="nsub-group">
            <a class="nsub-head has-sub" href="index.html#onpint">Caldera On Pint <svg class="caret sm" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M6 9l6 6 6-6"/></svg></a>
            <div class="nsub-items">
              <a href="yellow.html">Caldera Witbier</a>
              <a href="blue.html">Caldera Blue</a>
              <a href="strong.html">Caldera Strong</a>
            </div>
          </div>
          <div class="nsub-group">
            <a class="nsub-head" href="ontap.html">Caldera On Tap</a>
            <div class="nsub-items">
              <a href="ontap.html">Caldera Hefeweizen</a>
              <a href="ontap.html">Caldera Blue</a>
              <a href="ontap.html">Caldera Strong</a>
            </div>
          </div>
        </div>
      </div>
      {a("index.html#craft","The Craft","craft")}{a("about.html","About Us","about")}{a("blog.html","Journal","blog")}{a("faq.html","FAQ","faq")}{a("contact.html","Contact","contact")}
    </nav>
    <a class="nav-cta" href="find.html">Where to Find Caldera</a>
  </div>
  <button class="nav-tog" aria-label="Menu" aria-expanded="false"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
</div></header>'''

import re as _re
_F = build.FOOTER
_F = _re.sub(r'<div class="foot-col"><h5>The Beers</h5>.*?</div>\s*', '', _F, flags=_re.S, count=1)
_F = _F.replace('<span>\u00a9 2026 Caldera. A unit of Karnani FnB Specialities LLP. Please drink responsibly.</span>',
                '<span>\u00a9 2026 Karnani FnB Specialities LLP.</span>')
FOOTER_W = (_F
    .replace("logo_horiz_white.png","logo_horiz_black.png")
    .replace("<footer>",'<footer class="sec bg-black">',1)
    .replace('<a href="index.html#beers">Caldera Hefeweizen</a>','<a href="ontap.html">Caldera On Tap</a>')
    .replace('<a href="yellow.html">Caldera Yellow</a>','<a href="yellow.html">Caldera Witbier</a>')
    .replace('<a href="index.html#beers">Our Beers</a>','<a href="index.html#beers">Caldera On Pint</a><a href="ontap.html">Caldera On Tap</a>'))
SCRIPT_W = '<script src="assets/caldera-white.js"></script>'

PAGE_SLUGS = ["index","ontap","yellow","blue","strong","about","faq","find","blog","contact","privacy"]

def pretty(slug):
    """find.html -> /find ; index.html -> /"""
    stem = slug[:-5] if slug.endswith(".html") else slug
    return "/" if stem == "index" else "/" + stem

def canon(slug):
    return SITE_URL + pretty(slug)

def standalone_w(title, desc, body, active, bodyclass="", slug="index.html"):
    bc = f' class="{bodyclass}"' if bodyclass else ""
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            + HEADBITS_W.format(title=title,desc=desc) + '\n'
            + SOCIAL_W.format(url=canon(slug), title=title, desc=desc, site=SITE_URL) + '\n</head>\n<body'+bc+'>\n'
            + nav_w(active) + '\n<main>\n' + body + '\n</main>\n' + FOOTER_W + '\n' + SCRIPT_W + '\n</body>\n</html>\n')

def beer_card(img, acc, style, name, desc, body, taste, abv, serve, badges, link):
    tastes="".join(f"<span>{t}</span>" for t in taste)
    bdg="".join(f'<span class="fmt-badge">{b}</span>' for b in badges)
    return f'''  <article class="pshow" style="--acc:var(--{acc})">
    <div class="pshow-media"><img src="assets/{img}" alt="Caldera {name} bottle"></div>
    <div class="pshow-copy">
      <div class="pshow-style rv">{style}</div>
      <h2 class="pshow-name rv d1">CALDERA <b>{name}</b></h2>
      <div class="pshow-desc rv d1">{desc}</div>
      <p class="pshow-body rv d2">{body}</p>
      <div class="pshow-taste rv d2">{tastes}</div>
      <div class="pshow-abv rv d2"><div class="a"><b>{abv}</b><span>ABV v/v</span></div><div class="a"><b>{serve}</b><span>Serve</span></div></div>
      <div class="fmt-badges rv d3">{bdg}</div>
      <div class="pshow-foot rv d3"><a class="pshow-link" href="{link}">Discover {name.title()} <span class="arw">&rarr;</span></a></div>
    </div>
  </article>'''

# ===================== HOME =====================
HERO_W = '''<section id="hero" class="sec bg-black hero-dark">
  <div class="hero-media"><video id="heroVid" autoplay muted loop playsinline preload="auto" poster="assets/hero_poster.jpg" aria-label="A glass of Caldera being poured at the bar"><source src="assets/hero.webm" type="video/webm"><source src="assets/hero.mp4" type="video/mp4"></video></div>
  <div class="hero-dark-scrim"></div>
  <div class="hero-dark-inner">
    <h1 class="hero-big">Calcutta's Finest Craft</h1>
    <p class="hero-sub2">Distinctive craft beers, brewed in Calcutta.<br>Enjoy Caldera on tap or by the pint.</p>
    <div class="hero-ctas"><a class="btn btn-gold" href="#beers">Explore Our Beers</a><a class="btn btn-ghost" href="find.html">Where to Find Caldera</a></div>
  </div>
</section>'''

STATEMENT_W = '''<section class="sec bg-white statement"><div class="wrap maxw">
  <div class="eyebrow tag">Made for moments together</div>
  <p class="big" data-words>Some plans start with "just one." Then an old story comes up, someone pulls up a chair, and there's another reason to stay. Caldera is brewed for the pleasure of good beer and <em>good company.</em></p>
</div></section>'''

RANGE_W = f'''<section id="beers" class="sec bg-white">
  <div class="wrap maxw"><div class="ib-head rangehead">
    <h2 class="rangetitle">Our Beers</h2>
    <p>Like it citrusy, crisp or full-bodied? Get to know the Caldera range and find the beer that suits your taste.</p>
    <div class="range-cats">
      <a class="range-cat" href="#onpint"><span class="rc-k">Caldera</span><span class="rc-v">On Pint</span></a>
      <a class="range-cat" href="ontap.html"><span class="rc-k">Caldera</span><span class="rc-v">On Tap</span></a>
    </div>
  </div></div>
  <div class="wrap maxw" id="onpint"><div class="bandhead rv">
    <div><h3 class="pshow-name pintname">CALDERA <b>ON PINT</b></h3></div>
    <a class="pshow-link" href="find.html">Where to Find Bottles <span class="arw">&rarr;</span></a>
  </div></div>
{beer_card("witbier_travertine.jpg","wit","Belgian-Style Wheat Beer","WITBIER","Citrusy &amp; Spicy","Bright citrus, gentle spice and soft wheat come together in an easygoing Belgian-style wheat beer.",["Citrus","Gentle spice","Soft wheat"],"&lt; 5%","4&ndash;6&deg;C",["On Pint"],"yellow.html")}
{beer_card("blue_blue.jpg","blue","German-Style Pilsner","BLUE","Crispy &amp; Dry","Clean malt, balanced hop bitterness and a refreshing finish. A German-style pilsner for those who like their beer crisp.",["Clean malt","Balanced bitterness","Dry finish"],"&lt; 5%","4&ndash;6&deg;C",["On Tap","On Pint"],"blue.html")}
{beer_card("strong_red.jpg","strong","Strong Lager","STRONG","Smooth &amp; Roasty","A fuller-bodied lager with rich malt character and a smooth finish. For those who prefer a bolder beer.",["Rich malt","Full body","Smooth finish"],"&lt; 8%","4&ndash;6&deg;C",["On Tap","On Pint"],"strong.html")}
</section>'''

KIOSK_W = '''<section class="sec bg-black tapcine"><div class="wrap maxw">
  <div class="tapcine-head rv">
    <div><h3 class="pshow-name tapname">CALDERA <b>ON TAP</b></h3></div>
    <a class="pshow-link" href="ontap.html">See What's on Tap <span class="arw">&rarr;</span></a>
  </div>
  <div class="tapcine-stage rv d1"><video id="tapVid" muted loop playsinline preload="none" poster="assets/tap_poster.jpg" aria-label="Caldera on tap — beer tower and fresh pours" data-webm="assets/tap.webm" data-mp4="assets/tap.mp4"></video></div>
</div></section>'''

CRAFT_PTS = '''    <div class="craft-pts">
      <div class="craft-pt rv d2"><div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5s6.5-5.8 6.5-10.5a6.5 6.5 0 1 0-13 0C5.5 15.7 12 21.5 12 21.5z"/><circle cx="12" cy="10.8" r="2.4"/></svg></div><h4>Brewed in Calcutta</h4><p>Our home is Calcutta. Our beer belongs wherever the city gets together.</p></div>
      <div class="craft-pt rv d2"><div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h10l-1 15.4A2 2 0 0 1 14 20.2h-4a2 2 0 0 1-2-1.8L7 3z"/><path d="M7.4 9h9.2"/></svg></div><h4>A style for your taste</h4><p>From soft wheat beers to crisp pilsner and fuller-bodied lager, there's more than one way to enjoy Caldera.</p></div>
      <div class="craft-pt rv d3"><div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5v19M3.6 7.25l16.8 9.5M20.4 7.25l-16.8 9.5"/></svg></div><h4>Enjoy it chilled</h4><p>Serve at 4&ndash;6&deg;C in a clean glass, with room for the head to settle. Take a moment to enjoy the aroma before your first sip.</p></div>
      <div class="craft-pt rv d3"><div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M15.8 8.2l-2.1 5.5-5.5 2.1 2.1-5.5 5.5-2.1z"/></svg></div><h4>Get to know the range</h4><p>Explore each beer for its style, flavour and serving details.</p></div>
    </div>'''

CRAFT_W = '''<section id="craft" class="sec bg-white">
  <div class="wrap maxw craft-inner">
    <div class="eyebrow rv">The Craft</div>
    <h2 class="rv d1" style="margin-top:16px">A little more about <em>your beer.</em></h2>
    <p class="lead rv d1">Every Caldera has its own character. Get to know what's in your glass, find the style you enjoy, and let us take care of the brewing.</p>
''' + CRAFT_PTS + '''
  </div>
</section>'''

CHEERS_W = '''<section class="sec bg-white imgband"><div class="wrap maxw">
  <figure><img src="assets/cheers_bridge.jpg" alt="Friends toasting with Caldera, Howrah Bridge and the Hooghly at twilight behind" id="cheersImg">
    <div class="ib-cap"><span class="eyebrow">Your Caldera</span><h2>Good company. Great pours. <em>Endless adda.</em></h2><p>The place can change. The pleasure of catching up stays the same.</p></div>
  </figure>
</div></section>'''

CAL_W = '''<section id="cal" class="sec bg-white"><div class="wrap maxw">
  <div class="eyebrow tag">The Cal Way of Life</div>
  <p class="quote">There's always more to <em>talk about.</em></p>
  <p class="cal-body">An old friend. A familiar table. A conversation that wanders from football to food and somehow back again. In Calcutta, that's a perfectly good plan. Pull up a chair. Make time for your people.</p>
  <div class="cal-sub">Meet Cal. Always up for an adda.</div>
</div></section>'''

FINDHOME_W = '''<section id="find" class="sec bg-white findsec"><div class="wrap maxw">
  <div class="eyebrow">Find Caldera</div>
  <h2>Where's your next <em>Caldera?</em></h2>
  <p class="note">Looking for Caldera on tap or by the pint? Tell us your area and which beer you're after. We'll help you check availability.</p>
  <div class="cta-btns"><a class="btn btn-gold" href="ontap.html">Find on Tap</a><a class="btn btn-ghost" href="find.html">Find on Pint</a><a class="btn btn-ghost" href="contact.html">Partner with Us</a></div>
  <p class="note" style="font-size:.84rem;margin-top:16px">Availability can change. Please check with the outlet before visiting.</p>
  <p class="legalnote">Available at licensed outlets only. We do not sell alcohol online.</p>
</div></section>'''

CRATE_W = '''<section class="sec bg-white imgband"><div class="wrap maxw">
  <figure><img src="assets/crate_dark.jpg" alt="The Caldera range on ice" id="bandImg"></figure>
</div></section>'''

HOME_W = "\n".join([HERO_W, STATEMENT_W, CRATE_W, RANGE_W, KIOSK_W, CRAFT_W, CHEERS_W, CAL_W, FINDHOME_W])

# ===================== CALDERA ON TAP page =====================
def tapcard(acc, name, style, desc, note, link):
    return f'''  <article class="tapcard rv" style="--acc:var(--{acc})">
    <div class="tc-top"><span class="pshow-style">{style}</span><h3 class="tc-name">CALDERA <b>{name}</b></h3></div>
    <div class="pshow-desc tc-desc">{desc}</div>
    <p class="tc-body">{note}</p>
    <div class="fmt-badges"><span class="fmt-badge">On Tap</span></div>
    <a class="pshow-link" href="{link}">More about {name.title()} <span class="arw">&rarr;</span></a>
  </article>'''

ONTAP = '''<section class="sec bg-white chero"><div class="wrap maxw">
  <div class="eyebrow">Caldera On Tap</div>
  <h1>Fresh from the <em>keg.</em></h1>
  <p>Draught Caldera, poured at bars, restaurants, caf&eacute;s and taprooms across the city. Here's what you'll find on tap.</p>
</div></section>

<section class="sec bg-black tapcine"><div class="wrap maxw">
  <div class="tapcine-head rv">
    <div><h3 class="pshow-name tapname">CALDERA <b>ON TAP</b></h3></div>
  </div>
  <div class="tapcine-stage rv d1"><video id="tapVid" muted loop playsinline preload="none" poster="assets/tap_poster.jpg" aria-label="Caldera on tap — beer tower and fresh pours" data-webm="assets/tap.webm" data-mp4="assets/tap.mp4"></video></div>
</div></section>

<section class="sec bg-white tapsec"><div class="wrap maxw">
  <h2 class="rv">Available on tap.</h2>
  <p class="tapsec-lead rv">Three Caldera styles are poured on draught. Ask your venue which one is running &mdash; or get in touch and we'll point you to the nearest tap.</p>
  <div class="tap-grid">
''' + "\n".join([
  tapcard("hefe","HEFEWEIZEN","German-Style Wheat Beer","Fruity &amp; Smooth","Our wheat beer, poured fresh from the tower. Soft, hazy and easy-drinking &mdash; only ever on tap, never bottled.","contact.html"),
  tapcard("blue","BLUE","German-Style Pilsner","Crispy &amp; Dry","Clean malt and balanced hop bitterness with a refreshing, dry finish. Crisp on draught.","blue.html"),
  tapcard("strong","STRONG","Strong Lager","Smooth &amp; Roasty","A fuller-bodied lager with rich malt character and a smooth, rounded finish.","strong.html"),
]) + '''
  </div>
</div></section>

<section class="sec bg-white findsec"><div class="wrap maxw">
  <div class="eyebrow">Pouring Near You</div>
  <h2>Find Caldera <em>on tap.</em></h2>
  <p class="note">Tell us your area and the beer you're after, and we'll help you track down the nearest pour.</p>
  <div class="cta-btns"><a class="btn btn-gold" href="contact.html">Ask Where It's on Tap</a><a class="btn btn-ghost" href="find.html">Find on Pint</a></div>
  <p class="legalnote">Available at licensed outlets only. We do not sell alcohol online.</p>
</div></section>'''

import re
# ---- beer pages ----
BADGES = {"yellow":["On Pint"], "blue":["On Tap","On Pint"], "strong":["On Tap","On Pint"]}
def dress_beer(html, key):
    html = (html.replace("Bottle &amp; Tap","On Tap &middot; On Pint").replace("Bottled (330 ml)","On Pint (bottle)")
                .replace("Citrusy &amp; smooth.","Citrusy &amp; Spicy")
                .replace("Crisp &amp; dry.","Crispy &amp; Dry")
                .replace("Bold &amp; smooth.","Smooth &amp; Roasty"))
    bdg = '<div class="fmt-badges">'+''.join(f'<span class="fmt-badge">{b}</span>' for b in BADGES[key])+'</div>'
    html = html.replace('<div class="bhero-ctas">', bdg+'<div class="bhero-ctas">', 1)
    # base of every pint page: the range-on-ice shot, shown on white
    m = re.search(r'<div class="cta-btns">(.*?)</div>', html, re.S)
    oth = m.group(1) if m else ''
    newbase = ('<section class="sec bg-white imgband pintbase"><div class="wrap maxw">\n'
               '  <figure><img src="assets/crate_dark.jpg" alt="The Caldera range on ice"></figure>\n'
               '</div></section>\n\n'
               '<section class="sec bg-white findsec"><div class="wrap maxw">\n'
               '  <div class="eyebrow">Explore the Range</div>\n'
               '  <h2>Thirsty for <em>more?</em></h2>\n'
               '  <div class="cta-btns">' + oth + '</div>\n'
               '  <p class="legalnote">Available at licensed outlets only. We do not sell alcohol online.</p>\n'
               '</div></section>')
    html = re.sub(r'<section class="findsec rangesec".*?</section>', newbase, html, flags=re.S)
    return html

yellow_w = dress_beer(build.yellow, "yellow")
blue_w   = dress_beer(build.blue,   "blue")
strong_w = dress_beer(build.strong, "strong")

# ---- about: drop struck eyebrow + the four vanity stats ----
import re
ABOUT_W = build.ABOUT
ABOUT_W = ABOUT_W.replace('<span class="eyebrow rv">Karnani FnB Specialities LLP</span>\n    ','')
ABOUT_W = re.sub(r'<div class="bstats">.*?</div>\s*</div>\s*', '', ABOUT_W, flags=re.S, count=1)
ABOUT_W = ABOUT_W.replace('<div class="infobox" style="margin-top:28px">','<div class="infobox about-info">')

FIND_W = (build.FIND.replace("In Bottles","On Pint")
          .replace("Ask Where to Buy Bottles","Ask Where to Get a Pint")
          .replace("Grab a 330 ml bottle to take home from licensed stores and retailers stocking Caldera.",
                   "Grab a 330 ml pint bottle to take home from licensed stores and retailers stocking Caldera."))

pages = {
  "index.html":   ("Caldera Craft Beer", "Caldera - Calcutta's Finest Craft Beer. Craft styles brewed in Kolkata. Enjoy Caldera on tap and on pint.", HOME_W, "beers", ""),
  "ontap.html":   ("Caldera On Tap", "Caldera on tap - Hefeweizen, Blue and Strong poured fresh from the keg at venues across Kolkata.", ONTAP, "beers", ""),
  "yellow.html":  ("Caldera Witbier", "Caldera Witbier - Belgian-style wheat beer. Citrusy and spicy. ABV below 5%.", yellow_w, "beers", ""),
  "blue.html":    ("Caldera Blue", "Caldera Blue - German-style Pilsner. Crispy and dry. ABV below 5%.", blue_w, "beers", ""),
  "strong.html":  ("Caldera Strong", "Caldera Strong - Strong Lager. Smooth and roasty. ABV below 8%.", strong_w, "beers", ""),
  "about.html":   ("About Caldera", "About Caldera - Calcutta's Finest Craft, brewed by Karnani FnB Specialities LLP in Kolkata.", ABOUT_W, "about", ""),
  "faq.html":     ("Caldera FAQ", "Caldera FAQ - craft beer explained, lager vs ale, and where to find Caldera in Kolkata.", build.FAQ, "faq", ""),
  "find.html":    ("Find Caldera", "Find Caldera on tap and on pint at licensed outlets across Kolkata.", FIND_W, "find", ""),
  "blog.html":    ("The Cal Journal - Caldera", "The Cal Journal - stories on craft beer, Calcutta and the Caldera way of life.", build.BLOG, "blog", ""),
  "contact.html": ("Contact Caldera", "Contact Caldera - find us on tap or on pint, stock our bottles, or partner with us.", build.CONTACT, "contact", ""),
  "privacy.html": ("Privacy Policy - Caldera", "Caldera privacy policy - how Karnani FnB Specialities LLP handles information shared through this website.", build.PRIVACY, "", ""),
}
DROP = [
  '<p class="note" style="font-size:.84rem;margin-top:16px">Availability can change. Please check with the outlet before visiting.</p>',
  '<p class="legalnote">Available at licensed outlets only. We do not sell alcohol online.</p>',
]
def clean(html):
    for d in DROP:
        html = html.replace(d, '')
    # never strand a lone word: bind short trailing tokens to the word before
    html = html.replace('Karnani FnB Specialities LLP', 'Karnani FnB Specialities&nbsp;LLP')
    html = html.replace('86A Topsia Road (S), Kolkata 700046', '86A Topsia Road (S), Kolkata&nbsp;700046')
    html = html.replace('Ask Where to Get a Pint', 'Ask Where to Get a&nbsp;Pint')
    html = html.replace('Ask Where It\'s on Tap', 'Ask Where It\'s on&nbsp;Tap')
    html = html.replace('enjoyed over good conversation.', 'enjoyed over good&nbsp;conversation.')
    html = prettify_links(html)
    return html

def prettify_links(html):
    """index.html#beers -> /#beers ; find.html -> /find"""
    def sub(m):
        stem, frag = m.group(1), m.group(2) or ''
        if stem not in PAGE_SLUGS: return m.group(0)
        return 'href="%s%s"' % (pretty(stem), frag)
    return re.sub(r'href="/?([A-Za-z0-9_-]+)\.html(#[A-Za-z0-9_-]+)?"', sub, html)

for fn,(t,d,b,a,bc) in pages.items():
    (WHITE/fn).write_text(clean(standalone_w(t,d,b,a,bc,fn)), encoding="utf-8")
print("white built:", ", ".join(pages.keys()))
