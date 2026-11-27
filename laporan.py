import json

FILE_PEMBAYARAN = "pembayaran.json"
FILE_PENYEWAAN = "penyewaan.json"


# ==========================
# LOAD PEMBAYARAN
# ==========================

def load_pembayaran():

    try:

        with open(FILE_PEMBAYARAN, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        return []


# ==========================
# LOAD PENYEWAAN
# ==========================

def load_penyewaan():

    try:

        with open(FILE_PENYEWAAN, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        return []


# ==========================
# TOTAL PENDAPATAN
# ==========================

def total_pendapatan():

    pembayaran = load_pembayaran()

    total = 0

    for bayar in pembayaran:

        if bayar["status"] == "Lunas":

            total += bayar["jumlah_bayar"]

    print("\n===== TOTAL PENDAPATAN KOS =====")
    print("Total Pendapatan : Rp", total)


# ==========================
# DAFTAR BELUM BAYAR
# ==========================

def daftar_belum_bayar():

    penyewaan = load_penyewaan()
    pembayaran = load_pembayaran()

    print("\n===== DAFTAR PENGHUNI BELUM BAYAR =====")

    ada_data = False

    for sewa in penyewaan:

        if sewa["status"] == "Aktif":

            sudah_bayar = False

            for bayar in pembayaran:

                if (
                    bayar["id_sewa"] == sewa["id_sewa"]
                    and bayar["status"] == "Lunas"
                ):

                    sudah_bayar = True
                    break

            if sudah_bayar == False:

                print(
                    "\nNama Penghuni :",
                    sewa["nama_penghuni"]
                )

                print(
                    "ID Kamar :",
                    sewa["id_kamar"]
                )

                print(
                    "ID Sewa :",
                    sewa["id_sewa"]
                )

                print(
                    "------------------------------------"
                )

                ada_data = True

    if ada_data == False:

        print(
            "SEMUA PENGHUNI SUDAH MEMBAYAR"
        )


# ==========================
# BACKUP DATA
# ==========================

def backup_data():

    pembayaran = load_pembayaran()

    try:

        with open(
            "backup_pembayaran.json",
            "w"
        ) as file:

            json.dump(
                pembayaran,
                file,
                indent=4
            )

        print(
            "\nBACKUP BERHASIL DIBUAT"
        )

    except:

        print(
            "\nGAGAL MEMBUAT BACKUP"
        )


# ==========================
# MUAT DATA
# ==========================

def muat_data():

    pembayaran = load_pembayaran()
    penyewaan = load_penyewaan()

    print("\n===== MUAT DATA =====")

    print(
        "Jumlah Data Pembayaran :",
        len(pembayaran)
    )

    print(
        "Jumlah Data Penyewaan :",
        len(penyewaan)
    )

    print(
        "\nDATA BERHASIL DIMUAT"
    )