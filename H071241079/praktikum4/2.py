n = int(input("Masukkan angka: "))

def hitung_langkah(n):
    langkah = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2  
        else:
            n = 3 * n + 1
        print(n) 
        langkah += 1
    return langkah

try:
    if n <= 0:
        print("Input tidak valid")
    else: 
        jumlah_langkah = hitung_langkah(n)
        print(f"Jumlah langkah: {jumlah_langkah}")

except ValueError:
    print("Input tidak valid") 