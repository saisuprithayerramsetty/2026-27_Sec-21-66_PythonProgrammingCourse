def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("GCD:", gcd(a,b))