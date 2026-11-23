import json

# Tuple
STATUS_PENGHUNI = (
    "aktif",
    "tidak aktif"
)


def baca_data():

    try:
        file = open("penghuni.json", "r")
        data = json.load(file)
        file.close()

        return data

    except:
        return []


def simpan_data(data):

    file = open("penghuni.json", "w")

    json.dump(data, file, indent=4)

    file.close()


def id_sudah_ada(data, id_penghuni):

    # Set
    daftar_id = set()

    for penghuni in data:
        daftar_id.add(penghuni["id"])

    return id_penghuni in daftar_id


def tambah_penghuni():

    data = baca_data()

    print("\n=== TAMBAH PENGHUNI ===")

    while True:

        id_penghuni = input("Masukkan ID Penghuni : ").upper()

        if id_penghuni == "":
            print("ID tidak boleh kosong")

        elif id_sudah_ada(data, id_penghuni):
            print("ID sudah digunakan")

        else:
            break

    while True:

        nama = input("Masukkan Nama Penghuni : ")

        if nama == "":
            print("Nama tidak boleh kosong")

        else:
            break

    while True:

        no_hp = input("Masukkan Nomor HP : ")

        if no_hp == "":
            print("Nomor HP tidak boleh kosong")

        elif not no_hp.isdigit():
            print("Nomor HP harus berupa angka")

        else:
            break

    # Dictionary
    penghuni = {
        "id": id_penghuni,
        "nama": nama,
        "no_hp": no_hp,
        "status": STATUS_PENGHUNI[0]
    }

    data.append(penghuni)

    simpan_data(data)

    print("Data penghuni berhasil ditambahkan")


def lihat_penghuni():

    data = baca_data()

    print("\n=== DAFTAR PENGHUNI ===")

    if len(data) == 0:
        print("Belum ada data penghuni")
        return

    nomor = 1

    for penghuni in data:

        print("\nData Penghuni", nomor)
        print("ID      :", penghuni["id"])
        print("Nama    :", penghuni["nama"])
        print("No HP   :", penghuni["no_hp"])
        print("Status  :", penghuni["status"])

        nomor += 1


def cari_penghuni():

    data = baca_data()

    print("\n=== CARI PENGHUNI ===")

    id_cari = input("Masukkan ID Penghuni : ").upper()

    for penghuni in data:

        if penghuni["id"] == id_cari:

            print("\nData Ditemukan")
            print("ID      :", penghuni["id"])
            print("Nama    :", penghuni["nama"])
            print("No HP   :", penghuni["no_hp"])
            print("Status  :", penghuni["status"])

            return

    print("Data penghuni tidak ditemukan")


def menu_penghuni():

    while True:

        print("\n=== MANAJEMEN PENGHUNI ===")
        print("1. Tambah Penghuni")
        print("2. Lihat Penghuni")
        print("3. Cari Penghuni")
        print("0. Keluar")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            tambah_penghuni()

        elif pilih == "2":
            lihat_penghuni()

        elif pilih == "3":
            cari_penghuni()

        elif pilih == "0":
            print("Keluar dari menu penghuni")
            break

        else:
            print("Menu tidak tersedia")


menu_penghuni()
