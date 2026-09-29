import re

emojis = {
    1: '🎓', 2: '🛒', 3: '🌡️', 4: '🗳️',
    5: '🔢', 6: '🛗', 7: '⏰', 8: '🚥', 9: '📦'
}

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Fix the emoji property
    content = re.sub(r'"emoji":\s*".*?",', f'"emoji": "{emojis[i]}",', content)
    
    # Fix the broken header emoji
    content = re.sub(r'<div class="([^"]*?)" id="level-emoji">.*?</div>', f'<div class="\\1" id="level-emoji">{emojis[i]}</div>', content)
    
    # Fix the broken cooking emoji
    content = re.sub(r'<div class="([^"]*?)" id="cooking-emoji">.*?</div>', f'<div class="\\1" id="cooking-emoji">{emojis[i]}</div>', content)

    # Fix success and fail emojis
    content = re.sub(r'emoji\.innerText\s*=\s*".*?";\s*title\.innerText\s*=\s*"BERHASIL!"', 
                     'emoji.innerText = "🎉👏";\n                    title.innerText = "BERHASIL!"', content)
    content = re.sub(r'emoji\.innerText\s*=\s*".*?";\s*title\.innerText\s*=\s*"GAGAL / ERROR"', 
                     'emoji.innerText = "❌💥";\n                    title.innerText = "GAGAL / ERROR"', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed emojis cleanly.")