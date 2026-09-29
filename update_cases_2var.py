import json
import re

cases = [
    {
        "id": 1,
        "emoji": "🎓",
        "concept": "IF-ELSE & AND",
        "title": "Penentuan Kelulusan Ujian",
        "desc": "Misi: Cek nilai 2 ujian. Jika nilai_teori dan nilai_praktek >= 75 maka lulus.",
        "vars": ["nilai_teori", "nilai_praktek"],
        "correct": [
            "INPUT nilai_teori, nilai_praktek",
            "IF nilai_teori >= 75 AND nilai_praktek >= 75 THEN",
            "  PRINT \"Selamat, Anda Lulus!\"",
            "ELSE",
            "  PRINT \"Anda Belum Lulus, Silakan Remidi\"",
            "END IF"
        ],
        "distractors": [
            "IF nilai_teori < 75 OR nilai_praktek < 75 THEN",
            "PRINT \"Nilai tidak valid\""
        ],
        "icon": "fa-graduation-cap"
    },
    {
        "id": 2,
        "emoji": "🛒",
        "concept": "IF-ELSE & AND",
        "title": "Diskon Belanja Swalayan",
        "desc": "Misi: Cek total dan status. Jika >= 100000 dan status_member == Aktif maka diskon.",
        "vars": ["total_belanja", "status_member"],
        "correct": [
            "INPUT total_belanja, status_member",
            "IF total_belanja >= 100000 AND status_member == \"Aktif\" THEN",
            "  PRINT \"Anda mendapatkan diskon khusus 20%!\"",
            "ELSE",
            "  PRINT \"Belanja kurang atau bukan member\"",
            "END IF"
        ],
        "distractors": [
            "IF total_belanja < 100000 OR status_member == \"Pasif\" THEN",
            "PRINT \"Masukkan uang pembayaran\""
        ],
        "icon": "fa-shopping-cart"
    },
    {
        "id": 3,
        "emoji": "🌡️",
        "concept": "IF-ELSE & AND",
        "title": "Klasifikasi Suhu Tubuh",
        "desc": "Misi: Cek suhu dan gejala. Jika suhu > 37.5 dan gejala == Ya maka arahkan ke IGD.",
        "vars": ["suhu_tubuh", "gejala_batuk"],
        "correct": [
            "INPUT suhu_tubuh, gejala_batuk",
            "IF suhu_tubuh > 37.5 AND gejala_batuk == \"Ya\" THEN",
            "  PRINT \"Peringatan: Pasien berisiko ke IGD\"",
            "ELSE",
            "  PRINT \"Suhu atau gejala aman ke Poli Umum\"",
            "END IF"
        ],
        "distractors": [
            "IF suhu_tubuh < 37.5 OR gejala_batuk == \"Tidak\" THEN",
            "PRINT \"Alat rusak\""
        ],
        "icon": "fa-thermometer-half"
    },
    {
        "id": 4,
        "emoji": "🗳️",
        "concept": "IF-ELSE & AND",
        "title": "Kategori Usia Pemilih",
        "desc": "Misi: Cek umur dan wni. Jika >= 17 dan status_wni == Ya maka boleh memilih.",
        "vars": ["umur", "status_wni"],
        "correct": [
            "INPUT umur, status_wni",
            "IF umur >= 17 AND status_wni == \"Ya\" THEN",
            "  PRINT \"Silakan menggunakan hak pilih Anda\"",
            "ELSE",
            "  PRINT \"Belum memenuhi syarat untuk memilih\"",
            "END IF"
        ],
        "distractors": [
            "IF umur <= 17 AND status_wni == \"Tidak\" THEN",
            "PRINT \"Cek NIK lagi\""
        ],
        "icon": "fa-id-card"
    },
    {
        "id": 5,
        "emoji": "🔢",
        "concept": "IF-ELSE & AND",
        "title": "Validasi Dua Angka Genap",
        "desc": "Misi: Cek sisa bagi 2 angka. Jika keduanya MOD 2 == 0 maka cetak pesan genap.",
        "vars": ["angka_pertama", "angka_kedua"],
        "correct": [
            "INPUT angka_pertama, angka_kedua",
            "IF angka_pertama MOD 2 == 0 AND angka_kedua MOD 2 == 0 THEN",
            "  PRINT \"Kedua angka tersebut Bilangan Genap\"",
            "ELSE",
            "  PRINT \"Terdapat angka ganjil di antaranya\"",
            "END IF"
        ],
        "distractors": [
            "IF angka_pertama MOD 2 != 0 OR angka_kedua MOD 2 != 0 THEN",
            "PRINT \"Angka tidak valid\""
        ],
        "icon": "fa-divide"
    },
    {
        "id": 6,
        "emoji": "🛗",
        "concept": "IF-ELSE & OR",
        "title": "Cek Muatan Beban Lift",
        "desc": "Misi: Cek beban dan orang. Jika beban > 500 OR orang > 6 maka tolak.",
        "vars": ["berat_total", "jumlah_orang"],
        "correct": [
            "INPUT berat_total, jumlah_orang",
            "IF berat_total > 500 OR jumlah_orang > 6 THEN",
            "  PRINT \"Kelebihan muatan! Lift tidak bergerak\"",
            "ELSE",
            "  PRINT \"Kapasitas aman, lift siap berjalan\"",
            "END IF"
        ],
        "distractors": [
            "IF berat_total <= 500 AND jumlah_orang <= 6 THEN",
            "PRINT \"Lift rusak\""
        ],
        "icon": "fa-elevator"
    },
    {
        "id": 7,
        "emoji": "⏰",
        "concept": "IF-ELSE & AND",
        "title": "Status Jam Masuk Sekolah",
        "desc": "Misi: Cek jam dan menit. Jika jam == 7 AND menit > 15 maka terlambat.",
        "vars": ["jam_hadir", "menit_hadir"],
        "correct": [
            "INPUT jam_hadir, menit_hadir",
            "IF jam_hadir == 7 AND menit_hadir > 15 THEN",
            "  PRINT \"Status: Terlambat, silakan lapor piket\"",
            "ELSE",
            "  PRINT \"Status: Tepat waktu, silakan masuk\"",
            "END IF"
        ],
        "distractors": [
            "IF jam_hadir < 7 OR menit_hadir <= 15 THEN",
            "PRINT \"Bel istirahat berbunyi\""
        ],
        "icon": "fa-clock"
    },
    {
        "id": 8,
        "emoji": "🚥",
        "concept": "IF-ELSE & AND",
        "title": "Lampu Lalu Lintas",
        "desc": "Misi: Cek timer dan kepadatan. Jika timer > 30 AND kepadatan == Tinggi, hijau diperpanjang.",
        "vars": ["angka_timer", "kepadatan_jalan"],
        "correct": [
            "INPUT angka_timer, kepadatan_jalan",
            "IF angka_timer > 30 AND kepadatan_jalan == \"Tinggi\" THEN",
            "  PRINT \"Lampu Hijau diperpanjang urai macet\"",
            "ELSE",
            "  PRINT \"Lampu Merah menyala normal, berhenti\"",
            "END IF"
        ],
        "distractors": [
            "IF angka_timer <= 30 OR kepadatan_jalan == \"Rendah\" THEN",
            "PRINT \"Lampu Kuning menyala\""
        ],
        "icon": "fa-traffic-light"
    },
    {
        "id": 9,
        "emoji": "📦",
        "concept": "IF-ELSE & AND",
        "title": "Validasi Stok Barang",
        "desc": "Misi: Cek stok dan pesanan. Jika stok >= pesanan AND pesanan > 0, maka proses.",
        "vars": ["stok_barang", "jumlah_pesanan"],
        "correct": [
            "INPUT stok_barang, jumlah_pesanan",
            "IF stok_barang >= jumlah_pesanan AND jumlah_pesanan > 0 THEN",
            "  PRINT \"Pesanan dapat diproses ke pembayaran\"",
            "ELSE",
            "  PRINT \"Mohon maaf, stok kurang atau tidak valid\"",
            "END IF"
        ],
        "distractors": [
            "IF stok_barang < jumlah_pesanan OR jumlah_pesanan == 0 THEN",
            "PRINT \"Barang diskon besar-besaran\""
        ],
        "icon": "fa-box-open"
    }
]

