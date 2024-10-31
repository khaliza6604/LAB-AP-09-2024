# Meminta input string dari pengguna
user_input = input("Masukkan sebuah string: ")

# Mengambil panjang string
length = len(user_input)

# Menampilkan semua substring yang mungkin
print("Semua substring yang mungkin:")
for i in range(length):
    for j in range(i + 1, length + 1):
        print(user_input[i:j])
