# Task 7: Retail Billing
rates = {"grocery": 0.05, "stationery": 0.12}
items = []
subtotal = 0

for _ in range(int(input("Number of products: "))):
    name = input("Product: ")
    category = input("Category (grocery/stationery): ").lower()
    price = float(input("Unit price: "))
    quantity = int(input("Quantity: "))
    amount = price * quantity
    items.append((name, category, amount))
    subtotal += amount

discount = min(subtotal * 0.10, 200) if subtotal >= 1000 else 0
tax = sum((amount - discount * amount / subtotal) * rates[category]
          for name, category, amount in items) if subtotal else 0

print("\nINVOICE")
for name, category, amount in items:
    print(name, "-", round(amount, 2))
print("Subtotal:", round(subtotal, 2))
print("Discount:", round(discount, 2))
print("Tax:", round(tax, 2))
print("Total:", round(subtotal - discount + tax, 2))
