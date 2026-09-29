import glob

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'startTimer();' not in content:
        content = content.replace('loadLevel(0);', 'loadLevel(0);\n            startTimer();')
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed startTimer invocation.")