import re, glob

emojis = {
    1: '🎓', 2: '🛒', 3: '🌡️', 4: '🗳️',
    5: '🔢', 6: '🛗', 7: '⏰', 8: '🚥', 9: '📦'
}

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The emoji property is something like "emoji": "dYZ"", followed by "concept"
    content = re.sub(r'"emoji":\s*".*?",', f'"emoji": "{emojis[i]}",', content)
    
    # Fix the corrupted success emojis
    content = re.sub(r'emoji\.innerText = ".*?";\n\s*title\.innerText = "BERHASIL!"', 
                     'emoji.innerText = "🎉👏";\n                    title.innerText = "BERHASIL!"', content)
    
    # Fix the corrupted fail emojis
    content = re.sub(r'emoji\.innerText = ".*?";\n\s*title\.innerText = "GAGAL / ERROR"', 
                     'emoji.innerText = "❌💥";\n                    title.innerText = "GAGAL / ERROR"', content)
    
    # Fix header level-emoji
    content = re.sub(r'(<div class="[^"]*?" id="level-emoji">).*?(</div>)', 
                     f'\\g<1>{emojis[i]}\\g<2>', content)
    
    # Fix cooking-emoji
    content = re.sub(r'(<div class="[^"]*?" id="cooking-emoji">).*?(</div>)', 
                     f'\\g<1>{emojis[i]}\\g<2>', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed emojis aggressively.")