#using for loop
n = int(input("Enter N (use pass for multiples of 3): "))

for number in range(1, n + 1):
    if number % 3 == 0:
        pass
        print(f"Used pass for multiple of 3: {number} (N is {n})")
    else:
        print(f"for loop number = {number} (up to {n})")


#using while loop
n = int(input("Enter N (use pass for multiples of 3): "))

number = 1
while number <= n:
    if number % 3 == 0:
        pass
        print(f"Used pass for multiple of 3: {number} (N is {n})")
    else:
        print(f"while loop number = {number} (up to {n})")
    number = number + 1