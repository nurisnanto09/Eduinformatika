import glob
import re

new_layout = '''
            <!-- Mobile Studi Kasus (Hidden on Desktop) -->
            <div class="block lg:hidden px-6 pt-4 pb-0">
                <div class="bg-indigo-50 border-l-4 border-indigo-500 p-4 rounded-xl shadow-sm">
                    <h3 class="text-sm font-bold text-indigo-800 mb-1 flex items-center gap-2">
                        <i class="fas fa-book-open"></i> Studi Kasus
                    </h3>
                    <p class="text-sm text-indigo-900 leading-relaxed level-story-text"></p>
                </div>
            </div>

            <!-- Workspace Layout (Two Columns) -->
            <div class="flex-1 p-6 flex flex-col-reverse lg:flex-row gap-6 overflow-y-auto lg:overflow-hidden lg:h-full">
                
                <!-- Left Column -->
                <div class="flex-1 flex flex-col gap-4 min-h-0">
                    <!-- Desktop Studi Kasus (Hidden on Mobile) -->
                    <div class="hidden lg:block">
                        <div class="bg-indigo-50 border-l-4 border-indigo-500 p-4 rounded-xl shadow-sm">
                            <h3 class="text-sm font-bold text-indigo-800 mb-1 flex items-center gap-2">
                                <i class="fas fa-book-open"></i> Studi Kasus
                            </h3>
                            <p class="text-sm text-indigo-900 leading-relaxed level-story-text"></p>
                        </div>
                    </div>

                    <!-- Kumpulan Blok -->
                    <div class="flex-1 flex flex-col min-h-0">
                        <h4 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
                            <i class="fas fa-layer-group text-orange-500"></i> Blok Tersedia
                        </h4>
                        <p class="text-xs text-gray-500 mb-3">Klik sebuah blok untuk menambahkannya ke lembar resep.</p>
                        <div id="source-blocks" class="lg:flex-1 flex flex-col gap-2 p-4 bg-orange-100/50 rounded-xl border-2 border-dashed border-orange-200 min-h-[100px] lg:min-h-0 lg:overflow-y-auto transition-all duration-300">
                            <!-- Source blocks injected here -->
                        </div>
                    </div>
                </div>

                <!-- Right Column -->
                <div class="flex-1 flex flex-col gap-4 min-h-0">
                    <!-- Lembar Resep -->
                    <div class="flex-1 flex flex-col min-h-0">
                        <h4 class="font-bold text-blue-900 mb-3 flex items-center gap-2">
                            <i class="fas fa-file-code text-blue-500"></i> Lembar Resep (Pseudocode)
                        </h4>
                        <p class="text-xs text-gray-500 mb-3">Klik blok di sini untuk mengembalikannya.</p>

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

                        <div id="target-blocks" class="lg:flex-1 flex flex-col gap-2 p-4 bg-slate-800 rounded-xl border-2 border-slate-900 min-h-[150px] lg:min-h-0 shadow-inner lg:overflow-y-auto transition-all duration-300">
                            <!-- Target blocks injected here -->
                            <div class="text-center text-slate-500 text-sm mt-4 font-mono italic" id="empty-state">-- Lembar Masih Kosong --</div>
                        </div>
                    </div>
                    
                    <!-- Action Bar (Bottom Right) -->
                    <div class="flex justify-between items-center bg-white p-4 rounded-xl border border-gray-200 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)] mt-0 lg:mt-2">
                        <button onclick="resetWorkspace()" class="text-gray-600 hover:text-red-500 font-bold px-4 py-2 rounded-lg transition-colors flex items-center gap-2">
                            <i class="fas fa-undo"></i> Kosongkan
                        </button>
                        <button onclick="masakPesanan()" class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 px-8 rounded-xl shadow-lg shadow-orange-500/30 transition-transform active:scale-95 flex items-center gap-2 text-lg">
                            <i class="fas fa-fire-burner"></i> Jalankan Program!
                        </button>
                    </div>
                </div>
            </div>
'''

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The header fixes
    # We replace: <div class="bg-white p-5 border-b border-gray-200 flex justify-between items-center shadow-sm">
    # With: <div class="bg-white p-5 border-b border-gray-200 flex flex-col lg:flex-row justify-between items-start lg:items-center shadow-sm gap-4">
    content = content.replace(
        '<div class="bg-white p-5 border-b border-gray-200 flex justify-between items-center shadow-sm">',
        '<div class="bg-white p-5 border-b border-gray-200 flex flex-col lg:flex-row justify-between items-start lg:items-center shadow-sm gap-4">'
    )

    # Replace the whole Workspace Layout
    # Find from <!-- Workspace Layout (Two Columns) --> to the line before <!-- Cooking Animation Overlay
    start_pattern = r'<!-- Workspace Layout \(Two Columns\) -->.*?</div>\s*</div>\s*</div>\s*(?=<!-- Cooking Animation Overlay)'
    match = re.search(start_pattern, content, re.DOTALL)
    if match:
        content = content.replace(match.group(0), new_layout + '\n        ')
    else:
        # Fallback if the regex doesn't match perfectly, just use index finding
        start_idx = content.find('<!-- Workspace Layout (Two Columns) -->')
        end_idx = content.find('<!-- Cooking Animation Overlay')
        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + new_layout + '\n        ' + content[end_idx:]

    # Fix JS for level-story
    # Replace document.getElementById('level-story').innerText = lvl.story;
    # with document.querySelectorAll('.level-story-text').forEach(el => el.innerText = lvl.story);
    content = content.replace(
        "document.getElementById('level-story').innerText = lvl.story;",
        "document.querySelectorAll('.level-story-text').forEach(el => el.innerText = lvl.story);"
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied robust flex layout.")