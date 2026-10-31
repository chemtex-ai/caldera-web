# -*- coding: utf-8 -*-
import json, collections, pathlib, build_white as bw

data=json.loads(pathlib.Path('outlets_public.json').read_text(encoding='utf-8'))
AREAS=[a for a,_ in collections.Counter(o['area'] for o in data).most_common()]
ntap=sum(1 for o in data if o['tap']); npint=sum(1 for o in data if o['pint'])

def card(o):
    typ=f'<span class="ocard-type">{o["type"]}</span>' if o['type'] else ''
    return (f'<li class="ocard" data-name="{o["name"].lower()}" data-area="{o["area"]}" '
            f'data-tap="{int(o["tap"])}" data-pint="{int(o["pint"])}">'
            f'<div class="ocard-main"><h3>{o["name"]}</h3>{typ}</div>'
            f'<div class="ocard-meta"><span class="ocard-area">{o["area"]}</span></div></li>')

chips='<button class="achip is-on" data-area="">All areas</button>' + ''.join(
    f'<button class="achip" data-area="{a}">{a}</button>' for a in AREAS)

BODY=f'''<section class="chero chero-tight"><div class="wrap maxw">
  <div class="eyebrow">Where to Find Caldera</div>
  <h1>Find a Caldera <em>near you.</em></h1>
  <p>Caldera is poured on tap and sold by the pint across Kolkata. Search by name, or narrow it down to your part of the city.</p>
</div></section>

<section class="sec outlets"><div class="wrap maxw">

  <div class="ofilters">
    <div class="oseg" role="tablist" aria-label="Format">
      <button class="oseg-btn is-on" data-fmt="tap"  role="tab" aria-selected="true">On Tap <i>{ntap}</i></button>
      <button class="oseg-btn"       data-fmt="pint" role="tab" aria-selected="false">On Pint <i>{npint}</i></button>
    </div>
    <div class="osearch">
      <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6"/></svg>
      <input type="search" id="oq" placeholder="Search a bar, club or store" aria-label="Search outlets" autocomplete="off">
    </div>
  </div>

  <div class="achips" aria-label="Filter by area">{chips}</div>

  <p class="ocount" id="ocount" aria-live="polite"></p>
  <ul class="olist" id="olist">{''.join(card(o) for o in data)}</ul>

  <div class="oempty" id="oempty" hidden>
    <h3>Nothing matching that.</h3>
    <p>Try a different spelling or clear the area filter &mdash; or tell us your neighbourhood and we'll point you at the nearest pour.</p>
    <a class="btn btn-gold" href="contact.html">Ask About Availability</a>
  </div>

  <p class="onote">This list covers outlets actively serving Caldera. Stock moves quickly, so it's worth a quick call before you set off for a particular beer.</p>
</div></section>

<section class="sec bg-black cta-band"><div class="wrap maxw ctab">
  <h2>Can't spot it yet?</h2>
  <p>We're growing across the city fast, and new outlets come on all the time. Tell us where you are and which beer you're after.</p>
  <div class="hero-ctas">
    <a class="btn btn-gold" href="contact.html">Ask About Availability</a>
    <a class="btn btn-ghost" href="contact.html">Stock or Serve Caldera</a>
  </div>
</div></section>'''

html=bw.clean(bw.standalone_w("Where to Find Caldera — Bars & Stores in Kolkata",
  "Find Caldera on tap and by the pint across Kolkata. Search bars, clubs and stores serving Caldera, filtered by area.",
  BODY,"find","","find.html"))
html=html.replace('</body>','<script src="assets/outlets.js"></script>\n</body>')
(bw.WHITE/"find.html").write_text(html,encoding="utf-8")
(bw.ASSETS/"outlets.js").write_text(pathlib.Path("outlets.js").read_text(encoding="utf-8"),encoding="utf-8")
print(f"find.html rebuilt — {len(data)} outlets ({ntap} tap / {npint} pint), {len(AREAS)} areas")
