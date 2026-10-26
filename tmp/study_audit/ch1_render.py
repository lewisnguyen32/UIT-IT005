import json, pathlib, zipfile, xml.etree.ElementTree as ET
import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw

base=pathlib.Path(__file__).resolve().parent
manifest=json.loads((base/'manifest.json').read_text(encoding='utf-8-sig'))
sources={i['id']:i for i in manifest if i.get('id')}
for id,pages in [('T1',[27,28,67]),('E17',[8,12,31,32,33,34,35,36,42,43,44,45,46,50]),('E15',[2,4])]:
    doc=pdfium.PdfDocument(sources[id]['path'])
    for p in pages:
        im=doc[p-1].render(scale=1.7).to_pil().convert('RGB')
        im.save(base/f'{id}_ch1_page_{p:03d}.png')
    if id=='E17':
        for start in range(0,len(pages),4):
            ims=[]
            for p in pages[start:start+4]:
                im=Image.open(base/f'{id}_ch1_page_{p:03d}.png')
                im.thumbnail((1000,700))
                canvas=Image.new('RGB',(1020,740),'white')
                canvas.paste(im,((1020-im.width)//2,30))
                ImageDraw.Draw(canvas).text((10,10),f'{id} PDF page {p}',fill='black')
                ims.append(canvas)
            out=Image.new('RGB',(2040,1480),'#ddd')
            for n,im in enumerate(ims):out.paste(im,((n%2)*1020,(n//2)*740))
            out.save(base/f'{id}_ch1_contact_{start//4+1}.png')

with zipfile.ZipFile(sources['E14']['path']) as z:
    for name in sources['E14']['media']:
        out=base/('E14_'+pathlib.Path(name).name)
        out.write_bytes(z.read(name))
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
    root=ET.fromstring(z.read('word/document.xml'))
    rels=ET.fromstring(z.read('word/_rels/document.xml.rels'))
    relmap={r.attrib['Id']:r.attrib['Target'] for r in rels}
    prev=[]
    for p in root.findall('.//w:body/w:p',ns):
        text=''.join(p.itertext())
        blips=p.findall('.//a:blip',ns)
        if blips:
            print('IMAGE_CONTEXT',prev[-2:],text,[(relmap.get(b.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'))) for b in blips])
        if text:prev.append(text)
