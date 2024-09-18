detik = int(input("Masukan Jumlah detik: "))

jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = detik % 60

print(f"{jam:02d}:{menit:02d}:{detik:02d}")