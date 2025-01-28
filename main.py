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

kanji_n5 = {
    'angka': [
        { 'kanji': '一', 'onyomi': 'ichi, itsu', 'kunyomi': 'hito, hitotsu', 'arti': 'satu' },
        { 'kanji': '二', 'onyomi': 'ni', 'kunyomi': 'futa, futatsu', 'arti': 'dua' },
        { 'kanji': '三', 'onyomi': 'san', 'kunyomi': 'mi, mittsu', 'arti': 'tiga' },
        { 'kanji': '四', 'onyomi': 'shi', 'kunyomi': 'yo, yon, yottsu', 'arti': 'empat' },
        { 'kanji': '五', 'onyomi': 'go', 'kunyomi': 'itsu, itsutsu', 'arti': 'lima' },
        { 'kanji': '六', 'onyomi': 'roku', 'kunyomi': 'mu, muttsu', 'arti': 'enam' },
        { 'kanji': '七', 'onyomi': 'shichi', 'kunyomi': 'nana, nanatsu', 'arti': 'tujuh' },
        { 'kanji': '八', 'onyomi': 'hachi', 'kunyomi': 'ya, yattsu', 'arti': 'delapan' },
        { 'kanji': '九', 'onyomi': 'kyuu, ku', 'kunyomi': 'kokono, kokonotsu', 'arti': 'sembilan' },
        { 'kanji': '十', 'onyomi': 'juu, ji', 'kunyomi': 'to, too', 'arti': 'sepuluh' },
        { 'kanji': '百', 'onyomi': 'hyaku', 'kunyomi': 'momo', 'arti': 'seratus' },
        { 'kanji': '千', 'onyomi': 'sen', 'kunyomi': 'chi', 'arti': 'seribu' },
        { 'kanji': '万', 'onyomi': 'man, ban', 'kunyomi': '-', 'arti': 'sepuluh ribu' }
    ],
    'waktu': [
        { 'kanji': '日', 'onyomi': 'nichi, jitsu', 'kunyomi': 'hi, ka', 'arti': 'hari/matahari' },
        { 'kanji': '月', 'onyomi': 'getsu, gatsu', 'kunyomi': 'tsuki', 'arti': 'bulan' },
        { 'kanji': '年', 'onyomi': 'nen', 'kunyomi': 'toshi', 'arti': 'tahun' },
        { 'kanji': '時', 'onyomi': 'ji', 'kunyomi': 'toki', 'arti': 'waktu' },
        { 'kanji': '分', 'onyomi': 'bun, fun, bu', 'kunyomi': 'wa(keru), wa(karu)', 'arti': 'menit/bagian' },
        { 'kanji': '午', 'onyomi': 'go', 'kunyomi': '-', 'arti': 'tengah hari' },
        { 'kanji': '半', 'onyomi': 'han', 'kunyomi': 'naka(ba)', 'arti': 'setengah' }
    ],
    'alam': [
        { 'kanji': '山', 'onyomi': 'san', 'kunyomi': 'yama', 'arti': 'gunung' },
        { 'kanji': '川', 'onyomi': 'sen', 'kunyomi': 'kawa', 'arti': 'sungai' },
        { 'kanji': '天', 'onyomi': 'ten', 'kunyomi': 'ame, ama', 'arti': 'langit' },
        { 'kanji': '木', 'onyomi': 'moku, boku', 'kunyomi': 'ki, ko', 'arti': 'pohon' },
        { 'kanji': '水', 'onyomi': 'sui', 'kunyomi': 'mizu', 'arti': 'air' },
        { 'kanji': '火', 'onyomi': 'ka', 'kunyomi': 'hi', 'arti': 'api' },
        { 'kanji': '土', 'onyomi': 'do, to', 'kunyomi': 'tsuchi', 'arti': 'tanah' }
    ],
    'keluarga': [
        { 'kanji': '父', 'onyomi': 'fu', 'kunyomi': 'chichi', 'arti': 'ayah' },
        { 'kanji': '母', 'onyomi': 'bo', 'kunyomi': 'haha', 'arti': 'ibu' },
        { 'kanji': '子', 'onyomi': 'shi, su', 'kunyomi': 'ko', 'arti': 'anak' },
        { 'kanji': '男', 'onyomi': 'dan, nan', 'kunyomi': 'otoko', 'arti': 'laki-laki' },
        { 'kanji': '女', 'onyomi': 'jo, nyo, nyou', 'kunyomi': 'onna, me', 'arti': 'perempuan' }
    ],
    'lain-lain': [
        { 'kanji': '何', 'onyomi': 'ka', 'kunyomi': 'nani, nan', 'arti': 'apa' },
        { 'kanji': '名', 'onyomi': 'mei, myou', 'kunyomi': 'na', 'arti': 'nama' },
        { 'kanji': '大', 'onyomi': 'dai, tai', 'kunyomi': 'oo(kii)', 'arti': 'besar' },
        { 'kanji': '小', 'onyomi': 'shou', 'kunyomi': 'chi(sai), ko', 'arti': 'kecil' }
    ]
}

