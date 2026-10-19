#calc
# jari = float(input("Masukkan jari jari: "))

# luas = round(3.14 * jari ** 2, 2)
# keliling = round(2 * 3.14 * jari, 2)
# print(luas)
# print(keliling)

# #name tag
# nama = input("Masukkan nama lengkap anda: ").strip().upper()
# kota = input("Masukkan kota asal anda: ").title()

# print(f"Nama : {nama} \nKota : {kota} \nPanjang nama: {len(nama)}")

#waktu
# detik = int(input("Masukkan detik: "))

# jam = detik // 3600
# menit = (detik % 3600) // 60
# detik = detik % 60
# print(f"Hasil : {jam} jam {menit} menit {detik} detik")

#toko
nama1 = input("Masukkan nama barang: ")
harga1 = float(input("Masukkan harga barang: "))
jumlah1 = int(input("Masukkan jumlah barang anda: "))

nama2 = input("Masukkan nama barang: ")
harga2 = float(input("Masukkan harga barang: "))
jumlah2 = int(input("Masukkan jumlah barang anda: "))

nama3 = input("Masukkan nama barang: ")
harga3 = float(input("Masukkan harga barang: "))
jumlah3 = int(input("Masukkan jumlah barang anda: "))

total1 = (jumlah1 * harga1) * 0.10
total2 = (jumlah2 * harga2) * 0.10
total3 = (jumlah3 * harga3) * 0.10

grandTotal = total1 + total2 + total3
print(f"Struk anda \n{nama1} : {harga1} x{jumlah1} \n{nama2} : {harga2} x{jumlah2} \n{nama3} : {harga3} x{jumlah3}")
print("==="*5)
print(f"Total Belanja : {grandTotal}")