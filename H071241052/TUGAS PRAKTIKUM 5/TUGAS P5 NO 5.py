def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Memproses huruf kecil
        if char.islower():
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        # Memproses huruf besar
        elif char.isupper():
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Biarkan angka dan karakter spesial tetap sama
        else:
            encrypted_text += char
    
    return encrypted_text

# Input dari user
input_string = input("Masukkan string: ")
shift_value = int(input("Masukkan jumlah pergeseran (shift): "))

# Proses enkripsi
encrypted_result = caesar_cipher(input_string, shift_value)

# Menampilkan output sesuai format
print(f"Text  : {input_string}")
print(f"Shift : {shift_value}")
print(f"Cipher: {encrypted_result}")
