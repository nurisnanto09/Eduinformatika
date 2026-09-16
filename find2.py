import re
with open('kisi.html', 'r', encoding='utf-8') as f:
    c = f.read()
for m in re.finditer(r'<p[^>]*class="[^"]*"[^>]*>', c):
    if 'text-gray-100' in m.group(0) or 'text-gray-200' in m.group(0) or 'text-gray-300' in m.group(0) or 'text-gray-400' in m.group(0) or 'text-gray-500' in m.group(0):
        pass # too many
        
for m in re.finditer(r'teks: `([^`]+)`', c):
    print(m.group(1)[:100])
