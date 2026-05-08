import math
from datetime import datetime
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
numerator = math.pi * (width**2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)
denominator = 10_000_000_000
volume = numerator / denominator
print(f"The approximate volume is {volume:.2f} liters.")
wants_to_buy = input("Do you want to buy tires with these dimensions? (yes/no): ").lower()
phone_number = ""

if wants_to_buy == "yes":
    phone_number = input("Please enter your phone number: ")
    print("Thank you. A representative will contact you shortly.")
current_date = datetime.now()
with open("volumes.txt", "at") as volumes_file:
    if phone_number:
        print(f"{current_date:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}, {phone_number}", 
              file=volumes_file)
    else:
        print(f"{current_date:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}", 
              file=volumes_file)