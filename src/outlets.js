(function(){
  var list=document.getElementById('olist'); if(!list) return;
  var items=[].slice.call(list.children),
      q=document.getElementById('oq'),
      count=document.getElementById('ocount'),
      empty=document.getElementById('oempty'),
      segs=[].slice.call(document.querySelectorAll('.oseg-btn')),
      chips=[].slice.call(document.querySelectorAll('.achip')),
      fmt='tap', area='', term='';

  function apply(){
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
