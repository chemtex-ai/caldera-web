(function(){
  var reduce=matchMedia("(prefers-reduced-motion:reduce)").matches;

  /* hero video — portrait clip on phones, landscape on larger screens (only one set downloads) */
  (function(){
    var v=document.getElementById("heroVid"); if(!v) return;
    if(matchMedia("(max-width:760px)").matches){
      v.setAttribute("poster","assets/hero_mob_poster.jpg");
      v.innerHTML='<source src="assets/hero_mob.webm" type="video/webm"><source src="assets/hero_mob.mp4" type="video/mp4">';
      try{v.load();}catch(e){}
    }
  })();

  /* Hefeweizen 'On Tap' ambient video — lazy load + silent autoplay once scrolled into view */
  (function(){
    var tv=document.getElementById("tapVid"); if(!tv||reduce) return;
    var loaded=false;
    function load(){
      if(loaded) return; loaded=true;
      tv.innerHTML='<source src="'+tv.getAttribute("data-webm")+'" type="video/webm"><source src="'+tv.getAttribute("data-mp4")+'" type="video/mp4">';
      try{tv.load();}catch(e){}
      var p=tv.play(); if(p&&p.catch){p.catch(function(){});}
    }
    if("IntersectionObserver" in window){
      var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){load();o.disconnect();}});},{rootMargin:"200px 0px"});
      o.observe(tv);
    }else{load();}
  })();

  /* ---- AGE GATE (21+) ---- */
  (function(){
    var ok=false; try{ok=localStorage.getItem("caldera_age_ok")==="1";}catch(e){}
    if(ok) return;
    document.documentElement.classList.add("gated");
    function mount(){
      if(document.getElementById("agegate")) return;
      var g=document.createElement("div"); g.id="agegate"; g.setAttribute("role","dialog"); g.setAttribute("aria-modal","true"); g.setAttribute("aria-label","Age verification");
      g.innerHTML=''
        +'<div class="ag-card ag-live">'
        +'<img src="assets/logo_horiz_white.png" alt="Caldera — Calcutta\'s Finest Craft">'
        +'<div class="ag-rule"></div>'
        +'<h2 class="ag-q">Are you of legal<br>drinking <em>age?</em></h2>'
        +'<p class="ag-note">You must be <b>21 years or older</b> to enter. This website contains information about alcoholic beverages.</p>'
        +'<div class="ag-btns"><button class="btn btn-gold" id="ag-yes">Yes, I\'m 21 or older</button><button class="btn btn-ghost" id="ag-no">No, I\'m under 21</button></div>'
        +'<p class="ag-legal">Consumption of alcohol is injurious to health. Be safe — don\'t drink and drive. Please enjoy responsibly. By entering you confirm you are of legal drinking age in your region.</p>'
        +'</div>'
        +'<div class="ag-card ag-deny">'
        +'<img src="assets/logo_horiz_white.png" alt="Caldera" style="opacity:.55">'
        +'<h2 class="ag-q">Come back when<br>you\'re <em>21.</em></h2>'
        +'<p class="ag-note">You must be of legal drinking age to view this site. Thanks for stopping by — the Cal Bear will be waiting.</p>'
        +'<button class="btn btn-ghost" id="ag-back">Go back</button>'
        +'</div>';
      document.body.appendChild(g);
      g.querySelector("#ag-yes").addEventListener("click",function(){try{localStorage.setItem("caldera_age_ok","1");}catch(e){}document.documentElement.classList.remove("gated");g.remove();});
      g.querySelector("#ag-no").addEventListener("click",function(){g.classList.add("denied");});
      g.querySelector("#ag-back").addEventListener("click",function(){g.classList.remove("denied");});
    }
    if(document.body) mount(); else document.addEventListener("DOMContentLoaded",mount);
  })();

  /* word split (home statement / quote) */
  document.querySelectorAll("[data-words]").forEach(function(el){
    var frag=document.createDocumentFragment();
    Array.prototype.forEach.call(el.childNodes,function(c){
      if(c.nodeType===3){c.textContent.split(/(\s+)/).forEach(function(t){
        if(t.trim()){var s=document.createElement("span");s.className="w";s.textContent=t;frag.appendChild(s);}else if(t)frag.appendChild(document.createTextNode(t));});}
      else if(c.nodeType===1){var w=document.createElement(c.tagName.toLowerCase());w.className=((c.getAttribute("class")||"")+" w").trim();w.textContent=c.textContent;frag.appendChild(w);}
    });
    el.innerHTML="";el.appendChild(frag);
  });

  /* nav */
  var nav=document.getElementById("nav");
  if(nav){
    function onScroll(){nav.classList.toggle("solid",scrollY>30);}
    onScroll();addEventListener("scroll",onScroll,{passive:true});
    var tog=nav.querySelector(".nav-tog");
    if(tog){tog.addEventListener("click",function(){var o=nav.classList.toggle("open");tog.setAttribute("aria-expanded",o?"true":"false");});}
    nav.querySelectorAll(".nav-links a,.nav-cta").forEach(function(a){a.addEventListener("click",function(){nav.classList.remove("open");if(tog)tog.setAttribute("aria-expanded","false");});});
  }

  /* contact form — AJAX submit to Netlify (captures + notifies), shows in-page success */
  var cf=document.querySelector(".cform");
  if(cf){
    cf.addEventListener("submit",function(e){
      e.preventDefault();
      var btn=cf.querySelector("button[type=submit]"); if(btn){btn.disabled=true;}
      var body=new URLSearchParams(new FormData(cf)).toString();
      fetch("/",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:body})
        .then(function(){cf.classList.add("sent");})
        .catch(function(){cf.classList.add("sent");});
    });
  }

  if(reduce || !window.gsap) return;
  gsap.registerPlugin(ScrollTrigger);
  document.body.classList.add("anim");

  /* home hero load-in */
  if(document.querySelector(".hero-h1 .ln>span")){
    gsap.set(".hero-h1 .ln>span",{yPercent:110});
    gsap.set([".hero-eyebrow .eyebrow",".hero-sub",".hero-ctas",".hero-meta"],{opacity:0,y:20});
    var tl=gsap.timeline({defaults:{ease:"power3.out"}});
    tl.to(".hero-eyebrow .eyebrow",{opacity:1,y:0,duration:.7},.2)
      .to(".hero-h1 .ln>span",{yPercent:0,duration:1,stagger:.12},.3)
      .to(".hero-sub",{opacity:1,y:0,duration:.8},.7)
      .to(".hero-ctas",{opacity:1,y:0,duration:.8},.85)
      .to(".hero-meta",{opacity:1,y:0,duration:.8},.98);
  }

  /* reveals */
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target);}});},{threshold:.12,rootMargin:"0px 0px -8% 0px"});
  document.querySelectorAll(".rv").forEach(function(el){io.observe(el);});

  /* word reveal */
  document.querySelectorAll("[data-words]").forEach(function(el){gsap.to(el.querySelectorAll(".w"),{opacity:1,stagger:.5,ease:"none",scrollTrigger:{trigger:el,start:"top 78%",end:"bottom 55%",scrub:true}});});

  /* parallax */
  function par(sel,amt){gsap.utils.toArray(sel).forEach(function(img){gsap.fromTo(img,{yPercent:-(amt/2)},{yPercent:amt/2,ease:"none",scrollTrigger:{trigger:img,start:"top bottom",end:"bottom top",scrub:true}});});}
  par("#bandImg",12); par("#craftImg",12); par(".ahero img",10); par("#cheersImg",14);
})();
