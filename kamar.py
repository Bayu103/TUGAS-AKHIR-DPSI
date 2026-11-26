import json

FILE_KAMAR = "kamar.json"


# ==========================
# LOAD DATA KAMAR
# ==========================

def load_kamar():

    try:

        with open(FILE_KAMAR, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        data_awal = [

            {
                "id_kamar": "K01",
                "tipe": "Kamar Mandi Dalam",
                "harga": 1000000,
                "status": "Kosong"
            },

            {
                "id_kamar": "K02",
                "tipe": "Kamar Mandi Luar",
                "harga": 500000,
                "status": "Kosong"
            },

            {
                "id_kamar": "K03",
                "tipe": "Kamar Mandi Dalam",
                "harga": 1000000,
                "status": "Kosong"
            }

        ]

        save_kamar(data_awal)

        return data_awal


# ==========================
# SAVE DATA KAMAR
# ==========================

def save_kamar(data):

    with open(FILE_KAMAR, "w") as file:
        json.dump(data, file, indent=4)


# ==========================
# TAMBAH KAMAR
# ==========================

def tambah_kamar():

    data = load_kamar()

    print("\n===== TAMBAH KAMAR =====")

    while True:

        id_kamar = input(
            "Masukkan ID Kamar : "
        ).upper()

        if id_kamar == "":
            print("ID KAMAR TIDAK BOLEH KOSONG")
            continue

        id_sudah_ada = False

        for kamar in data:

            if kamar["id_kamar"] == id_kamar:
                id_sudah_ada = True
                break

        if id_sudah_ada:

            print("ID SUDAH DIGUNAKAN")

        else:
            break

    print("\nPilih Tipe Kamar")
    print("1. Kamar Mandi Dalam")
    print("2. Kamar Mandi Luar")

    while True:

        pilihan = input(
            "Masukkan Pilihan : "
        )

        if pilihan == "1":

            tipe = "Kamar Mandi Dalam"
            harga = 1000000
            break

        elif pilihan == "2":

            tipe = "Kamar Mandi Luar"
            harga = 500000
            break

        else:

            print("PILIHAN TIDAK VALID")

    kamar_baru = {

        "id_kamar": id_kamar,
        "tipe": tipe,
        "harga": harga,
        "status": "Kosong"
    }

    data.append(kamar_baru)

    save_kamar(data)

    print("\nKAMAR BERHASIL DITAMBAHKAN")


# ==========================
# DAFTAR KAMAR
# ==========================

def lihat_daftar_kamar():

    data = load_kamar()

    print("\n====================================================================")
    print(" DAFTAR KAMAR ")
    print("====================================================================")

    print(
        f"{'ID':<10}"
        f"{'TIPE':<25}"
        f"{'HARGA':<15}"
        f"{'STATUS'}"
    )

    print("====================================================================")

    if len(data) == 0:

        print("BELUM ADA DATA KAMAR")

    else:

        for kamar in data:

            print(
                f"{kamar['id_kamar']:<10}"
                f"{kamar['tipe']:<25}"
                f"{kamar['harga']:<15}"
                f"{kamar['status']}"
            )

    print("====================================================================")


# ==========================
# CARI KAMAR
# ==========================

def cari_kamar():

    data = load_kamar()

    print("\n===== CARI KAMAR =====")

    id_cari = input(
        "Masukkan ID Kamar : "
    ).upper()

    ditemukan = False

    for kamar in data:

        if kamar["id_kamar"] == id_cari:

            print("\n===== INFORMASI KAMAR =====")

            print(
                "ID Kamar :",
                kamar["id_kamar"]
            )

            print(
                "Tipe :",
                kamar["tipe"]
            )

            print(
                "Harga : Rp",
                kamar["harga"]
            )

            print(
                "Status :",
                kamar["status"]
            )

            ditemukan = True
            break

    if ditemukan == False:
        print("ID KAMAR TIDAK DITEMUKAN")


# ==========================
# STATUS KAMAR
# ==========================

def status_kamar():

    data = load_kamar()

    print("\n===== STATUS KAMAR =====")

    if len(data) == 0:

        print("BELUM ADA DATA KAMAR")
        return

    for kamar in data:

        print(
            kamar["id_kamar"],
            ":",
            kamar["status"]
        )
