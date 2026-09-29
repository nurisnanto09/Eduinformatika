import re, glob

emojis = {
    1: '🎓', 2: '🛒', 3: '🌡️', 4: '🗳️',
    5: '🔢', 6: '🛗', 7: '⏰', 8: '🚥', 9: '📦'
}

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the emoji in the JSON levels array
    content = re.sub(r'("emoji":\s*)"[^"]*"', f'\\1"{emojis[i]}"', content)
    
    # Fix the corrupted success emojis
    content = re.sub(r'emoji\.innerText = ".*?";\s*title\.innerText = "BERHASIL!"', 
                     'emoji.innerText = "🎉👏";\n                    title.innerText = "BERHASIL!"', content)
    
    # Fix the corrupted fail emojis
    content = re.sub(r'emoji\.innerText = ".*?";\s*title\.innerText = "GAGAL / ERROR"', 
                     'emoji.innerText = "❌💥";\n                    title.innerText = "GAGAL / ERROR"', content)
    
    # Fix header level-emoji if corrupted
    content = re.sub(r'<div class="(.*?) id="level-emoji">.*?</div>', 
                     f'<div class="\\1 id="level-emoji">{emojis[i]}</div>', content)
    
    # Fix cooking-emoji if corrupted
    content = re.sub(r'<div class="(.*?) id="cooking-emoji">.*?</div>', 
                     f'<div class="\\1 id="cooking-emoji">{emojis[i]}</div>', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed emojis.")