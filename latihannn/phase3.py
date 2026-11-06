data = {
    "Ani":   [80, 90, 70],
    "Budi":  [60, 50, 40],
    "Citra": [95, 85, 90],
    "Dodi":  [70, 65, 75]
}
drata = {}
print("hasil mahasiswa kelas 2b: ")
for nama, (n, j, i)in data.items() :
    nilai = (n + j + i)
    rata = round(nilai / 3, 1)
    drata[nama] = rata

for nama, rata in drata.items() :
    if min(data[nama]) < 50 :
        predikat = "REMEDIAL"
    elif rata >= 85 :
        predikat = "A"
    elif rata >=70 :
        predikat = "B"
    elif rata >= 60 :
        predikat = "C"
    else :
        predikat = "D"
    print(f"{nama} | {rata} | {predikat}")


        
