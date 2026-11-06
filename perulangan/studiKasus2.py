#DIMAS BAGUS PRATAMA
#2606681
#1C
#Studi Kasus 2

listHewan = []

jumlah = int(input("Masukkan jumlah hewan yang akan di input: "))

for x in range(jumlah) :
    hewan = input(f"Masukkan nama hewan ke {x + 1} ")
    listHewan.append(hewan)
    
for i in range(len(listHewan)):
    print(f"hewan ke-{i+1} adalah {listHewan[i]}")