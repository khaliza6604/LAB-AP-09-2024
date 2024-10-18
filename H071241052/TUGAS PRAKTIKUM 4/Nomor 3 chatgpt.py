def hitung_langkah(n):
    langkah = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        langkah += 1
    return langkah

def main():
    try:
        # Meminta input dari Budi
        n = int(input("Masukkan bilangan bulat positif: "))
        
        # Memastikan input adalah bilangan bulat positif
        if n <= 0:
            print("Input tidak Valid")
        else:
            # Menghitung jumlah langkah
            jumlah_langkah = hitung_langkah(n)
            print(f"Jumlah langkah: {jumlah_langkah}")
    
    except ValueError:
        # Menangani input yang bukan bilangan bulat
        print("Input tidak Valid")

# Menjalankan program
main()
