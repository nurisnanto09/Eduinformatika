import glob
import re

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Success Emoji
    content = re.sub(
        r'emoji\.innerText\s*=\s*".*?";\s*(title\.innerText\s*=\s*"BERHASIL!";)',
        r'emoji.innerText = "🎉👏";\n                    \1',
        content
    )
    
    # Fail Emoji
    content = re.sub(
        r'emoji\.innerText\s*=\s*".*?";\s*(title\.innerText\s*=\s*"GAGAL / ERROR";)',
        r'emoji.innerText = "❌💀";\n                    \1',
        content
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed overlay emojis.")