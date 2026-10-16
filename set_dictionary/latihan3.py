#Latihan 3
#Dimas Bagus Pratama
#2606681

student_info = {
    "Alice": {"age" : 20, "major": "Computer Science"},
    "Bob": {"age" : 21, "major": "Mathematics"},
    "Charlie": {"age" : 19, "major": "Physics"}
}

student = input("Inputkan nama siswa: ")
data = student_info[student]

print(f"Umur {student} adalah {data.get("age")} dan Prodi nya adalah {data.get("major")}")