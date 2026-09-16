import re
with open('kisi.html', 'r', encoding='utf-8') as f:
    c = f.read()
start = c.find('id="modalOverlay"')
end = c.find('modalSoalTeks', start)
print(c[start:end+50])
