# -*- coding: utf-8 -*-
import pathlib
import os
SITE = pathlib.Path(os.environ.get("CALDERA_SITE",
    pathlib.Path(__file__).resolve().parent.parent / "_work" / "site"))
SITE.mkdir(parents=True, exist_ok=True)   # scratch tree; git-ignored

HEADBITS = '''<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta name="theme-color" content="#090705">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500&family=Oswald:wght@400;500;600;700&family=Rock+Salt&display=swap">
<link rel="stylesheet" href="assets/caldera.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>'''

def nav(active=""):
    def a(href,label,key):
        cls=' class="active"' if key==active else ''
        return f'<a href="{href}"{cls}>{label}</a>'
    return f'''<header id="nav"><div class="wrap maxw nav-row">
  <a class="brand" href="index.html" aria-label="Caldera home"><img src="assets/logo_horiz_white.png" alt="Caldera — Calcutta's Finest Craft"></a>
  <div class="nav-right">
    <nav class="nav-links" aria-label="Primary">
      <div class="nav-drop">
        <a class="nav-droptrig{' active' if active=='beers' else ''}" href="index.html#beers">Our Beers <svg class="caret" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="nav-sub">
          <a href="yellow.html">Caldera Witbier</a>
          <a href="blue.html">Caldera Blue</a>
          <a href="strong.html">Caldera Strong</a>
        </div>
      </div>
      {a("index.html#craft","The Craft","craft")}{a("about.html","About Us","about")}{a("blog.html","Journal","blog")}{a("faq.html","FAQ","faq")}{a("contact.html","Contact","contact")}
    </nav>
    <a class="nav-cta" href="find.html">Where to Find Caldera</a>
  </div>
  <button class="nav-tog" aria-label="Menu" aria-expanded="false"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
</div></header>'''

FOOTER = '''<footer><div class="wrap maxw">
  <div class="foot-top">
    <div class="foot-brand">
      <img src="assets/logo_horiz_white.png" alt="Caldera">
      <p>Calcutta's Finest Craft. Brewed in Calcutta, enjoyed over good conversation.</p>
      <div class="foot-social">
        <a href="https://instagram.com/caldera.craftbeer/" target="_blank" rel="noopener" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
        <a href="https://facebook.com/caldera.craftbeer/" target="_blank" rel="noopener" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3V6h-3c-2 0-3.5 1.5-3.5 3.5V11H8v3h2.5v7h3v-7H16l.5-3h-3V9.5c0-.3.2-.5.5-.5z"/></svg></a>
      </div>
    </div>
    <div class="foot-col"><h5>Explore</h5><a href="index.html#beers">Our Beers</a><a href="find.html">Where to Find</a><a href="about.html">About Us</a><a href="blog.html">Journal</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a></div>
    <div class="foot-col"><h5>The Beers</h5><a href="yellow.html">Caldera Yellow</a><a href="blue.html">Caldera Blue</a><a href="strong.html">Caldera Strong</a><a href="index.html#beers">Caldera Hefeweizen</a></div>
    <div class="foot-col"><h5>Get in Touch</h5><p>Karnani FnB Specialities LLP</p><p style="color:var(--txt-faint);font-size:.82rem">Haute Street Corporate Park,<br>86A Topsia Road (S), Kolkata 700046</p><a href="tel:18001233415">1800 123 3415</a><a href="mailto:hello@caldera.beer">hello@caldera.beer</a><p style="color:var(--txt-faint);font-size:.78rem">FSSAI Lic. 12819019001451</p></div>
  </div>
  <div class="statutory"><span class="s">Consumption of alcohol is injurious to health</span><span class="s">Don't drink &amp; drive</span><span class="s">Not for sale to persons below 21 years</span><span class="s">For sale in West Bengal only</span><span class="s">Produce of India</span></div>
  <div class="foot-legal"><span>© 2026 Caldera. A unit of Karnani FnB Specialities LLP. Please drink responsibly.</span><span><a href="privacy.html">Privacy Policy</a> · Calcutta's Finest Craft</span></div>
</div></footer>'''

SCRIPT = '<script src="assets/caldera.js"></script>'

# ---- Calcutta skyline line-art (licensed artwork, text removed + gold-tinted) ----
CITYLINE = '<img src="assets/skyline_kol.png" alt="" aria-hidden="true" class="cityart">'

# inject skyline band at the top of the footer
FOOTER = FOOTER.replace('<footer><div class="wrap maxw">',
                        '<footer><div class="wrap maxw"><div class="foot-skyline">' + CITYLINE + '</div>', 1)

def standalone(title, desc, body, active):
    return (f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            + HEADBITS.format(title=title,desc=desc) + '\n</head>\n<body>\n'
            + nav(active) + '\n<main>\n' + body + '\n</main>\n' + FOOTER + '\n' + SCRIPT + '\n</body>\n</html>\n')

def bodyonly(title, desc, body, active):
    return (HEADBITS.format(title=title,desc=desc) + '\n' + nav(active) + '\n<main>\n' + body + '\n</main>\n' + FOOTER + '\n' + SCRIPT + '\n')

