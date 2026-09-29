import glob
import re

timer_html = '''            <!-- Header Level Info -->
            <div class="bg-white p-5 border-b border-gray-200 flex justify-between items-center shadow-sm">
                <div class="flex items-start gap-4">
                    <div class="text-4xl bg-orange-100 p-3 rounded-full border-2 border-orange-300 shadow-sm" id="level-emoji">🎓</div>
                    <div>
                        <span id="level-concept" class="text-xs font-bold bg-blue-100 text-blue-800 px-2 py-1 rounded mb-1 inline-block">Sequence</span>
                        <h2 id="level-title" class="text-xl font-bold text-gray-800">1. Teh Manis</h2>
                        <p id="level-desc" class="text-sm text-gray-600 mt-1">Koki, tolong buatkan urutan algoritma yang benar untuk menyajikan secangkir teh manis!</p>
                    </div>
                </div>
                
                <!-- Timer -->
                <div class="flex flex-col items-center bg-red-50 border-2 border-red-200 p-2 rounded-xl shadow-inner min-w-[120px]">
                    <span class="text-xs font-bold text-red-500 uppercase tracking-wider mb-1"><i class="fas fa-stopwatch"></i> Sisa Waktu</span>
                    <span id="timer-display" class="text-3xl font-mono font-bold text-red-700">05:00</span>
                </div>
            </div>'''

timer_js = '''
        let timeLeft = 300; // 5 menit
        let timerInterval;

        function startTimer() {
            const display = document.getElementById('timer-display');
            timerInterval = setInterval(() => {
                if(isCooking) return; // pause timer while processing
                
                timeLeft--;
                
                let m = Math.floor(timeLeft / 60);
                let s = timeLeft % 60;
                display.innerText = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
                
                if (timeLeft <= 60 && timeLeft > 0) {
                    display.classList.add('animate-pulse');
                }
                
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    alert("Waktu Habis! Mengulangi misi...");
                    location.reload();
                }
            }, 1000);
        }
'''

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace HTML
    # We find the existing header
    header_pattern = r'<!-- Header Level Info -->\s*<div class="bg-white p-5 border-b border-gray-200 flex items-start gap-4 shadow-sm">.*?<p id="level-desc"[^>]*>.*?</p>\s*</div>\s*</div>'
    match = re.search(header_pattern, content, re.DOTALL)
    if match:
        content = content.replace(match.group(0), timer_html)
    
    # 2. Inject JS Variables & Function
    if 'let timeLeft' not in content:
        content = content.replace('let isCooking = false;', 'let isCooking = false;\n' + timer_js)
    
    # 3. Call startTimer() in DOMContentLoaded
    if 'startTimer()' not in content:
        content = content.replace('loadLevel(0);', 'loadLevel(0);\n            startTimer();')
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected timer HTML and JS.")