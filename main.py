import random
import os

# Data Base =====================================================================================
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
    'wa': [('wa', 'わ'), ('wo', 'を'), ('n', 'ん')],
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
    'wa': [('wa', 'ワ'), ('wo', 'ヲ'), ('n', 'ン')],
}

kanji = {
    'angka': [
        ('satu', '一'), ('dua', '二'), ('tiga', '三'), ('empat', '四'), ('lima', '五'),
        ('enam', '六'), ('tujuh', '七'), ('delapan', '八'), ('sembilan', '九'), ('sepuluh', '十'),
        ('seratus', '百'), ('seribu', '千'), ('sepuluh ribu', '万'), ('seratus juta', '億')
    ],
    'elemen': [
        ('api', '火'), ('air', '水'), ('tanah', '土'), ('pohon', '木'), ('emas', '金'),
        ('batu', '石'), ('angin', '風'), ('langit', '空'), ('petir', '雷')
    ],
    'waktu': [
        ('waktu', '時'), ('tahun', '年'), ('bulan', '月'), ('hari', '日'), ('minggu', '週'),
        ('jam', '時'), ('menit', '分'), ('detik', '秒'), ('pagi', '朝'), ('siang', '昼'),
        ('sore', '夕'), ('malam', '夜'), ('kemarin', '昨日'), ('besok', '明日')
    ],
    'keluarga': [
        ('ayah', '父'), ('ibu', '母'), ('kakak laki-laki', '兄'), ('kakak perempuan', '姉'),
        ('adik laki-laki', '弟'), ('adik perempuan', '妹'), ('keluarga', '家族'),
        ('anak laki-laki', '息子'), ('anak perempuan', '娘'), ('kakek', '祖父'), ('nenek', '祖母')
    ],
    'sifat': [
        ('besar', '大'), ('kecil', '小'), ('panjang', '長'), ('pendek', '短'), ('baru', '新'),
        ('lama', '古'), ('baik', '良'), ('buruk', '悪'), ('kuat', '強'), ('lemah', '弱')
    ],
    'hewan': [
        ('anjing', '犬'), ('kucing', '猫'), ('burung', '鳥'), ('kuda', '馬'), ('ikan', '魚'),
        ('ular', '蛇'), ('serigala', '狼'), ('kelinci', '兎'), ('tikus', '鼠'), ('sapi', '牛')
    ],
    'alam': [
        ('gunung', '山'), ('sungai', '川'), ('laut', '海'), ('hutan', '森'), ('bunga', '花'),
        ('bulan', '月'), ('matahari', '日'), ('bintang', '星'), ('awan', '雲'), ('salju', '雪')
    ],
    'profesi': [
        ('guru', '先生'), ('dokter', '医者'), ('petani', '農家'), ('polisi', '警察'), ('koki', '料理人'),
        ('penulis', '作家'), ('seniman', '芸術家'), ('insinyur', '技師'), ('pedagang', '商人')
    ]
}

# Logika ========================================================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# marked = {"hiragana": [], "katakana": [], "kanji": [], "hiragana_katakana": []}  # Save huruf ditandai

def get_combined_list():
    combined = []
    for key in hiragana_groups:
        if key in katakana_groups:
            combined.extend([
                (h_romaji, h_char, k_char)
                for (h_romaji, h_char), (_, k_char) in zip(hiragana_groups[key], katakana_groups[key])])
    return combined

def get_flat_list(group_data):
    # Mengembalikan daftar datar dari grup data.
    return [item for group in group_data.values() for item in group]

def mode_acak(group_data, nama_huruf):
    huruf = get_flat_list(group_data)
    while True:
        clear_screen()
        romaji, char = random.choice(huruf)
        print(f"\nHuruf: {char} (Romaji: {romaji})")
        print("Tekan Enter untuk huruf baru atau ketik 't' untuk berhenti.")
        action = input("Aksi: ").strip().lower()
        if action == "":
            continue
        else:
            break

