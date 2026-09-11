import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

os.makedirs('docs/presentation', exist_ok=True)
os.makedirs('slides', exist_ok=True)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# --- THEME COLORS ---
BG_DARK = RGBColor(10, 15, 29)        # #0A0F1D Deep Obsidian Navy
BG_CARD = RGBColor(19, 30, 54)        # #131E36 Card Surface
BG_CARD_LIGHT = RGBColor(28, 43, 75)  # #1C2B4B Lighter Surface

C_MAROON = RGBColor(138, 28, 52)      # #8A1C34 UTM Crimson
C_LIGHT_MAROON = RGBColor(185, 45, 75)
C_GOLD = RGBColor(212, 175, 55)       # #D4AF37 Champagne Gold
C_LIGHT_GOLD = RGBColor(235, 205, 120)
C_CYAN = RGBColor(14, 165, 233)       # #0EA5E9 Vibrant Tech Cyan
C_GREEN = RGBColor(16, 185, 129)      # #10B981 Success Emerald
C_RED = RGBColor(239, 68, 68)         # #EF4444 Danger Coral Red
C_AMBER = RGBColor(245, 158, 11)      # #F59E0B Alert Amber
C_PURPLE = RGBColor(168, 85, 247)     # #A855F7 Creative Violet

C_WHITE = RGBColor(255, 255, 255)
C_OFF_WHITE = RGBColor(241, 245, 249)
C_MUTED = RGBColor(148, 163, 184)
C_BORDER_SUBTLE = RGBColor(40, 56, 92)

# --- HELPER FUNCTIONS ---
def set_slide_base(slide, s_num, total=16):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.fill.background()
    return bg

def add_header(slide, s_num, category, title, subtitle=None):
    # Top bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.2))
    bar.fill.solid()
    bar.fill.fore_color.rgb = BG_CARD
    bar.line.fill.background()

    # Maroon accent top strip
    strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.08))
    strip.fill.solid()
    strip.fill.fore_color.rgb = C_MAROON
    strip.line.fill.background()

    # Gold bottom edge
    gold_edge = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.2), Inches(13.333), Inches(0.04))
    gold_edge.fill.solid()
    gold_edge.fill.fore_color.rgb = C_GOLD
    gold_edge.line.fill.background()

    tx = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.733), Inches(1.0))
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_top = Inches(0.05)

    p_badge = tf.paragraphs[0]
    p_badge.text = f"SLAID {s_num:02d} / 16  •  {category.upper()}"
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = C_GOLD
    p_badge.space_after = Pt(2)

    p_title = tf.add_paragraph()
    p_title.text = title
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = C_WHITE
    if subtitle:
        p_sub = tf.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = C_MUTED

def add_footer(slide, s_num):
    tx = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.4))
    tf = tx.text_frame
    p = tf.paragraphs[0]
    p.text = f"Bengkel Santai NextGen Celik Digital 2026  |  UTM KL × ASDAF PERKIM                                             Slaid {s_num} / 16"
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_MUTED

def add_card(slide, left, top, width, height, bg_color=BG_CARD, border_color=C_BORDER_SUBTLE, border_width=1.5, shape_type=MSO_SHAPE.ROUNDED_RECTANGLE):
    card = slide.shapes.add_shape(shape_type, Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)
    else:
        card.line.fill.background()
    return card

def add_banner(slide, left, top, width, height, text, bg_color, text_color=C_WHITE, font_size=11, bold=True):
    b = add_card(slide, left, top, width, height, bg_color=bg_color, border_color=None, shape_type=MSO_SHAPE.ROUNDED_RECTANGLE)
    tf = b.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = text_color
    p.alignment = PP_ALIGN.CENTER
    return b

def set_notes(slide, s_num, notes_text):
    notes = slide.notes_slide.notes_text_frame
    notes.text = f"PANDUAN & NADA PENCERAMAH (SLAID {s_num}):\n\n{notes_text}"


# ==========================================
# SLAID 1: HERO TITLE SLIDE
# ==========================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_base(s1, 1)

# Top Bar Maroon
s1_top = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.45))
s1_top.fill.solid()
s1_top.fill.fore_color.rgb = C_MAROON
s1_top.line.fill.background()

s1_gold = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(0.45), Inches(13.333), Inches(0.08))
s1_gold.fill.solid()
s1_gold.fill.fore_color.rgb = C_GOLD
s1_gold.line.fill.background()

# Title text
tx1 = s1.shapes.add_textbox(Inches(0.9), Inches(0.85), Inches(11.5), Inches(2.2))
tf1 = tx1.text_frame
tf1.word_wrap = True
p1 = tf1.paragraphs[0]
p1.text = "PROGRAM KHIDMAT MASYARAKAT SISWAZAH  •  UTM KL × ASDAF PERKIM"
p1.font.size = Pt(13)
p1.font.bold = True
p1.font.color.rgb = C_GOLD
p1.space_after = Pt(6)

p2 = tf1.add_paragraph()
p2.text = "BENGKEL SANTAI NEXTGEN CELIK DIGITAL 2026"
p2.font.size = Pt(32)
p2.font.bold = True
p2.font.color.rgb = C_WHITE
p2.space_after = Pt(6)

p3 = tf1.add_paragraph()
p3.text = "“LITERASI TEKNOLOGI & KESEDARAN KECERDASAN BUATAN (AI)”"
p3.font.size = Pt(20)
p3.font.bold = True
p3.font.color.rgb = C_CYAN

# 4 Stat Chips Strip
stats_data = [
    ("46 PELAJAR", "Tingkatan 1–5 & PPKI", C_MAROON),
    ("7 MEJA KLUSTER", "Fasilitator Berdedikasi", C_CYAN),
    ("13 KRU UTM", "Mahasiswa Komputeran", C_GOLD),
    ("SIFAR GAJET", "Interaktif Tanpa Telefon", C_GREEN)
]
for i, (st, sub, col) in enumerate(stats_data):
    sc = add_card(s1, 0.9 + (i * 2.95), 3.2, 2.75, 0.85, bg_color=BG_CARD, border_color=col, border_width=1.5)
    tf = sc.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = st
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = col
    p.alignment = PP_ALIGN.CENTER
    p_sub = tf.add_paragraph()
    p_sub.text = sub
    p_sub.font.size = Pt(9.5)
    p_sub.font.color.rgb = C_OFF_WHITE
    p_sub.alignment = PP_ALIGN.CENTER