# ---------------- HOME ----------------
def beer_section(num, img, acc, style, name, desc, body, taste, abv, serve, fmt, link):
    tastes="".join(f"<span>{t}</span>" for t in taste)
    return f'''  <article class="pshow" style="--acc:var(--{acc})">
    <div class="pshow-media"><img src="assets/{img}" alt="Caldera {name} bottle"></div>
    <div class="pshow-copy">
      <div class="pshow-num rv">{num}</div>
      <div class="pshow-style rv">{style}</div>
      <h2 class="pshow-name rv d1">CALDERA <b>{name}</b></h2>
      <div class="pshow-desc rv d1">{desc}</div>
      <p class="pshow-body rv d2">{body}</p>
      <div class="pshow-taste rv d2">{tastes}</div>
      <div class="pshow-abv rv d2"><div class="a"><b>{abv}</b><span>ABV v/v</span></div><div class="a"><b>{serve}</b><span>Serve</span></div></div>
      <div class="pshow-foot rv d3"><span class="pshow-fmt">{fmt}</span><a class="pshow-link" href="{link}">Discover {name.title()} <span class="arw">→</span></a></div>
    </div>
  </article>'''

HOME = f'''<section id="hero">
  <div class="hero-media"><video id="heroVid" autoplay muted loop playsinline preload="auto" poster="assets/hero_poster.jpg" aria-label="A glass of Caldera being poured at the bar"><source src="assets/hero.webm" type="video/webm"><source src="assets/hero.mp4" type="video/mp4"></video></div>
  <div class="hero-scrim"></div>
  <div class="hero-sweep"></div>
  <div class="wrap maxw hero-inner">
    <div class="hero-copy">
      <div class="hero-eyebrow"><span class="eyebrow">Calcutta's Finest Craft</span></div>
      <h1 class="hero-h1"><span class="ln"><span>The Calm</span></span><span class="ln"><span>in the <em>Chaos.</em></span></span></h1>
      <p class="hero-sub">Distinctive craft beers, brewed in Calcutta. Find your favourite — in bottles or on tap.</p>
      <div class="hero-ctas"><a class="btn btn-gold" href="#beers">Explore Our Beers</a><a class="btn btn-ghost" href="find.html">Where to Find Caldera</a></div>
      <div class="hero-meta"><div class="m"><b>04</b><span>Craft Styles</span></div><div class="m"><b>02</b><span>Ways to Pour</span></div><div class="m"><b>01</b><span>City We Love</span></div></div>
    </div>
  </div>
  <div class="scroll-cue"><span>Scroll</span><i></i></div>
</section>

<section class="statement"><div class="wrap maxw">
  <div class="eyebrow tag">Made for moments together</div>
  <p class="big" data-words>Some plans start with "just one." Then an old story comes up, someone pulls up a chair, and there's another reason to stay. Caldera is brewed for the pleasure of good beer and <em>good company.</em></p>
</div></section>

<section class="band">
  <img src="assets/crate_dark.jpg" alt="The Caldera range on ice" id="bandImg">
  <div class="wrap maxw band-inner">
    <span class="eyebrow rv">The Range</span>
    <h2 class="rv d1">Four styles.<br>Plenty of <em>character.</em></h2>
    <p class="rv d2">Like it citrusy, crisp or full-bodied? Get to know the Caldera range and find the beer that suits your taste.</p>
  </div>
</section>

<section id="beers">
{beer_section("01 / Yellow","witbier_travertine.jpg","wit","Belgian-Style Wheat Beer","WITBIER","Citrusy &amp; smooth.","Bright citrus, gentle spice and soft wheat come together in an easygoing Belgian-style wheat beer.",["Citrus","Gentle spice","Soft wheat"],"&lt; 5%","4–6°C","Bottled","yellow.html")}
{beer_section("02 / Blue","blue_blue.jpg","blue","German-Style Pilsner","BLUE","Crisp &amp; dry.","Clean malt, balanced hop bitterness and a refreshing finish. A German-style pilsner for those who like their beer crisp.",["Clean malt","Balanced bitterness","Dry finish"],"&lt; 5%","4–6°C","Bottle &amp; Tap","blue.html")}
{beer_section("03 / Strong","strong_red.jpg","strong","Strong Lager","STRONG","Bold &amp; smooth.","A fuller-bodied lager with rich malt character and a smooth finish. For those who prefer a bolder beer.",["Rich malt","Full body","Smooth finish"],"&lt; 8%","4–6°C","Bottle &amp; Tap","strong.html")}
</section>

<section class="tapcine"><div class="wrap maxw">
  <div class="tapcine-head rv">
    <div><div class="pshow-style">German-Style Wheat Beer · On Tap Only</div><h3 class="pshow-name" style="--acc:var(--hefe)">CALDERA <b style="color:var(--hefe)">HEFEWEIZEN</b></h3></div>
    <a class="pshow-link" href="contact.html" style="--acc:var(--hefe)">Ask About Hefeweizen on Tap <span class="arw">→</span></a>
  </div>
  <div class="tapcine-stage rv d1"><video id="tapVid" muted loop playsinline preload="none" poster="assets/tap_poster.jpg" aria-label="Caldera on tap — beer tower and fresh pours" data-webm="assets/tap.webm" data-mp4="assets/tap.mp4"></video></div>
</div></section>

<section id="craft">
  <div class="craft-bg"><img src="assets/glass_barley.jpg" alt="Caldera with malted barley" id="craftImg"></div>
  <div class="wrap maxw craft-inner">
    <div class="eyebrow rv">The Craft</div>
    <h2 class="rv d1" style="margin-top:16px">A little more about <em>your beer.</em></h2>
    <p class="lead rv d1">Every Caldera has its own character. Get to know what's in your glass, find the style you enjoy, and let us take care of the brewing.</p>
    <div class="craft-pts">
      <div class="craft-pt rv d2"><div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5s6.5-5.8 6.5-10.5a6.5 6.5 0 1 0-13 0C5.5 15.7 12 21.5 12 21.5z"/><circle cx="12" cy="10.8" r="2.4"/></svg></div><h4>Brewed in Calcutta</h4><p>Our home is Calcutta. Our beer belongs wherever the city gets together.</p></div>
      <div class="craft-pt rv d2"><div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h10l-1 15.4A2 2 0 0 1 14 20.2h-4a2 2 0 0 1-2-1.8L7 3z"/><path d="M7.4 9h9.2"/></svg></div><h4>A style for your taste</h4><p>From soft wheat beers to crisp pilsner and fuller-bodied lager, there's more than one way to enjoy Caldera.</p></div>
      <div class="craft-pt rv d3"><div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5v19M3.6 7.25l16.8 9.5M20.4 7.25l-16.8 9.5"/><path d="M12 5.8l2.3-1.3M12 5.8 9.7 4.5M12 18.2l2.3 1.3M12 18.2 9.7 19.5M5.1 8.9l-.3-2.6M5.1 8.9l-2.5.6M18.9 15.1l.3 2.6M18.9 15.1l2.5-.6M18.9 8.9l2.5.6M18.9 8.9l.3-2.6M5.1 15.1l-2.5-.6M5.1 15.1l-.3 2.6"/></svg></div><h4>Enjoy it chilled</h4><p>Serve at 4–6°C in a clean glass, with room for the head to settle. Take a moment to enjoy the aroma before your first sip.</p></div>
      <div class="craft-pt rv d3"><div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M15.8 8.2l-2.1 5.5-5.5 2.1 2.1-5.5 5.5-2.1z"/></svg></div><h4>Get to know the range</h4><p>Explore each beer for its style, flavour and serving details.</p></div>
    </div>
  </div>
</section>

<section class="cheers">
  <img src="assets/cheers_bridge.jpg" alt="Three friends toasting with Caldera Blue, Witbier and Strong, Howrah Bridge and the Hooghly at twilight behind" id="cheersImg">
  <div class="cheers-scrim"></div>
  <div class="wrap maxw cheers-cap">
    <span class="eyebrow rv">Your Caldera</span>
    <h2 class="rv d1">Good company. Great pours.<br><em>Endless adda.</em></h2>
    <p class="cheers-sub rv d2">The place can change. The pleasure of catching up stays the same.</p>
  </div>
</section>

<section id="cal"><div class="wrap maxw">
  <div class="eyebrow tag">The Cal Way of Life</div>
  <p class="quote">There's always more to <em>talk about.</em></p>
  <p class="cal-body">An old friend. A familiar table. A conversation that wanders from football to food and somehow back again. In Calcutta, that's a perfectly good plan. Pull up a chair. Make time for your people.</p>
  <div class="cal-sub">Meet Cal. Always up for an adda.</div>
</div><div class="cityline">{CITYLINE}</div></section>

<section id="find" class="findsec"><div class="wrap maxw">
  <div class="eyebrow">Find Caldera</div>
  <h2>Where's your next <em>Caldera?</em></h2>
  <p class="note">Looking for Caldera on tap or a store stocking our bottles? Tell us your area and which beer you're after. We'll help you check availability.</p>
  <div class="cta-btns"><a class="btn btn-gold" href="find.html">Find on Tap</a><a class="btn btn-ghost" href="find.html">Find Bottles</a><a class="btn btn-ghost" href="contact.html">Partner with Us</a></div>
  <p class="note" style="font-size:.84rem;margin-top:16px">Availability can change. Please check with the outlet before visiting.</p>
  <p class="legalnote">Available at licensed outlets only. We do not sell alcohol online.</p>
</div></section>'''

