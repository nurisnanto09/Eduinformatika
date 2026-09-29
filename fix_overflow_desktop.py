import glob

for file in glob.glob('game_koki_*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change grandparent's overflow
    content = content.replace(
        '<div class="flex-1 p-6 flex flex-col lg:flex-row gap-6 overflow-y-auto">',
        '<div class="flex-1 p-6 flex flex-col lg:flex-row gap-6 overflow-y-auto lg:overflow-hidden">'
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated grandparent overflow for desktop.")
