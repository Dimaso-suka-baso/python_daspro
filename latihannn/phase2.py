produk = {
    "beras" : (14000, 10),
    "minyak": (18000, 5),
    "gula": (16000, 0),
    "telur": (28000, 20)
}

for n, (j, i) in produk.items() :
    if i == 0 :
        print(f"{n} | Rp{j} | stok: HABIS")
    else :
        print(f"{n} | Rp{j} | stok: {i}")

keranjang = []

while True:
    nama = input("Masukkan nama barang (ketik selesai kalau udah): ")
    if nama == "selesai" :
        break

    if nama not in produk :
        print("barang tidak ada")
        continue
    jumlah = int(input("Masukkan jumlah barang: "))
    harga, stok = produk[nama]
    if jumlah > stok :
        print("stok tidak cukup")
        continue 

    subtotal = harga * jumlah
    keranjang.append((nama, jumlah, subtotal))
    produk[nama]=(harga, stok - jumlah)
    print("Berhasil ditambahkan")

total = 0
for nama, jumlah, subtotal in keranjang :
    total += subtotal

if total >= 200000 :
    disc = 0.10
    totalDisc = total * disc
    total = total - totalDisc
    print(f"Total : {total}")
elif total >= 100000 :
    disc = 0.05
    totalDisc = total * disc
    total -= totalDisc
    print(f"Total : {total}")
else :
    print(f"Total : {total}")

while True:
    bayar = int(input("Masukkan uang: "))
    if bayar >= total :
        break
    else: 
        print("Uang anda kurang harap masukkan lagi")

kembalian = int(bayar - total)
puluhan = kembalian // 50000
ribuan = kembalian % 50000 
print(f"Kembalian anda adalah {puluhan} lembar Rp50.000 dan {ribuan} ")

produkAwal = set()
produkTerjual = set()
for x, (y, z)in produk.items():
    produkAwal.add(x)
for (n, j, h) in keranjang :
    produkTerjual.add(n)
    
noTerjual = produkAwal.symmetric_difference(produkTerjual)
print(noTerjual)

produkAwal = set(produk(1))
print(produkAwal)