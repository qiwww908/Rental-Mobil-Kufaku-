# KUFAKU RENT v2.0
# Capstone Project Python - versi terminal, beginner-friendly
# Data hanya disimpan selama program berjalan (belum memakai database/file).

from datetime import datetime

mobil = [
    {"id": 101, "merk": "Toyota", "tipe": "Avanza", "tahun": 2022, "harga": 350000, "status": "Tersedia"},
    {"id": 102, "merk": "Honda", "tipe": "Brio", "tahun": 2021, "harga": 300000, "status": "Disewa"},
    {"id": 103, "merk": "Toyota", "tipe": "Innova", "tahun": 2023, "harga": 500000, "status": "Tersedia"},
    {"id": 104, "merk": "Mitsubishi", "tipe": "Pajero", "tahun": 2020, "harga": 700000, "status": "Tersedia"},
    {"id": 105, "merk": "Suzuki", "tipe": "Ertiga", "tahun": 2022, "harga": 325000, "status": "Disewa"},
]
mobil_terhapus = []


def input_angka(pesan, minimum=None, maksimum=None, boleh_batal=False):
    """Meminta angka dan memeriksa batas nilainya."""
    while True:
        teks = input(pesan).strip()
        if boleh_batal and teks == "0":
            return 0
        if not teks.isdigit():
            print("Input harus berupa angka.")
            continue
        angka = int(teks)
        if minimum is not None and angka < minimum:
            print("Angka minimal:", minimum)
            continue
        if maksimum is not None and angka > maksimum:
            print("Angka maksimal:", maksimum)
            continue
        return angka


def input_teks(pesan):
    """Meminta teks yang tidak boleh kosong."""
    while True:
        teks = input(pesan).strip()
        if teks != "":
            return teks
        print("Teks tidak boleh kosong.")


def konfirmasi(pesan):
    """Meminta jawaban y atau n."""
    while True:
        jawaban = input(pesan + " (y/n): ").strip().lower()
        if jawaban == "y":
            return True
        if jawaban == "n":
            return False
        print("Masukkan y atau n.")


def cari_mobil(id_mobil):
    """Mencari satu mobil berdasarkan ID."""
    for data in mobil:
        if data["id"] == id_mobil:
            return data
    return None


def tampilkan_data(data):
    """Menampilkan detail satu mobil."""
    print("ID     :", data["id"])
    print("Merk   :", data["merk"])
    print("Tipe   :", data["tipe"])
    print("Tahun  :", data["tahun"])
    print("Harga  : Rp", format(data["harga"], ",").replace(",", "."), "/ hari")
    print("Status :", data["status"])


def tampilkan_tabel(daftar):
    """Menampilkan daftar mobil sebagai tabel sederhana."""
    if len(daftar) == 0:
        print("Tidak ada data mobil.")
        return
    print("-" * 87)
    print(f'{"ID":<6} {"Merk":<16} {"Tipe":<16} {"Tahun":<8} {"Harga/Hari":<18} {"Status":<10}')
    print("-" * 87)
    for data in daftar:
        harga = "Rp" + format(data["harga"], ",").replace(",", ".")
        print(f'{data["id"]:<6} {data["merk"][:16]:<16} {data["tipe"][:16]:<16} {data["tahun"]:<8} {harga:<18} {data["status"]:<10}')
    print("-" * 87)


def id_baru():
    """Membuat ID baru yang belum digunakan."""
    terbesar = 100
    for data in mobil:
        if data["id"] > terbesar:
            terbesar = data["id"]
    for data in mobil_terhapus:
        if data["id"] > terbesar:
            terbesar = data["id"]
    return terbesar + 1


def input_tahun():
    """Memastikan tahun mobil masuk akal."""
    tahun_sekarang = datetime.now().year
    return input_angka("Tahun mobil: ", 1990, tahun_sekarang)


def input_status():
    """Membatasi status pada dua pilihan."""
    print("1. Tersedia")
    print("2. Disewa")
    pilihan = input_angka("Pilih status: ", 1, 2)
    if pilihan == 1:
        return "Tersedia"
    return "Disewa"


