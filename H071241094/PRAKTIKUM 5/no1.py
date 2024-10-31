
def palindrome():
    kata = input('Masukkan kalimat: ')
    palindrom = ''.join(reversed(kata.lower()))
    # Memeriksa apakah string sama dengan string terbalik
    if kata.lower() == palindrom:
        print('Palindrome')
    else:
        print('Not Palindrome')

palindrome()
