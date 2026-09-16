import re

with open('kisi.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace colors in JS config (though mostly we'll rely on class replacements)
content = content.replace('brandDark: "#0a0a0a"', 'brandDark: "#F8FAFC"')
content = content.replace('brandGray: "#151515"', 'brandGray: "#ffffff"')
content = content.replace('brandCard: "#121212"', 'brandCard: "#ffffff"')
content = content.replace('brandGreen: "#00e676"', 'brandGreen: "#2563EB"')
content = content.replace('brandGreenDark: "#0b4d24"', 'brandGreenDark: "#1D4ED8"')
content = content.replace('textGray: "#a3a3a3"', 'textGray: "#6B7280"')

# Grid background
content = content.replace('rgba(255, 255, 255, 0.05)', 'rgba(0, 0, 0, 0.05)')
content = content.replace('rgba(0, 230, 118, 0.2)', 'rgba(37, 99, 235, 0.2)')
content = content.replace('rgba(0, 230, 118, 0.15)', 'rgba(37, 99, 235, 0.15)')

# Text colors
content = content.replace('text-white', 'text-gray-800')
content = content.replace('text-gray-300', 'text-gray-600')
content = content.replace('text-gray-400', 'text-gray-500')

# Borders
content = content.replace('border-white/5', 'border-gray-200')
content = content.replace('border-white/10', 'border-gray-200')
content = content.replace('border-white/20', 'border-gray-300')
content = content.replace('divide-white/5', 'divide-gray-200')

# Backgrounds
content = content.replace('bg-white/5', 'bg-gray-50')
content = content.replace('bg-white/10', 'bg-gray-100')
content = content.replace('bg-brandGreen/10', 'bg-blue-50')
content = content.replace('border-brandGreen/20', 'border-blue-200')
content = content.replace('bg-brandGreen/20', 'bg-blue-100')

# Hover states
content = content.replace('hover:bg-white/5', 'hover:bg-gray-100')
content = content.replace('hover:bg-white/10', 'hover:bg-gray-200')
content = content.replace('hover:text-white', 'hover:text-blue-600')

# Fix naming to match index.html
content = content.replace('RuangInformatika', 'EduInformatika')
content = content.replace('Pak Ilyas', 'Guru Informatika')

# Inject Navbar item "Pembahasan Soal"
navbar_item = '<a href="#" class="hover:text-blue-600 transition">Pembahasan Soal</a>'
content = content.replace('<a href="materi-search-sort.html"', f'{navbar_item}\n        <a href="materi-search-sort.html"')

# Exception: There are some icons or badges that need white text, like inside solid buttons.
# Let's see... if it uses bg-brandGreen (which is now blue-600), the text should be white.
# I will do a quick regex for bg-brandGreen text-gray-800 -> text-white
content = re.sub(r'bg-brandGreen([^"]*)text-gray-800', r'bg-brandGreen\1text-white', content)

# Save
with open('kisi.html', 'w', encoding='utf-8') as f:
    f.write(content)