# Main Details Split Cards
c_left = add_card(s1, 0.9, 4.3, 5.6, 2.5, bg_color=BG_CARD, border_color=C_MAROON, border_width=2.0)
tf_l = c_left.text_frame
tf_l.word_wrap = True
tf_l.margin_left = Inches(0.35)
tf_l.margin_top = Inches(0.25)
p = tf_l.paragraphs[0]
p.text = "MAKLUMAT PENCERAMAH & SESI"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(8)
for line in [
    "Penceramah: Muhamad Arif bin Johar (DevOps Engineer)",
    "Penganjur: Universiti Teknologi Malaysia (UTM KL)",
    "Lokasi: Asrama Darul Falah (ASDAF) PERKIM, Bukit Persekutuan",
    "Tarikh: Sabtu, 12 September 2026  (8:30 AM – 12:00 PM)"
]:
    p = tf_l.add_paragraph()
    p.text = "• " + line
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(4)

c_right = add_card(s1, 6.8, 4.3, 5.6, 2.5, bg_color=BG_CARD, border_color=C_CYAN, border_width=2.0)
tf_r = c_right.text_frame
tf_r.word_wrap = True
tf_r.margin_left = Inches(0.35)
tf_r.margin_top = Inches(0.25)
p = tf_r.paragraphs[0]
p.text = "3 MISI UTAMA HARI INI"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.space_after = Pt(8)
for line in [
    "1. Bongkar Kuasa AI: Kenal alat pintar & bagaimana ia berfikir.",
    "2. Kebal Serangan Siber: Kuasai Formula 3T lawan scammer.",
    "3. Startup Sprint Meja: Cipta idea inovasi di kertas mahjong!"
]:
    p = tf_r.add_paragraph()
    p.text = "✔ " + line
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(4)

set_notes(s1, 1, "Beri salam penuh bertenaga! Sapu pandangan ke seluruh 7 meja kluster. Katakan kepada adik-adik ASDAF: 'Hari ini kita bukan nak belajar kuliah universiti yang membosankan. Kita datang nak bersantai, bergelak tawa, dan meneroka rahsia teknologi masa depan bersama abang & kakak UTM!'.")


# ==========================================
# SLAID 2: PENGENALAN PASUKAN UTM
# ==========================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_base(s2, 2)
add_header(s2, 2, "Pengenalan Pasukan", "Siapakah Kami? Abang & Kakak Fakulti Komputeran UTM", "Mahasiswa universiti yang datang untuk menjadi rakan mentor & penyokong impian anda")

# 4 Squad Cards Grid (2 x 2)
squads = [
    ("1. PENCERAMAH & LEAD TRAINER", "Muhamad Arif bin Johar", "Membimbing konsep AI, demo langsung di skrin pentas, dan kuiz interaktif dewan.", C_MAROON),
    ("2. 7 MENTOR MEJA KLUSTER", "Fasilitator Berdedikasi", "Duduk bersama adik-adik di setiap meja (Meja 1–7), memandu sesi amali dan perbincangan.", C_CYAN),
    ("3. SOKONGAN KHAS PPKI", "Bimbingan Inklusif", "Memberi perhatian mesra dan sokongan khas untuk rakan-rakan Pendidikan Khas.", C_GREEN),
    ("4. KRU LOGISTIK & HADIAH", "Pengurusan Acara", "Menjaga masa, menyalurkan kertas mahjong, marker pelbagai warna, dan menyediakan hadiah.", C_GOLD)
]

for idx, (title, sub, desc, col) in enumerate(squads):
    gx = 0.9 if idx % 2 == 0 else 6.8
    gy = 1.6 if idx < 2 else 3.8
    c = add_card(s2, gx, gy, 5.6, 2.0, bg_color=BG_CARD, border_color=col, border_width=2.0)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = col
    p.space_after = Pt(2)
    p_s = tf.add_paragraph()
    p_s.text = sub
    p_s.font.size = Pt(11)
    p_s.font.bold = True
    p_s.font.color.rgb = C_WHITE
    p_s.space_after = Pt(4)
    p_d = tf.add_paragraph()
    p_d.text = desc
    p_d.font.size = Pt(10.5)
    p_d.font.color.rgb = C_OFF_WHITE

# Bottom Callout Banner
add_banner(s2, 0.9, 6.0, 11.5, 0.7, "💬 PESANAN MESRA: Anggap abang & kakak UTM sebagai kawan. Jangan takut bertanya, tiada soalan yang bodoh hari ini!", C_MAROON, C_WHITE, 12, True)
add_footer(s2, 2)
set_notes(s2, 2, "Perkenalkan setiap fasilitator meja. Minta setiap mentor meja angkat tangan dan lambaikan tangan kepada adik-adik di meja masing-masing. Wujudkan suasana ceria tanpa rasa kekok.")


# ==========================================
# SLAID 3: ROBOT JAHAT VS PEMBANTU PINTAR (VERSUS LAYOUT)
# ==========================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_base(s3, 3)
add_header(s3, 3, "Modul 1: Asas Kecerdasan Buatan (AI)", "Apakah Itu AI Sebenarnya? Robot Jahat atau Pembantu Pintar?", "Membongkar mitos filem sains fiksyen vs aplikasi teknologi dalam kehidupan sebenar")

# Left Card: Mitos Filem (Red)
c_left = add_card(s3, 0.9, 1.6, 5.2, 4.2, bg_color=BG_CARD, border_color=C_RED, border_width=2.5)
tf_l = c_left.text_frame
tf_l.word_wrap = True
tf_l.margin_left = Inches(0.35)
tf_l.margin_top = Inches(0.25)
p = tf_l.paragraphs[0]
p.text = "MITOS FILEM SAINS FIKSYEN"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_RED
p.space_after = Pt(10)
for pt in [
    "Robot Terminator bersenjata nak kuasai bumi.",
    "Komputer ada emosi jahat nak musnahkan manusia.",
    "Teknologi misteri magik yang tiada siapa faham.",
    "Persepsi menakutkan yang sengaja dicipta di pawagam."
]:
    p = tf_l.add_paragraph()
    p.text = "❌ " + pt
    p.font.size = Pt(12)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(8)

# Center VS Badge
vs = add_card(s3, 6.3, 3.2, 0.8, 0.8, bg_color=C_GOLD, border_color=C_WHITE, border_width=2.0, shape_type=MSO_SHAPE.OVAL)
tf_vs = vs.text_frame
p = tf_vs.paragraphs[0]
p.text = "VS"
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = BG_DARK
p.alignment = PP_ALIGN.CENTER

# Right Card: Realiti Sebenar (Green/Cyan)
c_right = add_card(s3, 7.3, 1.6, 5.2, 4.2, bg_color=BG_CARD, border_color=C_GREEN, border_width=2.5)
tf_r = c_right.text_frame
tf_r.word_wrap = True
tf_r.margin_left = Inches(0.35)
tf_r.margin_top = Inches(0.25)
p = tf_r.paragraphs[0]
p.text = "REALITI SEBENAR AI HARI INI"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_GREEN
p.space_after = Pt(10)
for pt in [
    "Google Maps / Waze: Kira jalan terpantas elak jam.",
    "TikTok & YouTube: Cadang video ikut minat korang.",
    "Pengecaman Wajah: Buka skrin telefon guna muka.",
    "Program Matematik yang belajar mengecam corak data manusia untuk mudahkan kerja!"
]:
    p = tf_r.add_paragraph()
    p.text = "✔ " + pt
    p.font.size = Pt(12)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(8)

