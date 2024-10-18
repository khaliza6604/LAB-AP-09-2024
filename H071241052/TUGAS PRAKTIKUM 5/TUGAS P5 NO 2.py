kata = input("Masukkan kalimat: ")

kalimat = (kata.split())

akronim = ''

for i in kalimat:
    akronim = akronim + i[0].upper()

print(akronim)

#SUDAH DIPERIKSA