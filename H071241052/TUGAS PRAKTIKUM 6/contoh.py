import json

daftar_barang = [
    {"kode": "001", "nama": "Buku", "jumlah": 10, "harga": 15000},
    {"kode": "002", "nama": "Pensil", "jumlah": 20, "harga": 3000}
]

# Mengompres ke format JSON
teks_kompres = json.dumps(daftar_barang)
print(teks_kompres)