kanji_n4 = {
    'kata kerja': [
        { 'kanji': '行', 'onyomi': 'kou, gyou', 'kunyomi': 'iku, okiru, yukou', 'arti': 'pergi' },
        { 'kanji': '食', 'onyomi': 'shoku', 'kunyomi': 'taberu, kuto', 'arti': 'makan' },
        { 'kanji': '飲', 'onyomi': 'in', 'kunyomi': 'nomu', 'arti': 'minum' },
        { 'kanji': '見', 'onyomi': 'ken', 'kunyomi': 'miru, kakeru', 'arti': 'melihat' },
        { 'kanji': '会', 'onyomi': 'kai', 'kunyomi': 'au', 'arti': 'bertemu' },
        { 'kanji': '話', 'onyomi': 'wa', 'kunyomi': 'hanasu', 'arti': 'berbicara' },
        { 'kanji': '聞', 'onyomi': 'bun', 'kunyomi': 'kiku', 'arti': 'mendengar' },
        { 'kanji': '買', 'onyomi': 'bai', 'kunyomi': 'kau', 'arti': 'membeli' },
        { 'kanji': '作', 'onyomi': 'saku', 'kunyomi': 'tsukuru', 'arti': 'membuat' },
        { 'kanji': '使', 'onyomi': 'shi', 'kunyomi': 'tsukau', 'arti': 'menggunakan' }
    ],
    'waktu': [
        { 'kanji': '時', 'onyomi': 'ji, shi', 'kunyomi': 'toki', 'arti': 'waktu' },
        { 'kanji': '分', 'onyomi': 'bun, fun, bu', 'kunyomi': 'wa, wakeru', 'arti': 'menit, bagi' },
        { 'kanji': '日', 'onyomi': 'nichi, jitsu', 'kunyomi': 'hi, ka', 'arti': 'hari, matahari' },
        { 'kanji': '月', 'onyomi': 'getsu, gatsu', 'kunyomi': 'tsuki', 'arti': 'bulan' },
        { 'kanji': '年', 'onyomi': 'nen', 'kunyomi': 'toshi', 'arti': 'tahun' },
        { 'kanji': '今', 'onyomi': 'kon, kin', 'kunyomi': 'ima', 'arti': 'sekarang' },
        { 'kanji': '週', 'onyomi': 'shuu', 'kunyomi': '', 'arti': 'minggu' },
        { 'kanji': '前', 'onyomi': 'zen', 'kunyomi': 'mae', 'arti': 'sebelum, depan' },
        { 'kanji': '後', 'onyomi': 'go, kou', 'kunyomi': 'ato, ushiro', 'arti': 'setelah, belakang' },
        { 'kanji': '時', 'onyomi': 'ji', 'kunyomi': 'toki', 'arti': 'waktu' }
    ],
    'anggaran & angka': [
        { 'kanji': '百', 'onyomi': 'hyaku', 'kunyomi': '', 'arti': 'seratus' },
        { 'kanji': '千', 'onyomi': 'sen', 'kunyomi': '', 'arti': 'seribu' },
        { 'kanji': '万', 'onyomi': 'man', 'kunyomi': '', 'arti': 'sepuluh ribu' },
        { 'kanji': '億', 'onyomi': 'oku', 'kunyomi': '', 'arti': 'seratus juta' }
    ],
    'tempat & arah': [
        { 'kanji': '上', 'onyomi': 'jou, shou', 'kunyomi': 'ue, kami', 'arti': 'atas' },
        { 'kanji': '下', 'onyomi': 'ka, ge', 'kunyomi': 'shita, moto', 'arti': 'bawah' },
        { 'kanji': '中', 'onyomi': 'chuu, juu', 'kunyomi': 'naka', 'arti': 'dalam, tengah' },
        { 'kanji': '外', 'onyomi': 'gai, ge', 'kunyomi': 'soto, hoka', 'arti': 'luar' },
        { 'kanji': '東', 'onyomi': 'tou', 'kunyomi': 'higashi', 'arti': 'timur' },
        { 'kanji': '西', 'onyomi': 'sei, sai', 'kunyomi': 'nishi', 'arti': 'barat' },
        { 'kanji': '南', 'onyomi': 'nan', 'kunyomi': 'minami', 'arti': 'selatan' },
        { 'kanji': '北', 'onyomi': 'hoku', 'kunyomi': 'kita', 'arti': 'utara' }
    ],
    'benda & benda lainnya': [
        { 'kanji': '車', 'onyomi': 'sha', 'kunyomi': 'kuruma', 'arti': 'mobil' },
        { 'kanji': '電', 'onyomi': 'den', 'kunyomi': '', 'arti': 'listrik' },
        { 'kanji': '電話', 'onyomi': 'denwa', 'kunyomi': '', 'arti': 'telepon' },
        { 'kanji': '名', 'onyomi': 'mei, myou', 'kunyomi': 'na', 'arti': 'nama' },
        { 'kanji': '白', 'onyomi': 'haku', 'kunyomi': 'shiro', 'arti': 'putih' },
        { 'kanji': '黒', 'onyomi': 'koku', 'kunyomi': 'kuro', 'arti': 'hitam' },
        { 'kanji': '赤', 'onyomi': 'seki, shaku', 'kunyomi': 'aka', 'arti': 'merah' },
        { 'kanji': '青', 'onyomi': 'sei, shou', 'kunyomi': 'ao', 'arti': 'biru' }
    ]
}

