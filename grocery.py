import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row
    return dictionary

def main():
    STORE_NAME = "THE GALAXY GROCERY"
    TAX_RATE = 0.06
    
    try:
        products_dict = read_dictionary("products.csv", 0)

        print(f"{STORE_NAME}")
        print("-" * 30)

        total_items = 0
        subtotal = 0.0
        top_item_name = ""
        max_item_cost = 0.0

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                product_info = products_dict[product_id]
                name = product_info[1]
                price = float(product_info[2])
                
                if product_id == "D083" and quantity >= 2:
                    half_off_units = quantity // 2
                    full_price_units = quantity - half_off_units
                    item_total = (full_price_units * price) + (half_off_units * (price * 0.5))
                    print(f"{name}: {quantity} @ {price:.2f} (Promo: BOGO 50% applied)")
                else:
                    item_total = quantity * price
                    print(f"{name}: {quantity} @ {price:.2f}")

                if item_total > max_item_cost:
                    max_item_cost = item_total
                    top_item_name = name

                total_items += quantity
                subtotal += item_total

        sales_tax = subtotal * TAX_RATE
        total_due = subtotal + sales_tax

        print("-" * 30)
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_due:.2f}")
        
        print(f"\nThank you for shopping at {STORE_NAME}!")

        now = datetime.now()
        print(f"{now.strftime('%a %b %d %H:%M:%S %Y')}")

        print("\n" + "="*35)
        return_date = now + timedelta(days=30)
        print(f"Return by: {return_date.strftime('%b %d, %Y')} 9:00 PM")
        
        if top_item_name:
            print(f"COUPON: 15% OFF your next {top_item_name}!")
        print("="*35)

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except PermissionError as e:
        print(f"Error: permission denied\n{e}")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file\n{e}")

if __name__ == "__main__":
    main()