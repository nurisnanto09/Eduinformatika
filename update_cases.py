import json
import re

cases = [
    {
        "id": 1,
        "emoji": "🎓",
        "concept": "IF-ELSE",
        "title": "Penentuan Kelulusan Ujian",
        "desc": "Misi: Cek nilai Budi. Jika >= 75 maka lulus, sebaliknya remidi.",
        "correct": [
            "INPUT nilai",
            "IF nilai >= 75 THEN",
            "  PRINT \"Selamat, Anda Lulus!\"",
            "ELSE",
            "  PRINT \"Anda Belum Lulus, Silakan Remidi\"",
            "END IF"
        ],
        "distractors": [
            "IF nilai < 75 THEN",
            "PRINT \"Nilai tidak valid\""
        ],
        "icon": "fa-graduation-cap"
    },
    {
        "id": 2,
        "emoji": "🛒",
        "concept": "IF-ELSE",
        "title": "Diskon Belanja Swalayan",
        "desc": "Misi: Cek total belanja. Jika >= Rp100.000 maka diskon 10%, sebaliknya tidak ada diskon.",
        "correct": [
            "INPUT total_belanja",
            "IF total_belanja >= 100000 THEN",
            "  PRINT \"Anda mendapatkan diskon 10%!\"",
            "ELSE",
            "  PRINT \"Belanja kurang dari Rp100.000, tidak ada diskon\"",
            "END IF"
        ],
        "distractors": [
            "IF total_belanja < 100000 THEN",
            "PRINT \"Masukkan uang pembayaran\""
        ],
        "icon": "fa-shopping-cart"
    },
    {
        "id": 3,
        "emoji": "🌡️",
        "concept": "IF-ELSE",
        "title": "Klasifikasi Suhu Tubuh",
        "desc": "Misi: Cek suhu tubuh. Jika > 37.5 maka demam, sebaliknya normal.",
        "correct": [
            "INPUT suhu_tubuh",
            "IF suhu_tubuh > 37.5 THEN",
            "  PRINT \"Peringatan: Suhu tubuh tinggi / Demam\"",
            "ELSE",
            "  PRINT \"Suhu tubuh normal dan sehat\"",
            "END IF"
        ],
        "distractors": [
            "IF suhu_tubuh < 37.5 THEN",
            "PRINT \"Alat rusak\""
        ],
        "icon": "fa-thermometer-half"
    },
    {
        "id": 4,
        "emoji": "🗳️",
        "concept": "IF-ELSE",
        "title": "Kategori Usia Pemilih",
        "desc": "Misi: Cek umur warga. Jika >= 17 maka boleh memilih, sebaliknya tolak.",
        "correct": [
            "INPUT umur",
            "IF umur >= 17 THEN",
            "  PRINT \"Silakan menggunakan hak pilih Anda\"",
            "ELSE",
            "  PRINT \"Belum cukup umur untuk memilih\"",
            "END IF"
        ],
        "distractors": [
            "IF umur <= 17 THEN",
            "PRINT \"Cek NIK lagi\""
        ],
        "icon": "fa-id-card"
    },
    {
        "id": 5,
        "emoji": "🔢",
        "concept": "IF-ELSE & MOD",
        "title": "Validasi Genap Ganjil",
        "desc": "Misi: Cek sisa bagi angka dengan 2. Jika 0 maka genap, sebaliknya ganjil.",
        "correct": [
            "INPUT angka",
            "IF angka MOD 2 == 0 THEN",
            "  PRINT \"Angka tersebut adalah Bilangan Genap\"",
            "ELSE",
            "  PRINT \"Angka tersebut adalah Bilangan Ganjil\"",
            "END IF"
        ],
        "distractors": [
            "IF angka MOD 2 != 0 THEN",
            "PRINT \"Angka tidak valid\""
        ],
        "icon": "fa-divide"
    },
    {
        "id": 6,
        "emoji": "🛗",
        "concept": "IF-ELSE",
        "title": "Cek Muatan Beban Lift",
        "desc": "Misi: Cek berat total. Jika > 500 kg maka lift menolak bergerak, sebaliknya jalan.",
        "correct": [
            "INPUT berat_total",
            "IF berat_total > 500 THEN",
            "  PRINT \"Kelebihan muatan! Lift tidak dapat bergerak\"",
            "ELSE",
            "  PRINT \"Beban aman, lift siap berjalan\"",
            "END IF"
        ],
        "distractors": [
            "IF berat_total <= 500 THEN",
            "PRINT \"Lift rusak\""
        ],
        "icon": "fa-elevator"
    },
    {
        "id": 7,
        "emoji": "⏰",
        "concept": "IF-ELSE",
        "title": "Status Jam Masuk Sekolah",
        "desc": "Misi: Cek waktu kedatangan. Jika > 07.00 maka terlambat, sebaliknya tepat waktu.",
        "correct": [
            "INPUT waktu_kedatangan",
            "IF waktu_kedatangan > 07.00 THEN",
            "  PRINT \"Status: Terlambat, silakan catat di buku piket\"",
            "ELSE",
            "  PRINT \"Status: Tepat waktu, silakan masuk kelas\"",
            "END IF"
        ],
        "distractors": [
            "IF waktu_kedatangan <= 07.00 THEN",
            "PRINT \"Bel istirahat berbunyi\""
        ],
        "icon": "fa-clock"
    },
    {
        "id": 8,
        "emoji": "🚥",
        "concept": "IF-ELSE",
        "title": "Lampu Lalu Lintas",
        "desc": "Misi: Cek angka timer. Jika > 30 detik maka lampu merah, sebaliknya hijau.",
        "correct": [
            "INPUT angka_timer",
            "IF angka_timer > 30 THEN",
            "  PRINT \"Lampu Merah menyala, kendaraan wajib berhenti\"",
            "ELSE",
            "  PRINT \"Lampu Hijau menyala, silakan jalan\"",
            "END IF"
        ],
        "distractors": [
            "IF angka_timer <= 30 THEN",
            "PRINT \"Lampu Kuning menyala\""
        ],
        "icon": "fa-traffic-light"
    },
    {
        "id": 9,
        "emoji": "📦",
        "concept": "IF-ELSE",
        "title": "Validasi Stok Barang",
        "desc": "Misi: Cek stok sepatu e-commerce. Jika > 0 maka pesanan diproses, sebaliknya dibatalkan.",
        "correct": [
            "INPUT stok_sepatu",
            "IF stok_sepatu > 0 THEN",
            "  PRINT \"Pesanan dapat diproses ke tahap pembayaran\"",
            "ELSE",
            "  PRINT \"Mohon maaf, stok barang habis (Kosong)\"",
            "END IF"
        ],
        "distractors": [
            "IF stok_sepatu == 0 THEN",
            "PRINT \"Barang diskon besar-besaran\""
        ],
        "icon": "fa-box-open"
    }
]

