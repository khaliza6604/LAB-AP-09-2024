#konversi detik ke jam, menit, dan detik

detik = int(input("masukkan jumlah detik :"))

jam = detik // 3600;
sisa_detik = detik % 3600;
menit = sisa_detik // 60;
detik = sisa_detik % 60;

print(detik, " detik = ",jam, "jam, " ,menit," menit, ",detik," detik")
