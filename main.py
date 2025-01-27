import random
import os

# Data Base =====================================================================================
hiragana = [
    ('a', 'あ'), ('i', 'い'), ('u', 'う'), ('e', 'え'), ('o', 'お'),
    ('ka', 'か'), ('ki', 'き'), ('ku', 'く'), ('ke', 'け'), ('ko', 'こ'),
    ('sa', 'さ'), ('shi', 'し'), ('su', 'す'), ('se', 'せ'), ('so', 'そ'),
    ('ta', 'た'), ('chi', 'ち'), ('tsu', 'つ'), ('te', 'て'), ('to', 'と'),
    ('na', 'な'), ('ni', 'に'), ('nu', 'ぬ'), ('ne', 'ね'), ('no', 'の'),
    ('ha', 'は'), ('hi', 'ひ'), ('fu', 'ふ'), ('he', 'へ'), ('ho', 'ほ'),
    ('ma', 'ま'), ('mi', 'み'), ('mu', 'む'), ('me', 'め'), ('mo', 'も'),
    ('ya', 'や'), ('yu', 'ゆ'), ('yo', 'よ'),
    ('ra', 'ら'), ('ri', 'り'), ('ru', 'る'), ('re', 'れ'), ('ro', 'ろ'),
    ('wa', 'わ'), ('wo', 'を'), ('n', 'ん')
]

katakana = [
    ('a', 'ア'), ('i', 'イ'), ('u', 'ウ'), ('e', 'エ'), ('o', 'オ'),
    ('ka', 'カ'), ('ki', 'キ'), ('ku', 'ク'), ('ke', 'ケ'), ('ko', 'コ'),
    ('sa', 'サ'), ('shi', 'シ'), ('su', 'ス'), ('se', 'セ'), ('so', 'ソ'),
    ('ta', 'タ'), ('chi', 'チ'), ('tsu', 'ツ'), ('te', 'テ'), ('to', 'ト'),
    ('na', 'ナ'), ('ni', 'ニ'), ('nu', 'ヌ'), ('ne', 'ネ'), ('no', 'ノ'),
    ('ha', 'ハ'), ('hi', 'ヒ'), ('fu', 'フ'), ('he', 'ヘ'), ('ho', 'ホ'),
    ('ma', 'マ'), ('mi', 'ミ'), ('mu', 'ム'), ('me', 'メ'), ('mo', 'モ'),
    ('ya', 'ヤ'), ('yu', 'ユ'), ('yo', 'ヨ'),
    ('ra', 'ラ'), ('ri', 'リ'), ('ru', 'ル'), ('re', 'レ'), ('ro', 'ロ'),
    ('wa', 'ワ'), ('wo', 'ヲ'), ('n', 'ン')
]

hiragana_groups = {
    'a': [('a', 'あ'), ('i', 'い'), ('u', 'う'), ('e', 'え'), ('o', 'お')],
    'ka': [('ka', 'か'), ('ki', 'き'), ('ku', 'く'), ('ke', 'け'), ('ko', 'こ')],
    'sa': [('sa', 'さ'), ('shi', 'し'), ('su', 'す'), ('se', 'せ'), ('so', 'そ')],
    'ta': [('ta', 'た'), ('chi', 'ち'), ('tsu', 'つ'), ('te', 'て'), ('to', 'と')],
    'na': [('na', 'な'), ('ni', 'に'), ('nu', 'ぬ'), ('ne', 'ね'), ('no', 'の')],
    'ha': [('ha', 'は'), ('hi', 'ひ'), ('fu', 'ふ'), ('he', 'へ'), ('ho', 'ほ')],
    'ma': [('ma', 'ま'), ('mi', 'み'), ('mu', 'む'), ('me', 'め'), ('mo', 'も')],
    'ya': [('ya', 'や'), ('yu', 'ゆ'), ('yo', 'よ')],
    'ra': [('ra', 'ら'), ('ri', 'り'), ('ru', 'る'), ('re', 'れ'), ('ro', 'ろ')],
    'wa': [('wa', 'わ'), ('wo', 'を')],
    'n': [('n', 'ん')]
}

katakana_groups = {
    'a': [('a', 'ア'), ('i', 'イ'), ('u', 'ウ'), ('e', 'エ'), ('o', 'オ')],
    'ka': [('ka', 'カ'), ('ki', 'キ'), ('ku', 'ク'), ('ke', 'ケ'), ('ko', 'コ')],
    'sa': [('sa', 'サ'), ('shi', 'シ'), ('su', 'ス'), ('se', 'セ'), ('so', 'ソ')],
    'ta': [('ta', 'タ'), ('chi', 'チ'), ('tsu', 'ツ'), ('te', 'テ'), ('to', 'ト')],
    'na': [('na', 'ナ'), ('ni', 'ニ'), ('nu', 'ヌ'), ('ne', 'ネ'), ('no', 'ノ')],
    'ha': [('ha', 'ハ'), ('hi', 'ヒ'), ('fu', 'フ'), ('he', 'ヘ'), ('ho', 'ホ')],
    'ma': [('ma', 'マ'), ('mi', 'ミ'), ('mu', 'ム'), ('me', 'メ'), ('mo', 'モ')],
    'ya': [('ya', 'ヤ'), ('yu', 'ユ'), ('yo', 'ヨ')],
    'ra': [('ra', 'ラ'), ('ri', 'リ'), ('ru', 'ル'), ('re', 'レ'), ('ro', 'ロ')],
    'wa': [('wa', 'ワ'), ('wo', 'ヲ')],
    'n': [('n', 'ン')]
}

kanji = [('one', '一'), ('two', '二'), ('three', '三'), ('four', '四'), ('five', '五'),
         ('six', '六'), ('seven', '七'), ('eight', '八'), ('nine', '九'), ('ten', '十')]





