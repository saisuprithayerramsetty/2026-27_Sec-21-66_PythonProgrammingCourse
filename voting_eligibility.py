#to check eligibility for voting age
age = int(input("Enter the age: "))

if age >= 18:
    print(f"Eligilible for voting (Age = {age})")
else:
    print(f"Not eligible for voting (Age = {age})")