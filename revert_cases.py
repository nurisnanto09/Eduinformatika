import json
import re

cases = [
    {
        "id": 1,
        "emoji": "🎓",
        "concept": "IF-ELSE",
        "title": "Penentuan Kelulusan Ujian",
        "desc": "Misi: Cek nilai ujian Budi. Jika nilai >= 75 maka lulus, sebaliknya belum lulus.",
        "vars": ["nilai"],
        "correct": [
            "INPUT nilai",
            "IF nilai >= 75 THEN",
            "  PRINT \"Selamat, Anda Lulus!\"",
            "ELSE",
            "  PRINT \"Mohon maaf, Anda Belum Lulus\"",
            "END IF"
        ],
        "distractors": [
            "IF nilai < 75 THEN",
            "PRINT \"Silakan Remidi\""
        ],
        "icon": "fa-graduation-cap"
    },
    {
        "id": 2,
        "emoji": "🛒",
        "concept": "IF-ELSE",
        "title": "Diskon Belanja Swalayan",
        "desc": "Misi: Cek total belanja. Jika total >= Rp100.000 maka dapat diskon 10%.",
        "vars": ["total_belanja"],
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
            "PRINT \"Terima kasih telah berbelanja\""
        ],
        "icon": "fa-shopping-cart"
    },
    {
        "id": 3,
        "emoji": "🌡️",
        "concept": "IF-ELSE",
        "title": "Klasifikasi Suhu Tubuh",
        "desc": "Misi: Cek suhu tubuh pasien. Jika suhu > 37.5 maka demam, sebaliknya normal sehat.",
        "vars": ["suhu_tubuh"],
        "correct": [
            "INPUT suhu_tubuh",
            "IF suhu_tubuh > 37.5 THEN",
            "  PRINT \"Peringatan: Suhu tubuh tinggi / Demam\"",
            "ELSE",
            "  PRINT \"Suhu tubuh normal dan sehat\"",
            "END IF"
        ],
        "distractors": [
            "IF suhu_tubuh <= 37.5 THEN",
            "PRINT \"Silakan ke ruang dokter\""
        ],
        "icon": "fa-thermometer-half"
    },
    {
        "id": 4,
        "emoji": "🗳️",
        "concept": "IF-ELSE",
        "title": "Kategori Usia Pemilih Pemilu",
        "desc": "Misi: Cek umur warga. Jika umur >= 17 maka boleh memilih, sebaliknya tolak.",
        "vars": ["umur"],
        "correct": [
            "INPUT umur",
            "IF umur >= 17 THEN",
            "  PRINT \"Silakan menggunakan hak pilih Anda\"",
            "ELSE",
            "  PRINT \"Belum cukup umur untuk memilih\"",
            "END IF"
        ],
        "distractors": [
            "IF umur < 17 THEN",
            "PRINT \"Tunjukkan KTP Anda\""
        ],
        "icon": "fa-id-card"
    },
    {
        "id": 5,
        "emoji": "🔢",
        "concept": "IF-ELSE",
        "title": "Validasi Angka Genap atau Ganjil",
        "desc": "Misi: Cek sisa bagi dengan angka dua (MOD 2). Jika hasil 0 maka genap.",
        "vars": ["angka"],
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
            "PRINT \"Angka tersebut adalah Nol\""
        ],
        "icon": "fa-divide"
    },
    {
        "id": 6,
        "emoji": "🛗",
        "concept": "IF-ELSE",
        "title": "Cek Muatan Beban Lift",
        "desc": "Misi: Cek total berat. Jika berat_total > 500 maka lift menolak bergerak.",
        "vars": ["berat_total"],
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
            "PRINT \"Lift sedang dalam perbaikan\""
        ],
        "icon": "fa-elevator"
    },
    {
        "id": 7,
        "emoji": "⏰",
        "concept": "IF-ELSE",
        "title": "Penentuan Status Jam Masuk",
        "desc": "Misi: Cek waktu kedatangan siswa. Jika waktu > 07.00 maka terlambat.",
        "vars": ["waktu_kedatangan"],
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
            "PRINT \"Gerbang sekolah telah ditutup\""
        ],
        "icon": "fa-clock"
    },
    {
        "id": 8,
        "emoji": "🚥",
        "concept": "IF-ELSE",
        "title": "Lampu Lalu Lintas Otomatis",
        "desc": "Misi: Cek angka timer. Jika angka_timer > 30 maka lampu merah menyala.",
        "vars": ["angka_timer"],
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
            "PRINT \"Lampu Kuning menyala hati-hati\""
        ],
        "icon": "fa-traffic-light"
    },
    {
        "id": 9,
        "emoji": "📦",
        "concept": "IF-ELSE",
        "title": "Validasi Stok Barang Toko Online",
        "desc": "Misi: Cek stok_sepatu di aplikasi. Jika > 0 maka pesanan diproses, sebaliknya batal.",
        "vars": ["stok_sepatu"],
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
            "PRINT \"Masukkan produk ke keranjang\""
        ],
        "icon": "fa-box-open"
    }
]

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    case_data = {
        "id": cases[i-1]["id"],
        "emoji": cases[i-1]["emoji"],
        "concept": cases[i-1]["concept"],
        "title": cases[i-1]["title"],
        "desc": cases[i-1]["desc"],
        "vars": cases[i-1]["vars"],
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
        # Update title
        card = re.sub(r'<h2 class="text-xl font-bold text-gray-800 mb-2">.*?</h2>', f'<h2 class="text-xl font-bold text-gray-800 mb-2">{case["title"]}</h2>', card)
        # Update description
        card = re.sub(r'<p class="text-gray-600 text-sm mb-4">.*?</p>', f'<p class="text-gray-600 text-sm mb-4">{case["desc"]}</p>', card)
        
        portal_content = portal_content.replace(match.group(1), card)

with open('page_koki_algoritma.html', 'w', encoding='utf-8') as f:
    f.write(portal_content)

print("Reverted to 1 variable.")
