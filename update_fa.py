import os

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'font-awesome/6.0.0/css/all.min.css' in content:
            new_content = content.replace('font-awesome/6.0.0/css/all.min.css', 'font-awesome/6.4.0/css/all.min.css')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
