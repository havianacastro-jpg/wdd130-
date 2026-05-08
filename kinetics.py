import math

def main():
    
    print("--- Physics Kinetics Calculator ---")
    print("1. Calculate Kinetic Energy")
    print("2. Calculate Potential Energy")
    
    try:
        choice = input("Select an option (1 or 2): ")
        mass = float(input("Enter mass in kilograms (kg): "))
        
        if choice == "1":
            velocity = float(input("Enter velocity in meters per second (m/s): "))
            energy = calculate_kinetic_energy(mass, velocity)
            print(f"\nResult: The Kinetic Energy is {energy:,.2f} Joules.")
            
        elif choice == "2":
            height = float(input("Enter height in meters (m): "))
            energy = calculate_potential_energy(mass, height)
            print(f"\nResult: The Potential Energy is {energy:,.2f} Joules.")
        else:
            print("Invalid selection.")
            
    except ValueError as e:
        print(f"Input Error: {e}. Please enter valid numbers.")

def calculate_kinetic_energy(mass, velocity):
    
    if mass < 0:
        raise ValueError("Mass cannot be negative")
    return 0.5 * mass * (velocity ** 2)

def calculate_potential_energy(mass, height, gravity=9.80665):
    
    if mass < 0 or height < 0:
        raise ValueError("Mass and height must be non-negative")
    return mass * gravity * height

if __name__ == "__main__":
    main() 