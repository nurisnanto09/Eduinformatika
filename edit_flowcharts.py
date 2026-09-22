import re

def process_file(filepath, texts, shapes, loop, text_pool):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Text Pool
    pool_html = "\n".join([f"                <div class='text-block bg-white border border-blue-200 p-2 rounded shadow-sm text-xs flex items-center justify-center text-center font-bold text-gray-700 clickable hover:border-blue-500 min-h-[40px]' id='txt-{i}' onclick=\"selectText(this, '{t}')\">{t}</div>" for i, t in enumerate(text_pool)])
    content = re.sub(r'<div class="flex flex-col gap-2 pb-4 flex-1" id="text-pool">.*?</div>\s*</div>', f'<div class="flex flex-col gap-2 pb-4 flex-1" id="text-pool">\n{pool_html}\n            </div>\n        </div>', content, flags=re.DOTALL)
    
    # 2. Add slot-6
    slot_6 = """                <div class="arrow-down"></div>
                
                <div class="board-slot" id="slot-6" onclick="placeToZone(6)">
                    <div class="slot-placeholder"><span id="sl-6" class="transition-all duration-300 font-bold">Langkah 7</span></div>
                    <div class="rendered-shape hidden" id="rs-6"></div>
                    <div class="rendered-text" id="rt-6"></div>
                </div>"""
    content = content.replace('<div class="rendered-text" id="rt-5"></div>\n                </div>', '<div class="rendered-text" id="rt-5"></div>\n                </div>\n' + slot_6)
    
    # 3. Add Langkah 7 to dropdown
    content = content.replace('<option value="6">Langkah 6</option>', '<option value="6">Langkah 6</option>\n                        <option value="7">Langkah 7</option>')
    
    # 4. Progress display
    content = content.replace('0/6', '0/7')
    content = content.replace('scoreProgress / 6', 'scoreProgress / 7')
    
    # 5. Correct Answers & Board Array
    content = re.sub(r'const correctAnswerTexts = \[.*?\];', f'const correctAnswerTexts = {texts};', content)
    content = re.sub(r'const correctAnswerShapes = \[.*?\];', f'const correctAnswerShapes = {shapes};', content)
    content = re.sub(r'const correctLoop = ".*?";', f'const correctLoop = "{loop}";', content)
    board_7 = 'let board = [{ text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }];'
    content = re.sub(r'let board = \[.*?\];', board_7, content, count=1)
    
    reset_board_6 = r'board = \[\{ text: null, shape: null \}, \{ text: null, shape: null \}, \{ text: null, shape: null \},\s*\{ text: null, shape: null \}, \{ text: null, shape: null \}, \{ text: null, shape: null \}\];'
    reset_board_7 = 'board = [{ text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }, { text: null, shape: null }];'
    content = re.sub(reset_board_6, reset_board_7, content)
    
    # 6. Change all i<6 to i<7
    content = content.replace('i<6', 'i<7')
    
    # 7. checkAnswer scoring
    old_scoring = """            let shapeScore = 0; let textScore = 0; let loopScore = 0;
            
            for(let i=0; i<7; i++) {
                if(board[i].shape === correctAnswerShapes[i]) shapeScore += 10;
                if(board[i].text === correctAnswerTexts[i]) textScore += 5;
            }
            if(document.getElementById('loop-select').value === correctLoop) loopScore = 10;
            
            let total = shapeScore + textScore + loopScore;"""
            
    new_scoring = """            let shapeCorrect = 0; let textCorrect = 0; let loopScore = 0;
            
            for(let i=0; i<7; i++) {
                if(board[i].shape === correctAnswerShapes[i]) shapeCorrect++;
                if(board[i].text === correctAnswerTexts[i]) textCorrect++;
            }
            if(document.getElementById('loop-select').value === correctLoop) loopScore = 10;
            
            let shapeScore = Math.round((shapeCorrect / 7) * 60);
            let textScore = Math.round((textCorrect / 7) * 30);
            let total = shapeScore + textScore + loopScore;"""
    
    content = content.replace(old_scoring, new_scoring)
    
    # Error thresholds
    old_err = """                let errText = [];
                if(shapeScore < 60) errText.push("Bentuk");
                if(textScore < 30) errText.push("Urutan");
                if(loopScore === 0) errText.push("Looping");"""
    
    new_err = """                let errText = [];
                if(shapeCorrect < 7) errText.push("Bentuk");
                if(textCorrect < 7) errText.push("Urutan");
                if(loopScore === 0) errText.push("Looping");"""
                
    content = content.replace(old_err, new_err)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


texts_8 = '["Mulai", "Cari buku yang diinginkan di rak", "Serahkan buku ke meja pustakawan", "Tunjukkan kartu anggota", "Apakah buku tersedia untuk dipinjam?", "Terima buku yang sudah didata", "Selesai"]'
shapes_8 = '["oval", "persegi", "persegi", "jajar", "ketupat", "jajar", "oval"]'
loop_8 = "2"
pool_8 = [
    "Cari buku yang diinginkan di rak",
    "Serahkan buku ke meja pustakawan",
    "Tunjukkan kartu anggota",
    "Apakah buku tersedia untuk dipinjam?",
    "Terima buku yang sudah didata",
    "Mulai",
    "Selesai",
    "Apakah masa berlaku kartu anggota masih aktif?",
    "Kembalikan buku yang sudah dibaca ke rak"
]

texts_9 = '["Mulai", "Serahkan keranjang belanjaan ke meja kasir", "Kasir memindai kode batang setiap barang", "Apakah semua barang sudah selesai di-scan?", "Lakukan pembayaran", "Terima struk pembayaran dan barang", "Selesai"]'
shapes_9 = '["oval", "jajar", "persegi", "ketupat", "persegi", "jajar", "oval"]'
loop_9 = "3"
pool_9 = [
    "Serahkan keranjang belanjaan ke meja kasir",
    "Kasir memindai kode batang setiap barang",
    "Apakah semua barang sudah selesai di-scan?",
    "Lakukan pembayaran",
    "Terima struk pembayaran dan barang",
    "Mulai",
    "Selesai",
    "Ambil keranjang kosong dari pintu masuk",
    "Tawar harga barang ke kasir"
]

process_file(r'd:\PPG\Semester 2\PPL\Folder Baru\game_flowchart_8.html', texts_8, shapes_8, loop_8, pool_8)
process_file(r'd:\PPG\Semester 2\PPL\Folder Baru\game_flowchart_9.html', texts_9, shapes_9, loop_9, pool_9)
