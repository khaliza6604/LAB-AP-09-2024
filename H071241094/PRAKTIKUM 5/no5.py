def caesar_cipher(text, shift):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    hasil = ''
    for karakter in text:
        if karakter.isalpha():
            index = alfabet.index(karakter.lower())
            if karakter.islower() :
                hasil = hasil + alfabet[(index + shift) % 26] 
            elif karakter.isupper() :
                hasil = hasil + alfabet[(index + shift) % 26] 
            else :
                alfabet[(index + shift) % 26].upper()
        elif karakter.isdigit() or karakter in '@#!$%&*()_+-={}|[]:;<>?,./': # untuk Menangani Karakter Non-Huruf
            hasil = hasil + karakter
        else:
            hasil = hasil + karakter
    return hasil

text = input("Masukkan string: ")
shift = int(input("Masukkan jumlah pergeseran: "))

print('Text : ', text)
print('Shift : ', shift)
print('Cipher : ', caesar_cipher(text, shift))
