Enkripsi dan Dekripsi Data Menggunakan AES dengan LZString
Copyright © 2023 oleh Totok Hermawan

Skrip Python ini menunjukkan cara mengenkripsi dan mendekripsi data menggunakan algoritma Advanced Encryption Standard (AES) dalam mode Cipher Block Chaining (CBC) dengan kompresi LZString.

## Persyaratan

Pastikan Anda telah menginstal Python di sistem Anda.

Instal paket yang diperlukan dengan menggunakan perintah berikut:

```bash
pip install pycryptodome python-lzstring python-dotenv

Memulai
Klon repositori ini atau unduh berkas skrip.

Buat berkas .env di direktori yang sama dengan skrip dengan konten berikut:

dotenv
SECRET_KEY=kunci_rahasia_anda
CONS_ID=id_konsumen_anda

Gantilah kunci_rahasia_anda dan id_konsumen_anda dengan kunci rahasia dan ID konsumen Anda yang sebenarnya.

Opsional, Anda dapat menyediakan data yang akan dienkripsi di dalam skrip (gantilah "Sample Text" pada variabel data_to_encrypt).

Jalankan skrip:

python nama_skrip.py
Gantilah nama_skrip.py dengan nama sebenarnya dari berkas skrip Python Anda.

Skrip akan menghasilkan teks terenkripsi dan kemudian mendekripsinya untuk menampilkan data asli.

Catatan Penting
Pastikan bahwa berkas sample.json ada di direktori yang sama jika Anda membaca data dari berkas JSON.

Pastikan untuk menjaga kunci rahasia dan ID konsumen Anda tetap aman dan jangan membagikannya secara publik.

Silakan sesuaikan skrip sesuai dengan kebutuhan spesifik Anda.