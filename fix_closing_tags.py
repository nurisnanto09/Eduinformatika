import glob

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    target = '<!-- Cooking Animation Overlay'
    
    # Check if they are already there
    if '</div>\\n        </div>\\n        <!-- Cooking' not in content:
        # We need to insert closing tags for:
        # <div class="w-full flex flex-col bg-slate-50 relative h-full">
        # <div class="w-full h-full flex flex-col md:flex-row relative">
        closing = '        </div>\n    </div>\n\n    '
        content = content.replace(target, closing + target)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Fixed closing tags.")