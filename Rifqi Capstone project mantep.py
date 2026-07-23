# KUFAKU PROJECT - RENTAL MOBIL (versi rapi)
# Fitur: CRUD mobil + sewa mobil (dengan hitungan lama sewa & pembayaran) + pengembalian mobil
# Data mobil: id, merk, tipe, tahun, harga sewa/hari, status (Tersedia/Disewa)
# mobil ada 5, fitur nya ada CRUD + pengen nyewa atau pengen balikin. 
# isi menu (id, merk, tipe mobil, mobil tahun brp, harga sewa, sama tersedia apa engga)
# bedain di sewa sama tersedia 
# bikin konsep 2 udah di sewa kali yak, jadi bisa di sewa nya 3 yg ga bisa di sewa nya 2 
#  
mobil = [
    {"id": 101, "merk": "Toyota",     "tipe": "Avanza", "tahun": 2022, "harga": 350000, "status": "Tersedia"},
    {"id": 102, "merk": "Honda",      "tipe": "Brio",    "tahun": 2021, "harga": 300000, "status": "Disewa"},
    {"id": 103, "merk": "Toyota",     "tipe": "Innova",  "tahun": 2023, "harga": 500000, "status": "Tersedia"},
    {"id": 104, "merk": "Mitsubishi", "tipe": "Pajero",  "tahun": 2020, "harga": 700000, "status": "Tersedia"},
    {"id": 105, "merk": "Suzuki",     "tipe": "Ertiga",  "tahun": 2022, "harga": 325000, "status": "Disewa"},
]


def menu():
    print("\n======================================")
    print("             KUFAKU RENT             ")
    print("======================================")
    print("1. Lihat Data Mobil")
    print("2. Tambah Mobil")
    print("3. Update Data Mobil")
    print("4. Hapus Data Mobil")
    print("5. Rental Mobil")
    print("6. Pengembalian Mobil")
    print("7. Keluar")
    print("======================================")


def input_angka(teks):
    # Helper biar input angka ga bikin program crash kalau salah ketik
    while True:
        nilai = input(teks)
        if nilai.isdigit():
            return int(nilai)
        print("Input harus berupa angka. Coba lagi.")


def cari_mobil(id_mobil):
    # Mencari mobil berdasarkan id (primary key)
    for m in mobil:
        if m["id"] == id_mobil:
            return m
    return None


def tampilkan_data(data):
    print(f"ID     : {data['id']}")
    print(f"Merk   : {data['merk']}")
    print(f"Tipe   : {data['tipe']}")
    print(f"Tahun  : {data['tahun']}")
    print(f"Harga  : {data['harga']} / hari")
    print(f"Status : {data['status']}")


def read():
    while True:
        print("\n=== MENU READ ===")
        print("1. Tampilkan Semua Data")
        print("2. Cari Data Berdasarkan ID")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan menu : ")

        if pilihan == "1":
            if len(mobil) == 0:
                print("\nData mobil tidak tersedia.")
            else:
                print("\nDaftar Mobil:")
                for m in mobil:
                    print("---------------------------")
                    tampilkan_data(m)

        elif pilihan == "2":
            id_cari = input_angka("Masukkan id mobil yang dicari : ")
            data = cari_mobil(id_cari)

            if data is not None:
                print("\n--- Detail Mobil ---")
                tampilkan_data(data)
            else:
                print("\nData dengan ID tersebut tidak ditemukan.")

        elif pilihan == "3":
            break

        else:
            print("\nMenu tidak tersedia.")


def create():
    while True:
        print("\n=== MENU CREATE ===")
        print("1. Tambah Data Mobil")
        print("2. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan menu : ")

        if pilihan == "1":
            id_baru = input_angka("Masukkan ID mobil baru : ")

            if cari_mobil(id_baru) is not None:
                print("\nData dengan ID tersebut sudah ada. Gunakan ID lain.")
                continue

            merk = input("Masukkan merk mobil : ")
            tipe = input("Masukkan tipe mobil : ")
            tahun = input_angka("Masukkan tahun mobil : ")
            harga = input_angka("Masukkan harga sewa mobil (per hari) : ")
            status = "Tersedia"

            print("\nData yang akan disimpan:")
            print(f"ID     : {id_baru}")
            print(f"Merk   : {merk}")
            print(f"Tipe   : {tipe}")
            print(f"Tahun  : {tahun}")
            print(f"Harga  : {harga} / hari")
            print(f"Status : {status}")

            simpan = input("\nSimpan data ini? (y/n) : ").lower()

            if simpan == "y":
                mobil.append({
                    "id": id_baru,
                    "merk": merk,
                    "tipe": tipe,
                    "tahun": tahun,
                    "harga": harga,
                    "status": status,
                })
                print("\nData berhasil disimpan.")
            else:
                print("\nData dibatalkan.")

        elif pilihan == "2":
            break

        else:
            print("\nMenu tidak tersedia.")


