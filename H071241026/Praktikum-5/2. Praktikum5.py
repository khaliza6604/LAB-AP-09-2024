def acronym(s):
    s = s.split()
    print(s)
    acronym = ''.join(huruf[0].upper() for huruf in s)
    print(acronym)
s = input("Masukkan kalimat: ")

acronym(s)