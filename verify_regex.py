import json, re, glob
for file in glob.glob('game_koki_*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'"correct":\s*\[(.*?)\]', content, re.DOTALL)
        if match:
            blocks = [line.strip().strip('"').replace('",', '') for line in match.group(1).split('\n') if line.strip()]
            for block in blocks:
                m = re.search(r'(?:WHILE|IF)\s+([a-zA-Z0-9_]+)\s+(?:DO|THEN)', block)
                if m:
                    print(f'{file}: MATCHED {m.group(1)}')
