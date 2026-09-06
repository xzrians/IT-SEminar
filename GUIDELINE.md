# 📖 Panduan Kemas Kini Wiki (NextGen Tech Summit 2026)
*Buku Panduan Rasmi untuk Pengguna & Pembangun AI Agent*

Laman wiki ini dijana menggunakan **Jekyll Static Site Generator (SSG)** dan di-deploy secara automatik ke **GitHub Pages** menggunakan **GitHub Actions**.

---

## ⚡ 1. Ringkasan Pantas: Di Mana Nak Buat Perubahan?

Anda **TIDAK PERLU** mengedit kod HTML atau CSS untuk mengemas kini maklumat acara. Semua kandungan diuruskan melalui fail **YAML** di dalam folder `_data/`:

```text
📁 _data/
├── 💰 budget.yml       → Siling RM800, 3 Varian Bajet, Pax 66+5=71, Kos Makanan
├── 📦 operations.yml   → Dokumen Tak Hadir, Makanan Kantin/Luar, Goodies 47 Pax, Utiliti (Mahjong dll)
├── ⏰ timeline.yml     → Jadual Minit-ke-Minit (08:30 – 13:00) & PIC Sesi
├── 📚 curriculum.yml   → Silibus 2 Modul, Rangka 16 Slaid, 4 Aktiviti Praktikal & PPKI
├── 🪑 tables.yml       → Pembahagian 7 Meja Kluster, Pelajar T1–T5, PPKI & Mentor UTM
├── 🎯 quiz.yml         → 5 Soalan Kuiz "3, 2, 1... Angkat Tangan!", Jawapan & Hadiah
├── 👥 crew.yml         → Senarai 13 Kru UTM (6 Lead Pentas + 7 Mentor Meja)
├── 📋 checklist.yml    → Senarai Semak Pra-Acara, Hari Kejadian & Pasca
├── 🏫 asdaf.yml        → Latar Belakang ASDAF (1995), Profil Anak Yatim/Asnaf, 4 PPKI
└── 📊 stats.yml        → Kad Angka Statistik Utama di Header Web
```

---

## 🤖 2. Contoh Prompt Pantas untuk Diberikan Kepada AI

Jika anda menggunakan mana-mana model AI (Antigravity, ChatGPT, Claude, Copilot), anda hanya perlu **salin dan tampal (copy-paste)** arahan di bawah:

### 🔹 Contoh A: Menukar Jadual Program
> *"Tolong ubah masa Rehat Kudapan dalam `_data/timeline.yml` dari jam 10:20 ke 10:30 pagi dan laraskan waktu modul seterusnya."*

### 🔹 Contoh B: Menukar Harga atau Item Bajet
> *"Tolong kemas kini harga doorgift dalam `_data/budget.yml` daripada RM 2.50 kepada RM 3.00 seorang dan kira semula jumlah besar Varian 2."*

### 🔹 Contoh C: Menukar Soalan Kuiz
> *"Tolong tukar Soalan 3 dalam `_data/quiz.yml` kepada soalan tentang bahaya pautan pancingan data (phishing) berserta jawapannya."*

### 🔹 Contoh D: Menukar Nama / Agihan Kru Meja
> *"Tolong tukar nama Mentor Meja 1 dalam `_data/crew.yml` dan `_data/tables.yml` kepada nama [Nama Pelajar]."*

### 🔹 Contoh E: Menambah Keperluan Alatan Aktiviti
> *"Tolong tambahkan 5 botol gam cecair dan 10 keping kadbod warna ke dalam senarai utiliti di `_data/operations.yml`."*

---

## 🛠️ 3. Bagaimana Perubahan Diterbitkan (Deployment Workflow)?

Selepas fail `.yml` diedit, anda hanya perlu jalankan arahan git biasa:

```bash
# 1. Tambah fail yang diubah
git add .

# 2. Simpan rekod commit
git commit -m "kemaskini: maklumat bajet dan jadual terkini"

# 3. Hantar ke GitHub
git push origin main
```

**Apa yang berlaku selepas itu?**
1. GitHub Actions akan mengesan push ke cawangan `main`.
2. Aliran kerja [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) akan membina (*build*) laman Jekyll secara automatik di pelayan cloud GitHub.
3. Laman web rasmi akan dikemas kini dalam masa **~45 saat** di:  
   👉 **https://xzrians.github.io/ITSeminar/**

---

## 📌 4. Peraturan Tetap Acara (Constraint Check)

Sila pastikan mana-mana pengemaskinian mematuhi 3 ketetapan utama ini:

1. **Formula Pax Dewan:**  
   $$\mathbf{47\ Murid\ ASDAF} + \mathbf{6\ Staf\ ASDAF} + \mathbf{13\ Kru\ UTM} = \mathbf{66\ Orang\ Pax}$$  
   *(Untuk tempahan makanan jamuan: Tambah 5 pek penampan = **71 Pax**).*

2. **Prinsip Sifar Gajet (Zero-Device Requirement):**  
   Pelajar asrama tidak dibenarkan membawa telefon pintar peribadi. Sebarang aktiviti kuiz atau latihan mestilah berasaskan fizikal, kertas mahjong, dan skrin projektor dewan.

3. **Inklusiviti Pendidikan Khas (PPKI):**  
   Terdapat 4 orang murid PPKI yang ditempatkan di meja kluster bersama bimbingan rapat mentor meja (Meja 1, Meja 4, Meja 5, Meja 6).

---

## 📂 5. Struktur Seni Bina Repositori

```text
├── .github/workflows/deploy.yml   # Enjin automasi build & deploy ke GitHub Pages
├── _config.yml                    # Tetapan rasmi Jekyll & pautan URL repositori
├── _data/                         # 9 fail pengurusan data YAML (SUMBER UTAMA KANDUNGAN)
├── _includes/                     # Komponen reka bentuk Liquid HTML modular
│   ├── asdaf.html                 # Profil ASDAF
│   ├── budget.html                # Paparan 3 varian bajet & banner pax
│   ├── checklist.html             # Senarai semak interaktif
│   ├── crew.html                  # 13 kru UTM
│   ├── hero.html                  # Banner atas
│   ├── navbar.html                # Menu navigasi atas
│   ├── operations.html            # Operasi terperinci (tab switcher)
│   ├── quiz.html                  # 5 kad kuiz pantas
│   ├── stats.html                 # 6 kad statistik KPI
│   ├── tables.html                # 7 meja kluster
│   └── timeline.html              # Garis masa & carta aliran Mermaid.js
├── _layouts/default.html          # Template asas HTML (Google Fonts, Lucide, CSS)
├── assets/
│   ├── css/styles.css             # Sistem gaya tema dark mode & glassmorphism
│   └── js/app.js                  # Logik interaktif (tabs, reveal, simpanan local)
├── AGENTS.md                      # Panduan khusus untuk dibaca oleh model AI
├── GUIDELINE.md                   # Buku panduan kemas kini ini
├── README.md                      # Kertas cadangan master & ringkasan acara
└── index.html                     # Halaman utama laman web
```
