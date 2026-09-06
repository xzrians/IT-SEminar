# Reka Bentuk Spesifikasi: Mobile-First App Shell & Progressive Web App (PWA)
**Projek:** NextGen Tech Summit 2026 (UTM x ASDAF PERKIM)  
**Tarikh:** 7 September 2026  
**Status:** Draf untuk Semakan Pengguna  

---

## 1. Pengenalan & Latar Belakang Masalah

Laman wiki sedia ada mengandungi maklumat lengkap acara (profil ASDAF, jadual minit-ke-minit, silibus 2 modul, 16 slaid, 7 meja, 13 kru, 5 soalan kuiz, bajet RM800, dan utiliti). Walau bagaimanapun, analisis UI/UX mendapati:
1. **Keletihan Tatalan Vertikal (*Scroll Fatigue*):** Terdapat 10 seksyen bertindih secara menegak. Pada skrin telefon pintar, fasilitator terpaksa membuat tatalan (*scroll*) sehingga 10–12 skrin untuk mencari senarai semak atau soalan kuiz.
2. **Ketiadaan Navigasi Mudah Alih Natif:** Menu hamburger standard memerlukan 2–3 ketikan (*taps*) dan menutup pandangan skrin semasa.
3. **Risiko Ketiadaan Internet di Dewan Acara:** Lokasi Asrama Darul Falah di Bukit Persekutuan mempunyai liputan telekomunikasi yang berbeza-beza di dalam dewan. Jika sambungan internet terputus, laman web biasa akan gagal dimuat semula (*network error*).

### Matlamat Utama
- Menukar laman web kepada **Progressive Web App (PWA)** dengan sokongan luar talian 100% (*offline-first*) menggunakan Service Worker.
- Menyatukan (*consolidate*) 10 seksyen kepada **Mobile App Shell** dengan **Bar Navigasi Bawah (Bottom Navigation Bar)** mesra kawalan satu ibu jari (*one-thumb zone*).
- Membolehkan pemasangan aplikasi ke skrin utama telefon (*Add to Home Screen*) seperti aplikasi Android/iOS natif.

---

## 2. Seni Bina UI/UX: Mobile App Shell (4 Hab Utama)

Semua kandungan sedia ada (daripada fail YAML `_data/`) disusun semula ke dalam 4 hab berfokus yang boleh ditukar serta-merta tanpa memuat semula halaman (*zero reload*):

```
┌────────────────────────────────────────────────────────┐
│  HEADER ATAS: Logo | Tajuk | Status [🟢 Online] | 🖨️  │
├────────────────────────────────────────────────────────┤
│                                                        │
│                  KANDUNGAN HAB AKTIF                   │
│                                                        │
│  [Tab 1: Utama]   - Ringkasan KPI, ASDAF & Panduan     │
│  [Tab 2: Jadual]  - Atur Cara & 16 Slaid Pembentangan  │
│  [Tab 3: Meja]    - 7 Meja, 13 Kru, PPKI & Kuiz        │
│  [Tab 4: Logistik]- Bajet RM800, Makanan & Checklist   │
│                                                        │
├────────────────────────────────────────────────────────┤
│  NAVIGASI BAWAH: [⚡ Utama] [⏰ Jadual] [🪑 Meja] [🛠️ Ops] │
└────────────────────────────────────────────────────────┘
```

### Pecahan Kandungan 4 Hab:

#### Hab 1: ⚡ Hub Utama (`#tab-home`)
- **Hero & Countdown:** Tajuk acara, kiraan tarikh/waktu, lencana status bengkel.
- **KPI Metrik Pantas:** 47 Murid, 13 Kru, 6 Staf, 7 Meja, RM800 Bajet, 0 Telefon.
- **Profil Padat ASDAF:** Sejarah ringkas 1995, demografi Tingkatan 1–5, 4 murid PPKI.
- **Pautan Pintas:** Butang pantas ke Panduan Wiki (`GUIDELINE.md`).

#### Hab 2: ⏰ Atur Cara & Silibus (`#tab-timeline`)
- **Garis Masa Minit-ke-Minit:** 08:30 AM hingga 01:00 PM dengan penunjuk sesi semasa (*current session highlight*).
- **Sub-Tab Kurikulum & Pembentangan:**
  - *Ringkasan 2 Modul* (Celik AI & Keselamatan Siber).
  - *Rangka 16 Slaid Dewan* (Paparan kad slaid dengan nota penceramah).

#### Hab 3: 🪑 Meja, Kru & Interaktif (`#tab-people`)
- **7 Meja Kluster:** Susunan 3 Meja Lelaki & 4 Meja Perempuan berserta nama mentor bertugas.
- **Matriks 13 Kru UTM:** 6 Lead Pusat/Pentas & 7 Mentor Meja Dedikasi.
- **Kad Khas Inklusiviti PPKI:** 4 Prinsip santuni murid pendidikan khas di Meja 1, 4, 5, 6.
- **Kuiz Interaktif Showdown:** 5 Flashcard dengan butang pendedahan jawapan segera bagi kawalan pentas.

