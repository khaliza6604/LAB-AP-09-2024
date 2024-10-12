def anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = {}
    str2_set = {}
    
    # Menghitung Kemunculan Karakter di 
    for karakter in str1:
        if karakter.isalpha():
            str1_set[karakter] = str1_set.get(karakter, 0) + 1
    
    for karakter in str2:
        if karakter.isalpha():
            str2_set[karakter] = str2_set.get(karakter, 0) + 1
    
    # Menghitung Jumlah Karakter yang Harus Dihapus
    remove = sum(abs(str1_set.get(karakter, 0) - str2_set.get(karakter, 0)) for karakter in set(str1 + str2))
    
    return remove

str1 = input('Masukan string pertama :')
str2 = input('masukan String Kedua :')

print("Jumlah karakter yang harus dihapus:", anagram(str1, str2))

