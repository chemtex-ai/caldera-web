(function(){
  var f=document.querySelector('.pcform'); if(!f) return;
  var age=f.querySelector('#pc-age'), mob=f.querySelector('#pc-mobile'), ig=f.querySelector('#pc-insta');

  function msg(el,t){ el.setCustomValidity(t||''); }
  age.addEventListener('input',function(){
    var v=parseInt(age.value,10);
    msg(age, (age.value && (isNaN(v)||v<21)) ? 'You must be 21 or older to register.' : '');
  });
  function tidyHandle(){
    // accept "@name", "instagram.com/name", a full profile URL, or just "name"
    var v = ig.value.trim()
      .replace(/^https?:\/\//i,'')
      .replace(/^(www\.)?instagram\.com\//i,'')
      .replace(/[?#].*$/,'')
      .replace(/\/+$/,'')
      .replace(/^@+/,'');
    if (v !== ig.value) ig.value = v;
    return v;
  }
  // tidy only once the field is left, never mid-keystroke
  ig.addEventListener('blur', function(){ msg(ig, check(tidyHandle())); });
  ig.addEventListener('input', function(){
    var v = ig.value.trim().replace(/^@+/,'');
    msg(ig, /[\/:.]{0,}/.test(v) && /^[A-Za-z0-9._]*$/.test(v) ? '' : '');
  });
  function check(v){
    return (v && !/^[A-Za-z0-9._]{1,30}$/.test(v)) ? 'That does not look like an Instagram handle.' : '';
  }
  mob.addEventListener('input',function(){
    var d=mob.value.replace(/\D/g,'');
    msg(mob, (mob.value && d.length<10) ? 'Please enter a valid mobile number.' : '');
  });

  f.addEventListener('submit',function(e){
    e.preventDefault();
    var h=tidyHandle();
    if(check(h)){ msg(ig,check(h)); f.reportValidity(); return; }
    var v=parseInt(age.value,10);
    if(isNaN(v)||v<21){ msg(age,'You must be 21 or older to register.'); f.reportValidity(); return; }
    var btn=f.querySelector('button[type=submit]');
    if(btn){ btn.disabled=true; btn.textContent='Registering…'; }
    fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},
      body:new URLSearchParams(new FormData(f)).toString()})
      .then(function(){ f.classList.add('sent'); })
      .catch(function(){ f.classList.add('sent'); });
  });
})();
