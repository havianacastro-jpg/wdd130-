#ask for all user data
child_meal = float (input ("what is the price of a childs meal?: "))
adult_meal = float (input ("what is the price of an adults?: "))
children_count = int (input ("how many are children there?: "))
adults_count = int (input ("how many adults are there? "))

#calculate the subtotal
subtotal= (child_meal * children_count) + (adult_meal * adults_count)

#price
print (f"your subtotal is: $ {subtotal}")

#tax
taxe_rate = float (input ("what is the sales tax rate?: "))
# formula: subtotal * tax / 100
sales_tax = (subtotal * taxe_rate ) / 100
total= subtotal + sales_tax 
print (f"sales tax : $ {sales_tax:.2f}")
print (f"your total is: $ {total: .2f}") 

#money
amount = float (input("what is the payment amount?"))
change =amount - total
print (f"your change is: ${change: .2f}")
