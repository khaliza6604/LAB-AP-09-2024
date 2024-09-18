#Menentukkan harga tiket berdasarkan kategori usia dan status keanggotaan

usia = int(input("Masukkan usia: "))
status_keanggotaan = input("Apakah anda anggota? (ya/tidak): ").lower()

#kategori usia
if usia < 5:
    harga = 0
elif usia <= 12:
    harga = 50000
elif usia <= 59:
    harga = 100000
else:
    harga = 70000

#status keanggotaan 
hasil = harga - ((harga*20) / 100) if status_keanggotaan == "ya" else harga

print(f"Harga tiket: Rp. {int(hasil)}")