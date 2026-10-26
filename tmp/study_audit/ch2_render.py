from pathlib import Path
import json
import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw

root = Path(__file__).resolve().parent
manifest = {x['id']: x for x in json.loads((root/'manifest.json').read_text(encoding='utf-8')) if 'id' in x}
sets = [
    ('E17', [58,66,73,86]),
    ('E17', [87,89,91,92]),
    ('E17', [93,101,104,105]),
    ('E17', [106,107,108]),
    ('E10', [4]),
    ('E15', [12]),
]
for n,(sid,pages) in enumerate(sets,1):
    doc = pdfium.PdfDocument(manifest[sid]['path'])
    tiles=[]
    for p in pages:
        im = doc[p-1].render(scale=1.7).to_pil().convert('RGB')
        im.thumbnail((1500,1100))
        tile=Image.new('RGB',(1520,1160),'white')
        ImageDraw.Draw(tile).text((10,10),f'{sid} PDF page {p}',fill='black')
        tile.paste(im,(10,50))
        tiles.append(tile)
    cols=2 if len(tiles)>1 else 1
    sheet=Image.new('RGB',(1520*cols,1160*((len(tiles)+cols-1)//cols)),'#dddddd')
    for i,tile in enumerate(tiles):
        sheet.paste(tile,((i%cols)*1520,(i//cols)*1160))
    target=root/f'ch2_figures_{n}.png'
    sheet.save(target)
    print(target)
