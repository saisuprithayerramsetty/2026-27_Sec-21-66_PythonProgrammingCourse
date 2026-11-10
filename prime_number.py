n = int(input("Enter a number between 1 and 100: "))

if n < 1 or n > 100:
    print(f"{n} is not between 1 and 100")
elif n == 1:
    print(f"{n} is not a prime number")
elif n == 2 or n == 3 or n == 5 or n == 7:
    print(f"{n} is a prime number")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")
