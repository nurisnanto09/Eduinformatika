import re, glob

injection_html = '''
                    <div class="bg-slate-700 p-3 rounded-lg mb-3 shadow-inner">
                        <div class="mb-2">
                            <label class="text-xs font-bold text-slate-300">Nama Program <span class="text-red-400">*</span></label>
                            <div class="flex mt-1">
                                <span class="bg-slate-800 text-blue-400 px-3 py-1.5 rounded-l text-sm font-bold border border-slate-600 border-r-0">PROGRAM</span>
                                <input type="text" id="input-program" class="bg-slate-900 text-white px-3 py-1.5 rounded-r text-sm font-mono border border-slate-600 w-full focus:outline-none focus:border-blue-500" placeholder="nama_program (tanpa spasi)">
                            </div>
                        </div>
                        <div>
                            <label class="text-xs font-bold text-slate-300">Deklarasi Variabel <span class="text-red-400">*</span></label>
                            <div class="flex mt-1">
                                <span class="bg-slate-800 text-blue-400 px-3 py-1.5 rounded-l text-sm font-bold border border-slate-600 border-r-0">DEKLARASI</span>
                                <input type="text" id="input-deklarasi" class="bg-slate-900 text-white px-3 py-1.5 rounded-r text-sm font-mono border border-slate-600 w-full focus:outline-none focus:border-blue-500" placeholder="Ketik variabel yang digunakan (contoh: var_nama)">
                            </div>
                        </div>
                    </div>
'''

for file in glob.glob('game_koki_*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Inject HTML
    if 'id="input-program"' not in content:
        # Find the line with <p class="text-xs text-gray-500 mb-3">Klik blok di sini untuk mengembalikannya.</p>
        target_str = '<p class="text-xs text-gray-500 mb-3">Klik blok di sini untuk mengembalikannya.</p>'
        if target_str in content:
            content = content.replace(target_str, target_str + '\n' + injection_html)
    
    # 2. Inject JS Validation
    js_validation = '''
            const progName = document.getElementById('input-program').value.trim();
            const progDecl = document.getElementById('input-deklarasi').value.trim();

            if (!progName || !progDecl) {
                alert("Gagal: Nama Program dan Deklarasi Variabel wajib diisi!");
                return;
            }

            if (progName.includes(" ")) {
                alert("Gagal: Nama Program tidak boleh mengandung spasi! Harus ditulis sambung.");
                return;
            }

            let requiredVars = [];
            levels[currentLevel].correct.forEach(block => {
                let m = block.match(/(?:WHILE|IF)\\s+([a-zA-Z0-9_]+)\\s+(?:DO|THEN)/);
                if (m && !requiredVars.includes(m[1])) requiredVars.push(m[1]);
            });
            
            let isVarsCorrect = requiredVars.every(v => progDecl.includes(v));
            if (!isVarsCorrect) {
                alert("Gagal: Deklarasi variabel belum tepat! Pastikan kamu mendeklarasikan variabel yang persis sama dengan yang digunakan di blok (contoh: " + requiredVars.join(", ") + ").");
                return;
            }
'''
    if 'const progName = document.getElementById' not in content:
        # Find the start of masakPesanan
        target_js = '''        function masakPesanan() {
            if (isCooking) return;
            
            if (targetWorkspace.length === 0) {
                alert("Lembar resep masih kosong! Masukkan minimal 1 baris kode.");
                return;
            }'''
        
        if target_js in content:
            content = content.replace(target_js, target_js + '\n' + js_validation)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all game_koki files.")
