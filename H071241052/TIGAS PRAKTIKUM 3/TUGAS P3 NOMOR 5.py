# TUGAS P3 NOMOR 5

# A = int(input("Masukkan populasi awal serangga A: "))
# B = int(input("Masukkan populasi awal serangga B: "))
# day = int(input("masukkan jumlah hari: "))

# for i in range(1, day+1):
#     if day % 2 == 1:
#       A = int(A * 1.3)
#       B = int(B * 1.5)
#     else:
#        A = int(A * 0.8)
#        B = int(B * 0.6)

#     if i % 5 == 0:
#         A = int(A * 0.9)
#         B = int(B * 0.9)
#         print(f"hari ke {i}: predator memakan 10% populasi")
#     print(f"Hari {i}: Serangga A = {A}, Serangga B = {B}")


PA = int(input("Masukkan populasi awal Serangga A: "))
PB = int(input("Masukkan populasi awal Serangga B: "))
N = int(input("Masukkan jumlah hari: "))

for hari in range(1, N+1):
    if hari % 2 == 1:
        PA = int(PA * 1.3)
        PB = int(PB * 1.5)

    else:
        PA = int(PA * 0.8)
        PB = int(PB * 0.6)


    if hari % 5 == 0:
        PA = int(PA * 0.9)
        PB = int(PB * 0.9)
        print(f"Hari {hari}: Predator memakan 10% populasi.")

    print(f"Hari {hari}: Serangga A = {PA}, Serangga B = {PB}")
