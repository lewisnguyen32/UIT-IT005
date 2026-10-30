#!/usr/bin/env python3
"""Extract searchable slide text from HDH PPTX files; no third-party packages.

Default layout: HDH/tools/extract_theory.py and HDH/Lý thuyết/*.pptx.
Use --source-root for a separate read-only source tree during staging.
"""
import argparse
import hashlib
import json
import posixpath
import re
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

VERSION = '1.3'
NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
      'rel': 'http://schemas.openxmlformats.org/package/2006/relationships'}
FILES = ['#Week01-Chapter0 2024.pptx', '#Week02-Chapter2 2024.pptx',
         '#Week03-Chapter3 2024.pptx', '#Week04-Chapter4-1 2024.pptx',
         '#Week05-Chapter4-2 2024.pptx']

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def paragraphs(element):
    result = []
    for p in element.findall('.//a:p', NS):
        # Flatten each outer math object once, without pretending to preserve layout.
        def text_of(x):
            if x.tag in ('{%s}oMath' % NS['m'], '{%s}oMathPara' % NS['m']):
                pieces = [t.text or '' for t in x.findall('.//m:t', NS)]
                return '[Office Math (chữ phẳng, xem công thức gốc): ' + ' '.join(pieces) + ']'
            if x.tag == '{%s}t' % NS['a']: return x.text or ''
            if x.tag == '{%s}br' % NS['a']: return '\n'
            return ''.join(text_of(child) for child in x)
        s = text_of(p).strip()
        if s:
            result.append(s)
    return result

def slide_content(slide):
    """Keep text and table objects in slide shape-tree order."""
    blocks, flags = [], []
    def visit(node):
        kind = node.tag.rsplit('}', 1)[-1]
        if kind == 'sp':
            blocks.extend(paragraphs(node))
        elif kind == 'graphicFrame':
            for table in node.findall('.//a:tbl', NS):
                flags.append('bảng')
                rows = []
                for tr in table.findall('./a:tr', NS):
                    cells = []
                    for cell in tr.findall('./a:tc', NS):
                        if any(k in cell.attrib for k in ('gridSpan', 'rowSpan', 'hMerge', 'vMerge')):
                            if 'ô gộp; xem bảng gốc' not in flags: flags.append('ô gộp; xem bảng gốc')
                        cells.append('<br>'.join(paragraphs(cell)).replace('|', '\\|').replace('\n', '<br>'))
                    rows.append(cells)
                if rows:
                    width = max(map(len, rows))
                    rows = [r + [''] * (width - len(r)) for r in rows]
                    # Empty header avoids implying the original first row is a header.
                    fmt = lambda row: '| ' + ' | '.join(row) + ' |'
                    blocks.append('\n'.join([fmt([''] * width), fmt(['---'] * width)] + [fmt(r) for r in rows]))
        else:
            for child in node:
                visit(child)
    tree = slide.find('./p:cSld/p:spTree', NS)
    if tree is not None: visit(tree)
    return blocks, list(dict.fromkeys(flags))

