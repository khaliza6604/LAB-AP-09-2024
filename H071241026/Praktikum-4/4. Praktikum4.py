def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")

    while True:
        try:
            a = float(input("Angka pertama: "))
            b = float(input("Angka kedua: "))
            operasi = input("Operasi (+, -, *, /): ")
            if operasi in ['+', '-', '*', '/']:
                break
            else:
                print("Operasi tidak valid. Gunakan (+, -, *, /) atau /")
        except ValueError:
            print("Mohon masukkan angka yang valid")

    if operasi == '+':
        hasil = a + b
    elif operasi == '-':
        hasil = a - b
    elif operasi == '*':
        hasil = a * b
    elif operasi == '/':
        if a != 0:
            hasil = a / b
        else:
            print("Pembagian dengan nol tidak diperbolehkan")
            return

    print(f"Hasil dari {hasil :.0f}")

kalkulator()