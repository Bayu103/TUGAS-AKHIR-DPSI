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
# TAMBAH PENYEWAAN
# ==========================

def tambah_penyewaan():

    penyewaan = load_penyewaan()
    kamar = load_kamar()
    penghuni = load_penghuni()

    print("\n===== TAMBAH PENYEWAAN =====")

    id_penghuni = input(
        "Masukkan ID Penghuni : "
    ).upper()

    data_penghuni = None

    for p in penghuni:

        if p["id_penghuni"] == id_penghuni:

            if p["status"] == "Aktif":
                data_penghuni = p

            break

    if data_penghuni is None:

        print(
            "PENGHUNI TIDAK DITEMUKAN ATAU TIDAK AKTIF"
        )
        return

    # CEK PENYEWAAN AKTIF

    for sewa in penyewaan:

        if (
            sewa["id_penghuni"] == id_penghuni
            and sewa["status"] == "Aktif"
        ):

            print(
                "PENGHUNI MASIH MEMILIKI PENYEWAAN AKTIF"
            )
            return

    print("\n===== DAFTAR KAMAR KOSONG =====")

    kamar_kosong = []

    for k in kamar:

        if k["status"] == "Kosong":

            kamar_kosong.append(k)

            print(
                k["id_kamar"],
                "-",
                k["tipe"],
                "- Rp",
                k["harga"]
            )

    if len(kamar_kosong) == 0:

        print("TIDAK ADA KAMAR KOSONG")
        return

    id_kamar = input(
        "\nMasukkan ID Kamar : "
    ).upper()

    data_kamar = None

    for k in kamar:

        if (
            k["id_kamar"] == id_kamar
            and k["status"] == "Kosong"
        ):

            data_kamar = k
            break

    if data_kamar is None:

        print("KAMAR TIDAK TERSEDIA")
        return

    tanggal_mulai = input(
        "Masukkan Tanggal Mulai Sewa : "
    )

    id_sewa = "S0" + str(
        len(penyewaan) + 1
    )

    penyewaan_baru = {

        "id_sewa": id_sewa,
        "id_penghuni": data_penghuni["id_penghuni"],
        "nama_penghuni": data_penghuni["nama"],
        "id_kamar": data_kamar["id_kamar"],
        "tanggal_mulai": tanggal_mulai,
        "biaya_sewa": data_kamar["harga"],
        "status": "Aktif"

    }

    penyewaan.append(
        penyewaan_baru
    )

    for k in kamar:

        if k["id_kamar"] == id_kamar:

            k["status"] = "Terisi"
            break

    save_penyewaan(penyewaan)
    save_kamar(kamar)

    print(
        "\nPENYEWAAN BERHASIL DITAMBAHKAN"
    )


# ==========================
# LIHAT PENYEWAAN
# ==========================

def lihat_penyewaan():

    data = load_penyewaan()

    print(
        "\n=================================================================================================="
    )

    print(
        " DATA PENYEWAAN "
    )

    print(
        "=================================================================================================="
    )

    print(
        f"{'ID':<8}"
        f"{'PENGHUNI':<20}"
        f"{'KAMAR':<10}"
        f"{'TANGGAL':<15}"
        f"{'BIAYA':<15}"
        f"{'STATUS'}"
    )

    print(
        "=================================================================================================="
    )

    if len(data) == 0:

        print(
            "BELUM ADA DATA PENYEWAAN"
        )

    else:

        for sewa in data:

            print(
                f"{sewa['id_sewa']:<8}"
                f"{sewa['nama_penghuni']:<20}"
                f"{sewa['id_kamar']:<10}"
                f"{sewa['tanggal_mulai']:<15}"
                f"{sewa['biaya_sewa']:<15}"
                f"{sewa['status']}"
            )

    print(
        "=================================================================================================="
    )
