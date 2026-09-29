import glob

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('min-h-[200px]', 'min-h-0')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replaced min-h-[200px] with min-h-0.")