# ---------------- BEER PAGE ----------------
def beer_page(title, acc, style, ident, name, desc, sub, hero_img, shot1, shot2, abv, fmt,
              lead, para, aroma, mouthfeel, ingredients, pairing, other):
    tastes="".join(f"<span>{t}</span>" for t in aroma['chips'])
    oth="".join(f'<a class="btn btn-ghost" href="{h}">{l}</a>' for l,h in other)
    return f'''<section class="bhero" style="--acc:var(--{acc})">
  <div class="bhero-media"><img src="assets/{hero_img}" alt="Caldera {name} bottle and glass"></div>
  <div class="bhero-copy">
    <div class="crumb"><a href="index.html">Home</a> · <a href="index.html#beers">Our Beers</a> · {name.title()}</div>
    <div class="bhero-style">{style}</div>
    <h1 class="bhero-name">CALDERA <b>{name}</b></h1>
    <div class="bhero-desc">{desc}</div>
    <p class="bhero-sub">{sub}</p>
    <div class="bhero-ctas"><a class="btn btn-gold" href="find.html">Find {name.title()}</a><a class="btn btn-ghost" href="index.html#beers">All Beers</a></div>
  </div>
</section>

<section class="specs" style="--acc:var(--{acc})"><div class="wrap maxw">
  <div class="specs-grid">
    <div class="spec"><span class="k">ABV</span><span class="v acc">{abv}</span></div>
    <div class="spec"><span class="k">Style</span><span class="v">{style.split(' · ')[0]}</span></div>
    <div class="spec"><span class="k">Serve</span><span class="v">4–6°C</span></div>
    <div class="spec"><span class="k">Format</span><span class="v">{fmt}</span></div>
  </div>
</div></section>

<section class="detail" style="--acc:var(--{acc})"><div class="wrap maxw detail-grid">
  <div class="rv">
    <div class="eyebrow">Tasting Notes</div>
    <h2 style="margin-top:14px">{lead}</h2>
    <p>{para}</p>
    <p><b style="color:var(--txt)">Aroma.</b> {aroma['text']}</p>
    <p><b style="color:var(--txt)">Mouthfeel.</b> {mouthfeel}</p>
    <div class="taste">{tastes}</div>
  </div>
  <div class="infobox rv d1">
    <div class="row"><span class="k">ABV</span><span class="v">{abv} v/v</span></div>
    <div class="row"><span class="k">Style</span><span class="v">{style}</span></div>
    <div class="row"><span class="k">Serving Temperature</span><span class="v">4–6°C · in the Monaco Slim glass</span></div>
    <div class="row"><span class="k">Format</span><span class="v">{fmt}</span></div>
    <div class="row"><span class="k">Ingredients</span><span class="v">{ingredients}</span></div>
  </div>
</div></section>

<section class="findsec rangesec" style="--acc:var(--{acc})">
  <img class="range-bg" src="assets/range_bar.jpg" alt="The Caldera range on the bar">
  <div class="range-scrim"></div>
  <div class="wrap maxw rangesec-inner">
    <div class="eyebrow">Explore the Range</div>
    <h2>Thirsty for <em>more?</em></h2>
    <div class="cta-btns">{oth}</div>
    <p class="legalnote">Available at licensed outlets only. We do not sell alcohol online.</p>
  </div>
</section>'''

