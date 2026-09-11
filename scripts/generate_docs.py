import os
import yaml
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

import docx
from docx.shared import Inches as DocxInches, Pt as DocxPt, RGBColor as DocxRGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

os.makedirs('docs/presentation', exist_ok=True)
os.makedirs('docs/printables', exist_ok=True)
os.makedirs('slides', exist_ok=True)

with open('_data/curriculum.yml', 'r', encoding='utf-8') as f:
    curriculum = yaml.safe_load(f)

with open('_data/survey.yml', 'r', encoding='utf-8') as f:
    survey = yaml.safe_load(f)

with open('_config.yml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

print("Data loaded successfully.")
print("Total slides:", len(curriculum.get('presentation_slides', {}).get('slides', [])))

event_meta = config.get('event', {})

# ==========================================
# 1. GENERATE PPTX (16 SLIDES)
# ==========================================
print("--- Generating Presentation (PPTX) ---")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Colors
C_MAROON = RGBColor(122, 28, 48)     # #7A1C30 UTM Crimson Maroon
C_DEEP_MAROON = RGBColor(74, 14, 28) # #4A0E1C
C_NAVY = RGBColor(19, 34, 56)        # #132238 Midnight Navy
C_DARK_BG = RGBColor(15, 23, 42)     # #0F172A Dark Slate BG
C_CARD_BG = RGBColor(27, 38, 59)     # #1B263B Card BG
C_GOLD = RGBColor(197, 168, 128)     # #C5A880 Champagne Gold
C_LIGHT_GOLD = RGBColor(223, 186, 142) # #DFBA8E
C_WHITE = RGBColor(255, 255, 255)
C_OFF_WHITE = RGBColor(241, 245, 249)
C_MUTED = RGBColor(148, 163, 184)
C_GREEN = RGBColor(13, 130, 73)      # ASDAF Green

slides_data = curriculum.get('presentation_slides', {}).get('slides', [])

slide_content_details = {
    1: {
        "badge": "MAJLIS PEMBUKAAN & ALU-ALUAN",
        "subtitle": "Bengkel Santai • Literasi Teknologi & Kesedaran Kecerdasan Buatan (AI)",
        "highlights": [
            "Anjuran: Universiti Teknologi Malaysia (UTM KL) & ASDAF PERKIM",
            "Tarikh: Sabtu, 12 September 2026 (8:30 AM – 12:00 PM)",
            "Penceramah Utama: Muhamad Arif bin Johar (DevOps Engineer | UTM)",
            "Sasaran: 46 Pelajar ASDAF (T1–T5 & PPKI) bersama 13 Kru UTM"
        ],
        "card_title": "Objektif Utama Bengkel",
        "card_body": [
            "Membuka minda pelajar mengenai potensi sebenar teknologi dan AI.",
            "Mendedahkan kemahiran keselamatan siber & formula 3T lawan scam.",
            "Membina keyakinan diri melalui amali kertas mahjong & kuiz santai.",
            "Menyemai aspirasi kerjaya digital masa depan untuk anak ASDAF."
        ]
    },
    2: {
        "badge": "PENGENALAN PASUKAN UTM",
        "subtitle": "Mengenali Abang & Kakak Mentor Sepanjang Program",
        "highlights": [
            "13 Mahasiswa & Fasilitator Fakulti Komputeran UTM Kuala Lumpur",
            "7 Meja Kluster: Setiap meja dibimbing oleh Abang/Kakak Mentor khusus",
            "Pendekatan Mesra: Pembelajaran santai, tiada tekanan peperiksaan",
            "Sedia Membantu: Bimbingan amali, perbincangan idea & sokongan PPKI"
        ],
        "card_title": "Peranan Abang & Kakak Mentor",
        "card_body": [
            "Fasilitator Meja: Memandu sesi ice-breaking dan perbincangan modul.",
            "Mentor Startup Sprint: Membantu lakaran poster 4 Kotak Emas.",
            "Inklusiviti PPKI: Sokongan khusus untuk rakan Pendidikan Khas.",
            "Rakan Inspirasi: Berkongsi tip belajar dan peluang sambung belajar di IPT."
        ]
    },
    3: {
        "badge": "MODUL 1: ASAS AI",
        "subtitle": "Membezakan Fiksyen Filem vs Realiti Teknologi Sebenar",
        "highlights": [
            "AI BUKAN robot pemusnah atau magik misteri!",
            "AI ialah algoritma komputer yang belajar daripada ribuan data contoh.",
            "AI menganalisis corak (patterns) untuk menyelesaikan tugasan manusia.",
            "Ia berfungsi sebagai 'Pembantu Pintar' yang mempercepatkan kerja kita."
        ],
        "card_title": "Contoh AI di Sekeliling Kita",
        "card_body": [
            "Google Maps / Waze: Mengira laluan terpantas elak kesesakan jalan.",
            "YouTube / TikTok: Mencadangkan video mengikut minat tontonan anda.",
            "Pengecaman Wajah (Face Unlock): Membuka kunci telefon dengan selamat.",
            "Carian Google: Memahami maksud soalan walaupun tersilap ejaan."
        ]
    },
    4: {
        "badge": "MODUL 1: BAGAIMANA AI BERFIKIR",
        "subtitle": "Kecerdasan Mesin: Pembelajaran Melalui Data & Corak",
        "highlights": [
            "Komputer tidak melihat gambar seperti mata manusia.",
            "Komputer menukar gambar menjadi jutaan nombor piksel.",
            "Melalui 10,000+ contoh gambar kucing vs anjing, AI belajar:",
            "  - Bentuk telinga tajam vs telinga labuh",
            "  - Corak misai, hidung, dan tekstur bulu"
        ],
        "card_title": "Ujian Minda Dewan: Kucing vs Anjing Muffin",
        "card_body": [
            "Bolehkah komputer keliru antara muffin coklat dan muka anjing chihuahua?",
            "Ya! Komputer perlukan latihan data yang tepat dan banyak.",
            "Kelebihan Manusia: Kita mempunyai akal, logik, dan empati semula jadi.",
            "AI hebat memproses nombor, tetapi manusia yang memberi arahan bijak!"
        ]
    },
    5: {
        "badge": "MODUL 1: DEMO LANGSUNG AI",
        "subtitle": "Demonstrasi ChatGPT / Gemini Menjana Kreativiti Bahasa",
        "highlights": [
            "AI Generatif Bahasa: Memahami ayat dan membina respon bermakna.",
            "Eksperimen Dewan: Menjana Pantun Empat Kerat spontan di layar!",
            "Prompt Interaktif: 'Tulis pantun semangat anak ASDAF Bukit Persekutuan'.",
            "Keajaiban Prompting: Ketepatan hasil bergantung kepada arahan kita."
        ],
        "card_title": "Formula Prompt Pintar (A-T-G)",
        "card_body": [
            "A - Andaian Peranan: 'Bertindak sebagai guru sastera kreatif...'",
            "T - Tugasan Jelas: 'Tulis 2 rangkap pantun nasihat belajar rajin...'",
            "G - Gaya & Nada: 'Gunakan bahasa Melayu yang indah dan penuh semangat.'",
            "AI bertindak mengikut konteks yang kita tetapkan!"
        ]
    },
    6: {
        "badge": "MODUL 1: DEMO VISUAL AI",
        "subtitle": "Dari Teks Menjadi Seni Digital (Text-to-Image Generation)",
        "highlights": [
            "Canva Magic Media / DALL-E / Bing Image Creator.",
            "Komputer melukis piksel demi piksel berdasarkan huraian perkataan.",
            "Eksperimen Liar Meja: 'Harimau Malaya jersi UTM di stesen angkasa'.",
            "Hasil visual 4K dipaparkan dalam masa kurang 10 saat!"
        ],
        "card_title": "Aplikasi Kreatif Seni AI",
        "card_body": [
            "Membantu mereka bentuk poster acara dan logo kelab sekolah.",
            "Menghidupkan watak animasi dan komik ciptaan sendiri.",
            "Menzahirkan idea projek sebelum prototaip sebenar dibina.",
            "Peringatan: Gunakan imej AI secara beretika, jangan cipta bahan palsu."
        ]
    },
    7: {
        "badge": "MODUL 1: APLIKASI HARIAN PELAJAR",
        "subtitle": "AI Sebagai Rakan Belajar & Guru Tuisyen Peribadi",
        "highlights": [
            "Menerangkan formula Matematik & Sains yang rumit langkah demi langkah.",
            "Menyemak tatabahasa & kosa kata Bahasa Inggeris / Bahasa Melayu.",
            "Membantu menyusun jadual ulang kaji harian menjelang peperiksaan SPM/PT3.",
            "Menjawab soalan tanpa rasa segan atau takut dimarahi."
        ],
        "card_title": "Integriti Akademik: AI Bukan Alat Menipu!",
        "card_body": [
            "GUNAKAN AI UNTUK: Memahami konsep, mencari idea, latihan soalan.",
            "JANGAN GUNA UNTUK: Salin bulat-bulat kerja sekolah tanpa berfikir.",
            "Otak manusia adalah aset paling berharga — latih otak berfikir kritis.",
            "Kejujuran ilmu membawa keberkatan masa depan."
        ]
    },
    8: {
        "badge": "MODUL 1: KERJAYA & MASA DEPAN",
        "subtitle": "Peluang Hebat Bidang Digital Menanti Anak ASDAF",
        "highlights": [
            "Bakat teknologi tidak mengenal latar belakang atau tempat tinggal!",
            "Sesiapa yang mempunyai rasa ingin tahu tinggi boleh berjaya.",
            "Permintaan pasaran kerja terhadap pakar digital semakin melonjak.",
            "Gaji lumayan, fleksibiliti kerja, dan peluang membanggakan keluarga."
        ],
        "card_title": "5 Ikon Kerjaya Digital Masa Depan",
        "card_body": [
            "1. Pereka Permainan Digital (Game Developer & Animator)",
            "2. Jurutera Kecerdasan Buatan (AI & Machine Learning Engineer)",
            "3. Penganalisis Keselamatan Siber (Cyber Security Defender)",
            "4. Jurutera Dron & Robotik Pertanian Pintar",
            "5. Pembangun Aplikasi Web & Cloud DevOps Engineer"
        ]
    },
    9: {
        "badge": "MODUL 2: KESELAMATAN SIBER",
        "subtitle": "Bahaya Scam, Pancingan Data (Phishing) & Perangkap Maya",
        "highlights": [
            "Internet menawarkan ilmu, tetapi ada pemangsa mengintai mangsa.",
            "Scam Kejutan Hadiah: 'Tahniah! Anda menang RM10,000 dari Shopee'.",
            "Phishing Pautan Palsu: Web tiruan menyerupai bank atau media sosial.",
            "Umpan Tawaran Percuma: Topup percuma, diamond game percuma."
        ],
        "card_title": "Taktik Licik Penjenayah Siber",
        "card_body": [
            "Mewujudkan rasa cemas: 'Akaun anda akan disekat dalam 5 minit!'.",
            "Mewujudkan sifat tamak: Menjanjikan pulangan wang berganda tanpa usaha.",
            "Menyamar sebagai pihak berkuasa: Polis, mahkamah, LHDN, atau cikgu.",
            "Matlamat mereka: Mencuri nombor OTP, kata laluan, dan data peribadi."
        ]
    },
    10: {
        "badge": "MODUL 2: FORMULA PERTAHANAN DIRI",
        "subtitle": "Formula Emas 3T: Senjata Kebal Melawan Scammer",
        "highlights": [
            "T1: TIDAK PASTI — Jangan cepat percaya mesej atau pemanggil misteri.",
            "T2: TIDAK KONGSI — Jangan sesekali beri kata laluan, nombor IC, atau OTP.",
            "T3: TIDAK KLIK — Jangan tekan pautan biru yang mencurigakan di WhatsApp.",
            "Hafal Talian Kecemasan Scam Kebangsaan: 997 (NSRC)!"
        ],
        "card_title": "Tindakan Pantas Jika Terkena Scam",
        "card_body": [
            "1. Jangan panik — bertenang dan maklumkan segera kepada warden/guru.",
            "2. Hubungi talian 997 NSRC (Pusat Respons Scam Kebangsaan) dalam 24 jam.",
            "3. Tukar semua kata laluan akaun media sosial dan e-mel serta-merta.",
            "4. Buat laporan polis bersama penjaga untuk tindakan pembekuan akaun."
        ]
    },
    11: {
        "badge": "MODUL 2: KESELAMATAN AKAUN",
        "subtitle": "Rahsia Kata Laluan Kebal: Password vs Passphrase",
        "highlights": [
            "Kata Laluan Lemah: 'kucing123', 'asdaf2026', '12345678', tarikh lahir.",
            "Penggodam boleh memecahkan kata laluan lemah dalam masa kurang 3 saat!",
            "Konsep Passphrase: Gabungkan 3-4 perkataan rawak menjadi satu frasa.",
            "Contoh: 'HarimauLompatPagar99!' — Ambil masa 10,000 tahun untuk dipecah!"
        ],
        "card_title": "4 Pantang Larang Kata Laluan",
        "card_body": [
            "1. Jangan guna kata laluan yang sama untuk semua akaun.",
            "2. Jangan simpan kata laluan di dalam kertas terbuka atau chat WhatsApp.",
            "3. Aktifkan Pengesahan 2-Faktor (2FA) di Instagram, TikTok, dan Google.",
            "4. Log keluar (Log Out) akaun jika menggunakan komputer sekolah/makmal."
        ]
    },
    12: {
        "badge": "MODUL 2: ETIKA & REPUTASI DIGITAL",
        "subtitle": "Jejak Digital (Digital Footprint): Internet Tidak Pernah Lupa!",
        "highlights": [
            "Setiap gambar, komen, carian, dan muat naik meninggalkan jejak kekal.",
            "Walaupun dipadam (delete), orang lain mungkin sudah mengambil screenshot.",
            "Jejak digital membentuk reputasi anda di mata masyarakat dan majikan.",
            "Komen toksik & buli siber boleh memusnahkan masa depan orang lain dan diri sendiri."
        ],
        "card_title": "Prinsip Emas Sebelum Menekan 'Post' (T-H-I-N-K)",
        "card_body": [
            "T - Benarkah maklumat ini? (True)",
            "H - Adakah ia membantu orang lain? (Helpful)",
            "I - Adakah ia memberi inspirasi? (Inspiring)",
            "N - Adakah ia benar-benar perlu dikongsi? (Necessary)",
            "K - Adakah ayat ini baik dan berbudi bahasa? (Kind)"
        ]
    },
    13: {
        "badge": "MODUL 2: AMALI MEJA KLUSTER",
        "subtitle": "Bengkel Startup Sprint: Menjadi Pencipta Inovasi Teknologi",
        "highlights": [
            "7 Meja Kluster bertukar menjadi 7 'Syarikat Pemula Teknologi' (Startups)!",
            "Bahan Disediakan: Kertas mahjong, marker pelbagai warna, sticky notes.",
            "Misi Meja: Cipta 1 idea penyelesaian berasaskan teknologi/AI untuk ASDAF.",
            "Kolaborasi: Pelajar T1–T5 dan rakan PPKI berganding bahu menghasilkan idea."
        ],
        "card_title": "Contoh Tema Idea Inovasi Meja",
        "card_body": [
            "Meja 1 & 2: 'Sistem Pengesan Makanan Membazir Pintar di Dewan Makan'.",
            "Meja 3 & 4: 'AI Jadual Ulang Kaji & Peringatan Waktu Solat Asrama'.",
            "Meja 5 & 6: 'Aplikasi Pustakawan Digital Pintar ASDAF'.",
            "Meja 7: 'Sistem Keselamatan Pagar Asrama Menggunakan Pengecaman AI'."
        ]
    },
    14: {
        "badge": "MODUL 2: PANDUAN PEMBENTANGAN",
        "subtitle": "Format Kertas Mahjong: 4 Kotak Emas Inovasi",
        "highlights": [
            "Bahagikan kertas mahjong kepada 4 ruangan yang jelas dan berwarna-warni.",
            "Lukis logo syarikat dan guna kata kunci ringkas (bullet points).",
            "Setiap meja memilih 2 orang jurucakap untuk membentang di hadapan dewan.",
            "Masa Pitching: 2 Minit setiap meja — padat, meyakinkan dan bertenaga!"
        ],
        "card_title": "Struktur 4 Kotak Emas Pada Poster",
        "card_body": [
            "Kotak 1: Nama Inovasi & Ciptaan Logo Kumpulan.",
            "Kotak 2: Masalah Sebenar Yang Dihadapi di Asrama / Sekolah.",
            "Kotak 3: Cara Inovasi AI Berfungsi (Rajah aliran ringkas).",
            "Kotak 4: Kebaikan & Impak Positif Kepada Rakan-Rakan ASDAF."
        ]
    },
    15: {
        "badge": "CABARAN INTERAKTIF DEWAN",
        "subtitle": "Fast-Answer Tech Showdown: Kuiz Pantas Tanpa Gajet!",
        "highlights": [
            "Mekanik Sifar Gajet (Zero-Device): Tiada telefon pintar diperlukan!",
            "Soalan dipaparkan di layar skrin dewan secara bergilir-gilir.",
            "Mekanik Pantas: '3... 2... 1... ANGKAT TANGAN!'.",
            "Kategori Hadiah: Hamper Kumpulan, Hadiah Misteri Individu & Snek Ceria."
        ],
        "card_title": "5 Soalan Kuiz Hangat",
        "card_body": [
            "S1: AI bermaksud... (Jawapan: Artificial Intelligence / Kecerdasan Buatan)",
            "S2: Mesej 'Menang RM10,000 dari Shopee' dinamakan... (Jawapan: Scam / Phishing)",
            "S3: Formula 3T keselamatan siber... (Jawapan: Tidak Pasti, Tidak Kongsi, Tidak Klik)",
            "S4: Kata laluan paling selamat... (Jawapan: Passphrase gabungan perkataan)",
            "S5: Talian kecemasan scam NSRC... (Jawapan: 997)"
        ]
    },
    16: {
        "badge": "SESI PENUTUP & PENGHARGAAN",
        "subtitle": "Masa Depan Bermula Hari Ini: Terima Kasih Warga ASDAF PERKIM",
        "highlights": [
            "Pengisian Borang Soal Selidik Pasca-Program (Bahagian 2 & Komen).",
            "Penyampaian Hadiah Juara Startup Sprint & Pemenang Kuiz Dewan.",
            "Penyerahan Cenderamata Rasmi UTM kepada Pengurusan ASDAF.",
            "Sesi Jamuan Makan Tengah Hari & Bergambar Kenangan Bersama."
        ],
        "card_title": "Mesej Inspirasi Abang & Kakak UTM",
        "card_body": [
            "“Anak-anak ASDAF adalah generasi peneraju masa hadapan negara.”",
            "“Jangan pernah biarkan keterbatasan hari ini menghalang cita-cita besar.”",
            "“Kuasai teknologi, pelihara adab, dan terus melangkah dengan yakin!”",
            "Jumpa lagi di menara gading Universiti Teknologi Malaysia!"
        ]
    }
}

for item in slides_data:
    s_num = item['slide_no']
    slide = prs.slides.add_slide(blank_layout)
    
    # Background rectangle
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg_shape.line.fill.background()
    
    if s_num == 1:
        # Title slide background: Dark Navy with Maroon header accent
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = C_DARK_BG
        
        # Top banner accent
        top_accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.4))
        top_accent.fill.solid()
        top_accent.fill.fore_color.rgb = C_MAROON
        top_accent.line.fill.background()
        
        # Gold strip below
        gold_strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(0.4), Inches(13.333), Inches(0.08))
        gold_strip.fill.solid()
        gold_strip.fill.fore_color.rgb = C_GOLD
        gold_strip.line.fill.background()

        # Title Box
        txBox = slide.shapes.add_textbox(Inches(1.0), Inches(0.9), Inches(11.333), Inches(2.2))
        tf = txBox.text_frame
        tf.word_wrap = True
        
        p_badge = tf.paragraphs[0]
        p_badge.text = "PROGRAM KOMUNITI SISWAZAH UTM KL x ASDAF PERKIM"
        p_badge.font.size = Pt(14)
        p_badge.font.bold = True
        p_badge.font.color.rgb = C_GOLD
        p_badge.space_after = Pt(10)
        
        p_title = tf.add_paragraph()
        p_title.text = "BENGKEL SANTAI NEXTGEN CELIK DIGITAL 2026"
        p_title.font.size = Pt(32)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE
        p_title.space_after = Pt(8)
        
        p_theme = tf.add_paragraph()
        p_theme.text = "LITERASI TEKNOLOGI & KECERDASAN BUATAN (AI)"
        p_theme.font.size = Pt(20)
        p_theme.font.bold = True
        p_theme.font.color.rgb = C_LIGHT_GOLD
        
        # Left info card
        card1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(3.4), Inches(5.4), Inches(3.3))
        card1.fill.solid()
        card1.fill.fore_color.rgb = C_CARD_BG
        card1.line.color.rgb = C_MAROON
        card1.line.width = Pt(1.5)
        
        tf1 = card1.text_frame
        tf1.word_wrap = True
        tf1.margin_left = Inches(0.3)
        tf1.margin_right = Inches(0.3)
        tf1.margin_top = Inches(0.25)
        
        p1_hdr = tf1.paragraphs[0]
        p1_hdr.text = "MAKLUMAT SESI SEMINAR"
        p1_hdr.font.size = Pt(15)
        p1_hdr.font.bold = True
        p1_hdr.font.color.rgb = C_GOLD
        p1_hdr.space_after = Pt(10)
        
        for pt in slide_content_details[1]["highlights"]:
            p = tf1.add_paragraph()
            p.text = "• " + pt
            p.font.size = Pt(12)
            p.font.color.rgb = C_OFF_WHITE
            p.space_after = Pt(6)

        # Right info card
        card2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(3.4), Inches(5.4), Inches(3.3))
        card2.fill.solid()
        card2.fill.fore_color.rgb = C_CARD_BG
        card2.line.color.rgb = C_GOLD
        card2.line.width = Pt(1.5)
        
        tf2 = card2.text_frame
        tf2.word_wrap = True
        tf2.margin_left = Inches(0.3)
        tf2.margin_right = Inches(0.3)
        tf2.margin_top = Inches(0.25)
        
        p2_hdr = tf2.paragraphs[0]
        p2_hdr.text = slide_content_details[1]["card_title"].upper()
        p2_hdr.font.size = Pt(15)
        p2_hdr.font.bold = True
        p2_hdr.font.color.rgb = C_GOLD
        p2_hdr.space_after = Pt(10)
        
        for pt in slide_content_details[1]["card_body"]:
            p = tf2.add_paragraph()
            p.text = "✔ " + pt
            p.font.size = Pt(12)
            p.font.color.rgb = C_OFF_WHITE
            p.space_after = Pt(6)

    else:
        # Standard Slides (2 to 16)
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = C_DARK_BG
        
        # Header strip background
        hdr_bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.3))
        hdr_bg.fill.solid()
        hdr_bg.fill.fore_color.rgb = C_NAVY
        hdr_bg.line.fill.background()
        
        # Maroon top edge
        hdr_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.08))
        hdr_line.fill.solid()
        hdr_line.fill.fore_color.rgb = C_MAROON
        hdr_line.line.fill.background()

        # Gold bottom edge
        hdr_gold = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.3), Inches(13.333), Inches(0.05))
        hdr_gold.fill.solid()
        hdr_gold.fill.fore_color.rgb = C_GOLD
        hdr_gold.line.fill.background()
        
        details = slide_content_details.get(s_num, {
            "badge": item.get('section', 'MODUL PEMBELAJARAN').upper(),
            "subtitle": "NextGen Celik Digital 2026",
            "highlights": [item.get('visual', '')],
            "card_title": "Fokus Pembelajaran",
            "card_body": [item.get('speaker_notes', '')]
        })

        # Header Text Box
        tx_hdr = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.7), Inches(1.1))
        tf_h = tx_hdr.text_frame
        tf_h.word_wrap = True
        
        p_badge = tf_h.paragraphs[0]
        p_badge.text = f"SLAID {s_num:02d}  |  {details['badge']}"
        p_badge.font.size = Pt(11)
        p_badge.font.bold = True
        p_badge.font.color.rgb = C_GOLD
        p_badge.space_after = Pt(2)
        
        p_title = tf_h.add_paragraph()
        p_title.text = item['title']
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE
        
        p_sub = tf_h.add_paragraph()
        p_sub.text = details['subtitle']
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = C_MUTED
        
        # Left Content Card
        c_left = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.1))
        c_left.fill.solid()
        c_left.fill.fore_color.rgb = C_CARD_BG
        c_left.line.color.rgb = C_MAROON
        c_left.line.width = Pt(1.5)
        
        tf_left = c_left.text_frame
        tf_left.word_wrap = True
        tf_left.margin_left = Inches(0.35)
        tf_left.margin_right = Inches(0.35)
        tf_left.margin_top = Inches(0.3)
        
        p_lh = tf_left.paragraphs[0]
        p_lh.text = "POIN & KONSEP UTAMA"
        p_lh.font.size = Pt(15)
        p_lh.font.bold = True
        p_lh.font.color.rgb = C_GOLD
        p_lh.space_after = Pt(12)
        
        for hl in details["highlights"]:
            p = tf_left.add_paragraph()
            p.text = "• " + hl
            p.font.size = Pt(13)
            p.font.color.rgb = C_OFF_WHITE
            p.space_after = Pt(8)
            
        # Right Content Card
        c_right = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.1))
        c_right.fill.solid()
        c_right.fill.fore_color.rgb = C_GOLD
        c_right.line.color.rgb = C_GOLD
        c_right.line.width = Pt(1.5)
        
        tf_right = c_right.text_frame
        tf_right.word_wrap = True
        tf_right.margin_left = Inches(0.35)
        tf_right.margin_right = Inches(0.35)
        tf_right.margin_top = Inches(0.3)
        
        p_rh = tf_right.paragraphs[0]
        p_rh.text = details["card_title"].upper()
        p_rh.font.size = Pt(15)
        p_rh.font.bold = True
        p_rh.font.color.rgb = C_LIGHT_GOLD
        p_rh.space_after = Pt(12)
        
        for bd in details["card_body"]:
            p = tf_right.add_paragraph()
            p.text = "✔ " + bd
            p.font.size = Pt(12.5)
            p.font.color.rgb = C_OFF_WHITE
            p.space_after = Pt(8)
            
        # Footer
        tx_ft = slide.shapes.add_textbox(Inches(0.8), Inches(6.85), Inches(11.7), Inches(0.45))
        tf_ft = tx_ft.text_frame
        p_ft = tf_ft.paragraphs[0]
        p_ft.text = f"NextGen Celik Digital 2026  •  UTM KL x ASDAF PERKIM  •  Sabtu, 12 September 2026                                                                    Slaid {s_num} / 16"
        p_ft.font.size = Pt(9.5)
        p_ft.font.color.rgb = C_MUTED
    
    # Set Speaker Notes
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = f"NOTA PENCERAMAH (SLAID {s_num}):\n" + item.get('speaker_notes', '')

