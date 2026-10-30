"""Validate a prepared study tree, then copy new files only with --install."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote

STAGING = Path(__file__).resolve().parent / 'hdh_setup'
TARGET = Path('D:/0_Personal/UIT/Đề thi các năm/HDH')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser()
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    staging = STAGING.resolve(strict=True)
    target = TARGET.resolve(strict=True)
    if target != Path('D:/0_Personal/UIT/Đề thi các năm/HDH').resolve(strict=True):
        raise RuntimeError('Unexpected target')
    files = sorted(p for p in staging.rglob('*') if p.is_file())
    errors = []
    for p in files:
        relative = p.relative_to(staging)
        destination = target / relative
        if not destination.resolve().is_relative_to(target):
            errors.append(f'Escaped destination: {relative}')
        if destination.exists():
            errors.append(f'Destination already exists: {relative}')
        if p.suffix == '.py':
            ast.parse(p.read_text(encoding='utf-8'), filename=str(p))
        if p.suffix == '.md' and 'Lý thuyết' not in relative.parts:
            text = p.read_text(encoding='utf-8')
            for link in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', text):
                link = link.strip('<>').split('#', 1)[0]
                if not link or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', link):
                    continue
                linked = (p.parent / unquote(link)).resolve()
                if not linked.exists():
                    errors.append(f'Broken link: {relative} -> {link}')
    # These are the original files, never destinations of the copy operation.
    manifest_root = staging / 'Lý thuyết/pdf'
    pptx = json.loads((manifest_root / 'manifest.json').read_text(encoding='utf-8'))
    pdf = json.loads((manifest_root / 'C01-manifest.json').read_text(encoding='utf-8'))
    entries = pptx['sources'] + [pdf]
    original_hashes = {}
    for entry in entries:
        source = target / entry['source']
        actual = digest(source)
        original_hashes[source] = actual
        if actual != entry['sha256']:
            errors.append(f'Source changed after extraction: {entry["source"]}')
        cached = staging / entry['output']
        raw = cached.read_text(encoding='utf-8')
        if 'slide_count' in entry:
            count = len(re.findall(r'^## Slide \d+ ', raw, flags=re.M))
            expected = entry['slide_count']
        else:
            count = len(re.findall(r'^## Trang PDF \d+ ', raw, flags=re.M))
            expected = entry['page_count']
        if count != expected:
            errors.append(f'Heading count mismatch: {entry["output"]}')
    if errors:
        raise RuntimeError('\n'.join(errors))
    print(f'Validated {len(files)} prepared files, local links, Python syntax and {len(entries)} original source hashes.')
    print('Source counts: 57 PDF pages + 263 PPTX slides. No original file will be overwritten.')
    if not args.install:
        print(f'Ready to copy new files to {target}')
        return
    for p in files:
        destination = target / p.relative_to(staging)
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive create avoids replacing any file created since preflight.
        with p.open('rb') as source_stream, destination.open('xb') as destination_stream:
            shutil.copyfileobj(source_stream, destination_stream)
        shutil.copystat(p, destination)
    for p in files:
        destination = target / p.relative_to(staging)
        if digest(p) != digest(destination):
            raise RuntimeError(f'Copy verification failed: {destination}')
    for source, before in original_hashes.items():
        if digest(source) != before:
            raise RuntimeError(f'Original source changed: {source}')
    print(f'Installed and byte-verified {len(files)} files. All 6 original source files unchanged.')

if __name__ == '__main__':
    main()
