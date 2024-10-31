# x = ["kelvin", 1, "fahmi", 2, "mario", 3]
# print(x)

# x = list(range (10))
# for i in range(10):
#     print(x)

# JUMLAH LIST
# a = [0, 1, 2, 3, 4]
# print(len(a))


# OUTPUT SPESIFIK DALAM LIST
# a = ["apel", "mangga", "jeruk"]
# print(a[0])

# a = ["apel", "mangga", "jeruk"]
# print(a[len(a)-2])


# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# x = a[-2:]
# print(x)

# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# x = a[::-2]
# print(x)

#MEMANGGIL INDEKS DALAM LIST DUA DIMENSI
# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# b = [[1, 2], [3, 4]]
# x = b[1] [0]
# print(x)

# MAMASUKKAN STRING BARU PADA LIST
# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# # a.append("pisang")
# # a.insert(2, "anggur")
# a.extend(["pisang", "anggur"])
# print(a)

# MENAMBAHKAN VARIABEL GRUP PADA VARIABEL LAIN
# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# b = [[1, 2], [3, 4]]
# a.extend(b)
# print(a)

#MENGHAPUS LIST
# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# b = [[1, 2], [3, 4]]
# a.remove("apel")
# a.pop(2)
# print(a)

# MEMBALIK LIST
# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# b = [[1, 2], [3, 4]]
# a.reverse()
# print(a)

# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# b = [[1, 2], [3, 4]]
# print([i for i in a])

#TUPLE
# MENGGANTI STRING
# a = ("apel", "mangga", "jeruk", "pepaya", "nanas")
# b = [[1, 2], [3, 4]]
# a = list(a)
# a[0] = "anggur"
# a = tuple(a)
# print(a)

#SET
# BILANGAN SELALU BERURUTAN
# STRING KELUAR SECARA ACAK
# TIDAK DISARANKAN MENGUBAH STRING PADA SET
# TIDAK BISA MENGHAPUS STRING
# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# b = [[1, 2], [3, 4]]
# c = {1, 5, 2, 8, 3, 4}
# d = {"apel", "mangga", "jeruk", "pepaya", "melon"}
# d = list(d)
# d[0] = "anggur"
# d = set(d)
# print(d)

# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# b = [[1, 2], [3, 4]]
# c = {1, 5, 2, 8, 3, 4}
# d = {"apel", "mangga", "jeruk", "pepaya", "melon"}
# for i in d:
#     print(i)

# a = ["apel", "mangga", "jeruk", "pepaya", "nanas"]
# b = [[1, 2], [3, 4]]
# c = {1, 5, 2, 8, 3, 4}
# d = {"apel", "mangga", "jeruk", "pepaya", "melon"}

# m = {1, 2, 3, 4, 5}
# n = {4, 5, 6, 7, 8}
# #print(n.symmetric_difference(n))

# e = {
#     "nama": "kelvin",
#     "umur": 28
#     }
# print(e["nama"])
# print(e["umur"])

angka1 = input("masukkan angka1: ")
angka2 = input("masukkan angka2: ")
my_list = angka1 + angka2

print(len(my_list))






