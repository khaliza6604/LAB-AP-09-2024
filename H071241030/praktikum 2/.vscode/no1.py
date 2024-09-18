a = int(input("masukkan panjang sisi pertama : "))
b = int(input("masukkan panjang sisi kedua : " ))
c = int(input("masukkan panjang sisi ketiga : " ))

if a + b > c and b + c > a and a + c > b :
   if a == b == c :
      print("segitiga sama sisi")
   elif a == b  or b == c  or a == c :
      print("segitiga sama kaki")
   else :
      print("segitiga sembarang")
else :
   print("tidak dapat membentuk segitiga yang valid")

   