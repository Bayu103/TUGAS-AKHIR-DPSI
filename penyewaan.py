import json

FILE_SEWA = "penyewaan.json"
FILE_KAMAR = "kamar.json"
FILE_PENGHUNI = "penghuni.json"


# ==========================
# LOAD DATA
# ==========================
def load_penyewaan():

    try:
        with open(FILE_SEWA, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_penyewaan(data):

    with open(FILE_SEWA, "w") as file:
        json.dump(data, file, indent=4)


def load_kamar():

    try:
        with open(FILE_KAMAR, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_kamar(data):

    with open(FILE_KAMAR, "w") as file:
        json.dump(data, file, indent=4)


def load_penghuni():

    try:
        with open(FILE_PENGHUNI, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# ==========================
# TAMBAH PENYEWAAN
# ==========================
def tambah_penyewaan():

    penyewaan = load_penyewaan()
    kamar = load_kamar()
    penghuni = load_penghuni()

    print("\n===== TAMBAH PENYEWAAN =====")

    id_penghuni = input("Masukkan ID Penghuni : ").upper()

    data_penghuni = None

    for p in penghuni:

        if p["id_penghuni"] == id_penghuni:

            if p["status"] == "Aktif":
                data_penghuni = p

            break

    if data_penghuni is None:
        print("PENGHUNI TIDAK DITEMUKAN!")
        return

    print("\nDAFTAR KAMAR KOSONG")

    kamar_kosong = False

    for k in kamar:

        if k["status"] == "Kosong":

            kamar_kosong = True

            print(
                k["id_kamar"],
                "-",
                k["tipe"],
                "- Rp",
                k["harga"]
            )

    if kamar_kosong == False:
        print("TIDAK ADA KAMAR KOSONG!")
        return

    id_kamar = input("\nMasukkan ID Kamar : ").upper()

    data_kamar = None

    for k in kamar:

        if k["id_kamar"] == id_kamar and k["status"] == "Kosong":

            data_kamar = k
            break

    if data_kamar is None:
        print("KAMAR TIDAK TERSEDIA!")
        return

    tanggal_mulai = input("Masukkan Tanggal Mulai Sewa : ")

    id_sewa = "S0" + str(len(penyewaan) + 1)

    penyewaan_baru = {
        "id_sewa": id_sewa,
        "id_penghuni": data_penghuni["id_penghuni"],
        "nama_penghuni": data_penghuni["nama"],
        "id_kamar": data_kamar["id_kamar"],
        "tanggal_mulai": tanggal_mulai,
        "biaya_sewa": data_kamar["harga"],
        "status": "Aktif"
    }

    penyewaan.append(penyewaan_baru)

    for k in kamar:

        if k["id_kamar"] == id_kamar:
            k["status"] = "Terisi"

    save_penyewaan(penyewaan)
    save_kamar(kamar)

    print("\nPENYEWAAN BERHASIL DITAMBAHKAN!")

    # ==========================
# LIHAT PENYEWAAN
# ==========================
def lihat_penyewaan():

    data = load_penyewaan()

    print("\n====================================================================================")
    print("                                DATA PENYEWAAN")
    print("====================================================================================")
    print(f"{'ID':<8}{'PENGHUNI':<20}{'KAMAR':<10}{'TANGGAL':<15}{'BIAYA':<15}{'STATUS'}")
    print("====================================================================================")

    for sewa in data:

        print(
            f"{sewa['id_sewa']:<8}"
            f"{sewa['nama_penghuni']:<20}"
            f"{sewa['id_kamar']:<10}"
            f"{sewa['tanggal_mulai']:<15}"
            f"{sewa['biaya_sewa']:<15}"
            f"{sewa['status']}"
        )

    print("====================================================================================")