#### Hab 4: 🛠️ Logistik & Senarai Semak (`#tab-ops`)
- **Kalkulator & 3 Varian Bajet (RM800):** Paparan tab Varian 1 (Super-Lean), Varian 2 (Seimbang), dan Varian 3 (Penuh) berserta banner kiraan 71 pax.
- **Pek Dokumen & Makanan:** Strategi Kantin vs Luar (71 pax), goodies 47 murid, dan utiliti (kertas mahjong, marker, tape).
- **Checklist Operasi Interaktif:** Senarai semak Pra, Semasa dan Pasca acara dengan penyimpanan status automatik dalam `localStorage`.

---

## 3. Spesifikasi Progressive Web App (PWA)

Merujuk kepada dokumentasi Workbox (`/googlechrome/workbox`) dan piawaian W3C Web App Manifest:

### A. Web App Manifest (`manifest.webmanifest`)
- `name`: "NextGen Tech Summit 2026 | Panduan Fasilitator"
- `short_name`: "NextGen 2026"
- `start_url`: `{{ '/index.html' | relative_url }}`
- `scope`: `{{ '/' | relative_url }}`
- `display`: `standalone` (menghilangkan bar URL pelayar untuk pengalaman seumpama aplikasi natif)
- `background_color`: `#07090e`
- `theme_color`: `#07090e`
- `orientation`: `portrait-primary`
- `icons`:
  - 192x192 PNG/SVG (Ikon skrin utama Android/iOS)
  - 512x512 PNG/SVG (Ikon skrin percikan / splash screen)
  - Maskable icon (menyesuaikan dengan bentuk bulat/petak peranti Samsung, Pixel, iPhone)

### B. Service Worker (`sw.js`) & Strategi Caching
- **Skop:** Didaftarkan pada direktori punca repositori (`/IT-SEminar/`).
- **Nama Cache:** `nextgen-pwa-v1.0.0`
- **Strategi Precaching (App Shell):**
  - Mengasingkan dan memuat turun aset teras ke dalam cache pelayar semasa pemasangan pertama:
    - `index.html` (App Shell)
    - `assets/css/styles.css`
    - `assets/js/app.js`
    - `manifest.webmanifest`
    - Ikon aplikasi SVG
- **Strategi Runtime Caching (Stale-While-Revalidate):**
  - Memaparkan kandungan daripada cache serta-merta (kelajuan 0ms) sambil meminta kemas kini terkini dari rangkaian di latar belakang.
  - Sesuai untuk Google Fonts, Lucide Icons, dan CDN Mermaid.js.
- **Ketahanan Luar Talian (100% Offline Resilience):**
  - Sekiranya fasilitator membuka aplikasi tanpa capaian internet di dewan ASDAF, Service Worker menghantar kandungan cached tanpa sebarang skrin ralat.

### C. Penunjuk Status Rangkaian & Butang Pemasangan
- Header aplikasi memaparkan lencana hidup:
  - `🟢 Dalam Talian` (Sambungan aktif)
  - `📶 Mod Luar Talian` (Beroperasi daripada cache peranti)
- Prompt pemasangan automatik / butang *"Pasang Aplikasi"* apabila pelayar menyokong `beforeinstallprompt`.

---

## 4. Reka Bentuk Responsif & Degradasi Anggun (Desktop / Tablet)

- **Pada Skrin Telefon Pintar (< 768px):**
  - Bar navigasi bawah diaktifkan secara kekal dengan ikon bersaiz besar mesra sentuhan.
  - Header atas diringkaskan kepada format bar status.
- **Pada Skrin Tablet & Komputer Riba (> 768px):**
  - Bar navigasi bawah disorokkan secara automatik.
  - Navigasi atas berubah menjadi tab horizontal moden atau bar sisi kemas dengan ruang kerja yang selesa.
  - Mod cetakan (`window.print()`) kekal menyokong susun atur format dokumen kertas A4 untuk edaran mesyuarat.

---

## 5. Pelan Pengesahan & Pengujian

1. **Ujian PWA & Lighthouse:**
   - Skor PWA Lighthouse > 90% (Installable, Service Worker registered, valid manifest, HTTPS ready).
2. **Ujian Luar Talian (Offline Test):**
   - Matikan sambungan internet (Mod Penerbangan / DevTools Offline) dan uji muat semula laman web — pastikan semua modul, jadual dan kuiz kekal boleh diakses.
3. **Ujian Responsif Peranti Mudah Alih:**
   - iPhone SE (375px), iPhone 14 (390px), Android Samsung S21 (360px), dan iPad Mini (768px).
   - Pastikan tiada limpahan teks melintang (*horizontal overflow*) dan zon sentuhan butang mencukupi (*min-height: 44px*).
4. **Ujian Persistensi Checklist:**
   - Tanda semak beberapa tugasan operasi, tutup pelayar, buka semula — pastikan status kekal tersimpan melalui `localStorage`.
