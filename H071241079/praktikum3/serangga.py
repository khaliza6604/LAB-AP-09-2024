populasi_A = float(input("Masukkan populasi awal serangga A: "))
populasi_B = float(input("Masukkan populasi awal serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

for hari in range(1, jumlah_hari + 1):
    if hari % 2 == 1:  
        populasi_A += populasi_A * 0.30  
        populasi_B += populasi_B * 0.50  
    else:  
        populasi_A -= populasi_A * 0.20  
        populasi_B -= populasi_B * 0.40  
    
    print(f"Hari {hari}: Serangga A = {int(populasi_A)}, Serangga B = {int(populasi_B)}")
    
    if hari % 5 == 0:  
        print(f"Hari {hari}: Predator memakan 10% populasi.") 
        populasi_A -= populasi_A * 0.10  
        populasi_B -= populasi_B * 0.10  
        
        print(f"Hari {hari}: Serangga A = {int(populasi_A)}, Serangga B = {int(populasi_B)}") 