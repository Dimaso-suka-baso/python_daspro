#Dimas Bagus Pratama
#2606681

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
passwordAsli = "Latihan"
kesempatan = 3

print("=== MENU LOGIN ===")

while kesempatan > 0:
    username = input("Username: ")
    password = input("Password: ")

    if password == passwordAsli:
        print("Login berhasil dilakukan, Selamat Datang", username)
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f"Password salah! Sisa kesempatan anda adalah: {kesempatan}\n")
        else:
            print("Password yang Anda masukkan salah untuk ketiga kalinya dan Anda dikeluarkan dari menu login.")

#latihan 3
def lari(j,m,d,jS, mS, dS):
    mulai = j * 3600 + m * 60 + d
    selesai = jS * 3600 + mS * 60 + dS
    selisih = selesai - mulai
    if selisih < 0 :
        selisih += 24 * 3600
    selisihjam = selisih // 3600
    selisihmenit = (selisih % 3600) // 60
    selisihdetik = selisih % 60
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