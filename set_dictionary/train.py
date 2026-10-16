menu = {
    "nasi goreng": 20000,
    "es teh": 5000,
    "kopi": 8000,
}
menu["es teh"]= 6000
menu["mie ayam"]= 15000

# pesanan = {"nasi goreng": 2, "es teh": 3}

print("Selamat Datang di Resto kami \nsilahkan pesan sesuai menu yang tertera")
print("="*15)
for nama, harga in menu.items():
     print(f"{nama}: Rp {harga}")
print("="*15)

item = input("Masukkan menu yang ingin di pesan ").lower()
jumlah = int(input("Masukkan jumlah yang ingin di pesan "))
pesanan = {item : jumlah}

total = 0
for item, jumlah in pesanan.items():
    if item in menu :
        harga = menu[item]         # ambil harga item dari dictionary menu
        total = total + (harga * jumlah)  # harga dikali jumlah
    else :
        print(f"{item} tidak ada di menu")
    
print(f"total harga: {total}")


