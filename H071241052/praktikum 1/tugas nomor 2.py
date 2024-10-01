#tugas P1 nomor 2

karakter = input("Masukkan karakter yang ingin dicari: ")
kalimat = input("Masukkan kalimat: ")

# print("Karakter merupakan bagian dari Kalimat" * (karakter in kalimat) + 
#       "Karakter tidak ditemukan dalam Kalimat" * (karakter not in kalimat))

print((karakter in kalimat) * "karakter ada dalam kalimat" or "karakter tidak ada dalam kalimat")