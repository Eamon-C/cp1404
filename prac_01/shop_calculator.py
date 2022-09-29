"""
shop_calculator.py
CP1404
Calculates total cost of n number of items and applies discount at threshold (>$100)
"""

number_of_items = int(input("Number of items: "))
item_count = 0
total_cost = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
while item_count != number_of_items:
    total_cost += float(input("Price of item: "))
    item_count += 1
if total_cost > 100:
    total_cost *= 0.9
print(f"Total price for {number_of_items} item/s is ${total_cost:.2f}")
