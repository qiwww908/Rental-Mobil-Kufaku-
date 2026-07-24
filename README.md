# Sistem Rental Mobil KUFAKU RENT

> **Capstone Project Module 2 — Python Fundamentals**
> Aplikasi CLI (Command Line Interface) untuk mengelola data rental mobil menggunakan Python dasar.

---

## Deskripsi

**KUFAKU RENT** adalah aplikasi berbasis terminal yang dibuat untuk mengelola data rental mobil. Aplikasi ini mengimplementasikan operasi **CRUD** (Create, Read, Update, Delete) sebagai fitur utama, dilengkapi dengan fitur tambahan berupa sistem penyewaan mobil (rental) lengkap dengan perhitungan biaya sewa, pembayaran, dan pengembalian mobil.

Seluruh menu utama dibangun menggunakan **regular function** dan data disimpan dalam **list of dictionary**, sesuai dengan materi yang dipelajari. Tidak menggunakan OOP maupun library eksternal.

---

## Fitur

### Fitur Utama (CRUD)
- **Create** — Menambah data mobil baru dengan validasi ID duplikat dan konfirmasi sebelum simpan.
- **Read** — Menampilkan seluruh data mobil atau mencari berdasarkan ID.
- **Update** — Mengubah data mobil pada kolom tertentu (merk, tipe, tahun, harga, status) dengan konfirmasi.
- **Delete** — Menghapus data mobil dengan konfirmasi terlebih dahulu.

### Fitur Tambahan
- **Rental Mobil** — Sewa mobil dengan perhitungan otomatis (harga per hari x lama sewa), lengkap dengan validasi ketersediaan mobil.
- **Sistem Pembayaran** — Uang yang dibayarkan divalidasi sampai cukup; jika lebih, kembalian dihitung otomatis.
- **Pengembalian Mobil** — Mengembalikan mobil yang sedang disewa, status otomatis balik jadi "Tersedia".
- **Validasi Input** — Mencegah input tidak valid (misalnya huruf pada kolom angka) lewat fungsi `input_angka()`.
- **Konfirmasi Aksi** — Konfirmasi sebelum menyimpan, mengubah, atau menghapus data.

---

## Struktur Data

Setiap mobil memiliki **6 field**, dengan `id` sebagai kolom unik:

| Field    | Tipe    | Keterangan                          |
|----------|---------|--------------------------------------|
| `id`     | integer | ID unik mobil (contoh: 101)          |
| `merk`   | string  | Merk mobil (Toyota, Honda, dll)      |
| `tipe`   | string  | Tipe/model mobil                     |
| `tahun`  | integer | Tahun produksi mobil                 |
| `harga`  | integer | Harga sewa per hari (Rupiah)         |
| `status` | string  | Status mobil (Tersedia/Disewa)       |

Data awal berisi 5 mobil (3 berstatus Tersedia, 2 berstatus Disewa).

---

## Instalasi

### Prasyarat
- Python 3.x
- Tidak ada library eksternal yang dibutuhkan

### Langkah-langkah

1. Clone repository ini:
   ```bash
   git clone https://github.com/USERNAME/nama-repo.git
   cd nama-repo
   ```

2. Jalankan program:
   ```bash
   python "Rifqi_Capstone_project_mantep.py"
   ```

---

## Cara Penggunaan

Setelah program dijalankan, akan muncul menu utama:

```
======================================
             KUFAKU RENT
======================================
1. Lihat Data Mobil
2. Tambah Mobil
3. Update Data Mobil
4. Hapus Data Mobil
5. Rental Mobil
6. Pengembalian Mobil
7. Keluar
======================================
```

Pilih menu dengan mengetik angka **1–7**, lalu ikuti petunjuk pada layar.

### Contoh: Sistem Rental & Pembayaran

Saat menyewa mobil dengan harga Rp350.000/hari selama 3 hari (total Rp1.050.000):
- Jika Anda membayar Rp1.000.000 → sistem meminta kekurangan Rp50.000.
- Anda tambah Rp100.000 → total menjadi Rp1.100.000 → pembayaran **berhasil**, kembalian Rp50.000.
- Status mobil otomatis berubah menjadi "Disewa" sampai dikembalikan lewat menu Pengembalian.

---

## Struktur Kode

Program terbagi menjadi beberapa bagian:

1. **Data (Collection)** — list of dictionary berisi data mobil.
2. **Fungsi Bantu** — fungsi yang dipakai berulang (`cari_mobil`, `input_angka`, `tampilkan_data`).
3. **Fitur Read** — menampilkan & mencari data mobil.
4. **Fitur Create** — menambah data mobil.
5. **Fitur Update** — mengubah data mobil.
6. **Fitur Delete** — menghapus data mobil.
7. **Fitur Rental** — proses penyewaan mobil beserta pembayaran.
8. **Fitur Pengembalian** — proses pengembalian mobil.
9. **Menu Utama** — pusat kendali program (looping).

---

## Teknologi

- **Python 3** — bahasa pemrograman utama, tanpa library eksternal.

---

## Konsep yang Diterapkan

- Data collection (list & dictionary)
- Conditional statement (if / elif / else)
- Looping (for & while)
- Regular function & return value
- Input validation
- String formatting (f-string)

---

## Batasan

- Data tidak tersimpan permanen — akan reset setiap kali program dijalankan ulang.
- Belum ada validasi format untuk merk/tipe (bebas teks apapun).
- Single-user, dijalankan lewat terminal.

---

## Penulis

**Rifqi Adhadiaufa**
Capstone Project Module 2
