# import re

# def validate_ip(ip):
#     ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
#     ipv6_pattern = r"^(([\d,A-F,a-f]{1,4}\:){7})([\d,A-F,a-f]{1,4}$"
    
#     # Validasi alamat 
#     if re.match(ipv4_pattern, ip):
#         # Memastikan setiap segmen IPv4 berada di antara 0-255
#         parts = ip.split('.')
#         if all(0 <= int(part) <= 255 for part in parts):
#             return "IPv4"
   
#     elif re.match(ipv6_pattern, ip):
#         return "IPv6"
    
#     return "Bukan IP Address"

# n = int(input("Masukkan jumlah alamat IP yang akan divalidasi: "))

# # Input alamat IP dari pengguna dan simpan di dalam list
# ip_addresses = []
# print("Masukkan setiap alamat IP pada baris terpisah:")
# for _ in range(n):
#     # Mengambil input dari pengguna, menghapus spasi
#     ip_addresses.append(input().strip())

# print("Hasil Validasi:")
# for ip in ip_addresses:
#     print(validate_ip(ip))


import re

def validate_ip(ip):
    ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    
    # Validasi alamat IPv4
    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return "IPv4"
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    
    return "Bukan IP Address"

n = int(input("Masukkan jumlah alamat IP yang akan divalidasi: "))

ip_addresses = []
print("Masukkan setiap alamat IP pada baris terpisah:")
for _ in range(n):
    ip_addresses.append(input().strip())

# Menampilkan hasil validasi untuk setiap IP
print("Hasil Validasi:")
for ip in ip_addresses:
    print(validate_ip(ip))