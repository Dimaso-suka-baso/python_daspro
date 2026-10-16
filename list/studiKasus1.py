#Studi Kasus 1
#Dimas Bagus Pratama
#2606681

buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

#1
buah[2] = "cherry"
print(f"1. Ganti item dengan nama ceri menjadi cherry  \n{buah}")

#2
buahUser = (input("masukkan nama buah: "))
index = int(input("masukkan index: "))
buah.insert(index, buahUser)
print(f"2. Tambahkan item dengan nama dan index yang ditentukan oleh User \n{buah}")

#3
buah.sort()
print(f"3. Urutkan item pada list sesuai dengan abjadnya \n{buah}")