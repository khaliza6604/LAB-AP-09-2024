N = int(input('N = '))
M = int(input('M = '))

posisi_x = 0
posisi_y = 0

for i in range (N) :
    if i % 2 == 0 :
        for a in range (M):
            print(f"MOVE to ({i}, {a})")
    else: 
        for kolom in range (M - 1, -1, -1):
            print(f"MOVE to ({i}, {kolom})")