kanji_n3 = {
    'kata kerja': [
        {'kanji': '始', 'onyomi': 'shi', 'kunyomi': 'haji', 'arti': 'memulai'},
        {'kanji': '終', 'onyomi': 'shuu', 'kunyomi': 'owari, owaru', 'arti': 'selesai'},
        {'kanji': '探', 'onyomi': 'tan', 'kunyomi': 'sagasu', 'arti': 'mencari'},
        {'kanji': '努力', 'onyomi': 'doryoku', 'kunyomi': '', 'arti': 'usaha keras'},
        {'kanji': '運', 'onyomi': 'un', 'kunyomi': 'un', 'arti': 'keberuntungan'},
        {'kanji': '笑', 'onyomi': 'shou', 'kunyomi': 'warau', 'arti': 'tersenyum'},
        {'kanji': '住', 'onyomi': 'juu', 'kunyomi': 'sumu', 'arti': 'tinggal'},
        {'kanji': '待', 'onyomi': 'tai', 'kunyomi': 'matsu', 'arti': 'menunggu'},
        {'kanji': '止', 'onyomi': 'shi', 'kunyomi': 'tomeru', 'arti': 'berhenti'}
    ],
    'benda': [
        {'kanji': '図', 'onyomi': 'zu', 'kunyomi': 'e', 'arti': 'gambar, diagram'},
        {'kanji': '鍵', 'onyomi': 'ken', 'kunyomi': 'kagi', 'arti': 'kunci'},
        {'kanji': '袋', 'onyomi': 'tai, taku', 'kunyomi': 'fukuro', 'arti': 'tas, kantong'},
        {'kanji': '通', 'onyomi': 'tsuu', 'kunyomi': 'tooru, tooshite', 'arti': 'melalui'},
        {'kanji': '環', 'onyomi': 'kan', 'kunyomi': 'wa', 'arti': 'lingkaran, lingkungan'},
        {'kanji': '運転', 'onyomi': 'unten', 'kunyomi': '', 'arti': 'mengemudi'},
        {'kanji': '洗', 'onyomi': 'sen', 'kunyomi': 'arau', 'arti': 'mencuci'}
    ],
    'waktu': [
        {'kanji': '年', 'onyomi': 'nen', 'kunyomi': 'toshi', 'arti': 'tahun'},
        {'kanji': '月', 'onyomi': 'getsu, gatsu', 'kunyomi': 'tsuki', 'arti': 'bulan'},
        {'kanji': '日', 'onyomi': 'nichi, jitsu', 'kunyomi': 'hi, ka', 'arti': 'hari, matahari'},
        {'kanji': '週', 'onyomi': 'shuu', 'kunyomi': '', 'arti': 'minggu'},
        {'kanji': '分', 'onyomi': 'bun, fun', 'kunyomi': 'wa', 'arti': 'menit, bagi'},
        {'kanji': '時', 'onyomi': 'ji', 'kunyomi': 'toki', 'arti': 'waktu, jam'},
        {'kanji': '午', 'onyomi': 'go', 'kunyomi': '', 'arti': 'siang'},
        {'kanji': '朝', 'onyomi': 'chou', 'kunyomi': 'asa', 'arti': 'pagi'}
    ],
    'sifat': [
        {'kanji': '明', 'onyomi': 'mei', 'kunyomi': 'akarui', 'arti': 'terang, cerah'},
        {'kanji': '暗', 'onyomi': 'an', 'kunyomi': 'kurai', 'arti': 'gelap'},
        {'kanji': '高', 'onyomi': 'kou', 'kunyomi': 'takai', 'arti': 'tinggi'},
        {'kanji': '低', 'onyomi': 'tei', 'kunyomi': 'hikui', 'arti': 'rendah'},
        {'kanji': '強', 'onyomi': 'kyou, gou', 'kunyomi': 'tsuyoi', 'arti': 'kuat'},
        {'kanji': '弱', 'onyomi': 'jaku', 'kunyomi': 'yowai', 'arti': 'lemah'},
        {'kanji': '広', 'onyomi': 'kou', 'kunyomi': 'hiro', 'arti': 'luas'}
    ],
    'warna': [
        {'kanji': '青', 'onyomi': 'sei', 'kunyomi': 'ao', 'arti': 'biru'},
        {'kanji': '赤', 'onyomi': 'seki', 'kunyomi': 'aka', 'arti': 'merah'},
        {'kanji': '白', 'onyomi': 'haku', 'kunyomi': 'shiro', 'arti': 'putih'},
        {'kanji': '黒', 'onyomi': 'koku', 'kunyomi': 'kuro', 'arti': 'hitam'},
        {'kanji': '茶', 'onyomi': 'cha', 'kunyomi': '', 'arti': 'cokelat'}
    ]
}

