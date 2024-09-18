#tugas P1 nomor 1

def rekomendasi_investasi(harga_kemarin, harga_hari_ini):
    
    perubahan_persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100
    
    rekomendasi = {
        perubahan_persen > 5: "Beli",
        -3 <= perubahan_persen <= 5: "Tahan",
        perubahan_persen < -3: "Jual"
    }
    hasil_rekomendasi = rekomendasi[True]
    

    print(f"Perubahan persentase harga saham: {perubahan_persen:.2f}%")
    print(f"Rekomendasi investasi: {hasil_rekomendasi}")


harga_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_hari_ini = 105.0  

rekomendasi_investasi(harga_kemarin, harga_hari_ini)
