# TUGAS P3 NOMOR 1

# n = int(input("masukkan tinggi: "))
# for i in range (1, n+1):
#     print((n-i) * " " + (2*i-1) * "*")

# for j in range(n-1, -1, -1):
#     print((n-j) * " " + (2*j-1) * "*")

n = int(input("masukkan tinggi: "))
z = int(n / 2)
for i in range (1, z+1):
    print((z-i) * " " + (2*i-1) * "*")

for j in range(z-1, -1, -1):
    print((z-j) * " " + (2*j-1) * "*")