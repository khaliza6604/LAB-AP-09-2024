def hitung_langkah(n):
    if not isinstance(n, int) or n <= 0:
        return "Input tidak Valid"
    
    langkah = 0
    print(f"Langkah {langkah}: {n}")  # Menampilkan bilangan awal
    
    while n != 1:
        if n % 2 == 0:
            n //= 2  # Jika n genap, bagi dengan 2
        else:
            n = 3 * n + 1  # Jika n ganjil, kalikan dengan 3 dan tambahkan 1
        langkah += 1
        print(f"Langkah {langkah}: {n}")  # Menampilkan setiap langkah
        
    return f"Jumlah langkah: {langkah}"

# Contoh penggunaan
try:
    n = int(input("Masukkan bilangan bulat positif: "))
    hasil = hitung_langkah(n)
    print(hasil)
except ValueError:
    print("Input tidak Valid")