yellow = beer_page(
  "Caldera Yellow","wit","Belgian-Style Wheat Beer","yellow","WITBIER",
  "Citrusy &amp; smooth.","Bright citrus and a little spice give Caldera Witbier its easygoing character. Soft wheat rounds out the flavour, with a refreshing finish that keeps things light on the palate.",
  "yellow_hero.jpg","witbier_travertine.jpg","witbier_glass.jpg","&lt; 5%","Bottled (330 ml)",
  "If you enjoy a softer beer with a citrus lift, start here.",
  "Bright citrus, gentle spice and soft wheat come together in an easygoing Belgian-style wheat beer.",
  {"text":"Fresh orange peel and coriander over soft clove and cereal wheat.","chips":["Citrus","Gentle spice","Soft wheat"]},
  "A long-lasting white head and a medium, creamy body mellow the hop bitterness, with smooth carbonation and a clean, refreshing finish.",
  "Water, Malted Barley, Malted Wheat, Hops, Yeast, CO₂ &amp; Ethyl Alcohol (generated in the process).",
  "Vegetable cutlets, lightly spiced paneer, pizza, cheesy starters &amp; citrus-dressed salads.",
  [("Caldera Blue","blue.html"),("Caldera Strong","strong.html")])

blue = beer_page(
  "Caldera Blue","blue","German-Style Pilsner","blue","BLUE",
  "Crisp &amp; dry.","Caldera Blue brings clean malt and balanced hop bitterness together in a crisp, refreshing pilsner. It finishes dry, with a clean taste that lets the beer speak for itself.",
  "blue_hero.jpg","blue_blue.jpg","blue_glass.jpg","&lt; 5%","Bottle &amp; Tap",
  "A good place to start if you like your lager crisp and refreshing.",
  "Clean malt, balanced hop bitterness and a refreshing finish — a German-style pilsner for those who like their beer crisp.",
  {"text":"Light cereal malt with a clean, noble-style hop lift.","chips":["Clean malt","Balanced bitterness","Dry finish"]},
  "Light-to-medium body with bright carbonation and a dry, refreshing close that keeps you coming back.",
  "Water, Malted Barley, Malted Wheat, Rice, Hops, Yeast, CO₂ &amp; Ethyl Alcohol (generated in the process).",
  "Crisp fried starters, grilled paneer, Kolkata-style chilli dishes &amp; seafood.",
  [("Caldera Yellow","yellow.html"),("Caldera Strong","strong.html")])