def mode_acak_hk():
    combined_list = get_combined_list()
    while True:
        clear_screen()
        romaji, hiragana, katakana = random.choice(combined_list)
        print(f"\nHuruf: {hiragana} (Hiragana) | {katakana} (Katakana) | Romaji: {romaji}")
        print("Tekan Enter untuk huruf baru atau ketik 't' untuk berhenti.")
        action = input("Aksi: ").strip().lower()
        if action == "":
            continue
        else:
            break

def mode_vokal(group_data, nama_huruf):
    huruf = get_flat_list(group_data)  # Asumsikan ini mengembalikan daftar pasangan (romaji, karakter)
    remaining = huruf[:]  # Salin daftar huruf untuk pengacakan
    random.shuffle(remaining)  # Acak daftar huruf
    while remaining:
        clear_screen()
        romaji, char = remaining.pop()  # Ambil elemen terakhir dari daftar yang diacak
        print(f"\nHuruf {nama_huruf}: {romaji}")
        action = input("Tekan Enter untuk huruf berikutnya atau ketik 'q' untuk keluar: ").strip().lower()
        if action == "q":
            break
    if not remaining:
        print("\nSemua huruf sudah ditampilkan.")

def mode_abjad(group_data, nama_huruf):
    huruf = get_flat_list(group_data)  # Asumsikan ini mengembalikan daftar pasangan (romaji, karakter)
    remaining = huruf[:]  # Salin daftar huruf untuk pengacakan
    random.shuffle(remaining)  # Acak daftar huruf
    while remaining:
        clear_screen()
        romaji, char = remaining.pop()  # Ambil elemen terakhir dari daftar yang diacak
        print(f"\nHuruf {nama_huruf}: {char}")
        action = input("Tekan Enter untuk huruf berikutnya atau ketik 'q' untuk keluar: ").strip().lower()
        if action == "q":
            break
    if not remaining:
        print("\nSemua huruf sudah ditampilkan.")


# def mode_ditandai(nama_huruf):
#     if not marked[nama_huruf]:
#         print("\nTidak ada huruf yang ditandai.")
#     else:
#         print("\nHuruf yang ditandai:")
#         for romaji, char in marked[nama_huruf]:
#             print(f"{char} (Romaji: {romaji})", end="  ")
#         print()
#         repeat = input("\nApakah Anda ingin mengulang bagian yang ditandai? (y/n): ").strip().lower()
#         if repeat == "y":
#             while True:
#                 clear_screen()
#                 romaji, char = random.choice(marked[nama_huruf])
#                 print(f"\nHuruf: {char} (Romaji: {romaji})")
#                 print("Tekan Enter untuk huruf baru atau ketik 'q' untuk keluar dari pengulangan.")
#                 action = input("Aksi: ").strip().lower()
#                 if action == "q":
#                     break

def mode_tanpa_pengulangan(group_data):
    huruf = get_flat_list(group_data)
    remaining = huruf[:]
    random.shuffle(remaining)
    while remaining:
        clear_screen()
        romaji, char = remaining.pop()
        print(f"\nHuruf: {char} (Romaji: {romaji})")
        action = input("Tekan Enter untuk huruf berikutnya atau ketik 'q' untuk keluar: ").strip().lower()
        if action == "q":
            break
    if not remaining:
        print("\nSemua huruf sudah ditampilkan.")

def mode_tanpa_pengulangan_hk():
    combined_list = get_combined_list()
    remaining = combined_list[:] # Menyalin daftar
    random.shuffle(remaining) # Mengacak daftar

    while remaining: # Selama masih ada elemen tersisa
        clear_screen()
        romaji, hiragana, katakana = remaining.pop() # Mengambil elemen terakhir dari remaining
        print(f"\nHuruf: {hiragana} (Hiragana) | {katakana} (Katakana) | Romaji: {romaji}")
        action = input("Tekan Enter untuk huruf berikutnya atau ketik 'q' untuk keluar: ").strip().lower()
        if action == "q":
            break

    if not remaining:
        print("\nSemua huruf sudah ditampilkan.")

