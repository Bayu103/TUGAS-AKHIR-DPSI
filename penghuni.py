import json

FILE_PENGHUNI = "penghuni.json"


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
# EDIT PENGHUNI
# ==========================
def edit_penghuni():

    data = load_penghuni()

    print("\n===== EDIT PENGHUNI =====")

    id_penghuni = input("Masukkan ID Penghuni : ").upper()

    ditemukan = False

    for penghuni in data:

        if penghuni["id_penghuni"] == id_penghuni:

            print("\nData Saat Ini")
            print("Nama :", penghuni["nama"])
            print("Umur :", penghuni["umur"])
            print("Jenis Kelamin :", penghuni["jenis_kelamin"])

            nama_baru = input("\nMasukkan Nama Baru : ")

            try:
                umur_baru = int(input("Masukkan Umur Baru : "))

            except:

                print("UMUR HARUS ANGKA")
                return

            print("\n1. Laki-laki")
            print("2. Perempuan")

            pilihan = input("Pilih : ")

            if pilihan == "1":

                jenis_kelamin_baru = "Laki-laki"

            elif pilihan == "2":

                jenis_kelamin_baru = "Perempuan"

            else:

                print("PILIHAN TIDAK VALID")
                return

            penghuni["nama"] = nama_baru
            penghuni["umur"] = umur_baru
            penghuni["jenis_kelamin"] = jenis_kelamin_baru

            save_penghuni(data)

            print("\nDATA BERHASIL DIUBAH")

            ditemukan = True
            break

    if ditemukan == False:

        print("ID PENGHUNI TIDAK DITEMUKAN")


# ==========================
# HAPUS PENGHUNI
# (DINONAKTIFKAN)
# ==========================
def hapus_penghuni():

    data = load_penghuni()

    print("\n===== HAPUS PENGHUNI =====")

    id_penghuni = input("Masukkan ID Penghuni : ").upper()

    ditemukan = False

    for penghuni in data:

        if penghuni["id_penghuni"] == id_penghuni:

            konfirmasi = input(
                "Yakin ingin menonaktifkan penghuni? (Y/T) : "
            ).upper()

            if konfirmasi == "Y":

                penghuni["status"] = "Tidak Aktif"

                save_penghuni(data)

                print("PENGHUNI BERHASIL DINONAKTIFKAN")

            else:

                print("PROSES DIBATALKAN")

            ditemukan = True
            break

    if ditemukan == False:

        print("ID PENGHUNI TIDAK DITEMUKAN")


# ==========================
# STATUS PENGHUNI
# ==========================
def status_penghuni():

    data = load_penghuni()

    print("\n===== STATUS PENGHUNI =====")

    id_penghuni = input("Masukkan ID Penghuni : ").upper()

    ditemukan = False

    for penghuni in data:

        if penghuni["id_penghuni"] == id_penghuni:

            print("\nStatus Saat Ini :", penghuni["status"])

            print("1. Aktif")
            print("2. Tidak Aktif")

            pilihan = input("Pilih Status : ")

            if pilihan == "1":

                penghuni["status"] = "Aktif"

            elif pilihan == "2":

                penghuni["status"] = "Tidak Aktif"

            else:

                print("PILIHAN TIDAK VALID")
                return

            save_penghuni(data)

            print("STATUS BERHASIL DIUBAH")

            ditemukan = True
            break

    if ditemukan == False:

        print("ID PENGHUNI TIDAK DITEMUKAN")