add_banner(s3, 0.9, 6.0, 11.6, 0.7, "🗣️ SOALAN AUDIENS: 'Siapa pernah guna Waze atau tengok cadangan video YouTube? Itulah bukti korang dah guna AI setiap hari!'", BG_CARD_LIGHT, C_GOLD, 11.5, True)
add_footer(s3, 3)
set_notes(s3, 3, "Tanya audiens secara spontan: 'Bila dengar perkataan AI, apa yang terlintas di fikiran adik-adik?'. Tunggu 2-3 jawapan ringkas, kemudian jelaskan dengan perbandingan skrin ini.")


# ==========================================
# SLAID 4: BAGAIMANA AI BERFIKIR (PUZZLE / INTERACTIVE)
# ==========================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_base(s4, 4)
add_header(s4, 4, "Modul 1: Bagaimana AI Berfikir", "Ujian Minda AI: Komputer vs Mata Manusia (Kucing vs Chihuahua Muffin)", "Bagaimana algoritma mengenali objek dan kenapa komputer boleh tertipu?")

# 3 Step Visual Sequence
box1 = add_card(s4, 0.9, 1.6, 3.6, 4.2, bg_color=BG_CARD, border_color=C_CYAN, border_width=2.0)
tf = box1.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.25)
tf.margin_top = Inches(0.25)
p = tf.paragraphs[0]
p.text = "LANGKAH 1: DATA MASUK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.space_after = Pt(8)
for line in [
    "Komputer tak ada mata biologi macam manusia.",
    "Komputer cuma nampak nombor piksel (0 dan 1).",
    "Ia disuap dengan 10,000+ contoh gambar kucing."
]:
    p = tf.add_paragraph()
    p.text = "• " + line
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(6)

box2 = add_card(s4, 4.8, 1.6, 3.6, 4.2, bg_color=BG_CARD, border_color=C_GOLD, border_width=2.0)
tf = box2.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.25)
tf.margin_top = Inches(0.25)
p = tf.paragraphs[0]
p.text = "LANGKAH 2: CARI CORAK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(8)
for line in [
    "AI menganalisis corak:",
    "  - Bentuk telinga tiga segi",
    "  - Misai panjang kiri kanan",
    "  - Warna mata dan hidung",
    "Daripada corak itu, ia bina 'Formula Tekaan'."
]:
    p = tf.add_paragraph()
    p.text = "• " + line
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(6)

box3 = add_card(s4, 8.7, 1.6, 3.7, 4.2, bg_color=BG_CARD, border_color=C_AMBER, border_width=2.0)
tf = box3.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.25)
tf.margin_top = Inches(0.25)
p = tf.paragraphs[0]
p.text = "LANGKAH 3: AI BOLEH KELIRU!"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_AMBER
p.space_after = Pt(8)
for line in [
    "Ujian Klasik Muffin vs Chihuahua:",
    "Muffin ada 3 titik coklat (nampak macam 2 mata & 1 hidung anjing!).",
    "Komputer boleh keliru 50%!",
    "Kelebihan Manusia: Kita ada akal fikiran dan konteks sebenar."
]:
    p = tf.add_paragraph()
    p.text = "• " + line
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(6)

add_banner(s4, 0.9, 6.0, 11.5, 0.7, "🎯 PUNCHLINE: AI sangat laju mengira nombor, tapi manusia jauh lebih hebat berfikir dan memahami dunia!", C_MAROON, C_WHITE, 12, True)
add_footer(s4, 4)
set_notes(s4, 4, "Aktiviti pentas: Tunjuk gambar perbandingan muffin coklat dan muka anjing chihuahua. Minta murid angkat tangan siapa rasa komputer boleh tersilap. Dewan pasti terhibur bila tahu komputer boleh tertipu dengan muffin coklat.")


# ==========================================
# SLAID 5: LIVE DEMO 1 - MENGARANG PANTUN (CHAT SIMULATOR)
# ==========================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_base(s5, 5)
add_header(s5, 5, "Modul 1: Demonstrasi Langsung AI", "Eksperimen Dewan: Mengarang Pantun Bersama ChatGPT / Gemini", "Melihat bagaimana AI memahami arahan bahasa Melayu dalam masa nyata (Live Demo)")

# Prompt Chat Bubble (User Input - Green)
c_user = add_card(s5, 0.9, 1.6, 11.5, 1.3, bg_color=BG_CARD_LIGHT, border_color=C_GREEN, border_width=2.0)
tf_u = c_user.text_frame
tf_u.word_wrap = True
tf_u.margin_left = Inches(0.3)
tf_u.margin_top = Inches(0.15)
p = tf_u.paragraphs[0]
p.text = "👤 PROMPT PELAJAR (ARAHAN KEPADA AI):"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_GREEN
p = tf_u.add_paragraph()
p.text = "“Wahai AI, tolong tuliskan 2 rangkap pantun 4 kerat bertemakan semangat anak-anak asrama ASDAF Bukit Persekutuan menuntut ilmu dan celik teknologi!”"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_WHITE

# AI Response Bubble (Gold Border)
c_ai = add_card(s5, 0.9, 3.1, 11.5, 2.7, bg_color=BG_CARD, border_color=C_GOLD, border_width=2.0)
tf_ai = c_ai.text_frame
tf_ai.word_wrap = True
tf_ai.margin_left = Inches(0.35)
tf_ai.margin_top = Inches(0.2)
p = tf_ai.paragraphs[0]
p.text = "🤖 JAWAPAN SPONTAN AI (DALAM MASA 3 SAAT):"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(6)

pantun_lines = [
    "Pergi ke kedai membeli laksa,   Singgah sebentar di Bukit Persekutuan;",
    "Anak ASDAF hebat perkasa,       Celik digital peneraju masa depan!",
    "",
    "Kain songket cantik terbentang, Tenunan indah warisan bangsa;",
    "Semangat belajar setinggi bintang,  Bakal jurutera membina nusa."
]
for pl in pantun_lines:
    p = tf_ai.add_paragraph()
    p.text = pl
    p.font.size = Pt(12.5)
    p.font.bold = True if pl else False
    p.font.color.rgb = C_OFF_WHITE if pl else C_MUTED

add_banner(s5, 0.9, 6.0, 11.5, 0.7, "💡 FORMULA PROMPT: Semakin jelas dan terperinci arahan yang kita berikan, semakin hebat dan tepat jawapan AI!", C_MAROON, C_WHITE, 12, True)
add_footer(s5, 5)
set_notes(s5, 5, "Minta seorang wakil pelajar di Meja 1 sebutkan satu perkataan kegemaran mereka. Penceramah taip secara langsung di skrin projektor. Tunjukkan keajaiban AI menjana ayat puitis dalam sekelip mata.")


