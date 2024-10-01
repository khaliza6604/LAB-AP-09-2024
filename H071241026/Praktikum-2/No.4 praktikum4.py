#Penggunaan Data

data = int(input("Masukkan jumlah data yang digunakan (GB): " ))
waktu = input("Apakah mayoritas penggunaan data di luar jam sibuk(Off-Peak)atau di jam sibuk(peak)?: ")
jenis = input("Apakah anda pengguna personal atau pengguna bisnis?:  ")

if data < 10 and waktu == "off peak" and jenis == "personal" :
    paket = "A"
elif 10 <= data <= 50 and waktu == "peak" and jenis == "personal" :
    paket = "B"
elif data > 50 and waktu == "peak" :
    paket = "C"
elif data > 50 and waktu == "off peak" : 
    paket = "D"
else:
    paket = "Data Tidak Valid"

print(f"Paket yang sesuai : paket {paket}")
