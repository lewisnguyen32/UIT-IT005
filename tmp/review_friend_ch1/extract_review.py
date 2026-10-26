from pathlib import Path
import json
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image, ImageDraw

HERE=Path(__file__).resolve().parent
SOURCE=Path('C:/Users/phuoc/Downloads/Chương 1 - Ôn tập.pdf')
HERE.mkdir(parents=True,exist_ok=True)
reader=PdfReader(SOURCE)
blocks=[]
stats=[]
for i,page in enumerate(reader.pages,1):
    text=page.extract_text() or ''
    blocks.append(f'\n\n===== PDF PAGE {i} =====\n{text}')
    stats.append({'page':i,'chars':len(text)})
(HERE/'friend_ch1.txt').write_text(''.join(blocks),encoding='utf-8')
(HERE/'source.json').write_text(json.dumps({'path':str(SOURCE),'pages':len(reader.pages),'page_stats':stats},ensure_ascii=False,indent=2),encoding='utf-8')
pdf=pdfium.PdfDocument(SOURCE)
for i in range(len(pdf)):
    image=pdf[i].render(scale=2).to_pil().convert('RGB')
    image.save(HERE/f'page-{i+1:02}.png')
for start in range(0,len(pdf),4):
    sheet=Image.new('RGB',(1600,2200),'#dddddd')
    draw=ImageDraw.Draw(sheet)
    for n,i in enumerate(range(start,min(start+4,len(pdf)))):
        image=Image.open(HERE/f'page-{i+1:02}.png')
        image.thumbnail((780,1060))
        x=(n%2)*800
        y=(n//2)*1100
        sheet.paste(image,(x,y+30))
        draw.text((x+10,y+5),f'PDF page {i+1}',fill='black')
    sheet.save(HERE/f'contact-{start+1:02}.png')
print(json.dumps({'pages':len(reader.pages),'page_stats':stats},ensure_ascii=False))
print(''.join(blocks))
