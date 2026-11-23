

# DATA DUMMY PENGHUNI
data_penghuni = [
    {
        "id": "P001",
        "nama": "Andi Saputra",
        "no_hp": "081234567890",
        "asal": "Semarang",
        "jenis_kelamin": "Laki-laki"
    },
    {
        "id": "P002",
        "nama": "Budi Santoso",
        "no_hp": "082345678901",
        "asal": "Kendal",
        "jenis_kelamin": "Laki-laki"
    },
    {
        "id": "P003",
        "nama": "Citra Maharani",
        "no_hp": "083456789012",
        "asal": "Salatiga",
        "jenis_kelamin": "Perempuan"
    }
]


# 1. TAMBAH PENGHUNI
def tambah_penghuni():
    print("\n=== TAMBAH PENGHUNI ===")

    id_penghuni = input("Masukkan ID Penghuni: ")

    for penghuni in data_penghuni:
        if penghuni["id"] == id_penghuni:
            print("ID sudah digunakan!")
            return

    nama = input("Masukkan Nama: ")
    no_hp = input("Masukkan No HP: ")
    asal = input("Masukkan Asal: ")
    jenis_kelamin = input("Masukkan Jenis Kelamin: ")

    penghuni_baru = {
        "id": id_penghuni,
        "nama": nama,
        "no_hp": no_hp,
        "asal": asal,
        "jenis_kelamin": jenis_kelamin
    }

    data_penghuni.append(penghuni_baru)

    print("Data penghuni berhasil ditambahkan!")


# 2. TAMPILKAN PENGHUNI
def tampilkan_penghuni():
    print("\n=== DAFTAR PENGHUNI ===")

    if len(data_penghuni) == 0:
        print("Belum ada data penghuni.")
    else:
        for penghuni in data_penghuni:
            print("----------------------")
            print("ID              :", penghuni["id"])
            print("Nama            :", penghuni["nama"])
            print("No HP           :", penghuni["no_hp"])
            print("Asal            :", penghuni["asal"])
            print("Jenis Kelamin   :", penghuni["jenis_kelamin"])


# 3. UBAH PENGHUNI
def ubah_penghuni():
    print("\n=== UBAH DATA PENGHUNI ===")

    id_penghuni = input("Masukkan ID Penghuni: ")

    for penghuni in data_penghuni:
        if penghuni["id"] == id_penghuni:

            print("Data ditemukan!")

            penghuni["nama"] = input("Nama baru: ")
            penghuni["no_hp"] = input("No HP baru: ")
            penghuni["asal"] = input("Asal baru: ")
            penghuni["jenis_kelamin"] = input("Jenis Kelamin baru: ")

            print("Data berhasil diubah!")
            return

    print("ID penghuni tidak ditemukan!")


# 4. HAPUS PENGHUNI
def hapus_penghuni():
    print("\n=== HAPUS DATA PENGHUNI ===")

    id_penghuni = input("Masukkan ID Penghuni: ")

    for penghuni in data_penghuni:
        if penghuni["id"] == id_penghuni:

            konfirmasi = input("Yakin hapus data? (y/n): ")

            if konfirmasi == "y":
                data_penghuni.remove(penghuni)
                print("Data berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan!")

            return

    print("ID penghuni tidak ditemukan!")


# 5. MENU MANAJEMEN PENGHUNI
def menu_penghuni():

    while True:
        print("\n===== MANAJEMEN PENGHUNI =====")
        print("1. Tambah Penghuni")
        print("2. Tampilkan Penghuni")
        print("3. Ubah Penghuni")
        print("4. Hapus Penghuni")
        print("5. Kembali")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_penghuni()

        elif pilihan == "2":
            tampilkan_penghuni()

        elif pilihan == "3":
            ubah_penghuni()

        elif pilihan == "4":
            hapus_penghuni()

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak valid!")


# MENJALANKAN PROGRAM
menu_penghuni()
