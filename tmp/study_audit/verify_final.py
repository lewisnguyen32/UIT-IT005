from pathlib import Path
import hashlib, json, re

root=Path(__file__).resolve().parents[2]
here=Path(__file__).resolve().parent
mapping=json.loads((here/'question_classification.json').read_text(encoding='utf-8'))
totals=[0,0,0]
for sid, row in mapping.items():
    if not isinstance(row,dict): continue
    groups=[row[f'ch{i}'] for i in (1,2,3)]
    nums=sum(groups,[])
    assert len(nums)==len(set(nums))==row['count'],(sid,'duplicate/missing')
    assert sorted(nums)==list(range(1,row['count']+1)),(sid,'range')
    totals=[a+len(b) for a,b in zip(totals,groups)]
    if sid in ['E03','E08','E10']:
        source_text=(here/f'{sid}.txt').read_text(encoding='utf-8')
        numbered=[int(n) for n in re.findall(r'Câu\s+(\d+)\s*[.:]',source_text)]
        assert numbered==list(range(1,row['count']+1)),(sid,numbered)
    print(sid, 'count=',len(nums),'chapters=',[len(x) for x in groups])
assert totals==[26,75,71],totals
assert sum(totals)==172

plan=(root/'output/KE_HOACH_ON_NMMMT_7_NGAY.md').read_text(encoding='utf-8')
links=re.findall(r'\]\(<([^>]+)>\)',plan)
for link in links:
    assert Path(link).is_file(),link
assert len(links)==8,len(links)
days=[line for line in plan.splitlines() if re.match(r'\| \*\*[1-7]\*\* \|',line)]
assert len(days)==7,len(days)
for line in days:
    parts=line.split('|')
    learning=sum(int(n) for n in re.findall(r'(\d+)\s*\x27',parts[2]))
    assert learning==110,(parts[1],learning)
print('Schedule: 7 x (110 study + 10 break) =',7*120,'minutes; optional <=',7*60)

manifest=json.loads((here/'manifest.json').read_text(encoding='utf-8'))
selected=['T1','T2','T3','E01','E02','E03','E08','E10']
for rec in manifest:
    if rec.get('id') in selected:
        digest=hashlib.sha256(Path(rec['path']).read_bytes()).hexdigest()
        assert digest==rec['sha256'],rec['path']
print('Totals:',totals,'All 172 questions covered once; 8 local links valid; selected sources unchanged.')
