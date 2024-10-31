def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return 'Pembagian dengan 0 tidak diperbolehkan'


print("Selamat datang di kalkulator sederhana")

bil1 = int(input("Masukkan angka pertama: "))
bil2 = int(input("Masukkan angka kedua: "))
operator = input("Masukkan operasi (+, -, /, *): ")

if operator == "+":
    hasil = penjumlahan(bil1, bil2)
    print("Hasil: ", hasil)
elif operator == "-":
    hasil = pengurangan(bil1, bil2)
    print("Hasil: ", hasil)
elif operator == "*":
    hasil = perkalian(bil1, bil2)
    print("Hasil: ", hasil)
elif operator == "/":
    hasil = pembagian(bil1, bil2)
    print("Hasil: ", hasil)
else:
    print("Operasi tidak valid. Gunakan +, -, /, atau *.") 
    