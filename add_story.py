import json
import re

stories = [
    "Budi sedang mengikuti ujian di sekolah. Guru meminta Budi membuat program yang akan menerima input nilai skor ujiannya (skor_benar). Program akan mengalikan skor tersebut dengan 10 untuk mendapatkan nilai_akhir. Jika nilai akhir mencapai 75 atau lebih, program menampilkan pesan lulus. Jika tidak, program menampilkan pesan remidi.",
    "Ibu pergi berbelanja ke swalayan. Kasir menggunakan program otomatis yang meminta input jumlah_barang belanjaan Ibu. Program akan menghitung total_belanja dengan mengalikan jumlah barang dengan Rp 25.000. Jika total belanja mencapai Rp 100.000 atau lebih, layar mesin mencetak pemberitahuan diskon. Jika kurang, tidak ada diskon.",
    "Sebuah puskesmas menggunakan alat pemindai suhu otomatis yang mengukur suhu dalam skala Fahrenheit (suhu_fahrenheit). Program harus mengubahnya terlebih dahulu ke Celcius (suhu_celcius). Jika suhu Celcius terdeteksi lebih dari 37.5 derajat, alat mengeluarkan peringatan demam. Jika tidak, alat menampilkan status normal.",
    "Di tempat pemungutan suara, petugas meminta warga memasukkan tahun_lahir mereka ke dalam sistem. Sistem akan menghitung umur warga dengan mengurangi tahun berjalan (2024) dengan tahun lahir. Jika umur mencapai 17 tahun atau lebih, sistem memperbolehkan warga memilih. Jika masih di bawah 17 tahun, sistem akan menolak.",
    "Dalam pelajaran matematika, guru meminta siswa membuat program yang menerima input sebuah angka. Program harus menghitung sisa_bagi dari angka tersebut jika dibagi 2 (menggunakan operasi MOD). Jika sisa baginya adalah 0, layar menampilkan bahwa angka tersebut Genap. Jika ada sisa bagi, angka tersebut Ganjil.",
    "Sebuah lift kantor dilengkapi sensor yang mendeteksi jumlah_orang yang masuk. Program di dalam lift mengasumsikan berat rata-rata satu orang adalah 60 kg, sehingga menghitung berat_total keseluruhan. Jika berat total melebihi kapasitas 500 kg, mesin lift menolak bergerak. Jika beban aman, lift siap berjalan.",
    "Andi berlari menuju gerbang sekolah dan menempelkan kartu pelajarnya. Mesin mencatat waktu_sampai (dalam menit sejak jam 06.00 pagi). Program kemudian menghitung keterlambatan dengan mengurangi waktu sampai dengan 60 (batas masuk jam 07.00 = 60 menit). Jika menit keterlambatan lebih dari 0, mesin mencatat status terlambat.",
    "Sistem lampu lalu lintas pintar mendeteksi jumlah_mobil yang sedang antre di lampu merah. Program menghitung durasi_hijau yang dibutuhkan dengan mengalikan jumlah mobil dengan 5 detik. Jika durasi yang dibutuhkan lebih dari 30 detik, maka sistem akan memutus siklus dan lampu Merah menyala. Jika 30 detik ke bawah, lampu Hijau menyala.",
    "Siska memesan sepatu di aplikasi toko online yang meminta input jumlah_pesanan. Server langsung menghitung sisa_stok dengan mengurangi total stok di gudang (50 sepatu) dengan jumlah pesanan Siska. Jika sisa stok masih 0 atau lebih (bernilai positif), aplikasi memproses pesanan. Jika sisa stok negatif, pesanan dibatalkan."
]

injection_html = """
    <div class="px-6 pt-4 pb-0">
        <div class="bg-indigo-50 border-l-4 border-indigo-500 p-4 rounded-r-lg shadow-sm">
            <h3 class="text-sm font-bold text-indigo-800 mb-1 flex items-center gap-2">
                <i class="fas fa-book-open"></i> Studi Kasus
            </h3>
            <p class="text-sm text-indigo-900 leading-relaxed" id="level-story"></p>
        </div>
    </div>
"""

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the current levels array
    match = re.search(r'const levels = \[.*?\];', content, flags=re.DOTALL)
    if match:
        levels_str = match.group(0)
        # Parse it safely by extracting the dict
        # Since it's a JS array, we can use regex to inject the story
        story_json = json.dumps(stories[i-1], ensure_ascii=False)
        
        # Inject "story": "...", before "vars"
        new_levels_str = levels_str.replace('"vars":', f'"story": {story_json},\n        "vars":')
        content = content.replace(levels_str, new_levels_str)
        
    # Inject HTML after Mission Info
    if 'id="level-story"' not in content:
        # Find the end of Mission info which is followed by <!-- Workspaces -->
        target_html = '<!-- Workspaces -->'
        if target_html in content:
            content = content.replace(target_html, injection_html + '\n    ' + target_html)
            
    # Inject JS
    if "document.getElementById('level-story')" not in content:
        target_js = "document.getElementById('level-desc').innerText = lvl.desc;"
        if target_js in content:
            content = content.replace(target_js, target_js + "\n            document.getElementById('level-story').innerText = lvl.story;")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added story cards to all games.")