# Save presentation
pptx_path1 = 'docs/presentation/Bengkel_Santai_NextGen_Celik_Digital_2026.pptx'
pptx_path2 = 'slides/Bengkel_Santai_NextGen_Celik_Digital_2026.pptx'
prs.save(pptx_path1)
prs.save(pptx_path2)
print(f"Saved PPTX successfully to:\n- {pptx_path1}\n- {pptx_path2}")


# ==========================================
# 2. GENERATE DOCX (PRE & POST SURVEY)
# ==========================================
print("\n--- Generating Survey Form (DOCX) ---")

doc = docx.Document()

# Page Setup: A4 Portrait, Narrow Margins (0.35 in top/bottom, 0.45 in left/right)
# to strictly guarantee 1 single page!
section = doc.sections[0]
section.page_width = DocxInches(8.27)
section.page_height = DocxInches(11.69)
section.top_margin = DocxInches(0.35)
section.bottom_margin = DocxInches(0.35)
section.left_margin = DocxInches(0.45)
section.right_margin = DocxInches(0.45)

# Color constants in Hex for docx XML
HEX_MAROON = "7A1C30"
HEX_LIGHT_MAROON = "F9EBEF"
HEX_NAVY = "132238"
HEX_LIGHT_NAVY = "EEF2F6"
HEX_GOLD = "C5A880"
HEX_LIGHT_GRAY = "F8F9FA"
HEX_BORDER = "CCCCCC"

