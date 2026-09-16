import re
with open('kisi.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'<div id=\"modalSoalTeks\".*?>', c)
if m: print(m.group(0))

m = re.search(r'btnOpsi\.className = \".*?\"', c)
if m: print(m.group(0))
