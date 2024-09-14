penggunaan_data = int(input("masukkan jumlah data yang digunakan (GB) : "))
waktu_penggunaan = input("apakah mayoritas penggunaan di luar jam sibuk (off-peek) atau di jam sibuk (peak)? ")
jenis_penggunna = input("apakah anda penggunna personal atau bisnis? ")
paket_layanan = ['paket A', 'paket B', 'paket C', 'paket D', 'tidak ada paket yang cocok']

if penggunaan_data < 10 and waktu_penggunaan == 'off-peak' and jenis_penggunna == 'personal' :
    paket = "paket A"
elif penggunaan_data >= 10 and penggunaan_data <= 50 and waktu_penggunaan == 'peak' and jenis_penggunna == 'personal' :
    paket = "paket B"
elif penggunaan_data > 50 and waktu_penggunaan == 'peak' and jenis_penggunna == 'personal'or 'bisnis' :
    paket = "paket C"
elif penggunaan_data > 50 and waktu_penggunaan == 'off-peak' and jenis_penggunna == 'bisnis' :
    paket = "paket D"
else :
    paket = "tidak ada paket yang cocok"

print("paket yang sesuai : ",paket)
         