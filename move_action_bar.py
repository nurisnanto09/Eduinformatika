import glob
import re

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the action bar block
    match_action = re.search(r'<!-- Action Bar -->.*?</div>\s*</div>\s*</div>', content, re.DOTALL)
    if not match_action:
        # maybe it's just the div
        match_action = re.search(r'<!-- Action Bar -->\s*<div class="bg-white p-4 border-t[^>]*>.*?</div>', content, re.DOTALL)
    
    if match_action:
        action_bar_html = match_action.group(0)
        
        # Remove it from the bottom
        content = content.replace(action_bar_html, '')
        
        # Modify the action bar for top placement
        # Change border-t to border-b, and padding
        new_action_bar = action_bar_html.replace('bg-white p-4 border-t border-gray-200 flex justify-between items-center z-10 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]', 'px-6 pt-4 flex justify-between items-center')
        # Remove the comment
        new_action_bar = new_action_bar.replace('<!-- Action Bar -->', '<!-- Action Bar (Top) -->')
        
        # Insert it after Studi Kasus or before Workspace
        target = '<!-- Workspace -->'
        if target in content:
            content = content.replace(target, new_action_bar + '\n            ' + target)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Moved Action Bar to top.")