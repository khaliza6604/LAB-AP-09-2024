#Konversi celcius ke kelvin, reamur, dan fahrenheit

celcius = float(input("Masukkkan suhu dalam Celcius"))
Kelvin = 273.15 +celcius
Reamur = 4/5*celcius
farenheit = 9/5*celcius+32

print("Hasil konversi dari suhu 50 derajat Celcius ke Kelvin adalah =",Kelvin,"k")
print("Hasil konversi dari suhu 50 derajat Celcius ke Reamur adalah =",Reamur,"R")
print("Hasil konversi dari suhu 50 derajat Celcius ke Farenheit adalah =",farenheit, "f")