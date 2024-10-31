def akronim (kalimat):
    kata = kalimat.split()

    a = "" 
    for i in kata:
        a = a + i[0]
    print(a) 
akronim("Negara Republik Kesatuan Indonesia") 
akronim("Badan Usaha Milik Negara") 