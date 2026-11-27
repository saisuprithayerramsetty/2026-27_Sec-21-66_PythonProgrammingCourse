# Example solution: sort list of dictionaries
students = [
    {"name": "Akhila", "marks": 99},
    {"name": "Sanjana", "marks": 85},
    {"name": "Rizwana", "marks": 90},
]

by_marks = sorted(students, key=lambda d: d["marks"])
print("By marks ascending:", by_marks)

by_marks_desc = sorted(students, key=lambda d: d["marks"], reverse=True)
print("By marks descending:", by_marks_desc)