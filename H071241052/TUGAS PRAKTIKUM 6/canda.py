# import json
# daftar_barang = []


# while True:
#     print("=== Menu Inventori barang ===")
#     print("1. Tambah barang")
#     print("2. Hapus Barang")
#     print("3. Tampilkan Barang")
#     print("4. Cari barang")
#     print("5. Update Barang")
#     print("6. Keluar")
#     opsi = input("Pilih Opsi (1-6): ")

#     if opsi == "1":
#         kode_barang = input("Masukkan kode barang: ")
#         nama_barang = input("Masukkan nama barang: ")
#         jumlah_barang = input("Masukkan jumlah barang: ")
#         harga_barang = int(input("Masukkan harga per unit: "))
#         barang = {"kode": kode_barang, "nama": nama_barang, "jumlah": jumlah_barang, "harga": harga_barang}
#         daftar_barang.append(barang)
#         print("barang berhasil ditambahkan")
#     elif opsi == "2":
#         kode_hapus = input("Masukkan kode barang yang akan dihapus: ")
#         ditemukan = False
#         for barang in daftar_barang:
#             if barang["kode"] == kode_hapus:
#                 daftar_barang.remove(barang)
#                 print(f"barang berhasil dihapus")
#                 ditemukan = True
#         if not ditemukan:    
#                 print("Barang tidak ditemukan!")
#     elif opsi == "3":
#         # print(str(daftar_barang))
#         if not daftar_barang:
#             print("Barang tidak ada dalam inventori")
#         else:
#             for barang in daftar_barang:
#                 print(f"kode: {kode_barang}, nama: {nama_barang}, jumlah: {jumlah_barang}, harga per unit: {harga_barang}")
    
#     elif opsi == "4":
#         cari = input("Cari berdasarkan (1) Kode atau (2) Nama: ")
#         for barang in daftar_barang:
#             if cari == "1":
#                 cari_kode = input("Masukkan kode barang: ")
#                 if cari_kode == barang["kode"]:
#                     print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
#                     # print(str(barang)) # KENAPA OUTPUT BARANG TIDAK BERBENTUK TEKS
#                     break
#                 else:
#                     print("Barang tidak ditemukan!")
#             elif cari == "2":
#                 cari_nama = input("Masukkan nama barang: ")
#                 if cari_nama == barang["nama"]:
#                     print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
#                     # print(str(barang)) #KENAPA OUTPUT BARANG TIDAK BERBENTUK TEKS
#                 else:
#                     print("barang tidak ditemukan!")
#     elif opsi == "5": # DIPERBAIKI
#         kode_update = input("Masukkan kode barang yang ingin diupdate: ")
#         for j in daftar_barang:
#             if barang["kode"] == kode_update:
#                 barang["jumlah"] = input("Masukkan jumlah baru: ")
#                 barang["harga per unit"] = input("Masukkan harga per unit baru: ")
#                 print("Data barang berhasil diperbarui")
#             else:
#                 print("Barang tidak ditemukan!")
#     elif opsi == "6":
#         print("Terima kasih telah menggunakan program inventori")
#         break
#     else:
#         print("MASUKKAN ANGKA 1-6. BUKAN SIMBOL LAIN!!!")

daftar_barang = {}  # Mengubah dari list ke dictionary

while True:
    print("=== Menu Inventori barang ===")
    print("1. Tambah barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Barang")
    print("4. Cari barang")
    print("5. Update Barang")
    print("6. Keluar")
    opsi = input("Pilih Opsi (1-6): ")

    if opsi == "1":
        kode_barang = input("Masukkan kode barang: ")
        if kode_barang in daftar_barang:
            print("Kode barang sudah ada!")
        else:
            nama_barang = input("Masukkan nama barang: ")
            jumlah_barang = input("Masukkan jumlah barang: ")
            harga_barang = int(input("Masukkan harga per unit: "))
            barang = {"nama": nama_barang, "jumlah": jumlah_barang, "harga": harga_barang}
            daftar_barang[kode_barang] = barang  # Menyimpan barang berdasarkan kode
            print("Barang berhasil ditambahkan")

    elif opsi == "2":
        kode_hapus = input("Masukkan kode barang yang akan dihapus: ")
        if kode_hapus in daftar_barang:
            del daftar_barang[kode_hapus]
            print("Barang berhasil dihapus")
        else:
            print("Barang tidak ditemukan!")

    elif opsi == "3":
        if not daftar_barang:
            print("Barang tidak ada dalam inventori")
        else:
            # Menampilkan semua barang
            for kode, barang in daftar_barang.items():
                print(f"Kode: {kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")

    elif opsi == "4":
        cari = input("Cari berdasarkan (1) Kode atau (2) Nama: ")
        ditemukan = False
        if cari == "1":
            cari_kode = input("Masukkan kode barang: ")
            if cari_kode in daftar_barang:
                barang = daftar_barang[cari_kode]
                print(f"Kode: {cari_kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
                ditemukan = True
        elif cari == "2":
            cari_nama = input("Masukkan nama barang: ")
            for kode, barang in daftar_barang.items():
                if barang["nama"] == cari_nama:
                    print(f"Kode: {kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
                    ditemukan = True
        if not ditemukan:
            print("Barang tidak ditemukan!")

    elif opsi == "5":
        kode_update = input("Masukkan kode barang yang ingin diupdate: ")
        if kode_update in daftar_barang:
            barang = daftar_barang[kode_update]
            barang["jumlah"] = input("Masukkan jumlah baru: ")
            barang["harga"] = int(input("Masukkan harga per unit baru: "))
            print("Data barang berhasil diperbarui")
        else:
            print("Barang tidak ditemukan!")

    elif opsi == "6":
        print("Terima kasih telah menggunakan program inventori")
        break

    else:
        print("MASUKKAN ANGKA 1-6. BUKAN SIMBOL LAIN!!!")

