penjualan = [120, 150, 135, 180, 160]
print("Data penjualan awal: ",penjualan)
penjualan[2] = 140
print(f"Data penjualan setelah revisi hari kedua: \n{penjualan}")
penjualan.append(175)
print(f"Data penjualan ditambah hari berikutnya: \n{penjualan}")
penjualan.append( 155)
print(f"Data penjualan ditambah hari ketujuh: \n{penjualan}")
penjualan.remove(150) 
print(f"Data rekap: \n{penjualan}")
hargaProduk = 75000

totalProduk = sum(penjualan)
print(f"Total produk yang terjual: \n{totalProduk}")

pKotor = totalProduk * hargaProduk
print(f"Pendapatan kotor: {pKotor}")
bPlatform = int(pKotor * 0.5)
print(f"Biaya platform: \n{int(bPlatform)}")

pBersih = int(pKotor - bPlatform)
print(f"Pendapatan Bersih: {pBersih}")
