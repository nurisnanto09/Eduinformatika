with open('page_koki_algoritma.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('group block"', 'group flex flex-col h-full"')
content = content.replace('<p class="text-gray-600 text-sm mb-4">', '<p class="text-gray-600 text-sm mb-4 flex-grow">')

with open('page_koki_algoritma.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated portal card layout")
