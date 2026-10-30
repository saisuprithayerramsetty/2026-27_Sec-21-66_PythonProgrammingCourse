#using for loop
n = int(input("Enter the value of N: "))

for number in range(1, n + 1):
    print(f"{number}")

#using while loop
n = int(input("Enter the value of N: "))

number = 1
while number <= n:
    print(f"{number}")
    number = number + 1