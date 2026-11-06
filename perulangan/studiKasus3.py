#DIMAS BAGUS PRATAMA
#2606681
#1C
#Studi Kasus 3

banyakBilangan = int(input("Masukkan banyak bilangan: "))
bilangan = []

for x in range(banyakBilangan) :
    b = int(input(f"Masukkan bilangan ke-{x+1}: "))
    bilangan.append(b)

for a in bilangan :
    if a % 2 == 0 :
        print(f"Bilangan {a} adalah genap")
    else :
        print(f"Bilangan {a} adalah ganjil")