def update():
    kolom_valid = ["merk", "tipe", "tahun", "harga", "status"]

    while True:
        print("\n=== MENU UPDATE ===")
        print("1. Update Data Mobil")
        print("2. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan menu : ")

        if pilihan == "1":
            id_update = input_angka("Masukkan ID mobil yang ingin diupdate : ")
            data = cari_mobil(id_update)

            if data is None:
                print("\nData yang Anda cari tidak ditemukan.")
                continue

            print("\nData ditemukan:")
            tampilkan_data(data)

            lanjut = input("\nLanjutkan update? (y/n) : ").lower()
            if lanjut != "y":
                continue

            print("\nKolom yang bisa diubah: merk, tipe, tahun, harga, status")
            kolom = input("Masukkan nama kolom yang ingin diubah : ").lower()

            if kolom not in kolom_valid:
                print("\nNama kolom tidak valid.")
                continue

            if kolom in ("tahun", "harga"):
                nilai_baru = input_angka(f"Masukkan nilai baru untuk {kolom} : ")
            else:
                nilai_baru = input(f"Masukkan nilai baru untuk {kolom} : ")

            print(f"\n{kolom} akan diubah menjadi: {nilai_baru}")
            konfirmasi = input("Update data ini? (y/n) : ").lower()

            if konfirmasi == "y":
                data[kolom] = nilai_baru
                print("\nData berhasil diupdate.")
            else:
                print("\nUpdate dibatalkan.")

        elif pilihan == "2":
            break

        else:
            print("\nMenu tidak tersedia.")


def delete():
    while True:
        print("\n=== MENU DELETE ===")
        print("1. Hapus Data Mobil")
        print("2. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan menu : ")

        if pilihan == "1":
            id_hapus = input_angka("Masukkan ID mobil yang ingin dihapus : ")
            data = cari_mobil(id_hapus)

            if data is None:
                print("\nData yang Anda cari tidak ditemukan.")
                continue

            print("\nData yang akan dihapus:")
            tampilkan_data(data)

            konfirmasi = input("\nYakin ingin menghapus data ini? (y/n) : ").lower()

            if konfirmasi == "y":
                mobil.remove(data)
                print("\nData berhasil dihapus.")
            else:
                print("\nPenghapusan dibatalkan.")

        elif pilihan == "2":
            break

        else:
            print("\nMenu tidak tersedia.")


def rental():
    print("\n=== MENU RENTAL ===")
    id_sewa = input_angka("Masukkan ID mobil yang ingin disewa : ")
    data = cari_mobil(id_sewa)

    if data is None:
        print("\nData mobil tidak ditemukan.")
        return

    if data["status"] == "Disewa":
        print("\nMobil ini sedang disewa oleh orang lain. Silakan pilih mobil lain.")
        return

    lama_sewa = input_angka("Masukkan berapa hari ingin disewa : ")

    if lama_sewa <= 0:
        print("\nJumlah hari tidak valid.")
        return

    total_harga = data["harga"] * lama_sewa

    print(f"\nMobil {data['merk']} {data['tipe']} tersedia dengan harga {data['harga']} / hari.")
    print("\n--- Rincian Sewa Mobil ---")
    print(f"Mobil       : {data['merk']} {data['tipe']}")
    print(f"Harga/Hari  : {data['harga']}")
    print(f"Lama Sewa   : {lama_sewa} hari")
    print(f"Total Harga : {total_harga}")

    konfirmasi = input("\nLanjutkan penyewaan mobil ini? (y/n) : ").lower()

    if konfirmasi != "y":
        print("\nPenyewaan dibatalkan.")
        return

    while True:
        uang_bayar = input_angka("\nMasukkan jumlah uang yang dibayar : ")
        if uang_bayar < total_harga:
            kurang = total_harga - uang_bayar
            print(f"\nUang yang dibayarkan kurang sebesar {kurang}. Masukkan uang lagi.")
            continue
        break

    kembalian = uang_bayar - total_harga
    data["status"] = "Disewa"

    print("\nPembayaran berhasil.")
    print(f"Total Bayar : {uang_bayar}")
    print(f"Kembalian   : {kembalian}")
    print(f"\nMobil berhasil disewa selama {lama_sewa} hari. Selamat menikmati perjalanan!")


def pengembalian():
    print("\n=== MENU PENGEMBALIAN ===")
    id_kembali = input_angka("Masukkan ID mobil yang ingin dikembalikan : ")
    data = cari_mobil(id_kembali)

    if data is None:
        print("\nData mobil tidak ditemukan.")
        return

    if data["status"] == "Tersedia":
        print("\nMobil ini tidak sedang dalam status disewa.")
        return

    data["status"] = "Tersedia"
    print("\nMobil berhasil dikembalikan. Terima kasih telah menggunakan KUFAKU RENT!")


def main():
    while True:
        menu()
        pilihan = input("Masukkan pilihan menu : ")

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
            print("\nTerima kasih telah mempercayai kami.")
            break
        else:
            print("\nMenu tidak tersedia.")


if __name__ == "__main__":
    main()
