def harta_karun():
    total_jarak = 0
    
    while True:
        try:
            jarak_langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
        except:
            print("Input tidak valid. Masukkan bilangan bulat ")
            continue
        
        total_jarak += jarak_langkah

        def keputusan():
            print(f"Total jarak: {total_jarak} meter")
            if total_jarak > 20:
                bahaya = "Ya"
                keputusan_akhir = "Tidak aman menggali harta karun. Coba lagi!"
            else:
                bahaya = "Tidak"
                keputusan_akhir = "Aman! Kamu tepat menemukan harta karun dan menang!"
            print(f"Ada bahaya: {bahaya}")
            print(f"Keputusan: {keputusan_akhir}")
            
        if jarak_langkah == 0:
            keputusan()
            break

harta_karun()