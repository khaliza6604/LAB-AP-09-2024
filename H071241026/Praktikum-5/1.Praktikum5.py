def Palindrome(kata):
    kata = kata.replace(" ", "")
    kata_balik = kata[::-1] #slicing

    return kata == kata_balik

kata = input("Masukkan kalimat =").lower() 

if Palindrome (kata):
    print("Palindrome")
else:
    print("Not Palindrome")
