num = int(input("Enter the N: "))
a = 0
b = 1
for i in range(num):
    print(a)
    next_term = a + b
    a = b
    b = next_term