import re
with open('kisi.html', 'r', encoding='utf-8') as f:
    c = f.read()
m = re.search(r'<div id=\"modalOverlay\".*?>', c)
if m: print(m.group(0))
