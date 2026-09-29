import glob

for file in glob.glob('game_koki_*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add flex-1 and overflow-y-auto to source-blocks
    content = content.replace(
        '<div id="source-blocks" class="flex flex-col gap-2 p-4 bg-orange-100/50 rounded-xl border-2 border-dashed border-orange-200 min-h-[200px]">',
        '<div id="source-blocks" class="flex-1 flex flex-col gap-2 p-4 bg-orange-100/50 rounded-xl border-2 border-dashed border-orange-200 min-h-[200px] overflow-y-auto">'
    )
    
    # Add flex-1 and overflow-y-auto to target-blocks
    content = content.replace(
        '<div id="target-blocks" class="flex flex-col gap-2 p-4 bg-slate-800 rounded-xl border-2 border-slate-900 min-h-[200px] shadow-inner">',
        '<div id="target-blocks" class="flex-1 flex flex-col gap-2 p-4 bg-slate-800 rounded-xl border-2 border-slate-900 min-h-[200px] shadow-inner overflow-y-auto">'
    )
    
    # Optional: ensure grandparent doesn't scroll excessively or let it be. We can just leave grandparent as is, the flex-1 will take available height.
    # Actually, grandparent overflow-y-auto is fine for smaller screens.

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added internal scrolling to blocks containers.")
