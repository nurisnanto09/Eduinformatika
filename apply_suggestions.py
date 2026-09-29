import json
import re

cases = [
    {
        "id": 1,
        "emoji": "🎓",
        "concept": "Input & Proses -> IF-ELSE",
        "title": "Penentuan Kelulusan Ujian",
        "desc": "Misi: Hitung nilai akhir dari skor. Jika nilai_akhir >= 75 maka lulus.",
        "vars": ["skor_benar", "nilai_akhir"],
        "correct": [
            "INPUT skor_benar",
            "nilai_akhir <- skor_benar * 10",
            "IF nilai_akhir >= 75 THEN",
            "  PRINT \"Selamat, Anda Lulus!\"",
            "ELSE",
            "  PRINT \"Anda Belum Lulus, Silakan Remidi\"",
            "END IF"
        ],
        "distractors": [
            "IF nilai_akhir < 75 THEN",
            "nilai_akhir <- skor_benar + 10"
        ],
        "icon": "fa-graduation-cap"
    },
    {
        "id": 2,
        "emoji": "🛒",
        "concept": "Input & Proses -> IF-ELSE",
        "title": "Diskon Belanja Swalayan",
        "desc": "Misi: Hitung total belanja. Jika total_belanja >= Rp100.000 maka dapat diskon.",
        "vars": ["jumlah_barang", "total_belanja"],
        "correct": [
            "INPUT jumlah_barang",
            "total_belanja <- jumlah_barang * 25000",
            "IF total_belanja >= 100000 THEN",
            "  PRINT \"Anda mendapatkan diskon 10%!\"",
            "ELSE",
            "  PRINT \"Belanja kurang dari Rp100.000\"",
            "END IF"
        ],
        "distractors": [
            "IF total_belanja < 100000 THEN",
            "total_belanja <- jumlah_barang + 25000"
        ],
        "icon": "fa-shopping-cart"
    },
    {
        "id": 3,
        "emoji": "🌡️",
        "concept": "Input & Proses -> IF-ELSE",
        "title": "Klasifikasi Suhu Tubuh",
        "desc": "Misi: Konversi suhu ke Celcius. Jika suhu_celcius > 37.5 maka demam.",
        "vars": ["suhu_fahrenheit", "suhu_celcius"],
        "correct": [
            "INPUT suhu_fahrenheit",
            "suhu_celcius <- (suhu_fahrenheit - 32) * 5/9",
            "IF suhu_celcius > 37.5 THEN",
            "  PRINT \"Peringatan: Suhu tubuh tinggi / Demam\"",
            "ELSE",
            "  PRINT \"Suhu tubuh normal dan sehat\"",
            "END IF"
        ],
        "distractors": [
            "IF suhu_celcius <= 37.5 THEN",
            "suhu_celcius <- suhu_fahrenheit * 5/9"
        ],
        "icon": "fa-thermometer-half"
    },
    {
        "id": 4,
        "emoji": "🗳️",
        "concept": "Input & Proses -> IF-ELSE",
        "title": "Kategori Usia Pemilih Pemilu",
        "desc": "Misi: Hitung umur dari tahun lahir. Jika umur >= 17 maka boleh memilih.",
        "vars": ["tahun_lahir", "umur"],
        "correct": [
            "INPUT tahun_lahir",
            "umur <- 2024 - tahun_lahir",
            "IF umur >= 17 THEN",
            "  PRINT \"Silakan menggunakan hak pilih Anda\"",
            "ELSE",
            "  PRINT \"Belum cukup umur untuk memilih\"",
            "END IF"
        ],
        "distractors": [
            "IF umur < 17 THEN",
            "umur <- tahun_lahir - 2024"
        ],
        "icon": "fa-id-card"
    },
    {
        "id": 5,
        "emoji": "🔢",
        "concept": "Input & Proses -> IF-ELSE",
        "title": "Validasi Angka Genap atau Ganjil",
        "desc": "Misi: Hitung sisa bagi (MOD 2). Jika sisa_bagi == 0 maka bilangan genap.",
        "vars": ["angka", "sisa_bagi"],
        "correct": [
            "INPUT angka",
            "sisa_bagi <- angka MOD 2",
            "IF sisa_bagi == 0 THEN",
            "  PRINT \"Angka tersebut adalah Bilangan Genap\"",
            "ELSE",
            "  PRINT \"Angka tersebut adalah Bilangan Ganjil\"",
            "END IF"
        ],
        "distractors": [
            "IF sisa_bagi != 0 THEN",
            "sisa_bagi <- angka / 2"
        ],
        "icon": "fa-divide"
    },
    {
        "id": 6,
        "emoji": "🛗",
        "concept": "Input & Proses -> IF-ELSE",
        "title": "Cek Muatan Beban Lift",
        "desc": "Misi: Hitung total berat. Jika berat_total > 500 kg maka lift berhenti.",
        "vars": ["jumlah_orang", "berat_total"],
        "correct": [
            "INPUT jumlah_orang",
            "berat_total <- jumlah_orang * 60",
            "IF berat_total > 500 THEN",
            "  PRINT \"Kelebihan muatan! Lift tidak dapat bergerak\"",
            "ELSE",
            "  PRINT \"Beban aman, lift siap berjalan\"",
            "END IF"
        ],
        "distractors": [
            "IF berat_total <= 500 THEN",
            "berat_total <- jumlah_orang + 60"
        ],
        "icon": "fa-elevator"
    },
    {
        "id": 7,
        "emoji": "⏰",
        "concept": "Input & Proses -> IF-ELSE",
        "title": "Penentuan Status Jam Masuk",
        "desc": "Misi: Hitung keterlambatan. Jika keterlambatan > 0 menit maka terlambat.",
        "vars": ["waktu_sampai", "keterlambatan"],
        "correct": [
            "INPUT waktu_sampai",
            "keterlambatan <- waktu_sampai - 60",
            "IF keterlambatan > 0 THEN",
            "  PRINT \"Status: Terlambat, silakan catat piket\"",
            "ELSE",
            "  PRINT \"Status: Tepat waktu, silakan masuk\"",
            "END IF"
        ],
        "distractors": [
            "IF keterlambatan <= 0 THEN",
            "keterlambatan <- 60 - waktu_sampai"
        ],
        "icon": "fa-clock"
    },
    {
        "id": 8,
        "emoji": "🚥",
        "concept": "Input & Proses -> IF-ELSE",
        "title": "Lampu Lalu Lintas Otomatis",
        "desc": "Misi: Hitung durasi lampu hijau. Jika durasi_hijau > 30 maka lampu merah.",
        "vars": ["jumlah_mobil", "durasi_hijau"],
        "correct": [
            "INPUT jumlah_mobil",
            "durasi_hijau <- jumlah_mobil * 5",
            "IF durasi_hijau > 30 THEN",
            "  PRINT \"Lampu Merah menyala, kendaraan berhenti\"",
            "ELSE",
            "  PRINT \"Lampu Hijau menyala, silakan jalan\"",
            "END IF"
        ],
        "distractors": [
            "IF durasi_hijau <= 30 THEN",
            "durasi_hijau <- jumlah_mobil / 5"
        ],
        "icon": "fa-traffic-light"
    },
    {
        "id": 9,
        "emoji": "📦",
        "concept": "Input & Proses -> IF-ELSE",
        "title": "Validasi Stok Barang Toko",
        "desc": "Misi: Hitung sisa stok. Jika sisa_stok >= 0 maka pesanan diproses.",
        "vars": ["jumlah_pesanan", "sisa_stok"],
        "correct": [
            "INPUT jumlah_pesanan",
            "sisa_stok <- 50 - jumlah_pesanan",
            "IF sisa_stok >= 0 THEN",
            "  PRINT \"Pesanan dapat diproses ke pembayaran\"",
            "ELSE",
            "  PRINT \"Mohon maaf, stok barang habis\"",
            "END IF"
        ],
        "distractors": [
            "IF sisa_stok < 0 THEN",
            "sisa_stok <- jumlah_pesanan - 50"
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
    
    # Let's ensure the keyword arrow (<-) is in the syntax keywords if they need to type it?
    # No need, variable validation just checks requiredVars.
    
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
        card = re.sub(r'<h2 class="text-xl font-bold text-gray-800 mb-2">.*?</h2>', f'<h2 class="text-xl font-bold text-gray-800 mb-2">{case["title"]}</h2>', card)
        card = re.sub(r'<p class="text-gray-600 text-sm mb-4 flex-grow">.*?</p>', f'<p class="text-gray-600 text-sm mb-4 flex-grow">{case["desc"]}</p>', card)
        
        portal_content = portal_content.replace(match.group(1), card)

with open('page_koki_algoritma.html', 'w', encoding='utf-8') as f:
    f.write(portal_content)

print("Updated cases with Input -> Calculation -> IF logic.")
