# File Organizer

Skrip ini digunakan untuk mengorganisir file dalam folder tertentu ke dalam subfolder berdasarkan ekstensi file mereka. File akan dipindahkan ke folder yang sesuai dengan kategori yang telah ditentukan.

## Fitur

- Mengorganisir file berdasarkan ekstensi ke dalam folder yang telah ditentukan.
- Mendukung berbagai jenis file, termasuk dokumen, gambar, video, audio, dan lainnya.
- Folder baru akan dibuat jika belum ada.

## Kategori yang Didukung

Berikut adalah kategori file yang didukung oleh skrip ini:

- **TXT**: File teks (`.txt`)
- **PDF**: File PDF (`.pdf`)
- **WORD**: Dokumen Word (`.doc`, `.docx`)
- **EXCEL**: File Excel (`.xls`, `.xlsx`)
- **PPT**: Presentasi (`.ppt`, `.pptx`)
- **Picture**: Gambar (`.jpg`, `.jpeg`, `.png`, `.gif`)
- **Video**: File video (`.mp4`, `.mkv`, `.avi`)
- **Audio**: File audio (`.mp3`, `.wav`)
- **Zip**: File arsip (`.zip`, `.rar`)
- **SVG**: File SVG (`.svg`)
- **ETC**: Kategori untuk file dengan ekstensi lainnya

## Persyaratan

- Python 3.x
- Modul `os` dan `shutil` (sudah termasuk dalam Python standard library)

## Instalasi

1. Pastikan Python sudah terpasang di sistem Anda.
2. Salin kode skrip ke dalam file Python, misalnya `organizer.py`.

## Penggunaan

1. Jalankan skrip menggunakan terminal atau command prompt:

   ```bash
   python organizer.py
   ```
    atau
   ```bash
   python3 organizer.py
