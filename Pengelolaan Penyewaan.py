import json

FILE_SEWA = "penyewaan.json"
FILE_KAMAR = "kamar.json"
FILE_PENGHUNI = "penghuni.json"


# ==========================
# LOAD PENYEWAAN
# ==========================
def load_penyewaan():

    try:
        with open(FILE_SEWA, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# ==========================
# SAVE PENYEWAAN
# ==========================
def save_penyewaan(data):

    with open(FILE_SEWA, "w") as file:
        json.dump(data, file, indent=4)


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
# LOAD PENGHUNI
# ==========================
def load_penghuni():

    try:
        with open(FILE_PENGHUNI, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# ==========================
# SAVE PENGHUNI
# ==========================
def save_penghuni(data):

    with open(FILE_PENGHUNI, "w") as file:
        json.dump(data, file, indent=4)


# ==========================
# EDIT PENYEWAAN
# ==========================
def edit_penyewaan():

    data = load_penyewaan()

    print("\n===== EDIT STATUS PENYEWAAN =====")

    id_sewa = input("Masukkan ID Sewa : ").upper()

    ditemukan = False

    for sewa in data:

        if sewa["id_sewa"] == id_sewa:

            print("\nStatus Saat Ini :", sewa["status"])

            print("1. Aktif")
            print("2. Selesai")

            pilihan = input("Pilih Status Baru : ")

            if pilihan == "1":
                sewa["status"] = "Aktif"

            elif pilihan == "2":
                sewa["status"] = "Selesai"

            else:
                print("PILIHAN TIDAK VALID")
                return

            save_penyewaan(data)

            print("STATUS PENYEWAAN BERHASIL DIUBAH")

            ditemukan = True
            break

    if ditemukan == False:
        print("ID SEWA TIDAK DITEMUKAN")


# ==========================
# PENGHUNI KELUAR
# ==========================
def penghuni_keluar():

    penyewaan = load_penyewaan()
    kamar = load_kamar()
    penghuni = load_penghuni()

    print("\n===== PENGHUNI KELUAR =====")

    id_sewa = input("Masukkan ID Sewa : ").upper()

    ditemukan = False

    for data_sewa in penyewaan:

        if data_sewa["id_sewa"] == id_sewa:

            # Status Penyewaan
            data_sewa["status"] = "Selesai"

            id_kamar = data_sewa["id_kamar"]
            id_penghuni = data_sewa["id_penghuni"]

            # Status Kamar
            for data_kamar in kamar:

                if data_kamar["id_kamar"] == id_kamar:

                    data_kamar["status"] = "Kosong"

            # Status Penghuni
            for data_penghuni in penghuni:

                if data_penghuni["id_penghuni"] == id_penghuni:

                    data_penghuni["status"] = "Tidak Aktif"

            save_penyewaan(penyewaan)
            save_kamar(kamar)
            save_penghuni(penghuni)

            print("\nPENGHUNI BERHASIL KELUAR")
            print("STATUS PENYEWAAN : SELESAI")
            print("STATUS KAMAR : KOSONG")
            print("STATUS PENGHUNI : TIDAK AKTIF")

            ditemukan = True
            break

    if ditemukan == False:
        print("ID SEWA TIDAK DITEMUKAN")


# ==========================
# RIWAYAT PENYEWAAN
# ==========================
def riwayat_penyewaan():

    data = load_penyewaan()

    print("\n================================================================================")
    print("                             RIWAYAT PENYEWAAN")
    print("================================================================================")
    print(f"{'ID':<8}{'PENGHUNI':<20}{'KAMAR':<10}{'STATUS'}")
    print("================================================================================")

    for sewa in data:

        if sewa["status"] == "Selesai":

            print(
                f"{sewa['id_sewa']:<8}"
                f"{sewa['nama_penghuni']:<20}"
                f"{sewa['id_kamar']:<10}"
                f"{sewa['status']}"
            )

    print("================================================================================")