strong = beer_page(
  "Caldera Strong","strong","Strong Lager","strong","STRONG",
  "Bold &amp; smooth.","Caldera Strong is a fuller-bodied lager with rich malt character and a smooth finish. It has a bolder presence in the glass, with malt at the heart of its flavour.",
  "strong_hero.jpg","strong_red.jpg","strong_glass.jpg","&lt; 8%","Bottle &amp; Tap",
  "Choose this if you prefer a fuller, malt-led beer.",
  "A fuller-bodied lager with rich malt character and a smooth finish, for those who prefer a bolder beer.",
  {"text":"Toasted malt and a soft roast with a hint of caramel warmth.","chips":["Rich malt","Full body","Smooth finish"]},
  "A fuller body with smooth carbonation and a warming, rounded finish — bold but balanced.",
  "Water, Malted Barley, Malted Wheat, Rice, Hops, Yeast, CO₂ &amp; Ethyl Alcohol (generated in the process).",
  "Smoky tandoori dishes, mushroom kebabs, sausages &amp; rich, savoury food.",
  [("Caldera Yellow","yellow.html"),("Caldera Blue","blue.html")])

# ---------------- ABOUT ----------------
ABOUT = '''<section class="ahero">
  <img src="assets/brew_hall.jpg" alt="Inside the Caldera brewery">
  <div class="wrap maxw ahero-inner">
    <span class="eyebrow rv">Karnani FnB Specialities LLP</span>
    <h1 class="rv d1">Brewed in Calcutta.<br>Shared over <em>adda.</em></h1>
    <p class="rv d2">Caldera is the craft beer brand of Karnani FnB Specialities LLP, based in Kolkata. We brew for people who enjoy finding a flavour they like and sharing a good moment with the people around them.</p>
  </div>
</section>

<section class="astory"><div class="wrap maxw astory-grid">
  <div>
    <span class="eyebrow rv">Our Story</span>
    <h2 class="rv d1" style="margin-top:14px">More than where we <em>brew.</em></h2>
    <p class="body rv d1"><span class="dropcap">O</span>ur connection to Calcutta goes beyond where we brew. It's in the familiar meeting spots, the friendly disagreements and the way a quick catch-up becomes a proper adda. Those everyday moments are at the heart of Caldera.</p>
    <p class="body rv d2" style="margin-top:14px">Everyone has a different idea of their favourite beer. Some enjoy bright citrus and soft wheat. Others reach for a crisp pilsner or a fuller-bodied lager. Our four styles give you room to explore and find your own favourite — in bottles and on tap, with formats varying by beer.</p>
    <p class="body rv d2" style="margin-top:14px">We like the moments when people settle in and feel at home. A table with familiar faces. A story everyone has heard but wants to hear again. Time to talk without checking the clock. That's the feeling we want Caldera to be part of.</p>
  </div>
  <div class="rv d1">
    <div class="bstats">
      <div class="bstat"><b>04</b><span>Craft Styles</span></div>
      <div class="bstat"><b>Bottle<br>&amp; Tap</b><span>Ways to Enjoy</span></div>
      <div class="bstat"><b>Kolkata</b><span>Brewed in</span></div>
      <div class="bstat"><b>Calcutta</b><span>Finest Craft</span></div>
    </div>
    <div class="infobox" style="margin-top:28px">
      <div class="row"><span class="k" style="color:var(--amber)">The Brewery</span><span class="v">Karnani FnB Specialities LLP<br>Haute Street Corporate Park,<br>86A Topsia Road (S), Kolkata 700046</span></div>
      <div class="row"><span class="k" style="color:var(--amber)">FSSAI Licence</span><span class="v">12819019001451</span></div>
      <div class="row"><span class="k" style="color:var(--amber)">Get in Touch</span><span class="v">1800 123 3415 · hello@caldera.beer</span></div>
    </div>
  </div>
</div></section>

<section class="brewgrid"><div class="wrap maxw">
  <h2 class="rv">Inside the brewery.</h2>
  <div class="brew-cards">
    <figure class="rv tall"><img src="assets/brew_house.jpg" alt="Caldera brewhouse vessels"></figure>
    <figure class="rv d1"><img src="assets/brew_unitanks.jpg" alt="Caldera fermentation unitanks"></figure>
    <figure class="rv d1"><img src="assets/brew_hall2.jpg" alt="Caldera brewery hall"></figure>
  </div>
</div></section>

<section class="findsec"><div class="wrap maxw">
  <div class="eyebrow">Get to Know Caldera</div>
  <h2>Find your <em>Caldera.</em></h2>
  <p class="note">Get to know our beers, ask where to find them, or speak to us about serving Caldera at your venue.</p>
  <div class="cta-btns"><a class="btn btn-gold" href="index.html#beers">Explore Our Beers</a><a class="btn btn-ghost" href="contact.html">Get in Touch</a></div>
</div></section>'''

