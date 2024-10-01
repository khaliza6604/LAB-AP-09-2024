# tugas P2 nomor 2

usia = int(input("Masukkan usia: "))
keanggotaan = input("Apakah anda anggota (ya/tidak)?: ")



if usia < 5 : 
    harga_tiket = 0
elif usia <= 12:
     harga_tiket = 50000
elif usia <= 59: 
    harga_tiket = 100000
else : 
    harga_tiket = 70000

harga_final = harga_tiket * 0.8 if keanggotaan.lower() == 'ya' else harga_tiket

print(f"harga tiket: Rp.{harga_final:.0f}")