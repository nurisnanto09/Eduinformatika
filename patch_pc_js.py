with open('lkpd_pseudocode.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<script>'
replacement = '''<script>
        function updateMoodBadge(rowIdx, moodText) {
            const label = document.getElementById(`mood-label-${rowIdx}`);
            if (label) {
                label.innerText = moodText;
                let colorClass = 'text-gray-600';
                if (moodText.includes('Senang')) colorClass = 'text-emerald-600';
                else if (moodText.includes('Sedih')) colorClass = 'text-blue-600';
                else if (moodText.includes('Marah')) colorClass = 'text-rose-600';
                else if (moodText.includes('Mengantuk')) colorClass = 'text-amber-600';
                else if (moodText.includes('Semangat')) colorClass = 'text-purple-600';
                label.className = `text-[10px] font-black mt-0.5 text-center ${colorClass}`;
            }
        }
'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('lkpd_pseudocode.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Success')
else:
    print('Failed')
