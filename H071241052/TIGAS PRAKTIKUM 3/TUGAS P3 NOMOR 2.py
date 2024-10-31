# TUGAS P3 NOMOR 2
import random

angka = random.randint(1, 100)

# max_percobaan = 5

for i in range(1, 6):
    n = int(input("masukkan tebakan anda (0 untuk berhenti): "))

    if n == 0:
        print("Anda menghentikan permainan.")
        break
    if n == angka:
        print("Selamat! Anda menebak angka dengan banar")
        break
    elif n > angka:
        print("angka terlalu besar!")
    else:
        print("angka terlalu kecil!")

    if i != angka:
        print(f"Maaf kesempatan anda telah habis! Angka yang benar adalah {angka}")