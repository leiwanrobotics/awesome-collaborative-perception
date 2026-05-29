import json, re, time, sys
import requests, concurrent.futures as cf
from pathlib import Path
ROOT=Path('.')
d=json.load(open('data/snowballing/kept_enriched.json'))
def norm(s): return re.sub(r'[^a-z0-9]',' ',(s or '').lower()).split()
def sim(a,b):
    A,B=set(norm(a)),set(norm(b))
    return len(A&B)/max(1,len(A|B))
def cr(p):
    if p.get('doi') or p.get('arxiv'): return p
    t=p['title']
    try:
        r=requests.get('https://api.crossref.org/works',
            params={'query.bibliographic':t,'rows':2,'mailto':'jonaswanlei00@gmail.com'},
            timeout=30, headers={'User-Agent':'awesome-cp/1.0 (mailto:jonaswanlei00@gmail.com)'})
        if r.status_code==200:
            for it in r.json().get('message',{}).get('items',[]):
                ct=' '.join(it.get('title',[]) or [])
                if ct and sim(t,ct)>=0.75:
                    p['doi']=it.get('DOI','') or p.get('doi','')
                    break
    except Exception as e:
        print('err',e,file=sys.stderr)
    return p
miss=[p for p in d if not (p.get('doi') or p.get('arxiv'))]
print('querying crossref for',len(miss),'papers')
with cf.ThreadPoolExecutor(max_workers=6) as ex:
    list(ex.map(cr, miss))
n=sum(1 for p in d if p.get('doi') or p.get('arxiv'))
json.dump(d, open('data/snowballing/kept_enriched.json','w'), indent=1, ensure_ascii=False)
print('now with real id:',n,'/',len(d))
