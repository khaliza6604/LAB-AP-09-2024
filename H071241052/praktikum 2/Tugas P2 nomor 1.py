#Tugas P2 nomor 1

sisi_pertama = int(input("masukkan sisi pertama: "))
sisi_kedua = int(input("masukkan sisi kedua: "))
sisi_ketiga = int(input("masukkan sisi kedua: "))

if sisi_pertama + sisi_kedua > sisi_ketiga and sisi_pertama + sisi_ketiga > sisi_kedua and sisi_kedua + sisi_ketiga > sisi_pertama:
    if(sisi_pertama == sisi_kedua == sisi_ketiga): 
        print("segitiga sama sisi") 
    elif(sisi_pertama == sisi_kedua) or (sisi_pertama == sisi_ketiga) or (sisi_kedua == sisi_ketiga): 
        print("segitiga sama kaki")
    else :
        print("segitiga sembarang")
        
else: print("tidak dapat membentuk segitiga yang valid")
