#Latihan 2
#Dimas Bagus Pratama
#2606681
students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

list_prodi = list(students.values())
prodi_counter = {
    "Computer Science" :list_prodi.count("Computer Science"),
    "Mathematics" : list_prodi.count("Mathematics"),
    "Physics" : list_prodi.count("Physics")
}


print("prodi computer science sebanyak", prodi_counter["Computer Science"])
print("prodi mathematics sebanyak", prodi_counter["Mathematics"])
print("prodi physics sebanyak", prodi_counter["Physics"])
