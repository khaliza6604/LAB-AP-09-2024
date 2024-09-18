# TUgas P2 nomor 4
Data = int(input("Masukkan jumlah data yang digunakan: "))
jam = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)?: ")
paket = input("Apakah anda pengguna personal atau bisnis?: ")

if(Data < 10): penggunaan = "ringan"
elif(Data < 50): penggunaan = "sedang"
else: penggunaan = "berat"

if(penggunaan == "ringan") and (jam == "off-peak") and (paket == "personal"): print("paket A")
elif(penggunaan == "sedang") and (jam == "peak") and (paket == "personal"): print("paket B")
elif(penggunaan == "berat") and (jam == "peak"): print("paket C")
elif(penggunaan == "berat") and (jam == "off-peak") and (paket == "bisnis"): print("paket D")
else: print("tidak ada paket yang cocok")
