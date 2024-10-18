def harta():
    total_jarak = 0
    bahaya = False
    while True:
        try:
            jarak = int(input("Masukkan jarak langkah (meter) atau 0 untuk selesai: "))
            if jarak <= 0:
                print("Permainan selesai.")
                break
            if jarak > 20:
                bahaya = True

            total_jarak += jarak
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat ")

    print(f"Total jarak: {total_jarak} meter")

    if bahaya == True :
        print("Ada bahaya: Ya")
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Ada bahaya: Tidak")
        if total_jarak == 50:
            print("Aman! Kamu tepat menemukan harta karun dan menang!")
        else:
            print("Tidak menemukan harta karun. Coba lagi!")

harta() 