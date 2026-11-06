
#procedure tidak mengembalikan nilai
def perulangan(name):
    print(f"Selamat datang {name}")

perulangan("Subianto")

#function mengembalikan nilai dengan return
def count(panjang, lebar):
    luas = panjang * lebar
    return(luas)

# print(count(8,9))
count(8,9)

#warung mamah dapid

# namaBarang = input("Masukkan menu yang dipesan: ")
# harga = int(input("Harganya bosh: "))
# jumlah = int(input("Masukkan jumlah pesanannya bosh: "))

# def rincianBosh(namaBarang, harga, jumlah): 
#     total = harga * jumlah

#     print(f"Menu yang dipesan {namaBarang}")
#     print(f"Harganya bosh {harga}")
#     print(f"Totalnya bosh {total}")

# rincianBosh(namaBarang, harga, jumlah)

def login(username, password):
    u = "admin"
    p = 1234
    if username == u and password == p :
        logins = "berhasil"
    else :
        logins = "salah bosh"
    return(logins)

u = input("Masukkin: ")
p = int(input("Masukin: "))

print(login(u,p))

