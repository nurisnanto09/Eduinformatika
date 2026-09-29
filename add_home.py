import glob
import re

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the timer block
    timer_pattern = r'<!-- Timer -->\s*<div class="flex flex-col items-center bg-red-50 border-2 border-red-200 p-2 rounded-xl shadow-inner min-w-\[120px\]">.*?</div>'
    match = re.search(timer_pattern, content, re.DOTALL)
    
    if match:
        original_timer = match.group(0)
        
        # Wrap it in a new container alongside the Home button
        new_right_side = '''<!-- Right Actions: Home & Timer -->
                <div class="flex items-center gap-4">
                    <a href="page_koki_algoritma.html" class="flex flex-col items-center justify-center bg-blue-50 hover:bg-blue-600 text-blue-600 hover:text-white border-2 border-blue-200 hover:border-blue-600 p-2 rounded-xl transition-colors shadow-sm h-full" style="height: 100%; min-height: 72px; min-width: 72px;" title="Kembali ke Menu Utama">
                        <i class="fas fa-home text-2xl mb-1"></i>
                        <span class="text-[10px] font-bold uppercase tracking-wider">Kembali</span>
                    </a>
                    
                    ''' + original_timer + '''
                </div>'''
                
        content = content.replace(original_timer, new_right_side)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Added Home button next to timer.")