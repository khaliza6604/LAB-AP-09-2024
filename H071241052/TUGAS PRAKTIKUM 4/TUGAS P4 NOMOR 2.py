print("Selamat datang dalam permainan pemburu harta karun!")
print("Tugas Anda adalah berjalan hingga total jarak 50 meter.")
print("Jangan melangkah lebih dari 20 meter dalam satu langkah agar aman.")
print("Masukkan 0 atau langkah negatif untuk menyelesaikan permainan.")

def is_dangerous(langkah):
    return langkah > 20

def treasure_hunt():
    total_jarak = 0
    danger = False

    while True:
        try:
            langkah = int(input("Masukkan jarak langkah (dalam meter): ")) 
            if langkah == 0: 
                break 
            elif is_dangerous(langkah):
                print("Langkah berbahaya terdeteksi! Tidak aman untuk menggali, coba lagi!")
                danger = True
                continue
            
            total_jarak += langkah
            print(f"Total jarak: {total_jarak} meter") 

        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.")

    if total_jarak == 50 and not danger:
        print("Aman! Kamu tepat menemukan harta karun! Kamu menang!")
    elif danger:
        print("Tidak aman untuk menggali harta karun! Coba lagi!")
    else:
        print("Tidak menemukan harta karun! Coba lagi!")

print(treasure_hunt())