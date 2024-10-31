import os
import time

# Folder utama
myFolder = 'PRAKTIKUM 7'
FILE_DIRECTORY = os.path.join(myFolder, 'Bioskop')
FILE_FILM = os.path.join(FILE_DIRECTORY, 'Film.txt')
FILE_TIKET = os.path.join(FILE_DIRECTORY, 'Tiket.txt')

# Buat folder dan file jika belum ada
os.makedirs(FILE_DIRECTORY, exist_ok=True)

def tambah_film():
    try:
        nama_film = input("Masukkan nama film: ")
        if nama_film.strip():  # Cek apakah nama film tidak kosong
            with open(FILE_FILM, 'a') as file:
                file.write(nama_film.strip() + '\n')
            print(f"Film '{nama_film}' telah ditambahkan.")
        else:
            print("Nama film tidak boleh kosong.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan film: {e}")

# Fungsi untuk menampilkan daftar film
def tampilkan_daftar_film():
    print("Daftar Film yang Tersedia:")
    if os.path.exists(FILE_FILM):
        with open(FILE_FILM, 'r') as file:
            for i, film in enumerate(file):
                print(f"{i + 1}. {film.strip()}")
    else:
        print("Tidak ada film yang tersedia.")

# Fungsi untuk menghapus film
def hapus_film():
    tampilkan_daftar_film()
    pilihan_film = input("Masukkan nomor film yang ingin dihapus: ")
    try:
        pilihan_film = int(pilihan_film) - 1
        with open(FILE_FILM, 'r') as file:
            daftar_film = file.readlines()

        if 0 <= pilihan_film < len(daftar_film):
            film_terhapus = daftar_film.pop(pilihan_film)
            with open(FILE_FILM, 'w') as file:
                file.writelines(daftar_film)
            print(f"Film '{film_terhapus.strip()}' telah dihapus.")
        else:
            print("Pilihan film tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor film yang benar.")

# Fungsi untuk membeli tiket
def beli_tiket():
    tampilkan_daftar_film()
    pilihan_film = input("Masukkan pilihan film (nomor): ")
    try:
        pilihan_film = int(pilihan_film) - 1
        with open(FILE_FILM, 'r') as file:
            daftar_film = file.readlines()
            if 0 <= pilihan_film < len(daftar_film):
                film_terpilih = daftar_film[pilihan_film].strip()
                print(f"Anda telah membeli tiket untuk {film_terpilih}")
                simpan_informasi_tiket(film_terpilih)
            else:
                print("Pilihan film tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor film yang benar.")

# Fungsi untuk menghasilkan ID tiket unik
def generate_id_tiket():
    return f"TICK{int(time.time())}"

# Fungsi untuk menyimpan informasi tiket dalam format yang rapi
def simpan_informasi_tiket(film):
    id_tiket = generate_id_tiket()
    waktu_pembelian = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(FILE_TIKET, "a") as file:
        file.write(f"ID: {id_tiket} | Film: {film} | Waktu Pembelian: {waktu_pembelian}\n")
    simpan_bentuk_tiket_ke_file(id_tiket, film)

# Fungsi untuk menyimpan bentuk tiket ke file teks
def simpan_bentuk_tiket_ke_file(id_tiket, judul_film):
    tiket_file = os.path.join(FILE_DIRECTORY, f"{id_tiket}.txt")
    with open(tiket_file, "w") as file:
        file.write("+--------------------------------+\n")
        file.write("|          TIKET BIOSKOP         |\n")
        file.write("+--------------------------------+\n")
        file.write(f"| ID Tiket   : {id_tiket:<20} |\n")      
        file.write(f"| Film       : {judul_film:<20} |\n")
        file.write(f"| Tanggal    : {time.strftime('%d-%m-%Y')}, {time.strftime('%H:%M:%S')} |\n")
        file.write("+--------------------------------+\n")
        file.write("|   Terima kasih telah membeli   |\n")
        file.write("|           tiket Anda!          |\n")
        file.write("+--------------------------------+\n")

# Fungsi untuk menampilkan daftar tiket
def tampilkan_daftar_tiket():
    try:
        with open(FILE_TIKET, "r") as file:
            tiket = file.readlines()
            if tiket:
                print("Daftar Tiket yang Telah Dibeli:")
                for i, t in enumerate(tiket):
                    print(f"{i + 1}. {t.strip()}")
            else:
                print("Belum ada tiket yang dibeli.")
    except FileNotFoundError:
        print("File tiket.txt tidak ditemukan.")

