total_input_numbers = int(input("Enter how many numbers: "))
total_sum = 0
for i in range(total_input_numbers):
    number = int(input("Enter a number: "))
    total_sum = total_sum + number
total_average = total_sum / total_input_numbers if total_input_numbers > 0 else 0
print(f"Sum: {total_sum}")
print(f"Average: {total_average}")