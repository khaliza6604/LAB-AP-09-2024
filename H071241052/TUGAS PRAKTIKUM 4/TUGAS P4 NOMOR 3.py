n = int(input("Masukkan angka: "))

if n > 1

def hitung_langkah(n):
    langkah = 0
    if n % 2 == 0:
        n / 2
    elif n % 2 == 1:
        n * 3 + 1
        langkah  += 1


def main():
    try:
        if n <= 0:
            print("input tidak valid!") 
        else:
                jumlah_langkah = hitung_langkah(n)
        print(f"Jumlah langkah: {jumlah_langkah}")
    except ValueError:
         print("Input tidak valid!")

main()

