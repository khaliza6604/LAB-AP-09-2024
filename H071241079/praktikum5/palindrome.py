def palindrome(s): 
    s = s.lower()
    
    if s == s [::-1] : 
        print("palindrome") 
    else:
        print("bukan palindrome")

palindrome("Ibu Ratna Antar Ubi")  
palindrome("Sistem Informasi 2024") 