def extract(path):
    with zipfile.ZipFile(path) as z:
        pres = ET.fromstring(z.read('ppt/presentation.xml'))
        rels = ET.fromstring(z.read('ppt/_rels/presentation.xml.rels'))
        targets = {r.get('Id'): r.get('Target') for r in rels}
        slides = []
        for sid in pres.findall('./p:sldIdLst/p:sldId', NS):
            target = targets[sid.get('{%s}id' % NS['r'])]
            slidepath = posixpath.normpath(posixpath.join('ppt', target.lstrip('/'))) if not target.startswith('/') else target.lstrip('/')
            slide = ET.fromstring(z.read(slidepath))
            texts, content_flags = slide_content(slide)
            title = None
            for shape in slide.findall('.//p:sp', NS):
                ph = shape.find('./p:nvSpPr/p:nvPr/p:ph', NS)
                if ph is not None and ph.get('type') in ('title', 'ctrTitle'):
                    ps = paragraphs(shape)
                    if ps:
                        title = ' '.join(ps)
                        break
            if not title:
                candidates = [t for t in texts if not t.startswith('| ') and not t.startswith('Thực hiện bởi Trường Đại học')
                              and not re.fullmatch(r'[\d\s‹›<#>]+', t)]
                # Section labels supply context even when shapes are ordered after a graph.
                sections = [t for t in candidates if re.match(r'^\d+(?:\.\d+)+\.\s*\D', t)]
                title = sections[0] if sections else (candidates[0] if candidates else '(không có tiêu đề văn bản)')
            title = re.sub(r'\s+', ' ', title)
            flags = content_flags
            if slide.findall('.//m:oMath', NS) or slide.findall('.//m:oMathPara', NS):
                flags.append('Office Math: chữ phẳng không giữ bố cục; xem công thức gốc')
            relpath = posixpath.join(posixpath.dirname(slidepath), '_rels', posixpath.basename(slidepath) + '.rels')
            if relpath in z.namelist():
                rs = ET.fromstring(z.read(relpath))
                types = ' '.join(r.get('Type', '').lower() for r in rs)
                if any(x in types for x in ('/image', '/video', '/audio', '/media')): flags.append('media/hình')
                if '/chart' in types: flags.append('biểu đồ')
                if any(x in types for x in ('/oleobject', '/package')): flags.append('OLE/nhúng')
                if '/diagram' in types: flags.append('sơ đồ/SmartArt')
            meaningful = [t for t in texts if t != title and not t.isdigit()
                          and not t.startswith('Thực hiện bởi Trường Đại học')
                          and not re.match(r'^\d+(?:\.\d+)*\.\s', t)]
            if len(''.join(meaningful)) < 50: flags.append('ít hoặc không có chữ nội dung; xem slide gốc')
            slides.append((title, texts, flags))
        return slides

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()
    dest_root = Path(__file__).resolve().parent.parent
    output = dest_root / 'Lý thuyết' / 'pdf'
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / 'manifest.json'
    old = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {}
    extractor_sha = digest(Path(__file__).resolve())
    entries = []
    for i, name in enumerate(FILES, 1):
        src = args.source_root / 'Lý thuyết' / name
        outname = f'W{i:02}.md'
        oldentry = next((x for x in old.get('sources', []) if x['source'] == 'Lý thuyết/' + name), {})
        stat = src.stat()
        same_stat = oldentry.get('size_bytes') == stat.st_size and oldentry.get('mtime_ns') == stat.st_mtime_ns
        sha = oldentry.get('sha256') if same_stat and oldentry.get('sha256') else digest(src)
        if not args.force and oldentry.get('sha256') == sha and oldentry.get('extractor_sha256') == extractor_sha and oldentry.get('extraction_version') == VERSION and (output / outname).exists() and oldentry.get('slides'):
            oldentry['size_bytes'], oldentry['mtime_ns'] = stat.st_size, stat.st_mtime_ns
            entries.append(oldentry)
            print(f'{outname}: unchanged ({oldentry["slide_count"]} slides)')
            continue
        slides = extract(src)
        chunks = [f'# {name}\n\nBản trích xuất văn bản từ PPTX; thứ tự theo presentation. Hình và nội dung nhúng cần xem slide gốc. Không trích speaker notes.\n']
        meta = []
        for n, (title, texts, flags) in enumerate(slides, 1):
            safe_title = title.replace('\n', ' ').replace('#', '\\#')
            chunks.append(f'## Slide {n} — {safe_title}\n')
            if flags: chunks.append('> Lưu ý: ' + '; '.join(flags) + '.\n')
            chunks.extend(t + '\n' for t in texts)
            meta.append({'number': n, 'title': title, 'flags': flags})
        (output / outname).write_text('\n'.join(chunks), encoding='utf-8')
        entry = {'source': 'Lý thuyết/' + name, 'sha256': sha, 'size_bytes': stat.st_size, 'mtime_ns': stat.st_mtime_ns, 'slide_count': len(slides), 'extraction_version': VERSION, 'extractor_sha256': extractor_sha, 'output': 'Lý thuyết/pdf/' + outname, 'slides': meta}
        entries.append(entry)
        print(f'{outname}: extracted {len(slides)} slides')
    manifest_path.write_text(json.dumps({'extraction_version': VERSION, 'sources': entries}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    index = ['# Chỉ mục slide lý thuyết HDH', '', 'Bản chữ trích từ PPTX; khi có hình, sơ đồ hoặc dữ liệu thiếu hãy xem slide gốc. Số slide theo thứ tự trong tệp.', '', '**Tuần 5:** người học ghi nhận có vẻ học đến slide 28, từ slide 29 đọc thêm; đây là mốc chưa xác nhận chính thức.', '']
    for i, e in enumerate(entries, 1):
        index += [f'## [W{i:02}](W{i:02}.md) — {e["slide_count"]} slide', '']
        for s in e['slides']:
            flags = ' [' + ', '.join(s['flags']) + ']' if s['flags'] else ''
            index.append(f'- {s["number"]}: {s["title"]}{flags}')
        index.append('')
    (output / 'index.md').write_text('\n'.join(index), encoding='utf-8')

if __name__ == '__main__':
    main()