def set_cell_shading(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=50, bottom=50, left=80, right=80):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m_type, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m_type}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, border_color="BBBBBB"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

# 1. Header Banner Table
hdr_table = doc.add_table(rows=1, cols=1)
hdr_table.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr_table.autofit = False
hdr_cell = hdr_table.cell(0, 0)
hdr_cell.width = DocxInches(7.37)
set_cell_shading(hdr_cell, HEX_MAROON)
set_cell_margins(hdr_cell, top=70, bottom=70, left=100, right=100)

p_h = hdr_cell.paragraphs[0]
p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_h.paragraph_format.space_before = DocxPt(0)
p_h.paragraph_format.space_after = DocxPt(1)

run_inst = p_h.add_run("UNIVERSITI TEKNOLOGI MALAYSIA (UTM KL)  ×  ASRAMA DARUL FALAH (ASDAF) PERKIM\n")
run_inst.font.name = "Arial"
run_inst.font.size = DocxPt(8.5)
run_inst.font.bold = True
run_inst.font.color.rgb = DocxRGBColor(245, 208, 169) # Gold tint

run_htitle = p_h.add_run("BORANG SOAL SELIDIK PRE & POST (1 HELAIAN LENGKAP)\n")
run_htitle.font.name = "Arial Black"
run_htitle.font.size = DocxPt(12)
run_htitle.font.bold = True
run_htitle.font.color.rgb = DocxRGBColor(255, 255, 255)

