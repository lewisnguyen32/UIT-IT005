from pathlib import Path
import json, zipfile, hashlib, re
from lxml import etree
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'tmp' / 'study_audit'
OUT.mkdir(parents=True, exist_ok=True)
records = []
source_entries = sorted(
    path
    for name in ('Giữa Kỳ', 'Lý thuyết')
    for path in [ROOT / name, *(ROOT / name).rglob('*')]
)
for n, path in enumerate(source_entries):
    if not path.is_file():
        continue
    if path.name.startswith('ĐA ') or path.name == '_45_cau_ đáp án .docx':
        records.append({'path': str(path), 'status': 'excluded_answer_file'})
        continue
    sid = 'T' + str(1 if 'Chương1' in path.name else 2 if 'Chương 2' in path.name else 3) if 'Lý thuyết' in str(path) else 'E'+str(n).zfill(2)
    rec = {'id':sid, 'path':str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    blocks=[]
    if path.suffix.lower()=='.pdf':
        pdf=PdfReader(path)
        rec['pages']=len(pdf.pages)
        rec['page_stats']=[]
        for i,page in enumerate(pdf.pages,1):
            txt=page.extract_text() or ''
            rec['page_stats'].append({'page':i,'chars':len(txt),'images':len(page.images)})
            blocks.append(f'\n\n===== PDF PAGE {i} =====\n{txt}')
    elif path.suffix.lower()=='.docx':
        with zipfile.ZipFile(path) as z:
            rec['media']=[x for x in z.namelist() if x.startswith('word/media/')]
            ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','r':'http://schemas.openxmlformats.org/package/2006/relationships'}
            doc=etree.fromstring(z.read('word/document.xml'))
            for i,p in enumerate(doc.xpath('//w:body//w:p',namespaces=ns),1):
                txt=''.join(p.xpath('.//w:t/text()',namespaces=ns))
                if txt.strip(): blocks.append(f'[P{i}] {txt}')
            if 'word/_rels/document.xml.rels' in z.namelist():
                rel=etree.fromstring(z.read('word/_rels/document.xml.rels'))
                links=[el.get('Target') for el in rel if el.get('TargetMode')=='External']
                rec['external_links']=links
                if links: blocks.append('\nEXTERNAL LINKS\n'+'\n'.join(links))
    else:
        rec['status']='unsupported'
        records.append(rec)
        continue
    text=''.join(blocks) if path.suffix.lower()=='.pdf' else '\n'.join(blocks)
    out=OUT/f'{sid}.txt'
    out.write_text(text,encoding='utf-8')
    rec['extraction']=str(out)
    rec['chars']=len(text)
    rec['status']='extracted'
    records.append(rec)
(OUT/'manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
for r in records:
    print(r.get('id','--'),r.get('status'),Path(r['path']).name,'pages=',r.get('pages'), 'chars=',r.get('chars'), 'sparse=',[x['page'] for x in r.get('page_stats',[]) if x['chars']<100], 'media=',len(r.get('media',[])))
