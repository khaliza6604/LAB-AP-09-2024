harga_saham_kemarin = float(input("Masukkan harga saham kemarin: "))

harga_saham_hari_ini = 105.0

perubahan_peresentase = ((harga_saham_hari_ini - harga_saham_kemarin)/harga_saham_kemarin) *100

beli  =(perubahan_peresentase > 5) *1
tahan =(-3 <= perubahan_peresentase <= 5) *1
jual  =(perubahan_peresentase < -3) *1

rekomendasi = beli*"beli" + tahan*"tahan" + jual*"jual"

print(f"perubahan harga: {perubahan_peresentase:.2f}%")
print(f"rekomendasi_investasi: {rekomendasi}")
