jarak = 180
jarakPerLiter = 12
hargaBensin = 13000

jumlahBensin = jarak / jarakPerLiter
print("Anda perlu bensin sebanyak", round(jumlahBensin), "liter jika ingin menempuh jarak", jarak, "km")

totalBiaya = jumlahBensin * hargaBensin
print("total biaya bensin yang anda perlukan adalah Rp",int(totalBiaya))