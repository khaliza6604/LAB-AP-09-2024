#tugas P1 nomor 3

def format_waktu(total_detik):
    jam = total_detik // 3600
    menit = (total_detik % 3600) // 60
    detik = total_detik % 60
    
    return f"{jam:02}:{menit:02}:{detik:02}"

# Contoh penggunaan
total_detik = int(input("Masukkan jumlah detik: "))
print("Format waktu:", format_waktu(total_detik))
