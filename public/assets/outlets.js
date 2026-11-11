(function(){
  var list=document.getElementById('olist'); if(!list) return;
  var items=[].slice.call(list.children),
      q=document.getElementById('oq'),
      count=document.getElementById('ocount'),
      blurb=document.getElementById('oblurb'),
      banIc=document.getElementById('obanIc'),
      banner=document.getElementById('obanner'),
      empty=document.getElementById('oempty'),
      segs=[].slice.call(document.querySelectorAll('.oseg-btn')),
      chips=[].slice.call(document.querySelectorAll('.achip')),
      fmt='tap', area='', term='';

  var ICON={tap:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 4h6"/><path d="M12 4v4"/><path d="M4 8h11a2 2 0 0 1 2 2v2"/><path d="M17 15.5v4"/><path d="M4 8v3"/><circle cx="17" cy="13.6" r="1.6"/></svg>',pint:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 2h4v3.2l1.3 2.3a5 5 0 0 1 .7 2.5V20a2 2 0 0 1-2 2h-4a2 2 0 0 1-2-2V10a5 5 0 0 1 .7-2.5L10 5.2V2z"/><path d="M8 12h8"/></svg>'};
  var BLURB={
    tap:  'Enjoy fresh craft beer on tap at any of these outlets.',
    pint: 'Craft beer by the pint is available at these outlets.'
  };
  function apply(){
    if(blurb){ blurb.textContent=BLURB[fmt]; banIc.innerHTML=ICON[fmt];
                 banner.setAttribute('data-fmt',fmt); }
    var n=0;
    items.forEach(function(el){
      var ok = el.dataset[fmt]==='1'
            && (!area || el.dataset.area===area)
            && (!term || el.dataset.name.indexOf(term)>-1);
      el.hidden=!ok; if(ok)n++;
    });
    list.classList.toggle('area-fixed', !!area);
    count.textContent = n ? n+(n===1?' outlet':' outlets')+(area?' in '+area:'') : '';
    empty.hidden = n>0;
    chips.forEach(function(c){
      if(!c.dataset.area) return;
      var any=items.some(function(el){return el.dataset[fmt]==='1'&&el.dataset.area===c.dataset.area;});
      c.disabled=!any; c.classList.toggle('is-off',!any);
      if(!any&&area===c.dataset.area){area='';chips[0].classList.add('is-on');c.classList.remove('is-on');}
    });
  }
  segs.forEach(function(b){b.addEventListener('click',function(){
    segs.forEach(function(x){x.classList.remove('is-on');x.setAttribute('aria-selected','false');});
    b.classList.add('is-on'); b.setAttribute('aria-selected','true');
    fmt=b.dataset.fmt; apply();
  });});
  chips.forEach(function(c){c.addEventListener('click',function(){
    chips.forEach(function(x){x.classList.remove('is-on');});
    c.classList.add('is-on'); area=c.dataset.area; apply();
  });});
  if(q) q.addEventListener('input',function(){term=q.value.trim().toLowerCase();apply();});
  apply();
})();
