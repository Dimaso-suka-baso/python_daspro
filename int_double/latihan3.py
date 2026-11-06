jarak = 180
jarakPerLiter = 12
hargaBensin = 20000 #BBM naik harga

jumlahBensin = jarak / jarakPerLiter
print("Anda perlu bensin sebanyak", round(jumlahBensin), "liter jika ingin menempuh jarak", jarak, "km")

totalBiaya = jumlahBensin * hargaBensin
print("total biaya bensin yang anda perlukan adalah Rp",int(totalBiaya))