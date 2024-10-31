
def substrings(s):
    length = len(s)
    result = []
    
    # Menghasilkan semua substring
    for start in range(length):
        for end in range(start + 1, length + 1):
            result.append(s[start:end])
    
    # Mengurutkan hasil berdasarkan panjang substring
    result.sort(key=len)
    return result

# Meminta input dari pengguna
user_input = input("Input your string: ")
all_substrings = substrings(user_input)
print('=====================')

# Menampilkan semua substring
for substring in all_substrings:
    print(substring)


def MenampilkanSubstring(string) :
    for i in range(len(string)): 
        for j in range(len(string) - i): 
            print(string[j:j+i+1])

kata = input('Masukkan String: ')
MenampilkanSubstring(kata)