def display_group(group, language_groups, is_random=False):
    if group not in language_groups:
        clear_screen()
        print(f"Tidak ditemukan grup '{group}'")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    items = language_groups[group]
    if is_random:
        items = random.sample(items, len(items))

    for romaji, kana in items:
        clear_screen()
        print(f"{romaji} - {kana}")
        input("Tekan Enter untuk melanjutkan...")

def display_group_hk(group, is_random=False):
    if group not in hiragana_groups or group not in katakana_groups:
        clear_screen()
        print(f"Tidak ditemukan grup '{group}'")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    hiragana = hiragana_groups[group]
    katakana = katakana_groups[group]
    combined = [(h_romaji, h_char, k_char) for (h_romaji, h_char), (_, k_char) in zip(hiragana, katakana)]

    if is_random:
        combined = random.sample(combined, len(combined))

    for romaji, h_char, k_char in combined:
        clear_screen()
        print(f"{romaji} - {h_char} (Hiragana), {k_char} (Katakana)")
        input("Tekan Enter untuk melanjutkan...")

def choose_category(language_groups, is_random):
    while True:
        clear_screen()
        print("Masukkan salah satu kategori berikut:")
        print("a, ka, sa, ta, na, ha, ma, ya, ra, wa")
        group = input("\nMasukkan kategori: ").strip().lower()
        if group in ["q"]:
            return
        display_group(group, language_groups, is_random)

def choose_category_hk(is_random):
    while True:
        clear_screen()
        print("Masukkan salah satu kategori berikut:")
        print("a, ka, sa, ta, na, ha, ma, ya, ra, wa")
        group = input("\nMasukkan kategori: ").strip().lower()
        if group in ["q"]:
            return
        display_group_hk(group, is_random)

def tampilkan_kanji(Kanji):
    while True:
        clear_screen()
        print("\n=== Pilih Kategori Kanji ===")
        # Menampilkan daftar kategori secara dinamis
        kategori_set = list(kanji.keys())  # Mengambil kategori unik
        for idx, kategori in enumerate(kategori_set, 1):
            print(f"{idx}. {kategori}")
        print(f"{len(kategori_set) + 1}. Tampilkan Semua")
        print("0. Kembali")

        try:
            pilihan = int(input("\nPilih kategori (0-{}): ".format(len(kategori_set) + 1)).strip())
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue

        if pilihan == 0:
            break
        elif 1 <= pilihan <= len(kategori_set):
            kategori_terpilih = kategori_set[pilihan - 1]
            kanji_terpilih = kanji[kategori_terpilih]
        elif pilihan == len(kategori_set) + 1:
            kategori_terpilih = "Semua"
            kanji_terpilih = [kanji_item for items in kanji.values() for kanji_item in items]
        else:
            print("Pilihan tidak valid.")
            continue

        print("\n=== Kanji dari Kategori '{}' ===".format(kategori_terpilih))
        print("1. Sesuai Urutan")
        print("2. Acak")
        print("0. Kembali")

        try:
            opsi_tampil = int(input("\nPilih cara tampilkan (0-2): ").strip())
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue

        if opsi_tampil == 0:
            return
        elif opsi_tampil == 1:
            hasil = kanji_terpilih
        elif opsi_tampil == 2:
            hasil = random.sample(kanji_terpilih, len(kanji_terpilih))
        else:
            print("Pilihan tidak valid.")
            continue

        # Menampilkan hasil satu persatu
        for romaji, karakter in hasil:
            clear_screen()
            print("\n")
            print(f"{romaji} - {karakter}")
            stop = input("Tekan Enter untuk lanjut atau ketik 'q' untuk berhenti: ")
            if stop.lower() == 'q':
                print("Proses berhenti.")
                break
        else:
            # Jika belum berhenti, lanjutkan perulangan untuk kategori berikutnya
            input("\nTekan Enter untuk melanjutkan ke kategori berikutnya...")

