#!/usr/bin/env python3
"""Extract source PDF text once per changed source; keep page numbers."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from pypdf import PdfReader

VERSION = '1.0'
SOURCE = '[BHT CNPM] HDH _Chuong1.pdf'

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()
    src = args.source_root / 'Lý thuyết' / SOURCE
    out = Path(__file__).resolve().parent.parent / 'Lý thuyết' / 'pdf'
    out.mkdir(parents=True, exist_ok=True)
    mf, md, idx = (out / ('C01' + suffix) for suffix in ('-manifest.json', '.md', '-index.md'))
    old = json.loads(mf.read_text(encoding='utf-8')) if mf.exists() else {}
    stat = src.stat()
    same = old.get('size_bytes') == stat.st_size and old.get('mtime_ns') == stat.st_mtime_ns
    sha = old.get('sha256') if same and old.get('sha256') else digest(src)
    fingerprint = digest(Path(__file__).resolve())
    if not args.force and old.get('sha256') == sha and old.get('extractor_sha256') == fingerprint and md.exists() and idx.exists():
        old['mtime_ns'], old['size_bytes'] = stat.st_mtime_ns, stat.st_size
        mf.write_text(json.dumps(old, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'unchanged: {old["page_count"]} pages')
        return
    reader = PdfReader(str(src))
    chunks = ['# Chương 1 — bản trích xuất PDF', '', 'Bản chữ có thể thiếu hình, công thức hoặc sai thứ tự; xem PDF gốc khi cần.', '']
    index = ['# Chương 1 — chỉ mục trang PDF', '', 'Tiêu đề gợi ý từ văn bản đầu trang; kiểm PDF gốc khi cần.', '']
    pages = []
    for n, page in enumerate(reader.pages, 1):
        content = page.extract_text() or ''
        lines = [re.sub(r'\s+', ' ', line).strip() for line in content.splitlines() if line.strip()]
        candidates = [s for s in lines if len(s) >= 5 and not re.fullmatch(r'[\d\W_]+', s)]
        title = candidates[0][:150] if candidates else '(không có tiêu đề chữ rõ)'
        flags = []
        if len(''.join(lines)) < 80: flags.append('ít chữ hoặc không có chữ; xem PDF gốc')
        try:
            if len(page.images): flags.append('có ảnh; xem PDF gốc')
        except Exception:
            flags.append('không xác định được ảnh; xem PDF gốc')
        chunks += [f'## Trang PDF {n} — {title.replace(chr(35), chr(92)+chr(35))}', '']
        if flags: chunks += ['> Lưu ý: ' + '; '.join(flags) + '.', '']
        chunks += [content.strip() or '(Không trích được chữ.)', '']
        index.append(f'- {n}: {title}' + (' [' + '; '.join(flags) + ']' if flags else ''))
        pages.append({'number': n, 'title': title, 'flags': flags, 'text_chars': len(content.strip())})
    md.write_text('\n'.join(chunks), encoding='utf-8')
    idx.write_text('\n'.join(index) + '\n', encoding='utf-8')
    mf.write_text(json.dumps({'source': 'Lý thuyết/' + SOURCE, 'sha256': sha, 'size_bytes': stat.st_size, 'mtime_ns': stat.st_mtime_ns, 'page_count': len(pages), 'extraction_version': VERSION, 'extractor_sha256': fingerprint, 'output': 'Lý thuyết/pdf/C01.md', 'pages': pages}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'extracted: {len(pages)} pages; low text: {sum(p["text_chars"] < 80 for p in pages)}; with images: {sum(any("có ảnh" in f for f in p["flags"]) for p in pages)}')

if __name__ == '__main__':
    main()
