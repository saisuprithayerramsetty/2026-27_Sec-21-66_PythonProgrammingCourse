marks = int(input("Enter the marks out of 100: "))

if marks >= 90:
    print(f"Grade of a student:A (marks = {marks})")
elif marks >= 80 and marks <90:
    print(f"Grade of a student:B (marks = {marks})")
elif marks >= 70 and marks <80:
    print(f"Grade of a student:C (marks = {marks})")
else:
    print(f"Grade of a student:D (marks = {marks})")