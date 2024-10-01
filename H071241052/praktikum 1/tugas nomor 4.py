#tugas P1 nomor 4

def konversi_suhu(celcius):
    kelvin = celcius + 273.15
    reamur = celcius * 4 / 5
    fahrenheit = (celcius * 9 / 5) + 32
    
    return kelvin, reamur, fahrenheit

celcius = float(input("Masukkan suhu dalam Celcius: "))

kelvin, reamur, fahrenheit = konversi_suhu(celcius)

print(f"Suhu dalam Kelvin: {kelvin:.2f} K")
print(f"Suhu dalam Reamur: {reamur:.2f} °R")
print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f} °F")
