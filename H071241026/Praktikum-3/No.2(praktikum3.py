import random

angka_rahasia = random.randint(1, 100)
tebakan = 0
percobaan = 0

while percobaan < 5:
    tebakan = int(input("Masukkan angka yang Anda tebak (1-100) 0 untuk berhenti: "))

    if percobaan == 0:
        print("permainan di hentikan")
        break

    percobaan += 1

    if tebakan < angka_rahasia:
        print("Angka terlalu kecil.")
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Selamat Anda berhasil menebak angka rahasia.")
        break


    if tebakan != angka_rahasia:
        print(f"Maaf, Anda gagal menebak angka rahasia. Angka rahasia adalah {angka_rahasia}.")                  