# Live Koding
penilaian = int(input("Masukkan Penilaian: "))
tahun_pengalaman = int(input("Masukkan Tahun Pengalaman (dalam Bentuk Angka): "))
jenis_pekerjaan = input("Masukkan Jenis Pekerjaan: ")
gaji = int(input("Masukkan Gaji (dalam Bentuk Angka): "))

if penilaian >= 90:
  kategori = "Sangat Baik"
elif 70 <= penilaian < 90:
  kategori = "Baik"
elif 50 <= penilaian < 70:
  kategori = "Cukup"
else:
  kategori = "Kurang"
bonus = 0

if kategori == "Sangat Baik":
   bonus = 0.2 if tahun_pengalaman >= 5 else 0.15
    

elif kategori == "Baik":
     bonus = 0.1 if jenis_pekerjaan == "Manager" else 0.05
    

elif kategori == "Cukup":
     bonus = 0.05 if tahun_pengalaman >= 5 else 0

else:
    bonus = 0

total_gaji = gaji + (gaji *bonus)

print(f"Kategori Penilaian: {kategori}")
print(f'Bonus: {bonus *100}%')
print(f"Total Gaji Setelah Bonus: {total_gaji:.1f}")