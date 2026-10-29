n = int(input("Enter a number: "))

original_number = n
total_sum = 0

if n == 0:
    digit_count = 1
else:
    while n > 0:
        total_sum = total_sum + 1
        n = n // 10

print(f"Number of digits in {original_number} is {total_sum}")