harga = int(input("Harga barang: "))
jumlah = int(input("Masukkan jumlah: "))

total = harga * jumlah
discount = 0.10
totalDiskon = int(total * discount)

if total > 100000 :
    totalPembayaran = total - totalDiskon
    if totalPembayaran >= 150000 :
        print(f"Total belanja: {total} \nDiskon: {totalDiskon} \nTotal Pembayaran: {totalPembayaran} \nAnda mendapat voucher bonus")
    else : 
        print(f"Total belanja: {total} \nDiskon: {totalDiskon} \nTotal Pembayaran: {totalPembayaran} \nAnda tidak mendapatkan voucher bonus")
else :
    print("tidak mendapatkan diskon")



    