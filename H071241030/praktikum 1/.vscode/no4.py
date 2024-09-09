celcius =(input("konversi suhu dari dari Celcius ke Kelvin, Reamur dan Fahrenheit"))
celcius = int(input("Massukkan suhu dalam Celcius: "))

kelvin = celcius + 273
print("Hasil konversi dari suhu",celcius,"derajat Celcius ke Kelvin adalah : ",{kelvin:.2f},"K" )

reamur = (4/5) * celcius
print("hasil konversi dari suhu",celcius, "derajat Celcius ke Reamur adalah :  ",{reamur:.2f},"R")

fahrenheit = ((9/5) * celcius) + 32
print("Hasil konversi dari suhu", celcius,"derajat Celcius ke Fahrenheit adalah : ",{fahrenheit:.2f},"F")