# ---------------- CONTACT ----------------
CONTACT = '''<section class="chero"><div class="wrap maxw">
  <div class="eyebrow">Get in Touch</div>
  <h1>Let's talk <em>Caldera.</em></h1>
  <p>Looking for a particular beer? Want to know where to find us? Or thinking of serving Caldera at your venue? Tell us a little about what you need and we'll help.</p>
</div></section>

<section class="contact"><div class="wrap maxw contact-grid">
  <div class="cinfo">
    <div class="block"><h4>Visit the Brewery</h4><p>Karnani FnB Specialities LLP</p><p class="sub">Haute Street Corporate Park, 86A Topsia Road (S), Kolkata — 700046, India</p></div>
    <div class="block"><h4>Call</h4><a href="tel:18001233415">1800 123 3415</a></div>
    <div class="block"><h4>Email</h4><a href="mailto:hello@caldera.beer">hello@caldera.beer</a></div>
    <div class="block"><h4>Checking Availability</h4><p class="sub">Tell us your area, preferred beer and whether you're looking for bottles or beer on tap, and we'll help you check.</p></div>
    <div class="block"><h4>Partnerships</h4><p class="sub">Run a bar, restaurant or another licensed venue? Get in touch to discuss stocking or pouring Caldera.</p></div>
    <div class="block"><h4>Follow</h4><a href="https://instagram.com/caldera.craftbeer/" target="_blank" rel="noopener">@caldera.craftbeer · Instagram</a><a href="https://facebook.com/caldera.craftbeer/" target="_blank" rel="noopener">/caldera.craftbeer · Facebook</a></div>
    <div class="block"><h4>FSSAI Licence</h4><p class="sub">12819019001451</p></div>
  </div>
  <form class="cform" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="contact">
    <p hidden><label>Don't fill this out: <input name="bot-field"></label></p>
    <div><label for="cn">Name</label><input id="cn" name="name" type="text" required placeholder="Your name"></div>
    <div><label for="ce">Email</label><input id="ce" name="email" type="email" required placeholder="you@email.com"></div>
    <div><label for="cp">Phone</label><input id="cp" name="phone" type="tel" placeholder="Optional"></div>
    <div><label for="ct">I'm reaching out to</label><select id="ct" name="enquiry"><option>Find bottles</option><option>Find beer on tap</option><option>Stock or serve Caldera</option><option>Share feedback</option><option>Something else</option></select></div>
    <div><label for="cm">Message</label><textarea id="cm" name="message" placeholder="How can we help? For availability enquiries, please include your area and the beer you're looking for."></textarea></div>
    <button class="btn btn-gold" type="submit">Send Enquiry</button>
    <p class="ok">Thanks for getting in touch. We've received your enquiry and will reply using the contact details you shared.</p>
    <p class="cnote">By submitting you confirm you are of legal drinking age (21+). We'll only use your details to reply.</p>
  </form>
</div></section>'''

# ---------------- FAQ ----------------
FAQS = [
 ("What is craft beer?",
  "Craft beer is beer made by small, independent breweries using traditional methods and high-quality ingredients. It's brewed in limited batches, without shortcuts, and is known for its rich flavour, distinctive styles and strong local identity."),
 ("What is the difference between craft beer and regular beer?",
  "Regular, commercial beer is mass-produced by large breweries for a mild, uniform taste that's the same everywhere — often using adjuncts like rice or corn to keep costs down. Craft beer is brewed in smaller batches by independent brewers, with better malts and specialty hops, giving you a bolder, more flavourful and more varied beer."),
 ("What are lager and ale?",
  "They're the two main families of beer, set apart by how they ferment. Ale is brewed with top-fermenting yeast at warmer temperatures for a richer, fruitier, more aromatic character — our Witbier is an ale. Lager uses bottom-fermenting yeast at cooler temperatures and is cold-stored, or 'lagered', for a clean, crisp, refreshing taste — our Blue pilsner is a lager."),
 ("How do Caldera beers differ from the rest?",
  "Caldera is craft, not commercial — brewed in small batches with quality ingredients and real character, rather than mass-produced for uniformity. It's Calcutta's own, made locally in distinct styles, so you get more flavour, more variety, and a beer with a genuine local identity."),
 ("Why is my Caldera a little cloudy, or does it have some sediment?",
  "That's natural — especially in our wheat beers. A style like the Witbier is meant to be cloudy, thanks to the wheat and suspended yeast, and craft beer is often unfiltered. So a little haze or settling is a sign of character, not a fault."),
 ("Who makes Caldera?",
  "Caldera — Calcutta's Finest Craft — is brewed by Karnani FnB Specialities LLP, based in Kolkata."),
]
faq_items="".join(
  f'<details class="faq-item rv"><summary><span class="faq-q">{q}</span><span class="faq-chev" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></span></summary><div class="faq-a"><p>{a}</p></div></details>'
  for q,a in FAQS)

