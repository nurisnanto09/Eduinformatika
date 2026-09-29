import glob
import re

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The action bar might have extra closing divs after it before <!-- Workspace -->
    pattern = r'(<!-- Action Bar \(Top\) -->.*?Jalankan Program!.*?</button>\s*</div>)\s*</div>\s*</div>\s*(<!-- Workspace -->)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content.replace(match.group(0), match.group(1) + '\n            ' + match.group(2))
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed extra divs.")