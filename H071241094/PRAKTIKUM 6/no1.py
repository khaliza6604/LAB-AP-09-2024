# Inventori Barang Sederhana

inventori = {}

def tambah_barang():
    kode = input('masukan kode barang: ')
    nama = input('Masukkan nama barang: ')
    jumlah = int(input('Masukkan jumlah barang: '))
    harga = float(input('masukan harga per unit: '))
    inventori[kode] = {"nama": nama, "jumlah": jumlah, "harga": harga}
    print("barang berhasil ditambahkan")

def hapus_barang():
    kode = input('masukan kode barang: ')
    if kode in inventori:
        inventori.pop(kode)
        print('barang berhasil dihapus')
    else:
        print('barang tidak ditemukan')

def tampilkan_barang():
    if inventori : 
        for kode, data in inventori.items():
            print(f'Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}')
    else:
        print('inventori kosong')

def cari_barang():
    cari = input('Cari berdasarkan (1) Kode atau (2) Nama: ')
    
    if cari == "1":
        CariKode = input('Masukkan kode barang: ')
        if CariKode in inventori:
            data = inventori[CariKode]
            print(f'Kode: {CariKode}, Nama: {data["nama"]}, Jumlah: {data["jumlah"]}, Harga: {data["harga"]}')
        else:
            print('Barang tidak ditemukan.')

    elif cari == '2':
        CariNama = input('Masukkan nama barang: ')
        for kode, data in inventori.items():
            if data['nama'] == CariNama:
                print(f'Kode: {kode}, Nama: {data["nama"]}, Jumlah: {data["jumlah"]}, Harga: {data["harga"]}')
                break  
        else:
            print('Barang tidak ditemukan.')

                
            
def update_barang():
    kode = input("Masukkan kode barang yang ingin diupdate: ")
    if kode in inventori:
        jumlah_baru = int(input("Masukkan jumlah baru: "))
        inventori[kode]['jumlah'] = jumlah_baru

        harga_baru = float(input("Masukkan harga per unit baru: "))
        inventori[kode]['harga'] = harga_baru

        print('Data barang berhasil diperbarui')
    else :
        print('Barang tidak ditemukan')

def main():
    while True:
        print("=== Menu Inventori Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            tampilkan_barang()
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            update_barang()
        elif pilihan == "6":
            print("Selamat tinggal!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
main()