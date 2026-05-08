from datetime import datetime
subtotal = 0
print("Enter the price and quantity for each item (Enter 0 quantity to finish):")
while True:
    price = float(input("Enter price: "))
    if price == 0:
        break
    quantity = float(input("Enter quantity: "))
    if quantity == 0:
        break
    subtotal += price * quantity
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
discount_amount = 0
if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        discount_amount = round(subtotal * 0.10, 2)
        subtotal -= discount_amount
        print(f"Discount amount: {discount_amount:.2f}")
    else:
        difference = 50 - subtotal
        print(f"To receive the discount, add {difference:.2f} more to your order.")
sales_tax = round(subtotal * 0.06, 2)
total = subtotal + sales_tax
print(f"Sales tax amount: {sales_tax:.2f}")
print(f"Total: {total:.2f}")