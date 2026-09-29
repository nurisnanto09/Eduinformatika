import re

cases = [
    {"title": "Pembelian Tiket Bioskop", "icon": "fa-ticket", "desc": "Misi: Pembelian Tiket Bioskop (Batas Usia Minimal)"},
    {"title": "Game Tebak Angka", "icon": "fa-bullseye", "desc": "Misi: Game Tebak Angka Rahasia (Komparasi Nilai)"},
    {"title": "Mesin Vending Minuman", "icon": "fa-glass-water", "desc": "Misi: Mesin Vending Minuman (Cek Target Harga)"},
    {"title": "Validasi Panjang Password", "icon": "fa-lock", "desc": "Misi: Validasi Panjang Password Akun"},
    {"title": "Penarikan Saldo ATM", "icon": "fa-credit-card", "desc": "Misi: Simulasi Penarikan Saldo ATM (Batas Saldo)"},
    {"title": "Upload File Maksimal", "icon": "fa-file-upload", "desc": "Misi: Filter Ukuran File Unggahan (Batas Maksimal MB)"},
    {"title": "Pengisian Bahan Bakar", "icon": "fa-gas-pump", "desc": "Misi: Pengisian Bahan Bakar Kendaraan (Target Liter)"},
    {"title": "Kuis Pilihan Ganda", "icon": "fa-list-check", "desc": "Misi: Kuis Pilihan Ganda (Validasi Nilai Kelulusan)"},
    {"title": "Pendingin Ruangan (AC)", "icon": "fa-snowflake", "desc": "Misi: Pengecekan Suhu Ruangan Server Otomatis"}
]

with open('page_koki_algoritma.html', 'r', encoding='utf-8') as f:
    content = f.read()

for i, case in enumerate(cases):
    # Regex to capture the card block. We can just search for game_koki_1.html to game_koki_9.html
    # and replace the corresponding parts.
    pattern = r'(<a href="game_koki_' + str(i+1) + r'\.html".*?</a>)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        card = match.group(1)
        
        # Replace icon
        card = re.sub(r'<i class="fas fa-[^"]+"></i>', f'<i class="fas {case["icon"]}"></i>', card, count=1)
        
        # Replace title
        card = re.sub(r'<h2 class="text-xl font-bold text-gray-800 mb-2">.*?</h2>', f'<h2 class="text-xl font-bold text-gray-800 mb-2">{case["title"]}</h2>', card)
        
        # Replace description
        card = re.sub(r'<p class="text-gray-600 text-sm mb-4">.*?</p>', f'<p class="text-gray-600 text-sm mb-4">{case["desc"]}</p>', card)
        
        # Replace "Mulai Memasak"
        card = card.replace('Mulai Memasak', 'Mulai Misi')
        
        content = content.replace(match.group(1), card)

# Also update the title of the page?
content = content.replace('Portal Misi Koki Algoritma', 'Portal Misi Logika Algoritma')
content = content.replace('fa-hat-chef', 'fa-code-branch')

with open('page_koki_algoritma.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated page_koki_algoritma.html")
