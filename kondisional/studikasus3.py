#DIMAS BAGUS PRATAMA
#2606681
#1C
#Studi Kasus 3

nama = input("Masukkan nama: ")
nama = nama.title()
tugas = int(input("Masukkan nilai tugas: "))
uts = int(input("Masukkan nilai UTS: "))
uas = int(input("Masukkan nilai UAS: "))

avg = (tugas + uts + uas) / 3
if avg >= 70 :
    if tugas >= 60 and uts >=60 and uas>=60 :
        print(f"{nama} kamu LULUS tanpa remedial")
    else :
        print(f"{nama} kamu LULUS dengan remedial")
else :
    if avg >= 50:
        print(f"{nama} kamu TIDAK LULUS, boleh remedial")
    else :
        print(f"{nama} kamu TIDAK LULUS dan tidak boleh remedial")
