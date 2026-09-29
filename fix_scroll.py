import glob

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Left Column
    content = content.replace(
        '<!-- Left Column -->\n                <div class="flex-1 flex flex-col gap-4">',
        '<!-- Left Column -->\n                <div class="flex-1 flex flex-col gap-4 min-h-0">'
    )
    # Kumpulan Blok wrapper
    content = content.replace(
        '<!-- Kumpulan Blok -->\n                    <div class="flex-1 flex flex-col h-full">',
        '<!-- Kumpulan Blok -->\n                    <div class="flex-1 flex flex-col min-h-0">'
    )

    # 2. Right Column
    content = content.replace(
        '<!-- Right Column -->\n                <div class="flex-1 flex flex-col gap-4 h-full">',
        '<!-- Right Column -->\n                <div class="flex-1 flex flex-col gap-4 min-h-0">'
    )
    # Lembar Resep wrapper
    content = content.replace(
        '<!-- Lembar Resep -->\n                    <div class="flex-1 flex flex-col">',
        '<!-- Lembar Resep -->\n                    <div class="flex-1 flex flex-col min-h-0">'
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added min-h-0 to flex columns.")