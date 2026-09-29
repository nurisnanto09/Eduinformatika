import os
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('btn.innerText = sim.name;', 'btn.innerHTML = \'<i class="fas fa-play-circle mr-2"></i>\' + sim.name;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