kanji_n2 = {
    'kata kerja': [
        {'kanji': '理解', 'onyomi': 'rikai', 'kunyomi': '', 'arti': 'memahami'},
        {'kanji': '結婚', 'onyomi': 'kekkon', 'kunyomi': '', 'arti': 'pernikahan'},
        {'kanji': '送', 'onyomi': 'sou', 'kunyomi': 'okuru', 'arti': 'mengirim'},
        {'kanji': '達', 'onyomi': 'tatsu', 'kunyomi': '', 'arti': 'mencapai'},
        {'kanji': '許', 'onyomi': 'kyo', 'kunyomi': 'yurusu', 'arti': 'mengizinkan'}
    ],
    'benda': [
        {'kanji': '戦争', 'onyomi': 'sensou', 'kunyomi': '', 'arti': 'perang'},
        {'kanji': '都市', 'onyomi': 'toshi', 'kunyomi': '', 'arti': 'kota'},
        {'kanji': '法律', 'onyomi': 'houritsu', 'kunyomi': '', 'arti': 'hukum'},
        {'kanji': '風景', 'onyomi': 'fuukei', 'kunyomi': '', 'arti': 'pemandangan'},
        {'kanji': '部屋', 'onyomi': 'heya', 'kunyomi': '', 'arti': 'ruangan'}
    ],
    'waktu': [
        {'kanji': '未来', 'onyomi': 'mirai', 'kunyomi': '', 'arti': 'masa depan'},
        {'kanji': '時間', 'onyomi': 'jikan', 'kunyomi': '', 'arti': 'waktu'},
        {'kanji': '永遠', 'onyomi': 'eien', 'kunyomi': '', 'arti': 'selamanya'},
        {'kanji': '今度', 'onyomi': 'kondo', 'kunyomi': '', 'arti': 'lain waktu'},
        {'kanji': '歴史', 'onyomi': 'rekishi', 'kunyomi': '', 'arti': 'sejarah'}
    ],
    'sifat': [
        {'kanji': '優しい', 'onyomi': 'yuu', 'kunyomi': 'yasashii', 'arti': 'baik, lembut'},
        {'kanji': '恐ろしい', 'onyomi': 'kyo', 'kunyomi': 'osoroshii', 'arti': 'menakutkan'},
        {'kanji': '明確', 'onyomi': 'meikaku', 'kunyomi': '', 'arti': 'jelas'},
        {'kanji': '深い', 'onyomi': 'shin', 'kunyomi': 'fukai', 'arti': 'dalam'},
        {'kanji': '確実', 'onyomi': 'kakujitsu', 'kunyomi': '', 'arti': 'pasti'}
    ]
}

