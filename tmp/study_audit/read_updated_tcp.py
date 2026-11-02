from pathlib import Path
import hashlib
import json
import shutil
import sys
import logging
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8')
logging.getLogger('pypdf').setLevel(logging.ERROR)
root = Path.cwd()
original = Path('C:/Users/phuoc/Downloads/Chapter_3_2023_3.6 TCP_1st.pdf')
target = root / 'Lý thuyết' / original.name
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
if target.exists():
    if digest(target) != digest(original):
        raise RuntimeError('An existing source copy differs; refusing to overwrite it.')
else:
    shutil.copy2(original, target)
reader = PdfReader(target)
pages = [page.extract_text() or '' for page in reader.pages]
base = root / 'tmp/study_audit/T3_TCP_1st_2023_20261102'
base.with_suffix('.txt').write_text('\n\n'.join(f'===== PDF PAGE {i} =====\n{t}' for i, t in enumerate(pages, 1)), encoding='utf-8')
meta = {'code': 'T3-TCP-2023', 'original': str(original), 'local_copy': str(target), 'sha256': digest(target), 'pages': len(pages)}
base.with_suffix('.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(meta, ensure_ascii=False))
for i, content in enumerate(pages, 1):
    if any(key.lower() in content.lower() for key in ('EstimatedRTT', 'SampleRTT', 'DevRTT', 'TimeoutInterval')):
        print(f'\n===== PDF PAGE {i} =====\n{content}')
