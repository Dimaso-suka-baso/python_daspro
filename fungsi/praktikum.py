def greeting(nama):
    umur = 19
    print(f"halo {nama} dengan umur {umur}")

greeting("Andi")

def volBalok(p,l,t):
    volume = p * l * t
    return(volume)

print(volBalok(10,9,8))

namaGlobal = "Sam"

def menyapa():
    print(f"Selamat datang {namaGlobal}")

menyapa()

def kelilingSegitiga(a, b, c):
    print(a + b + c)

kelilingSegitiga(10, 6, 5)

def sapaan(nama = "Kuro"):
    print(f"Halo, {nama}")

sapaan()
sapaan("Shiro")

# def pengurangan(a, b):
#     print(f"Hasilnya adalah {a-b}")

# #menggunakan keyword arguments
# pengurangan(b = 2, a = 5)

# #tanpa keyword arguments
# pengurangan(2,5)

def pengurangan(a, b, c = 10):
    hasil = a - b - c
    return hasil

#menggunakan keyword arguments
pengurangan(b = 2, a = 5)

#tanpa keyword arguments
print(pengurangan(10, 5))
print(pengurangan(b = 10, a = 5))
print(pengurangan(10, 2, 5))

#Arbitrary Argument
def funcArgs(*angka):
    print(f"Angka terakhir yang dimasukkan yaitu {angka[-1]}")

funcArgs(1,2,8,9,5)
