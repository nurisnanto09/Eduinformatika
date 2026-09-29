import glob

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Workspace Layout wrapper
    content = content.replace(
        '<div class="flex-1 p-6 flex flex-col lg:flex-row gap-6 overflow-y-auto lg:overflow-hidden h-full">',
        '<div class="flex-1 p-6 flex flex-col lg:flex-row gap-6 overflow-y-auto lg:overflow-hidden lg:h-full">'
    )
    
    # 2. Source Blocks
    content = content.replace(
        'class="flex-1 flex flex-col gap-2 p-4 bg-orange-100/50 rounded-xl border-2 border-dashed border-orange-200 min-h-0 overflow-y-auto"',
        'class="lg:flex-1 flex flex-col gap-2 p-4 bg-orange-100/50 rounded-xl border-2 border-dashed border-orange-200 min-h-[100px] lg:min-h-0 lg:overflow-y-auto transition-all duration-300"'
    )
    
    # 3. Target Blocks
    content = content.replace(
        'class="flex-1 flex flex-col gap-2 p-4 bg-slate-800 rounded-xl border-2 border-slate-900 min-h-0 shadow-inner overflow-y-auto"',
        'class="lg:flex-1 flex flex-col gap-2 p-4 bg-slate-800 rounded-xl border-2 border-slate-900 min-h-[150px] lg:min-h-0 shadow-inner lg:overflow-y-auto transition-all duration-300"'
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied dynamic height for mobile.")