# Update the 9 HTML files
for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    case_data = {
        "id": cases[i-1]["id"],
        "emoji": cases[i-1]["emoji"],
        "concept": cases[i-1]["concept"],
        "title": cases[i-1]["title"],
        "desc": cases[i-1]["desc"],
        "correct": cases[i-1]["correct"],
        "distractors": cases[i-1]["distractors"]
    }
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    levels_json = json.dumps([case_data], indent=4, ensure_ascii=False)
    match = re.search(r'const levels = \[.*?\];', content, flags=re.DOTALL)
    if match:
        content = content.replace(match.group(0), f'const levels = {levels_json};')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Update page_koki_algoritma.html
with open('page_koki_algoritma.html', 'r', encoding='utf-8') as f:
    portal_content = f.read()

for i, case in enumerate(cases):
    pattern = r'(<a href="game_koki_' + str(i+1) + r'\.html".*?</a>)'
    match = re.search(pattern, portal_content, re.DOTALL)
    if match:
        card = match.group(1)
        
        # Replace icon
        card = re.sub(r'<i class="fas fa-[^"]+"></i>', f'<i class="fas {case["icon"]}"></i>', card, count=1)
        # Replace title
        card = re.sub(r'<h2 class="text-xl font-bold text-gray-800 mb-2">.*?</h2>', f'<h2 class="text-xl font-bold text-gray-800 mb-2">{case["title"]}</h2>', card)
        # Replace description
        card = re.sub(r'<p class="text-gray-600 text-sm mb-4">.*?</p>', f'<p class="text-gray-600 text-sm mb-4">{case["desc"]}</p>', card)
        
        portal_content = portal_content.replace(match.group(1), card)

with open('page_koki_algoritma.html', 'w', encoding='utf-8') as f:
    f.write(portal_content)

print("Updated all files successfully.")
