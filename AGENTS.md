# Panduan AI Agent: Struktur & Peraturan Pengemaskinian Wiki NextGen Celik Digital

Selamat datang, AI Agent. Dokumen ini bertujuan untuk memberi panduan segera tentang seni bina repositori ini supaya anda boleh terus mengemas kini maklumat tanpa perlu membuang masa menganalisis fail-fail yang tidak berkaitan.

---

## 1. Seni Bina Projek (Jekyll on GitHub Pages via GitHub Actions)
- Repositori ini ialah **Jekyll Static Site Generator** yang dihoskan di GitHub Pages (`https://xzrians.github.io/ITSeminar/`).
- GitHub Actions dibina secara automatik melalui `.github/workflows/deploy.yml` setiap kali cawangan `main` menerima perubahan (`git push origin main`).
- **PRINSIP TERAS:** **DATA-DRIVEN**. Jangan ubah teks atau angka secara hardcoded di dalam fail HTML jika data tersebut berada di dalam folder `_data/`. Kemas kini fail YAML berkenaan, dan Liquid template akan menjana paparan secara automatik.

---

## 2. Peta Rujukan Pantas: Fail Mana Yang Perlu Diedit?

| Anda Ingin Mengubah... | Fail Sasaran Utama | Format |
| :--- | :--- | :--- |
| **Bajet, Siling RM800, Varian Kos, Formula Pax Jamuan (66+5=71)** | `_data/budget.yml` | YAML |
| **Pek Dokumen Tak Hadir, Makanan Kantin/Luar, Goodies, Utiliti (Mahjong dll.)** | `_data/operations.yml` | YAML |
| **Jadual Atur Cara, Waktu Minit-ke-Minit, PIC Sesi** | `_data/timeline.yml` | YAML |
| **Silibus Modul, 16 Slaid Pembentangan, 4 Aktiviti Meja & PPKI** | `_data/curriculum.yml` | YAML |
| **7 Meja Kluster, Agihan Murid T1–T5, Murid PPKI, Mentor** | `_data/tables.yml` | YAML |
| **Soalan Kuiz Pantas (5 Soalan Tanpa Gajet), Jawapan, Hadiah** | `_data/quiz.yml` | YAML |
| **Senarai 13 Kru UTM & Skop Tanggungjawab** | `_data/crew.yml` | YAML |
| **Senarai Semak Tindakan (Pra, Semasa, Pasca)** | `_data/checklist.yml` | YAML |
| **Latar Belakang ASDAF, Demografi, Prinsip Pedagogi** | `_data/asdaf.yml` | YAML |
| **Nombor Statistik Header (KPI 47 murid, 13 kru, dll.)** | `_data/stats.yml` | YAML |
| **Tajuk Tapak, Deskripsi, Base URL GitHub Pages** | `_config.yml` | YAML |
| **Reka Bentuk / Komponen Liquid** | `_includes/*.html` | Liquid HTML |
| **Sistem Reka Bentuk CSS / Gaya Dark Mode** | `assets/css/styles.css` | Vanilla CSS |
| **Logik Interaktif (Tabs, Quiz Toggle, LocalStorage)** | `assets/js/app.js` | Vanilla JS |
| **Laporan Master / Playbook Acara Offline** | `README.md` | Markdown |

---

## 3. Peraturan Wajib untuk AI
1. **Kekalkan Formula Pax Rasmi:**
   - Asas Bilik: $47\text{ Pelajar ASDAF} + 6\text{ Staf ASDAF} + 13\text{ Pelajar UTM} = \mathbf{66\text{ Pax Keseluruhan}}$.
   - Makanan Jamuan: $66\text{ Pax Asas} + 5\text{ Pax Penampan (Buffer)} = \mathbf{71\text{ Pax}}$.
2. **Kekalkan Prinsip Sifar Gajet (Zero-Device Requirement):**
   - Pelajar asrama tidak dibenarkan membawa telefon pintar peribadi. Kuiz mestilah dijalankan di layar skrin dewan dengan mekanik "3, 2, 1... Angkat Tangan!".
3. **Inklusiviti Pendidikan Khas (PPKI):**
   - 4 orang pelajar PPKI diletakkan di Meja 1, Meja 4, Meja 5, dan Meja 6 dengan bimbingan mentor meja berdedikasi.
4. **Aliran Kerja Deployment:**
   - Setiap kali melakukan perubahan, jalankan:
     `git add .`  
     `git commit -m "update: [keterangan ringkas]"`  
     `git push origin main`  
   - GitHub Actions akan terus menjalankan build & publish secara automatik.
