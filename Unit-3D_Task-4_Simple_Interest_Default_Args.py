def simple_interest(p,r,t):
    simple=(p * r * t)/100
    return simple
p = float(input("Enter the amount of principal in rupees:"))
r = float(input("Enter the rate of interest:"))
t = float(input("Enter the duration of time:"))
result=simple_interest(p,r,t)
print(result)