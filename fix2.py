import os
import re

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_idx = content.find('function initSidebar() {};')
    if start_idx != -1:
        end_str = "document.getElementById('level-counter').innerText = currentLevel + 1;\n        }"
        end_idx = content.find(end_str, start_idx)
        if end_idx != -1:
            new_content = content[:start_idx] + 'function initSidebar() {}' + content[end_idx + len(end_str):]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed {filename}')
        else:
            print(f'End not found in {filename}')
    else:
        print(f'Start not found in {filename}')
