#Tugas Mandiri no 1
#Dimas Bagus Pratama
#2606681

list = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]

#tampilkan data nilai maksimum
print("Nilai maksimal:",max(list))

#tampilkan data nilai minimum
print("Nilai minimum:",min(list))

#tampilkan nilai rata-rata
rataRata = (88+ 75+ 63+ 97+ 82+ 74+ 91+ 80+ 81+ 63) / 10
print("Nilai rata-rata:",rataRata) 

#Tampilkan angka terbesar kedua
list.sort()
print("Urutan nilai dari terkecil ke terbesar", list)
print("Angka terbesar kedua:",list[8])
