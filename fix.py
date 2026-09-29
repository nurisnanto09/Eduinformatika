import os
import re

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r'function initSidebar\(\) \{\}\;[\s\S]*?document\.getElementById\(\'level-counter\'\)\.innerText = currentLevel \+ 1;\s*\}'
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, 'function initSidebar() {}', content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed {filename}')
    else:
        print(f'Pattern not found in {filename}')