# ==========================================
# SLAID 6: LIVE DEMO 2 - TEKS MENJADI GAMBAR 4K
# ==========================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_base(s6, 6)
add_header(s6, 6, "Modul 1: Demonstrasi Seni Visual AI", "Dari Teks Menjadi Gambar 4K: Canva Magic Media & DALL-E", "Menzahirkan imaginasi paling liar menjadi karya seni digital dalam 5 saat")

# 3 Step Workflow
steps_visual = [
    ("LANGKAH 1: IMAGINASI LIAR", "Murid Meja 4 beri idea spontan:", "“Harimau Malaya memakai jersi sukan UTM bermain bola sepak di stesen angkasa lepas!”", C_CYAN),
    ("LANGKAH 2: PROZES PIKSEL AI", "AI menterjemah teks ke visual:", "Algoritma menyusun corak bulu harimau, warna merah UTM, sfera bumi bercahaya & stadium bintang.", C_PURPLE),
    ("LANGKAH 3: HASIL KARYA 4K", "Terjana dalam 5 saat:", "Poster definisi tinggi sedia digunakan untuk logo kelab, buku komik, atau animasi sekolah!", C_GREEN)
]

for i, (st, sub, desc, col) in enumerate(steps_visual):
    c = add_card(s6, 0.9 + (i * 3.9), 1.6, 3.7, 4.2, bg_color=BG_CARD, border_color=col, border_width=2.0)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_top = Inches(0.25)
    p = tf.paragraphs[0]
    p.text = st
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = col
    p.space_after = Pt(6)
    p_s = tf.add_paragraph()
    p_s.text = sub
    p_s.font.size = Pt(11)
    p_s.font.bold = True
    p_s.font.color.rgb = C_WHITE
    p_s.space_after = Pt(8)
    p_d = tf.add_paragraph()
    p_d.text = desc
    p_d.font.size = Pt(11.5)
    p_d.font.color.rgb = C_OFF_WHITE

add_banner(s6, 0.9, 6.0, 11.5, 0.7, "🎨 ETIKA VISUAL: AI adalah alatan meluahkan kreativiti — jangan sekali-kali cipta gambar palsu (deepfake) yang fitnah orang lain!", C_AMBER, BG_DARK, 11.5, True)
add_footer(s6, 6)
set_notes(s6, 6, "Tunjukkan penjanaan gambar secara langsung menggunakan alatan AI teks-ke-imej di skrin besar. Selitkan mesej etika: Jangan guna AI untuk mengaibkan rakan.")


# ==========================================
# SLAID 7: AI SEBAGAI TUTOR PERIBADI & INTEGRITI
# ==========================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_base(s7, 7)
add_header(s7, 7, "Modul 1: Rakan Belajar Pelajar", "AI Sebagai Guru Tuisyen Peribadi 24 Jam: Boleh vs Jangan!", "Cara bijak memanfaatkan AI untuk peperiksaan SPM/PT3 tanpa hilang kejujuran ilmu")

# Do's (Green)
c_dos = add_card(s7, 0.9, 1.6, 5.6, 4.2, bg_color=BG_CARD, border_color=C_GREEN, border_width=2.0)
tf = c_dos.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.35)
tf.margin_top = Inches(0.25)
p = tf.paragraphs[0]
p.text = "✔ CARA TERBAIK GUNA AI (BOLEH!)"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_GREEN
p.space_after = Pt(10)
for pt in [
    "Terangkan soalan Matematik sukar langkah demi langkah.",
    "Semak ejaan, tatabahasa & kosa kata Bahasa Inggeris.",
    "Bina jadual ulang kaji harian menjelang peperiksaan.",
    "Beri kuiz latihan dan tanya soalan tanpa rasa segan."
]:
    p = tf.add_paragraph()
    p.text = "✔ " + pt
    p.font.size = Pt(12)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(8)

# Don'ts (Red)
c_donts = add_card(s7, 6.8, 1.6, 5.6, 4.2, bg_color=BG_CARD, border_color=C_RED, border_width=2.0)
tf = c_donts.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.35)
tf.margin_top = Inches(0.25)
p = tf.paragraphs[0]
p.text = "❌ PANTANG LARANG KERAS (JANGAN!)"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_RED
p.space_after = Pt(10)
for pt in [
    "Copy-paste bulat-bulat karangan atau jawapan kerja sekolah.",
    "Malas berfikir dan harap AI buat semua kerja rumah.",
    "Percaya 100% tanpa semak buku teks (AI boleh berhalusinasi).",
    "Menipu cikgu dan diri sendiri — otak manusia mesti dilatih!"
]:
    p = tf.add_paragraph()
    p.text = "❌ " + pt
    p.font.size = Pt(12)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(8)

add_banner(s7, 0.9, 6.0, 11.5, 0.7, "🧠 PESANAN INTEGRITI: 'AI patut buat otak kita makin pintar, bukan buat kita jadi malas berfikir!'", C_MAROON, C_WHITE, 12, True)
add_footer(s7, 7)
set_notes(s7, 7, "Tekankan aspek integriti. Pelajar asrama perlu tahu bahawa AI adalah guru tuisyen percuma yang sabar, tetapi SPM sebenar memerlukan otak dan pena mereka sendiri.")


# ==========================================
# SLAID 8: 5 KERJAYA DIGITAL MASA DEPAN
# ==========================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_base(s8, 8)
add_header(s8, 8, "Modul 1: Impian & Masa Depan", "Peluang Hebat Bidang Digital: Di Mana Tempat Anak ASDAF?", "5 Bidang Kerjaya Gaji Lumayan yang Tidak Memandang Latar Belakang Keturunan")

careers = [
    ("1. PEREKA GAME & ANIMASI", "Gaji Permulaan: RM4,000 - RM8,000", "Mencipta dunia permainan Roblox, Mobile Legends, dan animasi 3D kegemaran ramai.", C_PURPLE),
    ("2. JURUTERA AI & DATA", "Gaji Permulaan: RM5,000 - RM10,000", "Membina model kecerdasan buatan untuk meramal cuaca, kewangan, dan sistem kesihatan.", C_CYAN),
    ("3. PEJUANG SIBER (ETHICAL HACKER)", "Gaji Permulaan: RM4,500 - RM9,000", "Mempertahankan sistem perbankan negara dan laman web kerajaan daripada penjenayah siber.", C_RED),
    ("4. JURUTERA DRON & PERTANIAN", "Gaji Permulaan: RM4,000 - RM7,500", "Mengemudi dron pintar untuk menyembur baja dan memantau ladang sawit secara automatik.", C_GREEN),
    ("5. CLOUD & DEVOPS ENGINEER", "Gaji Permulaan: RM5,000 - RM11,000", "Menjaga pelayan internet gergasi supaya Instagram, WhatsApp & Shopee berjalan 24 jam.", C_GOLD)
]

