#latihan 1
#1
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()

fibonacci(8)

#2
def volTab(r,t,p = 22/7):
    volume = p * r**2 * t
    return volume

print(volTab(7,10))

#3
inputAngka= []

def nilaiTotal(*angka):
    total = sum(angka)
    return total

def nilaiRataRata(*angka):
    total = sum(angka)
    jumlahAngka = len(angka)
    rataRata = total / jumlahAngka
    return rataRata

jumlahAngka = int(input('Masukan jumlah angka yang diinginkan: '))

for i in range(jumlahAngka):
    inputAngka.append(int(input(f"Masukan Angka ke {i+1} : ")))
    
print(f"Total : {nilaiTotal(*inputAngka)}")
print(f"Rata-rata : {nilaiRataRata(*inputAngka)}")

#latihan 2

#latihan 3
def lari(j,m,d,jS, mS, dS):
    selisihjam = jS - j
    selisihmenit = mS - m
    selisihdetik = dS - d
    print(f"{selisihjam} jam - {selisihmenit} menit -  {selisihdetik} detik")

print("Input mulai: ")
j = int(input("Jam: "))
m = int(input("Menit: "))
d = int(input("Detik: "))

print("\nInput selesai")
jS = int(input("Jam: "))
mS = int(input("Menit: "))
dS = int(input("Detik: "))

lari(j,m,d,jS,mS,dS)