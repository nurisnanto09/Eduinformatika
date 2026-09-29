import glob
import re

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The accidental injected string has extra </div> tags:
    # </div>
    # </div>
    # </div>
    # Or </section></main></div>
    
    # Let's fix the Action Bar at the top:
    # Find the top action bar
    top_action_pattern = r'(<!-- Action Bar \(Top\) -->.*?<button.*?Kosongkan.*?</button>.*?<button.*?Jalankan Program!.*?</button>\s*</div>)\s*(</div>\s*</div>\s*</div>|</section>\s*</main>\s*</div>)'
    
    match = re.search(top_action_pattern, content, re.DOTALL)
    if match:
        clean_action_bar = match.group(1)
        # Replace the whole matched block with just the clean action bar
        content = content.replace(match.group(0), clean_action_bar)
        
    # Now we need to add the closing tags back at the bottom, right before <!-- Cooking Animation Overlay -->
    closing_tags = '''
        </section>
    </main>
</div>
'''
    if '</section>' not in content.split('<!-- Cooking Animation Overlay')[0]:
        content = content.replace('<!-- Cooking Animation Overlay', closing_tags + '<!-- Cooking Animation Overlay')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed HTML structure.")