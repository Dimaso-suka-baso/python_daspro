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
def nilaiTotal(*angka):
    return sum(angka)

def nilaiRataRata(*angka):
    return sum(angka) / len(angka)

inputAngka = []

while True:
    masukan = input("Masukkan angka (ketik 'selesai' untuk berhenti): ")
    if masukan.lower() == "selesai":
        break
    inputAngka.append(int(masukan))

if len(inputAngka) > 0:
    print(f"Total : {nilaiTotal(*inputAngka)}")
    print(f"Rata-rata : {nilaiRataRata(*inputAngka)}")
else:
    print("Belum ada angka yang dimasukkan.")

#latihan 2
passwordAsli = "Latihan"
kesempatan = 3

print("Menu Login SMAN 2 Harapan")

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