FAQ = f'''<section class="faqhero">
  <img class="faqhero-img" src="assets/glasses_trio.jpg" alt="Three glasses of Caldera on the bar">
  <div class="faqhero-scrim"></div>
  <div class="wrap maxw faqhero-inner">
    <span class="eyebrow rv">Good to Know</span>
    <h1 class="rv d1">Questions? We've got <em>answers.</em></h1>
    <p class="rv d2">A quick guide to craft beer, our styles, and how to enjoy Caldera at its best.</p>
  </div>
</section>

<section class="faqsec"><div class="wrap maxw faq-wrap">
  <div class="faq-list">
    {faq_items}
  </div>
  <div class="faq-cta rv">
    <div class="eyebrow">Still curious?</div>
    <h3>Ask us anything.</h3>
    <p>Can't find what you're looking for, or want to know where to grab a Caldera? We're always happy to help.</p>
    <a class="btn btn-gold" href="contact.html">Get in Touch</a>
  </div>
</div></section>'''

# ---------------- FIND CALDERA ----------------
FIND = '''<section class="chero"><div class="wrap maxw">
  <div class="eyebrow">Where to Find Caldera</div>
  <h1>Find a <em>Caldera</em> near you.</h1>
  <p>Caldera is served on tap and sold in bottles at licensed outlets across the city. Here's how to track one down — and if you can't, just ask and we'll point you the right way.</p>
</div></section>

<section class="findways"><div class="wrap maxw findways-grid">
  <div class="findway rv">
    <div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h10l-1 15.4A2 2 0 0 1 14 20.2h-4a2 2 0 0 1-2-1.8L7 3z"/><path d="M7.4 9h9.2"/></svg></div>
    <h2>On Tap</h2>
    <p>Fresh from the keg at bars, restaurants, cafés and taprooms pouring Caldera. Draught is the freshest way to enjoy it — crisp, aromatic and straight from the tap.</p>
    <a class="btn btn-gold" href="contact.html">Ask Where It's on Tap</a>
  </div>
  <div class="findway rv d1">
    <div class="cp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 2h6M10 2v3.5a4 4 0 0 1-1 2.6L7.8 9.6A4 4 0 0 0 7 12.2V20a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-7.8a4 4 0 0 0-.8-2.6L15 8.1a4 4 0 0 1-1-2.6V2"/><path d="M7 14h10"/></svg></div>
    <h2>In Bottles</h2>
    <p>Grab a 330 ml bottle to take home from licensed stores and retailers stocking Caldera. Perfect for your own adda, on your own terms.</p>
    <a class="btn btn-gold" href="contact.html">Ask Where to Buy Bottles</a>
  </div>
</div></section>

<section class="findnote"><div class="wrap maxw">
  <div class="eyebrow">Can't spot it yet?</div>
  <h2>Tell us your <em>area.</em></h2>
  <p class="note">We're growing across the city fast, and new outlets come on all the time. Tell us where you are and which beer you're after — we'll help you find the nearest pour or bottle. A live list of venues and stockists is on the way.</p>
  <div class="cta-btns"><a class="btn btn-gold" href="contact.html">Ask About Availability</a><a class="btn btn-ghost" href="contact.html">Stock or Serve Caldera</a></div>
  <p class="legalnote">Available at licensed outlets only. We do not sell alcohol online.</p>
</div></section>'''

# ---------------- BLOG ----------------
POSTS = [
 ("cheers_bridge.jpg","The Cal Way","The art of the adda, in a glass","Calcutta doesn't rush its conversations — and neither should its beer. A look at how the city's unhurried way of gathering shapes the way we brew and pour.","Coming soon"),
 ("witbier_travertine.jpg","Know Your Beer","Why your Witbier is cloudy — and proud of it","Haze isn't a flaw. We unpack what makes a Belgian-style wheat beer naturally cloudy, and why unfiltered craft beer carries more character.","Coming soon"),
 ("glasses_trio.jpg","Know Your Beer","Lager vs ale: a quick guide for the curious","Top-fermented or bottom-fermented? Warm or cool? A simple, no-jargon guide to the two great families of beer — and where Caldera's styles sit.","Coming soon"),
]
blog_cards="".join(
  f'<article class="blog-card rv"><div class="blog-media"><img src="assets/{img}" alt="{title}" loading="lazy"><span class="blog-cat">{cat}</span></div><div class="blog-body"><h3>{title}</h3><p>{excerpt}</p><span class="blog-soon">{tag}</span></div></article>'
  for img,cat,title,excerpt,tag in POSTS)

BLOG = f'''<section class="chero"><div class="wrap maxw">
  <div class="eyebrow">The Cal Journal</div>
  <h1>Stories from the <em>brewery.</em></h1>
  <p>Notes on craft, the city, and the Caldera way of life. Fresh stories are on the way — here's a taste of what's brewing.</p>
</div></section>

<section class="blogsec"><div class="wrap maxw">
  <div class="blog-grid">
    {blog_cards}
  </div>
</div></section>'''

