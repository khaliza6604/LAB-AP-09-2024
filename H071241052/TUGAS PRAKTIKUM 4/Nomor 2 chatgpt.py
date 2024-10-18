# Fungsi untuk memeriksa apakah langkah berbahaya atau tidak
def is_dangerous(step):
    return step > 20

# Fungsi utama untuk permainan pemburu harta karun
def treasure_hunt():
    total_distance = 0
    danger = False
    
    print("Selamat datang dalam permainan pemburu harta karun!")
    print("Tugas Anda adalah berjalan hingga total jarak 50 meter.")
    print("Jangan melangkah lebih dari 20 meter dalam satu langkah agar aman.")
    print("Masukkan 0 atau langkah negatif untuk menyelesaikan permainan.")
    
    while True:
        try:
            # Meminta input dari pemain
            step = int(input("Masukkan jarak langkah (dalam meter): "))
            
            # Jika pemain memasukkan 0 atau nilai negatif, akhiri permainan
            if step <= 0:
                break
            
            # Memeriksa apakah langkah berbahaya
            if is_dangerous(step):
                print("Langkah berbahaya terdeteksi! Tidak aman untuk menggali harta karun. Coba lagi!")
                danger = True
            
            # Menambah jarak langkah ke total jarak
            total_distance += step
            print(f"Total jarak: {total_distance} meter")
        
        except ValueError:
            # Jika input tidak valid
            print("Input tidak valid! Masukkan angka yang benar.")
    
    # Evaluasi akhir setelah keluar dari loop
    if total_distance == 50 and not danger:
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    elif danger:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")

# Memulai permainan
treasure_hunt()
