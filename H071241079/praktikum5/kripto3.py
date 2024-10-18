def hitung_penghapusan(s1, s2): 
    karakter_s1 = list(s1)
    karakter_s2 = list(s2)
    
    for karakter in karakter_s1:
        if karakter in karakter_s2:
            karakter_s2.remove(karakter) 
    
    return len(karakter_s1) + len(karakter_s2) 

s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ") 


hasil = hitung_penghapusan(s1, s2) 
print(f"Jumlah minimum penghapusan karakter: {hasil}") 