# ---------------- PRIVACY ----------------
PRIVACY = '''<section class="chero"><div class="wrap maxw">
  <div class="eyebrow">Legal</div>
  <h1>Privacy <em>Policy.</em></h1>
  <p>How Karnani FnB Specialities LLP ("Caldera", "we", "us") handles the information you share with us through this website.</p>
</div></section>

<section class="legal"><div class="wrap maxw legal-wrap">
  <p class="legal-updated">Last updated: 27 October 2026</p>

  <h3>1. Who we are</h3>
  <p>This website is operated by Karnani FnB Specialities LLP, Haute Street Corporate Park, 86A Topsia Road (S), Kolkata 700046, India. Caldera is our craft beer brand. For any privacy-related query, write to us at <a href="mailto:feedback@caldera.beer">feedback@caldera.beer</a>.</p>

  <h3>2. Information we collect</h3>
  <p>We only collect what you choose to share with us. When you use our enquiry or contact form, we collect your name, email address, phone number (if provided), your selected enquiry type and your message. We do not sell alcohol online and do not collect any payment information through this website.</p>

  <h3>3. How we use your information</h3>
  <p>We use the details you provide solely to respond to your enquiry — for example, to help you find Caldera on tap or in stores, to discuss stocking or serving Caldera, or to reply to feedback. We do not use your details for automated decision-making.</p>

  <h3>4. Age verification</h3>
  <p>This site is intended for people of legal drinking age (21 years or older). We ask you to confirm your age before entering. This confirmation is stored only in your own browser and is not sent to us.</p>

  <h3>5. Cookies and local storage</h3>
  <p>We keep our use of cookies and similar technologies to a minimum. Your age confirmation and small preferences are stored locally in your browser so you aren't asked repeatedly. Our hosting provider may set basic technical cookies required to serve the site securely.</p>

  <h3>6. Sharing your information</h3>
  <p>We do not sell or rent your personal information. We may share it with trusted service providers who help us operate the website and respond to enquiries (such as our hosting and email providers), who are required to protect it. We may also disclose information where required by law.</p>

  <h3>7. Data retention</h3>
  <p>We keep enquiry details only for as long as needed to respond to you and for our reasonable business records, after which they are deleted or anonymised.</p>

  <h3>8. Your choices</h3>
  <p>You may ask us to access, correct or delete the personal information you have shared with us by writing to <a href="mailto:feedback@caldera.beer">feedback@caldera.beer</a>. You can also clear your browser storage at any time to reset your age confirmation and preferences.</p>

  <h3>9. Changes to this policy</h3>
  <p>We may update this policy from time to time. Any changes will appear on this page with a revised "last updated" date.</p>

  <h3>10. Contact</h3>
  <p>Questions about this policy or your information? Email <a href="mailto:feedback@caldera.beer">feedback@caldera.beer</a> or call 1800 123 3415.</p>

  <p class="legalnote">Please drink responsibly. Consumption of alcohol is injurious to health. Not for sale to persons below 21 years.</p>
</div></section>'''

# ---------------- WRITE ----------------
pages = {
  "index.html":     ("Caldera Craft Beer", "Caldera - Calcutta's Finest Craft Beer. Four small-batch craft styles, brewed in Kolkata. Find Caldera on tap and in bottles.", HOME, "beers"),
  "yellow.html":    ("Caldera Yellow", "Caldera Yellow - Belgian-style Witbier. Citrusy and smooth, naturally crafted. ABV below 5%.", yellow, "beers"),
  "blue.html":      ("Caldera Blue", "Caldera Blue - German-style Pilsner. Crisp and dry. ABV below 5%.", blue, "beers"),
  "strong.html":    ("Caldera Strong", "Caldera Strong - Strong Lager. Rich and roasty, smoothly finished. ABV below 8%.", strong, "beers"),
  "about.html":     ("About Caldera", "About Caldera - Calcutta's Finest Craft, brewed by Karnani FnB Specialities LLP in Kolkata since 2016.", ABOUT, "about"),
  "faq.html":       ("Caldera FAQ", "Caldera FAQ - craft beer explained, lager vs ale, how to serve and store, and where to find Caldera in Kolkata.", FAQ, "faq"),
  "find.html":      ("Find Caldera", "Find Caldera on tap and in bottles at licensed outlets across Kolkata. Ask about availability in your area.", FIND, "find"),
  "blog.html":      ("The Cal Journal - Caldera", "The Cal Journal - stories on craft beer, Calcutta and the Caldera way of life.", BLOG, "blog"),
  "contact.html":   ("Contact Caldera", "Contact Caldera - find us on tap, stock our bottles, or partner with us. Brewed in Kolkata.", CONTACT, "contact"),
  "privacy.html":   ("Privacy Policy - Caldera", "Caldera privacy policy - how Karnani FnB Specialities LLP handles information shared through this website.", PRIVACY, ""),
}
if __name__ == "__main__":
    for fn,(t,d,b,a) in pages.items():
        (SITE/fn).write_text(standalone(t,d,b,a), encoding="utf-8")
    # body-only home for artifact main
    (SITE/"index_body.html").write_text(bodyonly(*pages["index.html"]), encoding="utf-8")
    print("built:", ", ".join(pages.keys()), "+ index_body.html")
