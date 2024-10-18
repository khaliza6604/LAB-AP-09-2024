def caesar_cipher(teks, pergeseran):
    hasil = ""

    for karakter in teks:
        if karakter.islower():
            geser = chr((ord(karakter) - ord('a') + pergeseran) % 26 + ord('a'))
            hasil += geser
        elif karakter.isupper():
            geser = chr((ord(karakter) - ord('A') + pergeseran) % 26 + ord('A'))
            hasil += geser
        else:
            hasil += karakter

    return hasil

input_teks = input("Masukkan string : ")
nilai_pergeseran = int(input("Masukkan jumlah pergeseran: "))

teks_terenkripsi = caesar_cipher(input_teks, nilai_pergeseran)

print("Teks  :", input_teks)
print("Shift :", nilai_pergeseran)
print("Cipher:", teks_terenkripsi)