# Logika ========================================================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

marked = {"hiragana": [], "katakana": [], "kanji": []} # Save huruf ditandai

def mode_acak(huruf, nama_huruf):
    while True:
    
        romaji, char = random.choice(huruf)
        print(f"\nHuruf: {char} (Romaji: {romaji})")
        print("Tekan Enter untuk huruf baru atau ketik 't' untuk menandai huruf ini.")
        action = input("Aksi: ").strip().lower()
        if action == "t":
            if (romaji, char) not in marked[nama_huruf]:
                marked[nama_huruf].append((romaji, char))
                print(f"{char} ({romaji}) telah ditandai.")
            else:
                print(f"{char} ({romaji}) sudah ditandai sebelumnya.")
        elif action == "":
            continue
        else:
            break

def mode_vokal(huruf, nama_huruf):
    while True:
    
        romaji, _ = random.choice(huruf)
        print(f"\nHuruf: {romaji}")
        print("Tekan Enter untuk huruf baru atau ketik 't' untuk menandai huruf ini.")
        action = input("Aksi: ").strip().lower()
        if action == "t":
            if romaji not in [mark[0] for mark in marked[nama_huruf]]:
                marked[nama_huruf].append((romaji, None))
                print(f"{romaji} telah ditandai.")
            else:
                print(f"{romaji} sudah ditandai sebelumnya.")
        elif action == "":
            continue
        else:
            break

def mode_ditandai(nama_huruf):

    if not marked[nama_huruf]:
        print("\nTidak ada huruf yang ditandai.")
    else:
        print("\nHuruf yang ditandai:")
        for romaji, char in marked[nama_huruf]:
            print(f"{char} (Romaji: {romaji})", end="  ")
        print()
        repeat = input("\nApakah Anda ingin mengulang bagian yang ditandai? (y/n): ").strip().lower()
        if repeat == "y":
            while True:
                clear_screen()
                romaji, char = random.choice(marked[nama_huruf])
                print(f"\nHuruf: {char} (Romaji: {romaji})")
                print("Tekan Enter untuk huruf baru atau ketik 'q' untuk keluar dari pengulangan.")
                action = input("Aksi: ").strip().lower()
                if action == "q":
                    break

def mode_tanpa_pengulangan(huruf):
    remaining = huruf[:]
    random.shuffle(remaining)
    while remaining:
    
        romaji, char = remaining.pop()
        print(f"\nHuruf: {char} (Romaji: {romaji})")
        action = input("Tekan Enter untuk huruf berikutnya atau ketik 'exit' untuk keluar: ").strip().lower()
        if action == "exit":
            break
    if not remaining:
        print("\nSemua huruf sudah ditampilkan.")

def display_group(group, language_groups, is_random=False):
    """Menampilkan elemen huruf berdasarkan grup yang dipilih (baik hiragana atau katakana)."""
    if group not in language_groups:
        print(f"Tidak ditemukan grup '{group}'")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    items = language_groups[group]
    
    # Jika is_random True, acak urutan item
    if is_random:
        items = random.sample(items, len(items))

    # Tampilkan elemen satu per satu
    for romaji, kana in items:
      # Memanggil fungsi clear_screen
        print(f"{romaji} - {kana}")
        input("Tekan Enter untuk melanjutkan...")

def choose_category(language_groups, is_random):
    """Memilih kategori huruf berdasarkan input pengguna."""
    while True:
    
        print("Masukkan salah satu kategori berikut:")
        print("a, ka, sa, ta, na, ha, ma, ya, ra, wa")
        
        group = input("\nMasukkan kategori: ").strip().lower()
        if group == 'exit':
            return False
        if group == 'back':
            return True
        
        # Tampilkan huruf berdasarkan kategori yang dipilih
        display_group(group, language_groups, is_random)
        return False





# Menu ==================================================================================================

def display_menu(): # Menu utama
    print("\n=== Pilihan Menu ===")
    print("1. Hiragana")
    print("2. Katakana")
    print("3. Kanji")
    print("0. Keluar")

def display_sub_menu(option): # Sub menu utama
    print(f"\n=== {option.capitalize()} Menu ===")
    print("1. Huruf Acak")
    print("2. Vokal Lengkap")
    print("3. Huruf Ditandai")
    print("4. Random Tanpa Pengulangan")
    print("5. Huruf Group")
    print("6. Huruf Group Acak")
    print("0. Kembali")

def main():
    while True:
        # Memilih jenis abjad
        display_menu()
        choice = input("Pilih opsi (1-4): ").strip()

        if choice == "1":
            huruf = hiragana
            language_groups = hiragana_groups
            nama_huruf = "hiragana"
        elif choice == "2":
            huruf = katakana
            language_groups = katakana_groups
            nama_huruf = "katakana"
        elif choice == "3":
            huruf = kanji
            nama_huruf = "kanji"
        elif choice == "0":
            print("\nSampai jumpa!")
            break
        else:
            print("\nPilihan tidak valid.")
            continue

        while True:
            # Memilih jenis pembelajaran
            display_sub_menu(nama_huruf)
            sub_choice = input("Pilih opsi (1-6): ").strip()

            if sub_choice == "1":
                mode_acak(huruf, nama_huruf)
            elif sub_choice == "2":
                mode_vokal(huruf, nama_huruf)
            elif sub_choice == "3":
                mode_ditandai(nama_huruf)
            elif sub_choice == "4":
                mode_tanpa_pengulangan(huruf)
            elif sub_choice == "5":
                choose_category(language_groups, is_random=False)
            elif sub_choice == "6":

                choose_category(language_groups, is_random=True)

            elif sub_choice == "0":
                break
            else:
                print("\nPilihan tidak valid.")

if __name__ == "__main__":
    main()