# Top row: 3 cards
for i in range(3):
    t, s, d, c = careers[i]
    card = add_card(s8, 0.9 + (i * 3.9), 1.6, 3.7, 2.0, bg_color=BG_CARD, border_color=c, border_width=2.0)
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_top = Inches(0.15)
    p = tf.paragraphs[0]
    p.text = t
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = c
    p_s = tf.add_paragraph()
    p_s.text = s
    p_s.font.size = Pt(9.5)
    p_s.font.bold = True
    p_s.font.color.rgb = C_WHITE
    p_d = tf.add_paragraph()
    p_d.text = d
    p_d.font.size = Pt(10)
    p_d.font.color.rgb = C_OFF_WHITE

# Bottom row: 2 cards
for i in range(2):
    t, s, d, c = careers[i+3]
    card = add_card(s8, 0.9 + (i * 5.85), 3.8, 5.65, 2.0, bg_color=BG_CARD, border_color=c, border_width=2.0)
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.15)
    p = tf.paragraphs[0]
    p.text = t
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = c
    p_s = tf.add_paragraph()
    p_s.text = s
    p_s.font.size = Pt(10)
    p_s.font.bold = True
    p_s.font.color.rgb = C_WHITE
    p_d = tf.add_paragraph()
    p_d.text = d
    p_d.font.size = Pt(10.5)
    p_d.font.color.rgb = C_OFF_WHITE

add_banner(s8, 0.9, 6.0, 11.5, 0.7, "🌟 MOTIVASI: 'Dunia IT tidak tanya kita anak siapa atau dari mana asal kita. Ia tanya kemahiran dan minat kita!'", C_MAROON, C_WHITE, 12, True)
add_footer(s8, 8)
set_notes(s8, 8, "Bakar semangat anak-anak ASDAF. Ceritakan kisah inspirasi bagaimana ramai jurutera teknologi berasal dari latar belakang keluarga susah tetapi berjaya menembusi syarikat gergasi.")


# ==========================================
# SLAID 9: DUNIA GELAP SIBER (SCAM & PHISHING)
# ==========================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_base(s9, 9)
add_header(s9, 9, "Modul 2: Keselamatan Siber", "Dunia Gelap Internet: Jerat Scam, Phishing & Hadiah Palsu", "Bagaimana penjenayah siber memancing data peribadi dan duit keluarga kita?")

# Fake Scam Message Mockup Card
c_scam = add_card(s9, 0.9, 1.6, 5.6, 4.2, bg_color=RGBColor(35, 15, 20), border_color=C_RED, border_width=2.5)
tf_s = c_scam.text_frame
tf_s.word_wrap = True
tf_s.margin_left = Inches(0.35)
tf_s.margin_top = Inches(0.25)
p = tf_s.paragraphs[0]
p.text = "⚠️ CONTOH MESEJ WHATSAPP JERAT SCAM:"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_RED
p.space_after = Pt(8)

p_box = tf_s.add_paragraph()
p_box.text = "“Tahniah! Nombor telefon anda telah dicabut bertuah memenangi RM10,000 TUNAI dari Shopee Sempena Hari Kemerdekaan! Sila klik pautan bit.ly/claim-wang-sekarang dan masukkan kata laluan untuk sahkan akaun dalam masa 10 MINIT sebelum hadiah dibatalkan!”"
p_box.font.size = Pt(12)
p_box.font.bold = True
p_box.font.color.rgb = RGBColor(254, 202, 202)
p_box.space_after = Pt(10)

p_w = tf_s.add_paragraph()
p_w.text = "Akibat Jika Klik: Penggodam curi akaun media sosial, curi duit simpanan ibu bapa, dan sebar gambar peribadi!"
p_w.font.size = Pt(11)
p_w.font.color.rgb = C_OFF_WHITE

# 3 Red Flags Card
c_flags = add_card(s9, 6.8, 1.6, 5.6, 4.2, bg_color=BG_CARD, border_color=C_AMBER, border_width=2.0)
tf_f = c_flags.text_frame
tf_f.word_wrap = True
tf_f.margin_left = Inches(0.35)
tf_f.margin_top = Inches(0.25)
p = tf_f.paragraphs[0]
p.text = "🚩 3 TANDA-TANDA JERAT SCAMMER"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_AMBER
p.space_after = Pt(10)
for pt in [
    "1. Janji Wang Percuma / Hadiah Gila: Mana ada orang bagi RM10,000 suka-suka tanpa usaha!",
    "2. Cipta Suasana Panik: 'Cepat! 10 minit lagi akaun disekat!' — Scammer nak mangsa bertindak tanpa fikir.",
    "3. Minta Kata Laluan / OTP: Pihak bank dan guru takkan pernah minta OTP atau password anda!"
]:
    p = tf_f.add_paragraph()
    p.text = pt
    p.font.size = Pt(12)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(10)

add_banner(s9, 0.9, 6.0, 11.5, 0.7, "🚨 INGAT: Bila nampak tawaran terlalu manis untuk dipercayai, 99.9% adalah PENIPUAN SIBER!", C_RED, C_WHITE, 12, True)
add_footer(s9, 9)
set_notes(s9, 9, "Tanya dewan: 'Siapa pernah dapat mesej macam ni kat WhatsApp mak ayah atau telefon sendiri?'. Beri amaran tegas tentang bahaya klik link sembarangan.")


# ==========================================
# SLAID 10: FORMULA EMAS 3T (3 PILLARS HERO LAYOUT)
# ==========================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_base(s10, 10)
add_header(s10, 10, "Modul 2: Formula Pertahanan Diri", "Formula Emas 3T: Senjata Utama Menewaskan Scammer", "Hafal 3 peraturan ini untuk melindungi diri, keluarga dan rakan-rakan seumur hidup")

pillars_3t = [
    ("T1", "TIDAK PASTI", "Siasat Dulu!", [
        "Jangan mudah percaya pemanggil misteri atau mesej hadiah.",
        "Rujuk warden, guru, atau ibu bapa sebelum buat sebarang tindakan.",
        "Sikap sangsi yang bijak adalah perisai terbaik anda."
    ], C_MAROON),
    ("T2", "TIDAK KONGSI", "Kunci Rahsia!", [
        "Jangan sesekali beri kata laluan, nombor IC, atau kod OTP.",
        "Kata laluan adalah seperti berus gigi peribadi — jangan kongsi!",
        "Simpan maklumat keluarga dengan cermat."
    ], C_GOLD),
    ("T3", "TIDAK KLIK", "Jangan Tekan!", [
        "Jangan tekan sebarang pautan biru yang mencurigakan di WhatsApp/SMS.",
        "Bila ragu-ragu, terus padam dan sekat (block) nombor tersebut.",
        "Satu klik salah boleh membuka pintu kepada penggodam."
    ], C_CYAN)
]

