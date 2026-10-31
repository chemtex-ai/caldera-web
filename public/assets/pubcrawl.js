(function(){
  var f=document.querySelector('.pcform'); if(!f) return;
  var age=f.querySelector('#pc-age'), mob=f.querySelector('#pc-mobile');

  function msg(el,t){ el.setCustomValidity(t||''); }
  age.addEventListener('input',function(){
    var v=parseInt(age.value,10);
    msg(age, (age.value && (isNaN(v)||v<21)) ? 'You must be 21 or older to register.' : '');
  });
  mob.addEventListener('input',function(){
    var d=mob.value.replace(/\D/g,'');
    msg(mob, (mob.value && d.length<10) ? 'Please enter a valid mobile number.' : '');
  });

  f.addEventListener('submit',function(e){
    e.preventDefault();
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
