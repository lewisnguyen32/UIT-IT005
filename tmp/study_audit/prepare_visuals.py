from pathlib import Path
import json, zipfile
from lxml import etree
import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw

HERE=Path(__file__).resolve().parent
manifest=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
visual=HERE/'visuals'
visual.mkdir(exist_ok=True)
for rec in manifest:
    sid=rec.get('id','')
    if rec.get('media'):
        dest=visual/sid
        dest.mkdir(exist_ok=True)
        with zipfile.ZipFile(rec['path']) as z:
            for member in rec['media']:
                p=dest/Path(member).name
                p.write_bytes(z.read(member))
                try:
                    im=Image.open(p)
                    print(sid,p.name,im.size)
                except Exception as exc: print(exc)
            ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
            rel=etree.fromstring(z.read('word/_rels/document.xml.rels'))
            lookup={r.get('Id'):r.get('Target') for r in rel}
            doc=etree.fromstring(z.read('word/document.xml'))
            anchors=[]
            for idx,p in enumerate(doc.xpath('//w:body//w:p',namespaces=ns),1):
                ids=p.xpath('.//a:blip/@r:embed',namespaces=ns)
                if ids: anchors.append({'paragraph':idx,'text':''.join(p.xpath('.//w:t/text()',namespaces=ns)),'images':[lookup.get(i) for i in ids]})
            (dest/'anchors.json').write_text(json.dumps(anchors,ensure_ascii=False,indent=2),encoding='utf-8')
    if sid in ['E01','E02']:
        dest=visual/sid
        dest.mkdir(exist_ok=True)
        pdf=pdfium.PdfDocument(rec['path'])
        for i in range(len(pdf)):
            im=pdf[i].render(scale=2.4).to_pil().convert('RGB')
            im.save(dest/f'page-{i+1:02}.png')
            print(sid,i+1,im.size)
        for start in range(0,len(pdf),3):
            sheet=Image.new('RGB',(1800,950),'#dddddd')
            draw=ImageDraw.Draw(sheet)
            for offset,i in enumerate(range(start,min(start+3,len(pdf)))):
                im=Image.open(dest/f'page-{i+1:02}.png')
                im.thumbnail((590,900))
                sheet.paste(im,(offset*600,30))
                draw.text((offset*600+10,5),f'{sid} page {i+1}',fill='black')
            sheet.save(dest/f'contact-{start+1:02}.png')
