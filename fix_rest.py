import os

for i in range(4, 10):
    filename = f'game_koki_{i}.html'
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    target_str = '''        function initSidebar() {};
                btn.onclick = () => loadLevel(idx);
                btn.innerHTML = 
                    <div class="text-2xl"></div>
                    <div class="flex-1">
                        <div class="font-bold text-sm">. </div>
                        <div class="text-xs "></div>
                    </div>
                ;
                levelList.appendChild(btn);
            });
            document.getElementById('level-counter').innerText = currentLevel + 1;
        }'''
        
    if target_str in content:
        new_content = content.replace(target_str, '        function initSidebar() {}')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed {filename}')
    else:
        print(f'Not found in {filename}')
