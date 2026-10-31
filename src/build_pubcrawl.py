# -*- coding: utf-8 -*-
"""The Pub Crawl — campaign landing page with registration form."""
import pathlib, build_white as bw

BADGE_BG = "#282722"   # the badge artwork's own backdrop, so its edge disappears

BODY = f'''<section class="pc-hero">
  <div class="wrap maxw pc-hero-inner">
    <img class="pc-badge" src="assets/pubcrawl_badge.jpg" alt="Caldera Pub Crawl" width="620" height="620">
    <h1 class="pc-title">The Pub&nbsp;Crawl</h1>
    <p class="pc-lede">Come, join us as we head to Calcutta's best pubs and engage ourselves
    in&nbsp;adda.</p>
    <a class="btn btn-gold pc-jump" href="#register">Register Your Interest</a>
    <p class="pc-note">Registration is free. Entries are shortlisted &mdash; we'll call&nbsp;you.</p>
  </div>
</section>

<section class="sec pc-how"><div class="wrap maxw">
  <h2 class="pc-h2">How it <em>works</em></h2>
  <ol class="pc-steps">
    <li><span class="pc-num">01</span><h3>Register</h3><p>A few details. It takes under a minute.</p></li>
    <li><span class="pc-num">02</span><h3>We shortlist</h3><p>The group is kept small. If you're selected, someone from the team will call you.</p></li>
    <li><span class="pc-num">03</span><h3>Join us</h3><p>We'll share the venue and the time.</p></li>
  </ol>
</div></section>

<section class="sec pc-form-sec" id="register"><div class="wrap maxw pc-form-wrap">
  <h2 class="pc-h2">Register your <em>interest</em></h2>
  <p class="pc-sub">You must be 21 or older to take part.</p>

  <form class="pcform" name="pubcrawl" method="POST" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="pubcrawl">
    <p class="pc-hp"><label>Leave this empty <input name="bot-field"></label></p>

    <div class="pc-field">
      <label for="pc-name">Full name</label>
      <input id="pc-name" name="name" type="text" required autocomplete="name" placeholder="Your name">
    </div>

    <div class="pc-field">
      <label for="pc-mobile">Mobile number</label>
      <input id="pc-mobile" name="mobile" type="tel" required inputmode="numeric"
             pattern="[0-9+ ]{{10,15}}" autocomplete="tel" placeholder="10-digit mobile number">
      <small>We'll only use this to contact you about the Pub Crawl.</small>
    </div>

    <div class="pc-field">
      <label for="pc-age">Age</label>
      <input id="pc-age" name="age" type="number" required min="21" max="99" step="1" placeholder="21">
      <small>You must be 21 or older.</small>
    </div>

    <div class="pc-field">
      <label for="pc-insta">Your Instagram handle</label>
      <div class="pc-at">
        <span aria-hidden="true">@</span>
        <input id="pc-insta" name="instagram" type="text" required maxlength="120"
               autocomplete="off" autocapitalize="none" spellcheck="false"
               placeholder="yourhandle">
      </div>
    </div>

    <label class="pc-check">
      <input type="checkbox" name="follows_instagram" value="yes" required>
      <span>I follow <b>@caldera.craftbeer</b> on Instagram</span>
    </label>

    <p class="pc-consent">By registering you agree we may contact you about this event. We don't share
    your details with anyone else. See our <a href="privacy.html">Privacy Policy</a>.</p>

    <button class="btn btn-gold pc-submit" type="submit">Register</button>

    <div class="pc-sent" role="status">
      <h3>You're registered.</h3>
      <p>Thank you. If you're selected, someone from the team will call you with the venue
      and the time.</p>
    </div>
  </form>

  <p class="pc-legal">Consumption of alcohol is injurious to health. Not for sale to persons below
  21 years. Please don't drink and drive &mdash; arrange your ride home before you set out.</p>
</div></section>'''

html = bw.clean(bw.standalone_w(
    "The Pub Crawl — Caldera",
    "Register for the Caldera Pub Crawl \u2014 join us as we head to Calcutta's best pubs and engage ourselves in adda. Registration is free. 21+.",
    BODY, "", "", "pubcrawl.html"))
_v = bw._v(pathlib.Path(__file__).resolve().parent/"pubcrawl.js")
html = html.replace('</body>', f'<script src="assets/pubcrawl.js?v={_v}"></script>\n</body>')
(bw.WHITE/"pubcrawl.html").write_text(html, encoding="utf-8")
import shutil
shutil.copy(pathlib.Path(__file__).resolve().parent/"pubcrawl_badge.jpg", bw.ASSETS/"pubcrawl_badge.jpg")
(bw.ASSETS/"pubcrawl.js").write_text(
    (pathlib.Path(__file__).resolve().parent/"pubcrawl.js").read_text(encoding="utf-8"), encoding="utf-8")
print("pubcrawl.html built")
