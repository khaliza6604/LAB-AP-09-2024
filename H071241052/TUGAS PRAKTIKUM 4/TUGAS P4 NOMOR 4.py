print("Selamat datang di kalkulator sederhana!")

def penjumlahan(a, b):
    return a + b

def perkalian(a, b):
    return a * b
def pengurangan(a, b):
    return a - b
def pembagian (a, b):
    return a / b

Angka_pertama = int(input("Angka pertama: "))
Angka_kedua = int(input("Angka kedua: "))
Operasi = input("Operasi (+, -, *, /): ")

if Operasi == "+":
    print(penjumlahan(Angka_pertama, Angka_kedua))
elif Operasi == "-":
    print(pengurangan(Angka_pertama, Angka_kedua))
elif Operasi == "*":
    print(perkalian(Angka_pertama, Angka_kedua))
elif Operasi == "/":
    print(pembagian(Angka_pertama, Angka_kedua))
    #Ada koma nol di belakang