run_hsub = p_h.add_run("Bengkel Santai NextGen Celik Digital 2026: Literasi Teknologi & AI  •  Sabtu, 12 September 2026")
run_hsub.font.name = "Arial"
run_hsub.font.size = DocxPt(8)
run_hsub.font.color.rgb = DocxRGBColor(255, 255, 255)

# Student Metadata Table (3 columns: Nama, No. Meja, Tingkatan)
meta_table = doc.add_table(rows=1, cols=3)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(meta_table, border_color="DDDDDD")
col_widths = [DocxInches(4.17), DocxInches(1.5), DocxInches(1.7)]

meta_fields = [
    ("Nama / Kod:", "_________________________________"),
    ("No. Meja:", "Meja [   ]"),
    ("Tingkatan:", "[  ] T1-T5  [  ] PPKI")
]

for idx, (label, val) in enumerate(meta_fields):
    cell = meta_table.cell(0, idx)
    cell.width = col_widths[idx]
    set_cell_margins(cell, top=40, bottom=40, left=60, right=60)
    set_cell_shading(cell, HEX_LIGHT_GRAY)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = DocxPt(0)
    p.paragraph_format.space_after = DocxPt(0)
    r1 = p.add_run(f"{label} ")
    r1.font.name = "Arial"
    r1.font.bold = True
    r1.font.size = DocxPt(8.5)
    r1.font.color.rgb = DocxRGBColor(19, 34, 56)
    r2 = p.add_run(val)
    r2.font.name = "Arial"
    r2.font.size = DocxPt(8.5)

