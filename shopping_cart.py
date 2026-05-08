items = []
prices = []
choice = 0

print ("welcome to the sgopping cart program!")

while choice != 5:
    print ("\nPlease select one of the following(only numbers):")
    print ("1. add items")
    print ("2. view cart")
    print ("3. remove item")
    print ("4. compute total")
    print ("5. quit")

    choice = int(input("please enter an action: "))
    if choice == 1:
        item_name = input ("what item would you like to add? ")
        item_price = float(input(f"What is the price of '{item_name}'? "))
        items.append(item_name)
        prices.append(item_price)
        print(f"'{item_name}' has been added to the cart.")

    elif choice == 2:
        # Option 2: Display the contents of the cart
        print("The contents of the shopping cart are:")
        for i in range(len(items)):
            # We use i + 1 so the user sees a list starting from 1
            print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")

    elif choice == 3:
        # Option 3: Remove an item by its index
        index_to_remove = int(input("Which item would you like to remove(only numers) " \
        "? "))
        # Convert user-friendly index (1-based) to Python index (0-based)
        real_index = index_to_remove - 1
        
        if 0 <= real_index < len(items):
            removed_item = items.pop(real_index)
            prices.pop(real_index)
            print(f"'{removed_item}' has been removed.")
        else:
            print("Sorry, that is not a valid item number.")

    elif choice == 4:
        # Option 4: Calculate the sum of all prices
        total_sum = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total_sum:.2f}")

print("Thank you. Goodbye!")
