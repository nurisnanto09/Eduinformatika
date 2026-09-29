import re, glob
for file in glob.glob('game_koki_*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'"correct":\s*\[(.*?)\]', content, re.DOTALL)
        if match:
            print(f'--- {file} ---')
            print(match.group(1).strip())
