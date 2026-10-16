#operator in python

#arithmetic

#penjumlahan
a = 2 + 3
print(a)
#pengurangan
b = 5 - 3
print(b)
#perkalian
c = 9 * 8
print(c)
#pembagian
d = 9 / 2
print(d)
#pembulatan 
e = 9 // 2
print(e)
#modulus
f = 10 % 3
print(f)
#eksponensial
g = 9 ** 2
print(g)

#comparison

#equal
print(2 == 0) #false
#not equal
print( 2 != 0) #true
#greater than 
print( 2 > 0 ) 
#less than
print( 4 < 8)
#greater than or equal to
print(4 <= 4)
#less than or equal to 
print(8 >= 8)

#assignment
x = 0
print(x)
x += 2
print(x)
x -= 9
print(x)
x *= 9
print(x)
x /= 2
print(x)
x //= 2
print(x)
x %= 3
print(x)
x **= 2
print(x)

#logical
print("Logical")
x = 2
print(x > 1 and x < 3) #true karena value x memenuhi kedua kriteria

print(x > 2 or x < 4) #true karena value x < 4 yaitu 2

print(not(x < 0 and x > 5)) #true karena x = 2 

#membership
print("Membership")
x = [1, 2, 3, 4]

print(2 in x)
print(9 in x)

print(2 not in x)
print(7 not in x)

#identity
print("identity")
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = x 

print(x is y)
print(x is z)

print(x is not y)
print(x is not z)

#quiz
#operator "and" akan bernilai true
x = 17 // 2
print(x)

#kondisional
x = 1
if (x > 0) :
    print("eksekusi perintah ini")

x = 5
if (x > 1) :
    print("x > 1")

x = 0 
if (x > 1) :
    print("x > 1") #no output tanpa else or elif

x = 3
if (x > 0 and x < 5) :
    print("x > 0 dan < 5")

nilai = 80
if (nilai > 75):
    print("Selamat anda lulus")
else :
    print("Ayo belajar lagi")

nilai = 80
absen = 70
if (nilai > 75 and absen > 80):
    print("Selamat anda lulus")
else : 
    print("Ayo belajar lagi")

umur = 16
if (umur >= 17):
    print("Anda boleh membuat SIM")
elif (umur < 17):
    print("Anda belum boleh membuat SIM")

a = 2
b = 5 
if (a > b):
    print("Nilai a lebih besar dari b")
elif(a < b):
    print("Nilai b lebih besar dari a")
else :
    print("Nilai a sama dengan b")

a = 2
b = 1

if a > b : print("Nilai a lebih besar dari b")

a = 2
b = 3

print("Nilai a lebih besar ") if a > b else print("Nilai a lebih besar dari b")

