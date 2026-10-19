#Dimas Bagus Pratama
#2606681


# no 1
total = 0
for harga in range(5):
    total += 25000
print(total)

# no 2
total = 0
data = 5
for tes in range(data):
    nilai = int(input("Masukan Nilai Mahasiswa : "))
    total += nilai
rataRata = total / data
print(rataRata)

# no 3
hasil = 0
for tes in range(0, 21, 2):
    hasil += tes
print(hasil)

# no 4
jumlah_lulus = 0
for tes in range(5):
    nilai = int(input("Masukkan nilai mahasiswa: "))
    if nilai >= 65:
        jumlah_lulus += 1
print(jumlah_lulus)