def read():
    """Melihat, mencari, memfilter, dan mengurutkan data mobil."""
    while True:
        print("\n=== MENU LIHAT DATA ===")
        print("1. Semua mobil")
        print("2. Cari berdasarkan ID")
        print("3. Cari berdasarkan merk")
        print("4. Mobil tersedia")
        print("5. Urutkan harga termurah")
        print("6. Kembali")
        pilihan = input("Pilihan: ").strip()

        if pilihan == "1":
            tampilkan_tabel(mobil)
        elif pilihan == "2":
            id_cari = input_angka("ID mobil: ", 1)
            data = cari_mobil(id_cari)
            if data is None:
                print("Mobil tidak ditemukan.")
            else:
                tampilkan_data(data)
        elif pilihan == "3":
            kata = input_teks("Masukkan merk yang dicari: ").lower()
            hasil = []
            for data in mobil:
                if kata in data["merk"].lower():
                    hasil.append(data)
            tampilkan_tabel(hasil)
        elif pilihan == "4":
            hasil = []
            for data in mobil:
                if data["status"] == "Tersedia":
                    hasil.append(data)
            tampilkan_tabel(hasil)
        elif pilihan == "5":
            hasil = sorted(mobil, key=lambda data: data["harga"])
            tampilkan_tabel(hasil)
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak tersedia.")


def create():
    """Menambahkan mobil dengan validasi setiap kolom."""
    while True:
        print("\n=== TAMBAH MOBIL ===")
        print("1. Tambah mobil")
        print("2. Kembali")
        pilihan = input("Pilihan: ").strip()
        if pilihan == "2":
            break
        if pilihan != "1":
            print("Pilihan tidak tersedia.")
            continue

        nomor = id_baru()
        merk = input_teks("Merk mobil: ")
        tipe = input_teks("Tipe mobil: ")
        tahun = input_tahun()
        harga = input_angka("Harga sewa per hari: ", 1)
        data = {"id": nomor, "merk": merk, "tipe": tipe,
                "tahun": tahun, "harga": harga, "status": "Tersedia"}
        print("\nData baru:")
        tampilkan_data(data)
        if konfirmasi("Simpan mobil ini?"):
            mobil.append(data)
            print("Mobil berhasil ditambahkan.")
        else:
            print("Penambahan dibatalkan.")


def update():
    """Mengubah satu kolom mobil tanpa mengubah ID."""
    while True:
        print("\n=== UPDATE MOBIL ===")
        print("1. Update mobil")
        print("2. Kembali")
        pilihan = input("Pilihan: ").strip()
        if pilihan == "2":
            break
        if pilihan != "1":
            print("Pilihan tidak tersedia.")
            continue

        nomor = input_angka("ID mobil: ", 1)
        data = cari_mobil(nomor)
        if data is None:
            print("Mobil tidak ditemukan.")
            continue
        tampilkan_data(data)
        if not konfirmasi("Lanjut update?"):
            continue

        print("1. Merk  2. Tipe  3. Tahun  4. Harga  5. Status")
        kolom = input_angka("Pilih kolom: ", 1, 5)
        if kolom == 1:
            nama_kolom = "merk"
            nilai = input_teks("Merk baru: ")
        elif kolom == 2:
            nama_kolom = "tipe"
            nilai = input_teks("Tipe baru: ")
        elif kolom == 3:
            nama_kolom = "tahun"
            nilai = input_tahun()
        elif kolom == 4:
            nama_kolom = "harga"
            nilai = input_angka("Harga baru: ", 1)
        else:
            nama_kolom = "status"
            nilai = input_status()

        print("Perubahan:", nama_kolom, "dari", data[nama_kolom], "menjadi", nilai)
        if konfirmasi("Simpan perubahan?"):
            data[nama_kolom] = nilai
            print("Data berhasil diupdate.")
        else:
            print("Update dibatalkan.")


