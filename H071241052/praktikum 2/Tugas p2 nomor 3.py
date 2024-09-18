# Tugas p2 nomor 3

nilai = int(input("masukkan nilai akhir: "))
kehadiran = int(input("masukkan persentase kehadiran: "))

#if(kehadiran <=75): print("Tidak lulus")
#elif(nilai >= 85) and (nilai <= 100): print("Lulus dengan predikat A")
#elif(nilai >= 70) and (nilai <= 84): print("Lulus dengan predikat B")
#elif(nilai <= 69): print("Lulus dengan predikat C")

if kehadiran >= 75: 
    if nilai >= 85: 
        predikat = "lulus predikat A"
    elif nilai >= 70 :
        predikat = "lulus predikat B"
    elif nilai <= 60 :
        predikat = "lulus predikat C"
    else:
        nilai_tugas = int(input("nilai tugas tambahan: "))
        if nilai_tugas >= 70:
            predikat = "lulus predikat C"
        else:
            predikat = "tidak lulus"
else:
    predikat = "tidak lulus"

print(predikat)
# elif(nilai < 69): print("Lulus dengan predikat C")
# elif(nilai < 84): print("Lulus dengan predikat B")
# elif(nilai <100): print("Lulus dengan predikat A")