# Fungsi untuk menampilkan detail tiket
def tampilkan_detail_tiket():
    tampilkan_daftar_tiket()
    try:
        pilihan = int(input("Pilih nomor tiket untuk melihat detail: ")) - 1
        with open(FILE_TIKET, "r") as file:
            tiket = file.readlines()
            if 0 <= pilihan < len(tiket):
                # Menampilkan detail dari tiket
                detail_tiket = tiket[pilihan].strip()
                print(f"Detail Tiket: {detail_tiket}")

                # Membaca dan menampilkan bentuk tiket dari file
                id_tiket = detail_tiket.split('|')[0].strip().split(': ')[1]  # Mengambil ID tiket
                tiket_file_path = os.path.join(FILE_DIRECTORY, f"{id_tiket}.txt")
                
                if os.path.exists(tiket_file_path):
                    with open(tiket_file_path, "r") as tiket_file:
                        print("\nTampilan Tiket:")
                        print(tiket_file.read())  # Menampilkan isi tiket
                else:
                    print("File tiket tidak ditemukan.")
            else:
                print("Pilihan tidak valid.")
    except (ValueError, IndexError):
        print("Input tidak valid.")

# Fungsi untuk menghapus tiket
def hapus_tiket():
    tampilkan_daftar_tiket()
    try:
        pilihan = int(input("Pilih nomor tiket untuk dihapus: ")) - 1
        with open(FILE_TIKET, "r") as file:
            tiket = file.readlines()

        if 0 <= pilihan < len(tiket):
            tiket.pop(pilihan)  # Menghapus tiket yang dipilih
            with open(FILE_TIKET, "w") as file:
                file.writelines(tiket)  # Menyimpan sisa tiket ke file
            print("Tiket telah dihapus.")
        else:
            print("Pilihan tidak valid.")
    except (ValueError, IndexError):
        print("Input tidak valid.")

# Menu Utama
def menu_utama():
    while True:
        print('--- Sistem Pemesanan Tiket Bioskop ---')
        print('1. Admin')
        print('2. Pengunjung')
        print('3. Keluar')
        
        pilihan = input('Pilih peran (1/2/3): ')
        
        if pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_pengunjung()
        elif pilihan == '3':
            print('Terima kasih telah menggunakan sistem ini.')
            break
        else:
            print('Pilihan tidak valid!\n')

# Menu Admin
def menu_admin():
    while True:
        print('\n--- Menu Admin ---')
        print('1. Tambah Film')
        print('2. Hapus Film')
        print('3. Tampilkan Daftar Tiket')
        print('4. Kembali')
        
        pilihan = input('Pilih opsi (1/2/3/4): ')
        
        if pilihan == '1':
            tambah_film()
        elif pilihan == '2':
            hapus_film()
        elif pilihan == '3':
            tampilkan_daftar_tiket()
            print('\n--- Daftar Tiket ---')
            print('1. Lihat Detail Tiket')
            print('2. Hapus Tiket')
            print('3. Kembali')
            opsi = input('Pilih opsi (1/2/3): ')
            if opsi == '1':
                tampilkan_detail_tiket()
            elif opsi == '2':
                hapus_tiket()
            elif opsi == '3':
                print('Kembali ke Menu Admin\n')
                break
            else:
                print('Pilihan tidak tersedia\n')
        elif pilihan == '4':
            print('Kembali ke Menu Utama\n')
            break
        else:
            print('Pilihan tidak valid\n')

# Fungsi menu Pengunjung
def menu_pengunjung():
    while True:
        print('\n--- Menu Pengunjung ---')
        print('1. Tampilkan Daftar Film')
        print('2. Beli Tiket')
        print('3. Kembali')
        
        pilihan = input('Pilih menu: ')
        
        if pilihan == '1':
            tampilkan_daftar_film()
        elif pilihan == '2':
            beli_tiket()
        elif pilihan == '3':
            print('Kembali ke Menu Utama\n')
            break
        else:
            print('Pilihan tidak valid.\n')

# Jalankan menu utama
menu_utama()