kanji_n1 = {
    'kata kerja': [
        {'kanji': '改善', 'onyomi': 'kaizen', 'kunyomi': '', 'arti': 'perbaikan'},
        {'kanji': '維持', 'onyomi': 'iji', 'kunyomi': '', 'arti': 'pemeliharaan'},
        {'kanji': '承知', 'onyomi': 'shouchi', 'kunyomi': 'shiru', 'arti': 'menerima'},
        {'kanji': '観察', 'onyomi': 'kansatsu', 'kunyomi': '', 'arti': 'mengamati'},
        {'kanji': '選択', 'onyomi': 'sentaku', 'kunyomi': '', 'arti': 'memilih'}
    ],
    'benda': [
        {'kanji': '領土', 'onyomi': 'ryoudou', 'kunyomi': '', 'arti': 'wilayah'},
        {'kanji': '物理', 'onyomi': 'butsuri', 'kunyomi': '', 'arti': 'fisika'},
        {'kanji': '優秀', 'onyomi': 'yuushuu', 'kunyomi': '', 'arti': 'unggul'},
        {'kanji': '文化', 'onyomi': 'bunka', 'kunyomi': '', 'arti': 'budaya'},
        {'kanji': '命令', 'onyomi': 'meirei', 'kunyomi': '', 'arti': 'perintah'}
    ],
    'waktu': [
        {'kanji': '時間帯', 'onyomi': 'jikantai', 'kunyomi': '', 'arti': 'waktu tertentu'},
        {'kanji': '瞬間', 'onyomi': 'shunkan', 'kunyomi': '', 'arti': 'momen'},
        {'kanji': '年代', 'onyomi': 'nendai', 'kunyomi': '', 'arti': 'periode, dekade'},
        {'kanji': '即時', 'onyomi': 'sokuji', 'kunyomi': '', 'arti': 'segera'},
        {'kanji': '長期', 'onyomi': 'chouki', 'kunyomi': '', 'arti': 'jangka panjang'}
    ],
    'sifat': [
        {'kanji': '自信', 'onyomi': 'jishin', 'kunyomi': '', 'arti': 'percaya diri'},
        {'kanji': '的確', 'onyomi': 'tekikaku', 'kunyomi': '', 'arti': 'tepat'},
        {'kanji': '意義', 'onyomi': 'igi', 'kunyomi': '', 'arti': 'makna'},
        {'kanji': '進歩', 'onyomi': 'shinpo', 'kunyomi': '', 'arti': 'kemajuan'},
        {'kanji': '徹底', 'onyomi': 'tettei', 'kunyomi': '', 'arti': 'penyelesaian menyeluruh'}
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
        print(f"Huruf: {romaji} - {kana}")
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
        print(f"Huruf: {romaji} - {h_char} (Hiragana), {k_char} (Katakana)")
        input("Tekan Enter untuk melanjutkan...")

def choose_category(language_groups, is_random):
    while True:
        clear_screen()
        print("Masukkan salah satu kategori berikut:")
        print("[ a, ka, sa, ta, na, ha, ma, ya, ra, wa ]")
        print("\nKetik 'q' untuk kembali")
        group = input("Masukkan kategori: ").strip().lower()
        if group in ["q"]:
            return
        display_group(group, language_groups, is_random)

def choose_category_hk(is_random):
    while True:
        clear_screen()
        print("Masukkan salah satu kategori berikut:")
        print("[ a, ka, sa, ta, na, ha, ma, ya, ra, wa ]")
        print("\nKetik 'q' untuk kembali")
        group = input("Masukkan kategori: ").strip().lower()
        if group in ["q"]:
            return
        display_group_hk(group, is_random)

kanji_levels = {
    'N5': kanji_n5,
    'N4': kanji_n4,
    'N3': kanji_n3,
    'N2': kanji_n2,
    'N1': kanji_n1,
}


def tampilkan_kanji():
    while True:
        clear_screen()
        print("\n=== Pilih Level Kanji ===")
        print("1. N5")
        print("2. N4")
        print("3. N3")
        print("4. N2")
        print("5. N1")
        print("0. Kembali")

        try:
            pilihan_level = int(input("\nPilih level (0-5): ").strip())
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue

        if pilihan_level == 0:
            return  # Kembali ke menu utama
        elif 1 <= pilihan_level <= 5:
            # Mengambil level sesuai pilihan: N5 untuk pilihan 1, N4 untuk 2, dll
            level_terpilih = f'N{6 - pilihan_level}'
            kanji_terpilih = kanji_levels.get(level_terpilih)

            if kanji_terpilih is None:
                print(f"Data untuk level {level_terpilih} tidak ditemukan.")
                continue
        else:
            print("Pilihan tidak valid.")
            continue

        kategori_set = list(kanji_terpilih.keys())  # Mengambil kategori unik
        for idx, kategori in enumerate(kategori_set, 1):
            print(f"{idx}. {kategori}")
        print(f"{len(kategori_set) + 1}. Tampilkan Semua")
        print("0. Kembali")

        try:
            pilihan_kategori = int(input("\nPilih kategori (0-{}): ".format(len(kategori_set) + 1)).strip())
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue

        if pilihan_kategori == 0:
            break
        elif 1 <= pilihan_kategori <= len(kategori_set):
            kategori_terpilih = kategori_set[pilihan_kategori - 1]
            kanji_terpilih_kategori = kanji_terpilih[kategori_terpilih]
        elif pilihan_kategori == len(kategori_set) + 1:
            kategori_terpilih = "Semua"
            kanji_terpilih_kategori = [kanji_item for items in kanji_terpilih.values() for kanji_item in items]
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
            hasil = kanji_terpilih_kategori
        elif opsi_tampil == 2:
            hasil = random.sample(kanji_terpilih_kategori, len(kanji_terpilih_kategori))
        else:
            print("Pilihan tidak valid.")
            continue

        # Menampilkan hasil satu persatu
        for kanji in hasil:
            clear_screen()
            print(f"Kanji: {kanji['kanji']}")
            print(f"Onyomi: {kanji['onyomi']}")
            print(f"Kunyomi: {kanji['kunyomi']}")
            print(f"Arti: {kanji['arti']}")
            stop = input("\nTekan Enter untuk lanjut atau ketik 'q' untuk berhenti: ")
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
            tampilkan_kanji()  # Akan kembali ke menu utama jika memilih '0' di dalam fungsi ini
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
