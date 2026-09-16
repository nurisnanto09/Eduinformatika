import re
with open('kisi.html', 'r', encoding='utf-8') as f:
    c = f.read()
for m in re.finditer(r'<[^>]*modalSoalTeks[^>]*>', c):
    print(m.group(0))
