# String = input("Masukkan string: ")

# # myString = "Bapak diminta menghadap presiden"
# myreversed = reversed(String)
# print(type(myreversed))
# print(''.join(myreversed))

# if String == str(myreversed):
#     print("Palindrom")
# else:
#     print("Bukan Palindrom")

# n = "sama"
# z = "sama"

# if n == z:
#     print("yeay!")


    # Mengubah semua huruf menjadi huruf kecil untuk mengabaikan perbedaan besar kecil huruf

    # Menghilangkan stringpastringi dan tanda baca jika ada
    # reversed_string = ''.join(e for e in string if e.istringalnum())
    
    # Membandingkan stringtring astringli dengan stringtring yang dibalik
def palindrome(string): 
    string = string.lower()
    reversed_string = string[::-1]
    if string == reversed_string :
        print("Palindrome")
    else:
        print("Bukan Palindrome")
    print(reversed_string)

palindrome("aku")
palindrome("ibu ratna antar ubi")

#SUDAH DIPERIKSA TAPI PERBAIKI SAJA