# Instruction & Scale Note
p_scale = doc.add_paragraph()
p_scale.paragraph_format.space_before = DocxPt(3)
p_scale.paragraph_format.space_after = DocxPt(2)
r_sc_lbl = p_scale.add_run("Skala Penilaian: ")
r_sc_lbl.font.name = "Arial"
r_sc_lbl.font.bold = True
r_sc_lbl.font.size = DocxPt(7.5)
r_sc_val = p_scale.add_run("1 = Sangat Tidak Setuju (STS)   |   2 = Tidak Setuju (TS)   |   3 = Neutral (N)   |   4 = Setuju (S)   |   5 = Sangat Setuju (SS)")
r_sc_val.font.name = "Arial"
r_sc_val.font.size = DocxPt(7.5)
r_sc_val.font.italic = True

# -------------------------------------------------------------
# Function to add Survey Section Table (Pre or Post)
# -------------------------------------------------------------
def add_survey_section(sec_data, is_pre=True):
    # Section Header Bar
    bar_tbl = doc.add_table(rows=1, cols=1)
    bar_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    b_cell = bar_tbl.cell(0, 0)
    b_cell.width = DocxInches(7.37)
    
    bg_color = HEX_MAROON if is_pre else HEX_NAVY
    set_cell_shading(b_cell, bg_color)
    set_cell_margins(b_cell, top=35, bottom=35, left=80, right=80)
    
    bp = b_cell.paragraphs[0]
    bp.paragraph_format.space_before = DocxPt(0)
    bp.paragraph_format.space_after = DocxPt(0)
    
    tag_run = bp.add_run(f"[{sec_data['tag']}: {sec_data['code']}] ")
    tag_run.font.name = "Arial"
    tag_run.font.bold = True
    tag_run.font.size = DocxPt(8.5)
    tag_run.font.color.rgb = DocxRGBColor(245, 208, 169)
    
    title_run = bp.add_run(sec_data['title'].upper())
    title_run.font.name = "Arial"
    title_run.font.bold = True
    title_run.font.size = DocxPt(8.5)
    title_run.font.color.rgb = DocxRGBColor(255, 255, 255)
    
    timing_run = bp.add_run(f"  •  ({sec_data['timing']})")
    timing_run.font.name = "Arial"
    timing_run.font.size = DocxPt(7.5)
    timing_run.font.italic = True
    timing_run.font.color.rgb = DocxRGBColor(220, 220, 220)

    # Questions Table: 7 columns (No, Kenyataan, 1, 2, 3, 4, 5)
    q_table = doc.add_table(rows=len(sec_data['questions']) + 1, cols=7)
    q_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(q_table, border_color="CCCCCC")
    
    q_widths = [DocxInches(0.35), DocxInches(4.52), DocxInches(0.5), DocxInches(0.5), DocxInches(0.5), DocxInches(0.5), DocxInches(0.5)]
    headers = ["No", "Kenyataan Soal Selidik", "1 (STS)", "2 (TS)", "3 (N)", "4 (S)", "5 (SS)"]
    
    # Header Row
    for col_idx, text in enumerate(headers):
        cell = q_table.cell(0, col_idx)
        cell.width = q_widths[col_idx]
        set_cell_margins(cell, top=30, bottom=30, left=40, right=40)
        set_cell_shading(cell, HEX_LIGHT_MAROON if is_pre else HEX_LIGHT_NAVY)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx != 1 else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = DocxPt(0)
        p.paragraph_format.space_after = DocxPt(0)
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.bold = True
        run.font.size = DocxPt(7.5)
        run.font.color.rgb = DocxRGBColor(122, 28, 48) if is_pre else DocxRGBColor(19, 34, 56)

    # Data Rows
    for row_idx, q in enumerate(sec_data['questions'], start=1):
        # Col 0: No
        c0 = q_table.cell(row_idx, 0)
        c0.width = q_widths[0]
        set_cell_margins(c0, top=25, bottom=25, left=30, right=30)
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.paragraph_format.space_before = DocxPt(0)
        p0.paragraph_format.space_after = DocxPt(0)
        r0 = p0.add_run(str(q['id']))
        r0.font.name = "Arial"
        r0.font.bold = True
        r0.font.size = DocxPt(7.5)
        
        # Col 1: Text
        c1 = q_table.cell(row_idx, 1)
        c1.width = q_widths[1]
        set_cell_margins(c1, top=25, bottom=25, left=40, right=40)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = DocxPt(0)
        p1.paragraph_format.space_after = DocxPt(0)
        r1 = p1.add_run(q['text'])
        r1.font.name = "Arial"
        r1.font.size = DocxPt(7.5)
        
        # Cols 2-6: Checkboxes [ ]
        for opt_idx in range(2, 7):
            c_opt = q_table.cell(row_idx, opt_idx)
            c_opt.width = q_widths[opt_idx]
            set_cell_margins(c_opt, top=25, bottom=25, left=20, right=20)
            p_opt = c_opt.paragraphs[0]
            p_opt.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_opt.paragraph_format.space_before = DocxPt(0)
            p_opt.paragraph_format.space_after = DocxPt(0)
            r_opt = p_opt.add_run("[   ]")
            r_opt.font.name = "Arial"
            r_opt.font.size = DocxPt(7.5)
            r_opt.font.color.rgb = DocxRGBColor(100, 116, 139)

    # Open Prompt / Comment Area
    op_table = doc.add_table(rows=1, cols=1)
    op_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    op_cell = op_table.cell(0, 0)
    op_cell.width = DocxInches(7.37)
    set_cell_margins(op_cell, top=35, bottom=35, left=60, right=60)
    set_cell_shading(op_cell, HEX_LIGHT_GRAY)
    
    op_p = op_cell.paragraphs[0]
    op_p.paragraph_format.space_before = DocxPt(0)
    op_p.paragraph_format.space_after = DocxPt(0)
    
    op_lbl = op_p.add_run(f"✎ {sec_data['open_prompt']}\n")
    op_lbl.font.name = "Arial"
    op_lbl.font.bold = True
    op_lbl.font.size = DocxPt(7.5)
    op_lbl.font.color.rgb = DocxRGBColor(19, 34, 56)
    
    if is_pre:
        op_lines = op_p.add_run("Jawapan: __________________________________________________________________________________________________")
    else:
        op_lines = op_p.add_run(
            "Baris 1: __________________________________________________________________________________________________\n"
            "Baris 2: __________________________________________________________________________________________________\n"
            "Baris 3: __________________________________________________________________________________________________"
        )
    op_lines.font.name = "Arial"
    op_lines.font.size = DocxPt(7)
    op_lines.font.color.rgb = DocxRGBColor(140, 140, 140)

