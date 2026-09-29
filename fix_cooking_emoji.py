import glob
import re

emojis = {
    1: '🎓', 2: '🛒', 3: '🌡️', 4: '🗳️',
    5: '🔢', 6: '🛗', 7: '⏰', 8: '🚥', 9: '📦'
}

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix cooking-emoji
    content = re.sub(r'<div class="([^"]*?)" id="cooking-emoji">.*?</div>', f'<div class="\\1" id="cooking-emoji">{emojis[i]}</div>', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed cooking emoji.")