n = int(input("Enter the number: "))

def prime_check(n, i):
    if n < 2:
        return False
    elif i * i > n:
        return True
    elif n % i == 0:
        return False
    else:
        return prime_check(n, i + 1)

if prime_check(n, 2):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")