for i, (code, title, action, pts, col) in enumerate(pillars_3t):
    c = add_card(s10, 0.9 + (i * 3.9), 1.6, 3.7, 4.2, bg_color=BG_CARD, border_color=col, border_width=2.5)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = f"{code}: {title}"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = col
    p_a = tf.add_paragraph()
    p_a.text = action
    p_a.font.size = Pt(12)
    p_a.font.bold = True
    p_a.font.color.rgb = C_WHITE
    p_a.space_after = Pt(8)
    for line in pts:
        p = tf.add_paragraph()
        p.text = "• " + line
        p.font.size = Pt(11)
        p.font.color.rgb = C_OFF_WHITE
        p.space_after = Pt(6)

add_banner(s10, 0.9, 6.0, 11.5, 0.7, "📞 TALIAN KECEMASAN SCAM KEBANGSAAN: 997 (NSRC) — Hubungi dalam 24 jam jika terkena scam!", C_AMBER, BG_DARK, 12, True)
add_footer(s10, 10)
set_notes(s10, 10, "Latihan laung dewan beramai-ramai! Penceramah jerit: 'T1!' Dewan balas: 'TIDAK PASTI!' Penceramah: 'T2!' Dewan: 'TIDAK KONGSI!' Penceramah: 'T3!' Dewan: 'TIDAK KLIK!' Jadikan suasana dewan gegak gempita.")


# ==========================================
# SLAID 11: RAHSIA KATA LALUAN KEBAL
# ==========================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_base(s11, 11)
add_header(s11, 11, "Modul 2: Keselamatan Akaun", "Rahsia Kata Laluan Kebal: Password vs Passphrase", "Berapa lama masa yang diperlukan oleh komputer penggodam untuk memecah masuk?")

# Red Box: Weak
c_weak = add_card(s11, 0.9, 1.6, 5.6, 4.2, bg_color=BG_CARD, border_color=C_RED, border_width=2.5)
tf_w = c_weak.text_frame
tf_w.word_wrap = True
tf_w.margin_left = Inches(0.35)
tf_w.margin_top = Inches(0.25)
p = tf_w.paragraphs[0]
p.text = "❌ KATA LALUAN LEMAH (MUDAH HACK)"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_RED
p.space_after = Pt(8)
for pt, time in [
    ("12345678", "0.0001 Saat"),
    ("asdaf2026", "0.02 Saat"),
    ("kucingcomel", "2 Saat"),
    ("Tarikh Lahir", "Kurang 1 Saat")
]:
    p = tf_w.add_paragraph()
    p.text = f"• '{pt}' ➔ Hack dalam {time}!"
    p.font.size = Pt(12)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(6)

p_sum = tf_w.add_paragraph()
p_sum.text = "Penggodam guna 'Dictionary Attack' yang menguji jutaan perkataan lazim dalam sekelip mata!"
p_sum.font.size = Pt(11)
p_sum.font.italic = True
p_sum.font.color.rgb = C_MUTED

# Green Box: Strong Passphrase
c_strong = add_card(s11, 6.8, 1.6, 5.6, 4.2, bg_color=BG_CARD, border_color=C_GREEN, border_width=2.5)
tf_s = c_strong.text_frame
tf_s.word_wrap = True
tf_s.margin_left = Inches(0.35)
tf_s.margin_top = Inches(0.25)
p = tf_s.paragraphs[0]
p.text = "✔ TEKNIK PASSPHRASE KEBAL"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_GREEN
p.space_after = Pt(8)
for pt, time in [
    ("KopiPanasTumpah99!", "10,000 TAHUN"),
    ("HarimauLompatPagar!", "400 JUTA TAHUN")
]:
    p = tf_s.add_paragraph()
    p.text = f"• '{pt}' ➔ Perlu {time}!"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_LIGHT_GOLD
    p.space_after = Pt(6)

for tip in [
    "1. Gabung 3–4 perkataan rawak menjadi satu ayat rahsia.",
    "2. Selitkan nombor dan simbol unik (!, @, #).",
    "3. Aktifkan 2FA (Pengesahan 2-Faktor) di akaun media sosial."
]:
    p = tf_s.add_paragraph()
    p.text = tip
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(4)

add_banner(s11, 0.9, 6.0, 11.5, 0.7, "🔐 PETUA: Buat ayat pelik yang senang anda ingat tapi mustahil diteka oleh orang lain!", C_MAROON, C_WHITE, 12, True)
add_footer(s11, 11)
set_notes(s11, 11, "Ajar teknik gabung 3 perkataan rawak. Minta seorang pelajar reka satu passphrase di depan dewan. Tunjukkan betapa kukuhnya kata laluan tersebut.")


# ==========================================
# SLAID 12: JEJAK DIGITAL (T-H-I-N-K)
# ==========================================
s12 = prs.slides.add_slide(blank_layout)
set_slide_base(s12, 12)
add_header(s12, 12, "Modul 2: Etika Digital", "Jejak Digital: Internet Tidak Pernah Lupa!", "Sebelum menekan butang 'POST' atau 'SEND' di media sosial, amalkan formula T-H-I-N-K")

think_letters = [
    ("T", "TRUE", "Adakah ini benar?", "Jangan sebar berita palsu atau khabar angin yang belum disahkan.", C_CYAN),
    ("H", "HELPFUL", "Adakah ia membantu?", "Adakah perkongsian ini memberi manfaat kepada orang yang membacanya?", C_GREEN),
    ("I", "INSPIRING", "Adakah ia memberi inspirasi?", "Gunakan media sosial untuk membakar semangat kejayaan, bukan merendahkan orang.", C_GOLD),
    ("N", "NECESSARY", "Adakah ia benar-benar perlu?", "Adakah aib atau masalah peribadi anda perlu diketahui oleh seluruh dunia?", C_AMBER),
    ("K", "KIND", "Adakah ayat ini berbudi bahasa?", "Hapuskan buli siber. Perkataan yang baik adalah sedekah.", C_PURPLE)
]

for i, (ltr, word, q, desc, col) in enumerate(think_letters):
    c = add_card(s12, 0.9 + (i * 2.33), 1.6, 2.18, 4.2, bg_color=BG_CARD, border_color=col, border_width=2.0)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.18)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = ltr
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = col
    p.alignment = PP_ALIGN.CENTER
    p_w = tf.add_paragraph()
    p_w.text = word
    p_w.font.size = Pt(13)
    p_w.font.bold = True
    p_w.font.color.rgb = C_WHITE
    p_w.alignment = PP_ALIGN.CENTER
    p_w.space_after = Pt(8)
    p_q = tf.add_paragraph()
    p_q.text = q
    p_q.font.size = Pt(10.5)
    p_q.font.bold = True
    p_q.font.color.rgb = col
    p_q.space_after = Pt(6)
    p_d = tf.add_paragraph()
    p_d.text = desc
    p_d.font.size = Pt(10)
    p_d.font.color.rgb = C_OFF_WHITE

