import re
with open('kisi.html', 'r', encoding='utf-8') as f:
    c = f.read()
start = c.find('id="modalOverlay"')
end = c.find('modalSoalTeks', start)
with open('out.txt', 'w', encoding='utf-8') as f2:
    f2.write(c[start:end+50])
