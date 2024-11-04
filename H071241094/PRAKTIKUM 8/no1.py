
import re

def validasi_string(s):
    if len(s) != 45:
        return False
    
    bagian_pertama = s[:40]
    bagian_terakhir = s[40:]
    
    # Validasi karakter 
    if not re.match(r"^[a-zA-Z02468]{40}$", bagian_pertama):
        return False
    
    if not re.match(r"^[13579\s]{5}$", bagian_terakhir):
        return False
    
    return True

input_pengguna = input("Masukkan string 45 karakter untuk divalidasi: ")

# Menampilkan hasil validasi
if validasi_string(input_pengguna):
    print("True")
else:
    print("False")
