#Tugas Mandiri no 3
#Dimas Bagus Pratama
#2606681

#input 10 teman sekaligus
listTeman = []

while True : 
    listTeman = input("masukkan nama teman anda: ").split(", ")

    if len(listTeman) < 10 :
        print("Nama teman yang anda masukkan kurang")
    else : 
        break

print(f"List 10 nama teman: \n{listTeman}")
