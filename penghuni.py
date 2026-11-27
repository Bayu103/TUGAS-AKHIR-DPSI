import json

FILE_PENGHUNI = "penghuni.json"


def load_penghuni():

    try:
        with open(FILE_PENGHUNI, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        data_awal = [
            {
                "id_penghuni": "P01",
                "nama": "Andi",
                "umur": 20,
                "jenis_kelamin": "Laki-laki",
                "status": "Aktif"
            },
            {
                "id_penghuni": "P02",
                "nama": "Siti",
                "umur": 21,
                "jenis_kelamin": "Perempuan",
                "status": "Aktif"
            }
        ]

        save_penghuni(data_awal)

        return data_awal


def save_penghuni(data):

    with open(FILE_PENGHUNI, "w") as file:
        json.dump(data, file, indent=4)


def tambah_penghuni():

    data = load_penghuni()

    print("\n===== TAMBAH PENGHUNI =====")

    while True:

        id_penghuni = input("Masukkan ID Penghuni : ").upper()

        if id_penghuni == "":

            print("ID PENGHUNI TIDAK BOLEH KOSONG!")
            continue

        id_sudah_ada = False

        for penghuni in data:

            if penghuni["id_penghuni"] == id_penghuni:

                id_sudah_ada = True
                break

        if id_sudah_ada:

            print("ID PENGHUNI SUDAH DIGUNAKAN!")

        else:

            break

    while True:
        nama = input("Masukkan Nama Penghuni : ")
        if nama == "":
            print("NAMA TIDAK BOLEH KOSONG!")
        else:
            break
    while True:

        try:

            umur = int(input("Masukkan Umur : "))

            if umur > 0:

                break

            else:

                print("UMUR HARUS LEBIH DARI 0")

        except:

            print("UMUR HARUS BERUPA ANGKA!")

    print("\nPilih Jenis Kelamin")
    print("1. Laki-laki")
    print("2. Perempuan")

    while True:

        pilihan = input("Masukkan Pilihan : ")

        if pilihan == "1":

            jenis_kelamin = "Laki-laki"
            break

        elif pilihan == "2":

            jenis_kelamin = "Perempuan"
            break

        else:

            print("PILIHAN TIDAK VALID!")

    penghuni_baru = {
        "id_penghuni": id_penghuni,
        "nama": nama,
        "umur": umur,
        "jenis_kelamin": jenis_kelamin,
        "status": "Aktif"
    }

    data.append(penghuni_baru)

    save_penghuni(data)

    print("\nPENGHUNI BERHASIL DITAMBAHKAN!")


def lihat_penghuni():

    data = load_penghuni()

    print("\n================================================================================")
    print("                                DAFTAR PENGHUNI")
    print("================================================================================")
    print(f"{'ID':<10}{'NAMA':<20}{'UMUR':<10}{'JENIS KELAMIN':<20}{'STATUS'}")
    print("================================================================================")

    for penghuni in data:

        print(
            f"{penghuni['id_penghuni']:<10}"
            f"{penghuni['nama']:<20}"
            f"{penghuni['umur']:<10}"
            f"{penghuni['jenis_kelamin']:<20}"
            f"{penghuni['status']}"
        )

    print("================================================================================")


def cari_penghuni():

    data = load_penghuni()

    print("\n===== CARI PENGHUNI =====")

    id_cari = input("Masukkan ID Penghuni : ").upper()

    ditemukan = False

    for penghuni in data:

        if penghuni["id_penghuni"] == id_cari:

            print("\n===== DETAIL PENGHUNI =====")
            print("ID Penghuni    :", penghuni["id_penghuni"])
            print("Nama           :", penghuni["nama"])
            print("Umur           :", penghuni["umur"])
            print("Jenis Kelamin  :", penghuni["jenis_kelamin"])
            print("Status         :", penghuni["status"])

            ditemukan = True
            break

    if ditemukan == False:

        print("ID PENGHUNI TIDAK DITEMUKAN")
