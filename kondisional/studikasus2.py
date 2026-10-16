#DIMAS BAGUS PRATAMA
#2606681
#1C
#Studi Kasus 2

gender = (input("Masukkan gender (pria/wanita) : "))
gender = gender.lower()
umur = int(input("Masukkan umur: "))
tinggi = int(input("Masukkan tinggi: "))
iq = int(input("Masukkan iq: "))

if umur >= 18 and umur <= 25 :
    if iq >= 130 :
        if tinggi >= 170 and gender == "wanita" :
            print("anda lolos seleksi")
        elif tinggi >= 175 and gender == "pria" :
            print("anda lolos seleksi")
        else :
            print("anda tidak memenuhi syarat tinggi")
    else :
        print("anda tidak memenuhi syarat iq")
else :
    print("anda tidak memenuhi syarat umur")