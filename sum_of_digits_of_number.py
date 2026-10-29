n = int(input("Enter the number: "))
original_number = n
total_sum = 0
while n > 0:
    digit = n%10
    total_sum = total_sum + digit
    n = n//10
print(f"the sum of digits in the number {original_number} is {total_sum}")