add_banner(s12, 0.9, 6.0, 11.5, 0.7, "👣 PERINGATAN: Majikan & penemuduga universiti akan cari nama korang di internet 5 tahun lagi!", C_MAROON, C_WHITE, 12, True)
add_footer(s12, 12)
set_notes(s12, 12, "Peringatan empati dan sentuhan emosi. Terangkan bahawa status TikTok/Instagram yang dipadam masih boleh diambil tangkap layar (screenshot). Jaga maruah diri.")


# ==========================================
# SLAID 13: MISI AMALI MEJA (STARTUP SPRINT)
# ==========================================
s13 = prs.slides.add_slide(blank_layout)
set_slide_base(s13, 13)
add_header(s13, 13, "Modul 2: Latihan Kumpulan", "Masa Menjadi Pencipta: Bengkel Startup Sprint Kertas Mahjong", "7 Meja Kluster kini bertukar menjadi 7 Syarikat Pemula Teknologi Muda ASDAF!")

# Left Card: Misi Syarikat
c_left = add_card(s13, 0.9, 1.6, 5.6, 4.2, bg_color=BG_CARD, border_color=C_GOLD, border_width=2.5)
tf = c_left.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.35)
tf.margin_top = Inches(0.25)
p = tf.paragraphs[0]
p.text = "🎯 MISI SETIAP MEJA (SYARIKAT ANDA)"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(10)
for line in [
    "Pilih 1 masalah sebenar di asrama ASDAF atau sekolah.",
    "Cipta 1 idea inovasi AI untuk selesaikan masalah tersebut.",
    "Lakar dan lukis poster di atas kertas mahjong bersama.",
    "Pilih 2 jurucakap meja untuk membentang di hadapan dewan!"
]:
    p = tf.add_paragraph()
    p.text = "✔ " + line
    p.font.size = Pt(12)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(8)

# Right Card: Peralatan & Format
c_right = add_card(s13, 6.8, 1.6, 5.6, 4.2, bg_color=BG_CARD, border_color=C_CYAN, border_width=2.0)
tf = c_right.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.35)
tf.margin_top = Inches(0.25)
p = tf.paragraphs[0]
p.text = "📦 PERALATAN & MASA AKTIVITI"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.space_after = Pt(10)
for line in [
    "Bahan: Kertas mahjong, marker pelbagai warna, sticky notes.",
    "Masa Perbincangan Meja: 35 Minit padat.",
    "Masa Pitching Pentas: 2 Minit setiap meja!",
    "Bimbingan Penuh: Mentor meja sedia membantu lakaran dan idea."
]:
    p = tf.add_paragraph()
    p.text = "• " + line
    p.font.size = Pt(12)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(8)

add_banner(s13, 0.9, 6.0, 11.5, 0.7, "🏆 HADIAH KUMPULAN: Meja dengan idea paling kreatif dan pembentangan paling bertenaga akan bawa pulang HAMPER JUARA!", C_GREEN, BG_DARK, 12, True)
add_footer(s13, 13)
set_notes(s13, 13, "Umumkan aktiviti kemuncak! Fasilitator meja segera edarkan kertas mahjong dan bekas marker. Tiup wisel tanda masa 35 minit bermula!")


# ==========================================
# SLAID 14: FORMAT PEMBENTANGAN 4 KOTAK EMAS (2x2 GRID DIAGRAM)
# ==========================================
s14 = prs.slides.add_slide(blank_layout)
set_slide_base(s14, 14)
add_header(s14, 14, "Modul 2: Panduan Amali", "Format Kertas Mahjong: 4 Kotak Emas Poster Inovasi", "Bahagikan kertas mahjong kepada 4 kuadran ringkas, jelas dan berwarna-warni")

quadrants = [
    ("KOTAK 1: IDENTITI & LOGO", "Nama Syarikat & Logo Inovasi", [
        "Nama aplikasi / robot AI ciptaan meja anda.",
        "Lukis logo ringkas & moto syarikat yang menarik."
    ], C_PURPLE),
    ("KOTAK 2: MASALAH SEBENAR", "Apa Isu Yang Hendak Diselesaikan?", [
        "Contoh: Pembaziran makanan di dewan makan.",
        "Contoh: Terlupa waktu solat / susah bangun pagi."
    ], C_RED),
    ("KOTAK 3: CARA TEKNOLOGI BERFUNGSI", "Bagaimana AI Membantu?", [
        "Lukis carta aliran atau rajah mudah alatan AI.",
        "Contoh: Kamera sensor AI kesan sisa makanan."
    ], C_CYAN),
    ("KOTAK 4: KEBAIKAN & IMPAK", "Manfaat Kepada Warga ASDAF", [
        "Asrama jadi lebih bersih dan jimat kos.",
        "Pelajar lebih berdisiplin dan gembira."
    ], C_GREEN)
]

for idx, (title, sub, pts, col) in enumerate(quadrants):
    gx = 0.9 if idx % 2 == 0 else 6.8
    gy = 1.6 if idx < 2 else 3.8
    c = add_card(s14, gx, gy, 5.6, 2.0, bg_color=BG_CARD, border_color=col, border_width=2.5)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = col
    p_s = tf.add_paragraph()
    p_s.text = sub
    p_s.font.size = Pt(11)
    p_s.font.bold = True
    p_s.font.color.rgb = C_WHITE
    p_s.space_after = Pt(3)
    for line in pts:
        p = tf.add_paragraph()
        p.text = "• " + line
        p.font.size = Pt(10)
        p.font.color.rgb = C_OFF_WHITE

add_banner(s14, 0.9, 6.0, 11.5, 0.7, "⏱️ SYARAT PITCHING: 2 Minit Pembentangan Pentas • Semua ahli kumpulan naik sokong 2 orang pembentang utama!", C_GOLD, BG_DARK, 12, True)
add_footer(s14, 14)
set_notes(s14, 14, "Tunjukkan struktur 4 kuadran ini di layar skrin dewan sepanjang masa 35 minit agar semua meja ada panduan visual yang jelas.")


# ==========================================
# SLAID 15: FAST-ANSWER TECH SHOWDOWN (ARCADE QUIZ ARENA)
# ==========================================
s15 = prs.slides.add_slide(blank_layout)
set_slide_base(s15, 15)
add_header(s15, 15, "Cabaran Kuiz Dewan", "Fast-Answer Tech Showdown: Pertarungan Kuiz Pantas!", "Mekanik Sifar Gajet: Mata pada skrin, tangan atas meja! '3... 2... 1... ANGKAT TANGAN!'")