def delete():
    """Menghapus mobil dan menyimpannya di daftar pemulihan."""
    while True:
        print("\n=== HAPUS MOBIL ===")
        print("1. Hapus mobil")
        print("2. Lihat data terhapus")
        print("3. Restore mobil")
        print("4. Kembali")
        pilihan = input("Pilihan: ").strip()
        if pilihan == "4":
            break
        if pilihan == "1":
            if len(mobil) == 0:
                print("Data mobil sudah kosong.")
                continue
            tampilkan_tabel(mobil)
            nomor = input_angka("ID yang akan dihapus: ", 1)
            data = cari_mobil(nomor)
            if data is None:
                print("Mobil tidak ditemukan.")
            else:
                tampilkan_data(data)
                if konfirmasi("Yakin hapus?"):
                    mobil.remove(data)
                    mobil_terhapus.append(data)
                    print("Mobil dihapus dan dapat di-restore.")
        elif pilihan == "2":
            tampilkan_tabel(mobil_terhapus)
        elif pilihan == "3":
            if len(mobil_terhapus) == 0:
                print("Belum ada mobil yang dihapus.")
                continue
            tampilkan_tabel(mobil_terhapus)
            nomor = input_angka("ID yang ingin di-restore: ", 1)
            ditemukan = None
            for data in mobil_terhapus:
                if data["id"] == nomor:
                    ditemukan = data
                    break
            if ditemukan is None:
                print("ID tidak ada di daftar terhapus.")
            elif konfirmasi("Restore mobil ini?"):
                mobil.append(ditemukan)
                mobil_terhapus.remove(ditemukan)
                print("Mobil berhasil dikembalikan.")
        else:
            print("Pilihan tidak tersedia.")


def rental():
    """Menyewa mobil dan menghitung pembayaran."""
    print("\n=== RENTAL MOBIL ===")
    tersedia = []
    for data in mobil:
        if data["status"] == "Tersedia":
            tersedia.append(data)
    tampilkan_tabel(tersedia)
    if len(tersedia) == 0:
        return

    nomor = input_angka("ID mobil yang ingin disewa (0 untuk batal): ", 1, boleh_batal=True)
    if nomor == 0:
        print("Rental dibatalkan.")
        return
    data = cari_mobil(nomor)
    if data is None:
        print("Mobil tidak ditemukan.")
        return
    if data["status"] != "Tersedia":
        print("Mobil sedang disewa.")
        return

    hari = input_angka("Lama sewa (hari, 0 untuk batal): ", 1, boleh_batal=True)
    if hari == 0:
        print("Rental dibatalkan.")
        return
    total = data["harga"] * hari
    print("Mobil:", data["merk"], data["tipe"])
    print("Lama sewa:", hari, "hari")
    print("Total: Rp", format(total, ",").replace(",", "."))
    if not konfirmasi("Lanjutkan penyewaan?"):
        print("Rental dibatalkan.")
        return

    while True:
        bayar = input_angka("Uang pembayaran (0 untuk batal): ", 1, boleh_batal=True)
        if bayar == 0:
            print("Pembayaran dibatalkan.")
            return
        if bayar < total:
            print("Uang kurang Rp", format(total - bayar, ",").replace(",", "."))
            continue
        kembalian = bayar - total
        data["status"] = "Disewa"
        print("Pembayaran berhasil. Kembalian: Rp", format(kembalian, ",").replace(",", "."))
        break


def pengembalian():
    """Mengubah status mobil yang disewa menjadi tersedia."""
    print("\n=== PENGEMBALIAN MOBIL ===")
    disewa = []
    for data in mobil:
        if data["status"] == "Disewa":
            disewa.append(data)
    tampilkan_tabel(disewa)
    if len(disewa) == 0:
        return

    nomor = input_angka("ID mobil yang dikembalikan (0 untuk batal): ", 1, boleh_batal=True)
    if nomor == 0:
        print("Pengembalian dibatalkan.")
        return
    data = cari_mobil(nomor)
    if data is None:
        print("Mobil tidak ditemukan.")
    elif data["status"] != "Disewa":
        print("Mobil ini tidak sedang disewa.")
    elif konfirmasi("Konfirmasi pengembalian?"):
        data["status"] = "Tersedia"
        print("Mobil berhasil dikembalikan.")
    else:
        print("Pengembalian dibatalkan.")


def main():
    """Menjalankan menu utama program."""
    while True:
        print("\n========== KUFAKU RENT v2.0 ==========")
        print("1. Lihat Data Mobil")
        print("2. Tambah Mobil")
        print("3. Update Data Mobil")
        print("4. Hapus / Restore Mobil")
        print("5. Rental Mobil")
        print("6. Pengembalian Mobil")
        print("7. Keluar")
        pilihan = input("Pilihan: ").strip()
        if pilihan == "1":
            read()
        elif pilihan == "2":
            create()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            delete()
        elif pilihan == "5":
            rental()
        elif pilihan == "6":
            pengembalian()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan KUFAKU RENT!")
            break
        else:
            print("Menu tidak tersedia.")


if __name__ == "__main__":
    main()
