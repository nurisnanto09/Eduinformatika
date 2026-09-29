import os
import re

for i in range(4, 10):
    filename = f'game_koki_{i}.html'
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start = content.find('function initSidebar() {};')
    if start != -1:
        end = content.find('document.getElementById(\'level-counter\').innerText = currentLevel + 1;', start)
        if end != -1:
            end = content.find('}', end) + 1
            new_content = content[:start] + 'function initSidebar() {}' + content[end:]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed {filename}')
