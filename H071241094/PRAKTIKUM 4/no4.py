def kalkulator():
    try:
        Angka1 = float(input("Masukkan angka pertama: "))
        Angka2 = float(input("Masukkan angka kedua: "))
    
        try :
            operator = str(input("Operasi (+, -, *, /): "))

            if operator not in ["+", "-", "*", "/"]:
                print("operator tidak valid")
                return
            if operator=="+":
                print("Hasil: ", Angka1+Angka2)
            elif operator=="-":
                print("Hasil: ", Angka1-Angka2)
            elif operator=="*":
                print("Hasil: ", Angka1*Angka2)
            else:
                try:
                    print("Hasil: ", Angka1/Angka2)
                except ZeroDivisionError:
                    print("Pembagian dengan 0 tidak diperbolehkan")
        except ValueError:
            print("Operasi tidak valid. Gunakan +, -, *, atau /.")
    except ValueError as a:
        print(f"Input tidak valid:{a}")
kalkulator()