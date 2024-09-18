#Menerima input dari pengguna

nilai_akhir = int(input("Masukkan nilai akhir Mahasiswa: "))
kehadiran = int(input("Masukkan persentase kehadiran mahasiswa: ")) 
tugas_tambahan = (input("Apakah semua tugas tambahan dinilai di atas 70(ya/tidak): "))

#Menentukan kelulusan berdasarkan nilai akhir dan kehadiran 

if kehadiran < 75:
    print("Tidak lulus. kehadiran kurang dari 75%")
elif nilai_akhir >= 85:
    print("lulus dengan predikat A")
elif 70 <= nilai_akhir >= 84:
    print("lulus dengan predikat B")
elif 60 <= nilai_akhir >= 69:
    print("lulus dengan predikat C")
elif nilai_akhir < 60:

    if tugas_tambahan == 'ya' and kehadiran >= 75:
        print("lulus dengan predikat C ")
    else:
        print("Tidak Lulus")