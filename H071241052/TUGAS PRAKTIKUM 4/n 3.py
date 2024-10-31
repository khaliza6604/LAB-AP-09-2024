def hitung_langkah(n):
    # Validasi input harus bilangan bulat positif
    if not isinstance(n, int) or n <= 0:
        print("Input tidak Valid")
        return

    langkah = 0

    # Proses pengubahan hingga n menjadi 1
    while n != 1:
        if n % 2 == 0:  # Jika n genap
            n = n // 2
        else:  # Jika n ganjil
            n = 3 * n + 1
        langkah += 1

    # Menampilkan jumlah langkah
    print(f"Jumlah langkah: {langkah}")

# Contoh penggunaan
n = input("Masukkan bilangan bulat positif: ")

# Coba ubah input ke integer
try:
    n = int(n)
    hitung_langkah(n)
except ValueError:
    print("Input tidak Valid")