# 5 Rapid Questions Box
c_q = add_card(s15, 0.9, 1.6, 7.5, 4.2, bg_color=BG_CARD, border_color=C_CYAN, border_width=2.5)
tf_q = c_q.text_frame
tf_q.word_wrap = True
tf_q.margin_left = Inches(0.35)
tf_q.margin_top = Inches(0.2)
p = tf_q.paragraphs[0]
p.text = "⚡ 5 SOALAN REBUTAN HADIAH SEGERA:"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(8)

quiz_items = [
    ("SOALAN 1:", "Apakah maksud singkatan AI dalam bahasa Melayu dan Inggeris?"),
    ("SOALAN 2:", "Mesej menang RM10,000 dari nombor misteri dinamakan apa?"),
    ("SOALAN 3:", "Apakah Formula 3T untuk menewaskan scammer?"),
    ("SOALAN 4:", "Manakah lebih kebal: Password 'asdaf2026' atau Passphrase?"),
    ("SOALAN 5:", "Apakah nombor talian kecemasan scam NSRC kebangsaan?")
]
for no, qtext in quiz_items:
    p = tf_q.add_paragraph()
    p.text = f"{no} {qtext}"
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(6)

# Prize & Mechanics Box
c_pz = add_card(s15, 8.7, 1.6, 3.7, 4.2, bg_color=RGBColor(30, 25, 45), border_color=C_PURPLE, border_width=2.5)
tf_p = c_pz.text_frame
tf_p.word_wrap = True
tf_p.margin_left = Inches(0.25)
tf_p.margin_top = Inches(0.2)
p = tf_p.paragraphs[0]
p.text = "🎁 HADIAH MENANTI!"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_PURPLE
p.space_after = Pt(8)
for line in [
    "5 Pemenang Kuiz Pantas!",
    "Hadiah Berguna Asrama:",
    "  • Pendrive 64GB",
    "  • Kipas Meja USB Boleh Cas",
    "  • Lampu Belajar LED USB",
    "  • Botol Termos Digital",
    "  • Set Pen Morandi & Nota",
    "Siapa pantas & tepat terus bawa pulang hadiah ke meja!"
]:
    p = tf_p.add_paragraph()
    p.text = line
    p.font.size = Pt(10.5)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(4)

add_banner(s15, 0.9, 6.0, 11.5, 0.7, "🚨 PERATURAN SHOWDOWN: Emcee kira 3, 2, 1 ANGKAT TANGAN! Mentor meja tolong tengok siapa paling pantas di meja anda!", C_MAROON, C_WHITE, 12, True)
add_footer(s15, 15)
set_notes(s15, 15, "Cipta debaran dewan! Gunakan muzik latar rancak jika ada. Emcee berdiri di hadapan dewan mengira detik undur. Pemenang naik pentas terus menerima hadiah dan tepukan gemuruh.")


# ==========================================
# SLAID 16: PENUTUP & PENGHARGAAN
# ==========================================
s16 = prs.slides.add_slide(blank_layout)
set_slide_base(s16, 16)
add_header(s16, 16, "Majlis Penutup & Jamuan", "Masa Depan Bermula Hari Ini: Terima Kasih ASDAF PERKIM!", "Semoga ilmu yang dikongsi menjadi pemangkin kejayaan dan pembakar semangat anak-anak ASDAF")

# 3 Next Steps Checkpoints
c_chk = add_card(s16, 0.9, 1.6, 5.6, 4.2, bg_color=BG_CARD, border_color=C_CYAN, border_width=2.0)
tf = c_chk.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.35)
tf.margin_top = Inches(0.25)
p = tf.paragraphs[0]
p.text = "📋 3 TINDAKAN AKHIR SEBELUM BERSURAI:"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.space_after = Pt(10)
for pt in [
    "1. Lengkapkan Borang Post-Survey (Bahagian 2 di bawah kertas survey anda) dan tulis komen ikhlas.",
    "2. Penyampaian Hadiah Juara Meja & Cenderamata Rasmi UTM kepada Pengurusan ASDAF PERKIM.",
    "3. Sesi Bergambar Kenangan Bersama & Jamuan Makan Tengah Hari Nasi Berlauk di Dewan Makan."
]:
    p = tf.add_paragraph()
    p.text = pt
    p.font.size = Pt(12)
    p.font.color.rgb = C_OFF_WHITE
    p.space_after = Pt(10)

# Inspirational Gold Card
c_quote = add_card(s16, 6.8, 1.6, 5.6, 4.2, bg_color=RGBColor(25, 20, 35), border_color=C_GOLD, border_width=2.5)
tf_q = c_quote.text_frame
tf_q.word_wrap = True
tf_q.margin_left = Inches(0.35)
tf_q.margin_top = Inches(0.25)
p = tf_q.paragraphs[0]
p.text = "🌟 PESANAN ABANG & KAKAK UTM:"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(10)

p_q1 = tf_q.add_paragraph()
p_q1.text = "“Jangan biarkan keterbatasan semalam menghalang impian esok hari.”"
p_q1.font.size = Pt(14)
p_q1.font.bold = True
p_q1.font.color.rgb = C_WHITE
p_q1.space_after = Pt(10)

p_q2 = tf_q.add_paragraph()
p_q2.text = "“Kuasai teknologi, pelihara adab, dan buktikan anak-anak ASDAF mampu menggegarkan persada negara!”"
p_q2.font.size = Pt(13)
p_q2.font.bold = True
p_q2.font.color.rgb = C_LIGHT_GOLD
p_q2.space_after = Pt(14)

p_sig = tf_q.add_paragraph()
p_sig.text = "— Mahasiswa Fakulti Komputeran Universiti Teknologi Malaysia"
p_sig.font.size = Pt(11)
p_sig.font.italic = True
p_sig.font.color.rgb = C_MUTED

add_banner(s16, 0.9, 6.0, 11.5, 0.7, "🎓 JUMPA LAGI DI MENARA GADING UNIVERSITI TEKNOLOGI MALAYSIA! TERIMA KASIH ASDAF!", C_MAROON, C_WHITE, 12, True)
add_footer(s16, 16)
set_notes(s16, 16, "Kata penutup menyentuh jiwa. Ucapkan terima kasih kepada pengetua, warden, guru ASDAF dan adik-adik semua. Ajak semua dewan berdiri untuk bergambar dan melaungkan slogan UTM x ASDAF!")


# ==========================================
# SAVE PRESENTATIONS
# ==========================================
paths = [
    'docs/presentation/Bengkel_Santai_NextGen_Celik_Digital_2026.pptx',
    'docs/presentation/Bengkel_Santai_NextGen_Celik_Digital_2026_Interaktif.pptx',
    'slides/Bengkel_Santai_NextGen_Celik_Digital_2026.pptx',
    'slides/Bengkel_Santai_NextGen_Celik_Digital_2026_Interaktif.pptx'
]

for p in paths:
    try:
        prs.save(p)
        print(f"Saved: {p}")
    except Exception as e:
        print(f"Note: Could not save to {p}: {e}")

print("Interactive Presentation generation completed!")