# Add Pre-Survey
add_survey_section(survey['pre'], is_pre=True)

# Continuous Flow Divider (NO CUT / NO POTONG)
sep_table = doc.add_table(rows=1, cols=1)
sep_table.alignment = WD_TABLE_ALIGNMENT.CENTER
sep_cell = sep_table.cell(0, 0)
sep_cell.width = DocxInches(7.37)
set_cell_shading(sep_cell, "F1F5F9")
set_cell_margins(sep_cell, top=25, bottom=25, left=60, right=60)

sp = sep_cell.paragraphs[0]
sp.alignment = WD_ALIGN_PARAGRAPH.CENTER
sp.paragraph_format.space_before = DocxPt(0)
sp.paragraph_format.space_after = DocxPt(0)

s_run = sp.add_run("▼  SILA KEKALKAN KERTAS INI SEPANJANG PROGRAM — SAMBUNG KE BAHAGIAN 2 SELEPAS TAMAT SEMINAR (TANPA POTONG)  ▼")
s_run.font.name = "Arial"
s_run.font.bold = True
s_run.font.size = DocxPt(7)
s_run.font.color.rgb = DocxRGBColor(122, 28, 48)

# Add Post-Survey
add_survey_section(survey['post'], is_pre=False)

# Footer info
p_foot = doc.add_paragraph()
p_foot.paragraph_format.space_before = DocxPt(2)
p_foot.paragraph_format.space_after = DocxPt(0)
p_foot.alignment = WD_ALIGN_PARAGRAPH.RIGHT
rf = p_foot.add_run("NextGen Celik Digital 2026  •  Borang Soal Selidik Rasmi 1 Muka Surat (A4)  •  UTM KL x ASDAF PERKIM")
rf.font.name = "Arial"
rf.font.size = DocxPt(6.5)
rf.font.color.rgb = DocxRGBColor(148, 163, 184)

# Save DOCX
docx_path1 = 'docs/printables/Borang_Soal_Selidik_Pre_Post_Survey.docx'
docx_path2 = 'Borang_Soal_Selidik_Pre_Post_Survey.docx'
doc.save(docx_path1)
doc.save(docx_path2)
print(f"Saved DOCX successfully to:\n- {docx_path1}\n- {docx_path2}")

print("\nAll presentation slides (PPTX) and survey forms (DOCX) generated successfully!")