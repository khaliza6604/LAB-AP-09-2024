x = int(input("Masukkan panjang sisi pertama :"))
y = int(input("Masukkan panjang sisi kedua :"))
z = int(input("Masukkan panjang sisi ketiga :"))

if x+y > z and y+z > x and x+z >y:   
    if x == y == z:
        print("Segitiga sama sisi")
    elif x==y or y == z or z==x :
        print("Segitiga sama kaki")
    else : 
        print("Segitiga sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid") 
    