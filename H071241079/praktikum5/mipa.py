def cetak_semua_substring(string):
    panjang = len(string)
    for i in range(1, panjang + 1):
        for j in range(panjang - i + 1):
            print(string[j:j + i])

input_pengguna = input("Input Your String: ")
print("========================")
cetak_semua_substring(input_pengguna) 