# Menu ==================================================================================================

def display_menu():
    clear_screen()
    print("\n=== Pilihan Menu ===")
    print("1. Hiragana")
    print("2. Katakana")
    print("3. Kanji")
    print("4. Hiragana dan Katakana")
    print("0. Keluar")

def display_sub_menu(option):
    print(f"\n=== {option.capitalize()} Menu ===")
    print("1. Huruf Acak")
    print("2. Vokal/Abjad")
    print("3. Random Tanpa Pengulangan")
    print("4. Huruf Group")
    print("5. Huruf Group Acak")
    print("0. Kembali")

def display_sub_menu_hk(option):
    print(f"\n=== {option.capitalize()} Menu ===")
    print("1. Huruf Acak")
    print("2. Random Tanpa Pengulanga ")
    print("3. Huruf Group")
    print("4. Huruf Group Acak")
    print("0. Kembali")

def main():
    while True:
        clear_screen()
        print("\n=== Pilihan Menu ===")
        print("1. Hiragana")
        print("2. Katakana")
        print("3. Kanji")
        print("4. Hiragana dan Katakana")
        print("0. Keluar")

        choice = input("Pilih opsi (1-4): ").strip()

        if choice == "1":
            group_data = hiragana_groups
            nama_huruf = "hiragana"
        elif choice == "2":
            group_data = katakana_groups
            nama_huruf = "katakana"
        elif choice == "3":  # Jika pilihan adalah Kanji
            tampilkan_kanji(kanji)  # Akan kembali ke menu utama jika memilih '0' di dalam fungsi ini
            continue  # Melanjutkan setelah menampilkan kanji
        elif choice == "4":
            while True:
                print(f"\n=== Hiragana dan Katakana Menu ===")
                print("1. Huruf Acak")
                print("2. Random Tanpa Pengulangan")
                print("3. Huruf Group")
                print("4. Huruf Group Acak")
                print("0. Kembali")
                sub_choice = input("Pilih opsi (1-4): ").strip()

                if sub_choice == "1":
                    mode_acak_hk()
                elif sub_choice == "2":
                    mode_tanpa_pengulangan_hk()
                elif sub_choice == "3":
                    choose_category_hk(is_random=False)
                elif sub_choice == "4":
                    choose_category_hk(is_random=True)
                elif sub_choice == "0":
                    break
                else:
                    print("\nPilihan tidak valid.")
            continue  # Melanjutkan setelah memilih opsi untuk Hiragana dan Katakana
        elif choice == "0":
            print("\nSampai jumpa!")
            clear_screen()
            break
        else:
            print("\nPilihan tidak valid.")
            continue

        # Pastikan nama_huruf sudah terdefinisi di sini
        while True:
            # Menampilkan submenu untuk Hiragana atau Katakana
            print(f"\n=== {nama_huruf.capitalize()} Menu ===")
            print("1. Huruf Acak")
            print("2. Vokal/Abjad")
            print("3. Random Tanpa Pengulangan")
            print("4. Huruf Group")
            print("5. Huruf Group Acak")
            print("0. Kembali")

            sub_choice = input("Pilih opsi (1-5): ").strip()

            if sub_choice == "1":
                mode_acak(group_data, nama_huruf)
            elif sub_choice == "2":
                print("1. Vokal Only")
                print("2. Abjad Only")
                pilih = input("Pilih opsi (1/2): ").strip()
                if pilih == "1":
                    mode_vokal(group_data, nama_huruf)
                elif pilih == "2":
                    mode_abjad(group_data, nama_huruf)
                else:
                    print("Pilihan tidak valid. Coba lagi...")
                    continue
            elif sub_choice == "3":
                mode_tanpa_pengulangan(group_data)
            elif sub_choice == "4":
                choose_category(group_data, is_random=False)
            elif sub_choice == "5":
                choose_category(group_data, is_random=True)
            elif sub_choice == "0":
                break
            else:
                print("\nPilihan tidak valid.")

if __name__ == "__main__":
    main()
