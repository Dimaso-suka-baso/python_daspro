#resep awal 4 gelas jus perlu 600 gram buah, susu 400 ml, dan gula 4 sendok makan

jus = int(input("jumlah jus yang ingin dibuat: "))
jumlahBuah = int(600 / 4 * jus )
jumlahSusu = int(400 / 4 * jus)
jumlahGula = int(4 / 4 * jus )

print(f"\nBahan bahan yang diperlukan adalah \nbuah {jumlahBuah} gram \nsusu {jumlahSusu} ml\ngula {jumlahGula} sendok makan")