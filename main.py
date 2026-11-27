def menu_kamar():

    while True:

        print("\n===== MENU KAMAR =====")
        print("1. Tambah Kamar")
        print("2. Daftar Kamar")
        print("3. Cari Kamar")
        print("4. Edit Kamar")
        print("5. Hapus Kamar")
        print("6. Status Kamar")
        print("0. Kembali")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            tambah_kamar()

        elif pilih == "2":
            lihat_daftar_kamar()

        elif pilih == "3":
            cari_kamar()

        elif pilih == "4":
            edit_kamar()

        elif pilih == "5":
            hapus_kamar()

        elif pilih == "6":
            status_kamar()

        elif pilih == "0":
            break

        else:
            print("PILIHAN TIDAK VALID")


# ==========================
# MENU PENGHUNI
# ==========================

def menu_penghuni():

    while True:

        print("\n===== MENU PENGHUNI =====")
        print("1. Tambah Penghuni")
        print("2. Lihat Penghuni")
        print("3. Edit Penghuni")
        print("4. Hapus Penghuni")
        print("5. Status Penghuni")
        print("0. Kembali")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            tambah_penghuni()

        elif pilih == "2":
            lihat_penghuni()

        elif pilih == "3":
            edit_penghuni()

        elif pilih == "4":
            hapus_penghuni()

        elif pilih == "5":
            status_penghuni()

        elif pilih == "0":
            break

        else:
            print("PILIHAN TIDAK VALID")


# ==========================
# MENU PENYEWAAN
# ==========================

def menu_penyewaan():

    while True:

        print("\n===== MENU PENYEWAAN =====")
        print("1. Tambah Penyewaan")
        print("2. Lihat Penyewaan")
        print("3. Edit Status Penyewaan")
        print("4. Penghuni Keluar")
        print("5. Riwayat Penyewaan")
        print("0. Kembali")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            tambah_penyewaan()

        elif pilih == "2":
            lihat_penyewaan()

        elif pilih == "3":
            edit_penyewaan()

        elif pilih == "4":
            penghuni_keluar()

        elif pilih == "5":
            riwayat_penyewaan()

        elif pilih == "0":
            break

        else:
            print("PILIHAN TIDAK VALID")


# ==========================
# MENU PEMBAYARAN
# ==========================

def menu_pembayaran():

    while True:

        print("\n===== MENU PEMBAYARAN =====")
        print("1. Input Pembayaran")
        print("2. Riwayat Pembayaran")
        print("3. Status Pembayaran")
        print("0. Kembali")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            input_pembayaran()

        elif pilih == "2":
            riwayat_pembayaran()

        elif pilih == "3":
            status_pembayaran()

        elif pilih == "0":
            break

        else:
            print("PILIHAN TIDAK VALID")


# ==========================
# MENU LAPORAN
# ==========================

def menu_laporan():

    while True:

        print("\n===== MENU LAPORAN =====")
        print("1. Total Pendapatan")
        print("2. Daftar Belum Bayar")
        print("3. Backup Data")
        print("4. Muat Data")
        print("0. Kembali")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            total_pendapatan()

        elif pilih == "2":
            daftar_belum_bayar()

        elif pilih == "3":
            backup_data()

        elif pilih == "4":
            muat_data()

        elif pilih == "0":
            break

        else:
            print("PILIHAN TIDAK VALID")


# ==========================
# MENU UTAMA
# ==========================

def menu_utama():

    while True:

        print("\n======================================")
        print(" SISTEM MANAJEMEN KOS ")
        print("======================================")

        print("1. Manajemen Kamar")
        print("2. Manajemen Penghuni")
        print("3. Manajemen Penyewaan")
        print("4. Pembayaran")
        print("5. Laporan")
        print("0. Keluar")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            menu_kamar()

        elif pilih == "2":
            menu_penghuni()

        elif pilih == "3":
            menu_penyewaan()

        elif pilih == "4":
            menu_pembayaran()

        elif pilih == "5":
            menu_laporan()

        elif pilih == "0":

            print(
                "\nTERIMA KASIH TELAH MENGGUNAKAN SISTEM"
            )

            break

        else:

            print("PILIHAN TIDAK VALID")


# ==========================
# PROGRAM UTAMA
# ==========================

if __name__ == "__main__":
    menu_utama()
