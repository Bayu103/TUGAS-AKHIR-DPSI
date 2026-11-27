import json

FILE_PEMBAYARAN = "pembayaran.json"
FILE_SEWA = "penyewaan.json"


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
# SAVE PEMBAYARAN
# ==========================
def save_pembayaran(data):

    with open(FILE_PEMBAYARAN, "w") as file:
        json.dump(data, file, indent=4)


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
# INPUT PEMBAYARAN
# ==========================
def input_pembayaran():

    pembayaran = load_pembayaran()
    penyewaan = load_penyewaan()

    print("\n===== INPUT PEMBAYARAN =====")

    id_sewa = input("Masukkan ID Sewa : ").upper()

    data_sewa = None

    for sewa in penyewaan:

        if sewa["id_sewa"] == id_sewa:

            data_sewa = sewa
            break

    if data_sewa is None:

        print("ID SEWA TIDAK DITEMUKAN")
        return

    bulan = input("Masukkan Bulan Pembayaran : ")

    # VALIDASI PEMBAYARAN GANDA
    for bayar in pembayaran:

        if (
            bayar["id_sewa"] == id_sewa
            and bayar["bulan"].lower() == bulan.lower()
        ):

            print("PEMBAYARAN BULAN INI SUDAH TERCATAT")
            return

    try:

        jumlah_bayar = int(
            input("Masukkan Jumlah Pembayaran : ")
        )

    except:

        print("INPUT HARUS ANGKA")
        return

    if jumlah_bayar < 0:

        print("PEMBAYARAN TIDAK BOLEH NEGATIF")
        return

    if jumlah_bayar >= data_sewa["biaya_sewa"]:

        status = "Lunas"

    else:

        status = "Belum Lunas"

    id_bayar = "B0" + str(len(pembayaran) + 1)

    pembayaran_baru = {
        "id_bayar": id_bayar,
        "id_sewa": data_sewa["id_sewa"],
        "nama_penghuni": data_sewa["nama_penghuni"],
        "bulan": bulan,
        "jumlah_bayar": jumlah_bayar,
        "status": status
    }

    pembayaran.append(pembayaran_baru)

    save_pembayaran(pembayaran)

    print("\nPEMBAYARAN BERHASIL DICATAT")


# ==========================
# RIWAYAT PEMBAYARAN
# ==========================
def riwayat_pembayaran():

    data = load_pembayaran()

    print("\n========================================================================================")
    print("                               RIWAYAT PEMBAYARAN")
    print("========================================================================================")
    print(f"{'ID':<8}{'PENGHUNI':<20}{'BULAN':<15}{'JUMLAH':<15}{'STATUS'}")
    print("========================================================================================")

    for bayar in data:

        print(
            f"{bayar['id_bayar']:<8}"
            f"{bayar['nama_penghuni']:<20}"
            f"{bayar['bulan']:<15}"
            f"{bayar['jumlah_bayar']:<15}"
            f"{bayar['status']}"
        )

    print("========================================================================================")


# ==========================
# STATUS PEMBAYARAN
# ==========================
def status_pembayaran():

    data = load_pembayaran()

    print("\n===== STATUS PEMBAYARAN =====")

    id_bayar = input("Masukkan ID Pembayaran : ").upper()

    ditemukan = False

    for bayar in data:

        if bayar["id_bayar"] == id_bayar:

            print("\nID Pembayaran :", bayar["id_bayar"])
            print("Nama Penghuni :", bayar["nama_penghuni"])
            print("Bulan         :", bayar["bulan"])
            print("Status        :", bayar["status"])

            ditemukan = True
            break

    if ditemukan == False:

        print("ID PEMBAYARAN TIDAK DITEMUKAN")