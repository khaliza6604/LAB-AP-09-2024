from collections import Counter

def min_deletions_to_anagram(s1, s2):
    # Hitung frekuensi setiap karakter di kedua string
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Hitung jumlah penghapusan
    deletions = 0
    
    # Iterasi melalui semua karakter di count1
    for char in count1:
        if char in count2:
            deletions += abs(count1[char] - count2[char])
        else:
            deletions += count1[char]
    
    # Iterasi melalui karakter yang hanya ada di count2
    for char in count2:
        if char not in count1:
            deletions += count2[char]
    
    return deletions

# Main program untuk input dan output
if __name__ == "__main__":
    # Input dari pengguna
    s1 = input("Masukkan string pertama: ")
    s2 = input("Masukkan string kedua: ")
    
    # Hitung jumlah minimum penghapusan
    result = min_deletions_to_anagram(s1, s2)
    
    # Tampilkan hasil
    print(f"Jumlah minimum penghapusan untuk membuat anagram: {result}")
