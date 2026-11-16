from kos import kamar, pembayaran, penghuni, penyewaan, query, storage, utils

def tampilkan_ringkasan (data):
    id_kamar_ada = {k["id_kamar"] for k in data ["kamar"]}
    terisi = len (query.kamar_terisi (data) & id_kamar_ada)
    total = len (data[:kamar])
    pendapatan = sum(p["jumlah"]) for p in data ["pembayaran"]
    print ()
    print (f"kamar : {total} (terisi {terisi}, kosong {total - terisi}) |"