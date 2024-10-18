# TUGAS P3 NOMOR 4

x = int(input("Masukkan total harga: "))
y = int(input("Masukkan uang yang diberikan: "))

z = y-x

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

# if x < y:
#     print(f"kembalian: {z}")

if z < 0:
    print("Uang anda tidak cukup")
else:
    print(f"kembalian: {z}")
    print("rindian kembalian")
    for i in pecahan_uang:
        if z >= i:
            jumlah_lembar = z // i
            z = z % i
            print(f"{jumlah_lembar} lembar uang Rp. {i}")