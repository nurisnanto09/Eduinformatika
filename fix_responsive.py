import glob

for i in range(1, 10):
    filename = f'game_koki_{i}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Left Column
    # Change <div class="flex-1 flex flex-col gap-4 min-h-0"> 
    # to <div class="contents lg:flex lg:flex-col lg:gap-4 lg:min-h-0 lg:flex-1">
    content = content.replace(
        '<!-- Left Column -->\n                <div class="flex-1 flex flex-col gap-4 min-h-0">',
        '<!-- Left Column -->\n                <div class="contents lg:flex lg:flex-col lg:gap-4 lg:min-h-0 lg:flex-1">'
    )
    
    # 2. Right Column
    # Change <div class="flex-1 flex flex-col gap-4 min-h-0">
    # to <div class="contents lg:flex lg:flex-col lg:gap-4 lg:min-h-0 lg:flex-1">
    content = content.replace(
        '<!-- Right Column -->\n                <div class="flex-1 flex flex-col gap-4 min-h-0">',
        '<!-- Right Column -->\n                <div class="contents lg:flex lg:flex-col lg:gap-4 lg:min-h-0 lg:flex-1">'
    )

    # 3. Add order classes to the children
    
    # Studi Kasus child:
    # Change <div class="hidden md:block"> to <div class="order-1 lg:order-none hidden md:block"> 
    # Wait! If Studi Kasus has hidden md:block, it won't even show on mobile!
    # The user asked for "Studi Kasus" on mobile! We must remove hidden md:block from Studi Kasus!
    content = content.replace(
        '<!-- Studi Kasus -->\n                    <div class="hidden md:block">',
        '<!-- Studi Kasus -->\n                    <div class="order-1 lg:order-none">'
    )
    
    # Lembar Resep child:
    # Right column has <div class="flex-1 flex flex-col min-h-0"> for Lembar Resep, and action bar below it.
    # We want both Lembar Resep and Action bar to be order 2!
    # Actually, they are siblings inside Right Column. If Right Column has contents, both become direct children.
    # So Lembar Resep needs order-2, Action Bar needs order-3? No, if Action Bar is order-3, it will be AFTER Blok Tersedia on mobile!
    # If we want Action Bar after Lembar Resep and BEFORE Blok Tersedia, we need:
    # Studi Kasus: order-1
    # Lembar Resep: order-2
    # Action Bar: order-3
    # Blok Tersedia: order-4
    
    # Let's apply these classes:
    
    # Lembar Resep
    content = content.replace(
        '<!-- Lembar Resep -->\n                    <div class="flex-1 flex flex-col min-h-0">',
        '<!-- Lembar Resep -->\n                    <div class="order-2 lg:order-none flex-1 flex flex-col min-h-0">'
    )
    
    # Action Bar
    content = content.replace(
        '<!-- Action Bar (Bottom Right) -->\n                    <div class="flex justify-between items-center bg-white p-4 rounded-xl border border-gray-200 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)] mt-2">',
        '<!-- Action Bar (Bottom Right) -->\n                    <div class="order-3 lg:order-none flex justify-between items-center bg-white p-4 rounded-xl border border-gray-200 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)] lg:mt-2 mt-0">'
    )
    
    # Blok Tersedia
    content = content.replace(
        '<!-- Kumpulan Blok -->\n                    <div class="flex-1 flex flex-col min-h-0">',
        '<!-- Kumpulan Blok -->\n                    <div class="order-4 lg:order-none flex-1 flex flex-col min-h-0">'
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied responsive layout order.")