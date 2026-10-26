import json
from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image, ImageDraw
import zipfile

base = Path(__file__).parent
manifest = json.loads((base/'manifest.json').read_text(encoding='utf-8-sig'))
files = {x.get('id'): x for x in manifest if x.get('id')}
out = base/'ch3_figures'
out.mkdir(exist_ok=True)
targets = {'E17':[115,116,117,118,119,124,126,131,134,137,138,141,142,143,144,145,147,148,151,152,153,154,155,157,159,160,162,164,165]}
for fid, pages in targets.items():
    pdf = pdfium.PdfDocument(files[fid]['path'])
    thumbs=[]
    for n in pages:
        page = pdf[n-1]
        img = page.render(scale=1.8).to_pil().convert('RGB')
        img.save(out/f'{fid}_p{n:03}.png')
        img.thumbnail((800,1000))
        tile=Image.new('RGB',(820,1030),'white')
        tile.paste(img,((820-img.width)//2,25))
        ImageDraw.Draw(tile).text((10,5),f'{fid} physical PDF page {n}',fill='black')
        thumbs.append(tile)
    for k in range(0,len(thumbs),4):
        subset=thumbs[k:k+4]
        sheet=Image.new('RGB',(1640,2060),'#dddddd')
        for j,tile in enumerate(subset):
            sheet.paste(tile,((j%2)*820,(j//2)*1030))
        sheet.save(out/f'{fid}_sheet{k//4+1}.png')
with zipfile.ZipFile(files['E14']['path']) as z:
    for name in files['E14']['media']:
        (out/('E14_'+Path(name).name)).write_bytes(z.read(name))
print('Rendered',sum(map(len,targets.values())),'pages and extracted E14 media')
