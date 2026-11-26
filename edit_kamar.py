import json

FILE_KAMAR = "kamar.json"


# ==========================
# LOAD KAMAR
# ==========================

def load_kamar():

    try:

        with open(FILE_KAMAR, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        return []


# ==========================
# SAVE KAMAR
# ==========================

def save_kamar(data):

    with open(FILE_KAMAR, "w") as file:
        json.dump(data, file, indent=4)


# ==========================
# EDIT KAMAR
# ==========================

def edit_kamar():

    data = load_kamar()

    if len(data) == 0:

        print("\nBELUM ADA DATA KAMAR")
        return

    print("\n===== EDIT KAMAR =====")

    id_kamar = input(
        "Masukkan ID Kamar : "
    ).upper()

    ditemukan = False

    for kamar in data:

        if kamar["id_kamar"] == id_kamar:

            print("\nData Saat Ini")
            print("Tipe :", kamar["tipe"])
            print("Harga :", kamar["harga"])

            print("\nPilih Tipe Baru")
            print("1. Kamar Mandi Dalam")
            print("2. Kamar Mandi Luar")

            pilihan = input("Pilihan : ")

            if pilihan == "1":

                kamar["tipe"] = "Kamar Mandi Dalam"
                kamar["harga"] = 1000000

            elif pilihan == "2":

                kamar["tipe"] = "Kamar Mandi Luar"
                kamar["harga"] = 500000

            else:

                print("PILIHAN TIDAK VALID")
                return

            save_kamar(data)

            print(
                "DATA KAMAR BERHASIL DIUBAH"
            )

            ditemukan = True
            break

    if ditemukan == False:

        print(
            "ID KAMAR TIDAK DITEMUKAN"
        )


# ==========================
# HAPUS KAMAR
# ==========================

def hapus_kamar():

    data = load_kamar()

    if len(data) == 0:

        print("\nBELUM ADA DATA KAMAR")
        return

    print("\n===== HAPUS KAMAR =====")

    id_kamar = input(
        "Masukkan ID Kamar : "
    ).upper()

    ditemukan = False

    for kamar in data:

        if kamar["id_kamar"] == id_kamar:

            if kamar["status"] == "Terisi":

                print(
                    "KAMAR SEDANG DIGUNAKAN"
                )

                print(
                    "KAMAR TIDAK DAPAT DIHAPUS"
                )

                ditemukan = True
                break

            konfirmasi = input(
                "Yakin ingin menghapus kamar? (Y/T) : "
            ).upper()

            if konfirmasi == "Y":

                data.remove(kamar)

                save_kamar(data)

                print(
                    "KAMAR BERHASIL DIHAPUS"
                )

            else:

                print(
                    "PENGHAPUSAN DIBATALKAN"
                )

            ditemukan = True
            break

    if ditemukan == False:

        print(
            "ID KAMAR TIDAK DITEMUKAN"
        )