hargaPaket = 35000
sewaTempat = 2000000
dokumentasi = 500000
satuRimIsi = 500
hargaKertas = 65000

print("SISTEM KALKULASI DANA PENYELENGGARAAN ACARA")
print("=======" *10)

jumlahPeserta = int(input("Masukkan jumlah peserta: "))

jumlahPaket = round(jumlahPeserta 
                    + jumlahPeserta 
                    * (10 / 100)) 
totalBiaya = round(jumlahPaket 
                   * hargaPaket)

print(f"Total paket konsumsi: {jumlahPaket} \nTotal biaya konsumsi peserta: Rp {totalBiaya}")
print("=======" *10)


jumlahKertas = (jumlahPeserta 
                + jumlahPeserta 
                * (5 / 100))

totalRimKertas = int((jumlahKertas + satuRimIsi - 1) 
                     //satuRimIsi)

totalBiayaKertas = totalRimKertas * hargaKertas

print(f"jumlah kertas: {int(jumlahKertas)} lembar \nPerkiraan rim: {totalRimKertas} \nJumlah sertifikat: {jumlahPeserta} lembar \nTotal biaya kertas: Rp {totalBiayaKertas}")
print("=======" *10)

biayaAcara = int((totalBiayaKertas 
                  + totalBiaya 
                  + sewaTempat 
                  + dokumentasi))

danaDarurat = int(biayaAcara * 0.10)

totalDana = biayaAcara + danaDarurat

biayaPendaftaran = totalDana / jumlahPeserta

print(f"Dana Penyelenggaraan: Rp {biayaAcara} \nDana darurat: Rp {danaDarurat} \nDana yang harus dikumpulkan: Rp {totalDana} \nBiaya pendaftaran: Rp {round(biayaPendaftaran)}")
print("=======" *10)
