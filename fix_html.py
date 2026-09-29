import glob

injection_html = '''
    <div class="px-6 pt-4 pb-0 hidden md:block">
        <div class="bg-indigo-50 border-l-4 border-indigo-500 p-4 rounded-r-lg shadow-sm">
            <h3 class="text-sm font-bold text-indigo-800 mb-1 flex items-center gap-2">
                <i class="fas fa-book-open"></i> Studi Kasus
            </h3>
            <p class="text-sm text-indigo-900 leading-relaxed" id="level-story"></p>
        </div>
    </div>
'''

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="level-story"' not in content:
        # Find '<!-- Workspace -->'
        target_html = '<!-- Workspace -->'
        if target_html in content:
            content = content.replace(target_html, injection_html + '\n            ' + target_html)
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected HTML successfully.")