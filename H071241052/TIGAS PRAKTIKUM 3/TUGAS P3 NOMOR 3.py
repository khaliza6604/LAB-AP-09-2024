# TUGAS P3 NOMOR 3
# full chatgpt

# Input ukuran grid NxM
N = int(input("N : "))
M = int(input("M : "))

# Mulai dari titik (0, 0)
for i in range(N):
    # Jika baris ganjil, bergerak ke kanan
    if i % 2 == 0:
        for j in range(M):
            print(f"MOVE ke ({i}, {j})")
    # Jika baris genap, bergerak ke kiri
    else:
        for j in range(M-1, -1, -1):
            print(f"MOVE ke ({i}, {j})")
