students = []

ssc_telugu = 0
ssc_english = 0
ssc_hindi = 0
cbse_telugu = 0
cbse_english = 0
cbse_hindi = 0

for number in range(1, 11):
    print(f"Student {number}")
    name = input("Name: ")
    board = input("Class 10 board (SSC/CBSE): ")
    medium = input("Medium (Telugu/English/Hindi): ")

    students.append({
        "name": name,
        "board": board,
        "medium": medium
    })

print("Student Details")
for student in students:
    print(f"{number}. Name: {student['name']}")
    print(f"Board: {student['board']}")
    print(f"Medium: {student['medium']}")

for student in students:
    if student["board"].lower() == "ssc" and student["medium"].lower() == "telugu":
        ssc_telugu += 1
    elif student["board"].lower() == "ssc" and student["medium"].lower() == "english":
        ssc_english += 1
    elif student["board"].lower() == "ssc" and student["medium"].lower() == "hindi":
        ssc_hindi += 1
    elif student["board"].lower() == "cbse" and student["medium"].lower() == "telugu":
        cbse_telugu += 1
    elif student["board"].lower() == "cbse" and student["medium"].lower() == "english":
        cbse_english += 1
    elif student["board"].lower() == "cbse" and student["medium"].lower() == "hindi":
        cbse_hindi += 1

print("Total students: ", len(students))
print("SSC Telugu:", ssc_telugu)
print("SSC English:", ssc_english)
print("SSC Hindi:", ssc_hindi)
print("CBSE Telugu:", cbse_telugu)
print("CBSE English:", cbse_english)
print("CBSE Hindi:", cbse_hindi)