# Replacement pattern for JS validation logic
# Replace this exact block:
'''
            let requiredVars = [];
            levels[currentLevel].correct.forEach(block => {
                let m = block.match(/(?:WHILE|IF|INPUT)\s+([a-zA-Z0-9_]+)/);
                if (m && !requiredVars.includes(m[1])) requiredVars.push(m[1]);
            });
'''
# With:
'''
            let requiredVars = levels[currentLevel].vars || [];
'''

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    case_data = cases[i-1]
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    levels_json = json.dumps([case_data], indent=4, ensure_ascii=False)
    
    # 1. Update levels JSON
    match = re.search(r'const levels = \[.*?\];', content, flags=re.DOTALL)
    if match:
        content = content.replace(match.group(0), f'const levels = {levels_json};')
    
    # 2. Update validation logic
    old_validation = r'''            let requiredVars = [];
            levels[currentLevel].correct.forEach(block => {
                let m = block.match(/(?:WHILE|IF|INPUT)\s+([a-zA-Z0-9_]+)/);
                if (m && !requiredVars.includes(m[1])) requiredVars.push(m[1]);
            });'''
    new_validation = r'''            let requiredVars = levels[currentLevel].vars || [];'''
    content = content.replace(old_validation, new_validation)
    
    # Let's ensure formatBlockText handles AND and OR properly
    if "const keywords = ['Program', 'Deklarasi'" in content:
        content = content.replace(
            "const keywords = ['Program', 'Deklarasi', 'Algoritma', 'IF', 'THEN', 'ELSE', 'DO', 'WHILE', 'FOR', 'TO', 'END IF', 'END WHILE', 'END FOR', 'PRINT', 'READ'];",
            "const keywords = ['Program', 'Deklarasi', 'Algoritma', 'IF', 'THEN', 'ELSE', 'DO', 'WHILE', 'FOR', 'TO', 'END IF', 'END WHILE', 'END FOR', 'PRINT', 'READ', 'INPUT', 'AND', 'OR', 'MOD'];"
        )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update Portal Page
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

print("Finished updating 2 variable logic.")
