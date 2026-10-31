# -*- coding: utf-8 -*-
"""Turn the internal sales extract into a PUBLIC-SAFE outlet list."""
import openpyxl, json, re, collections, pathlib

SRC='/mnt/user-data/attachments/81a4e492-c48c-5d78-8e4d-bd838c496421/52625157-Caldera_Active_Outlets_Aug-Oct_2026.xlsx'
wb=openpyxl.load_workbook(SRC,data_only=True); ws=wb['All outlets']
hdr=[c.value for c in ws[1]]
rows=[dict(zip(hdr,r)) for r in ws.iter_rows(min_row=2,values_only=True) if r[0]]

ZONE={'Kolkata (South)':'South Kolkata','Kolkata(North)':'North Kolkata',
 'Kolkata (Central)':'Central Kolkata','Bidhannagar Excise District':'Salt Lake & Bidhannagar',
 'Alipur Excise District':'Alipore','Barrackpore Excise District':'Barrackpore',
 'Baruipur Excise District':'Baruipur','Diamond Harbour Excise District':'Diamond Harbour',
 'Howrah Industrial':'Howrah','Nadia':'Nadia','North 24-Parganas (Rural)':'North 24-Parganas'}
TYPE={'OnShop – Stand Alone':'Bar & Restaurant','OnShop – Social Club':'Club',
      'OffShop - Retail':'Wine Shop','OffShop – Modern Trade':'Supermarket'}

LEGAL=re.compile(r'\s*\b(a unit of.*|pvt\.?\s*ltd\.?|private limited|pvt\.?|ltd\.?|limited|llp)\b\s*',re.I)
SHOPY=re.compile(r'\s*\b(f\s*\.?\s*l\s*\.?\s*(off|on)\s*shop|floff\s*shop|c\s*s\s*shop|csshop|off\s*shop|on\s*shop)\b\s*(-\s*\d+)?',re.I)
KEEPUP={'AM','PM','BBQ','KFC','TGI','JW','ITC','PDK','SN','BT'}
LOWER={'and','the','of','cum','by','at','in','on','for','a','an'}

def titlecase(n):
    out=[]
    for w in n.split():
        core=re.sub(r'[^A-Za-z]','',w)
        if core.lower() in LOWER and out: out.append(core.lower())
        elif core.upper() in KEEPUP or (len(core)<=3 and w.isupper() and core.lower() not in LOWER): out.append(w.upper())
        elif w.isupper() or w.islower(): out.append(w.capitalize())
        else: out.append(w)
    return ' '.join(out)

def clean_name(n):
    n=str(n).strip()
    n=re.sub(r'^\s*m\s*/\s*s\b\.?[\s\-]*','',n,flags=re.I)   # drop the Messrs trade prefix
    n=LEGAL.sub(' ',n); n=SHOPY.sub(' ',n)
    n=re.sub(r'\s{2,}',' ',n).strip(' ,-.')
    return titlecase(n)

def area(z):
    z=str(z or '')
    for k,v in ZONE.items():
        if k in z: return v
    return ''

out=[]
for r in rows:
    nm=clean_name(r['Outlet Name']); ar=area(r['Zone'])
    fmt=r['Format']
    review=[]
    if not ar: review.append('area missing')
    if re.match(r'^\s*[\d/]',str(r['Outlet Name'])): review.append('address as name')
    if len(nm)<4: review.append('name too short')
    out.append({
      'name':nm, 'raw':str(r['Outlet Name']).strip(), 'area':ar,
      'type':TYPE.get(r['Outlet Type'],''),
      'tap': fmt in ('Keg','Both'), 'pint': fmt in ('Bottle','Both'),
      'review':review,
    })

ok=[o for o in out if not o['review']]
# chain outlets without an area are indistinguishable -> flag duplicates too
seen=collections.Counter(o['name'].upper() for o in ok)
for o in ok:
    if seen[o['name'].upper()]>1 and not o['area']: o['review'].append('duplicate chain')
ok=[o for o in ok if not o['review']]

pathlib.Path('outlets_public.json').write_text(json.dumps(
    sorted(ok,key=lambda o:(o['area'],o['name'])),ensure_ascii=False,indent=1),encoding='utf-8')
pathlib.Path('outlets_review.json').write_text(json.dumps(
    [o for o in out if o['review']],ensure_ascii=False,indent=1),encoding='utf-8')

print(f"source rows        : {len(rows)}")
print(f"publishable now    : {len(ok)}")
print(f"  on tap           : {sum(1 for o in ok if o['tap'])}")
print(f"  on pint          : {sum(1 for o in ok if o['pint'])}")
print(f"needs human review : {len(out)-len(ok)}")
print("\nareas:")
for k,v in collections.Counter(o['area'] for o in ok).most_common(): print(f"  {k:26s} {v}")
