#smallest number among three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a <= b:
    if a <= c:
        smallest = a
    else:
        smallest = c
else:
    if b <= c:
        smallest = b
    else:
        smallest = c
print(f"Smallest of three numbers = {smallest} (among {a}, {b}, {c})")