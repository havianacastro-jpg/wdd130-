# Author: Hagot Coriantumr Viana Castro

EARTH_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    return (WATER_DENSITY * EARTH_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    return (-friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity**2)) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return (-0.04 * WATER_DENSITY * (fluid_velocity**2) * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds, smaller_diameter):
    k = 0.1 + (50 / reynolds) * (((larger_diameter / smaller_diameter)**4) - 1)
    return (-k * WATER_DENSITY * (fluid_velocity**2)) / 2000

def kpa_to_psi(kpa):
    return kpa * 0.1450377

def main():
    print(f"--- Water Supply Design ---")
    print(f"Designer: Hagot Coriantumr Viana Castro\n")
    
    t = float(input("Water tower height (meters): "))
    w = float(input("Water tank wall height (meters): "))
    L_supply = float(input("Length of supply pipe (meters): "))
    n_elbows = int(input("Number of 90° elbows: "))
    L_house = float(input("Length of pipe to the house (meters): "))

    v, f = 1.65, 0.013
    d_large, d_small = 0.28687, 0.048692

   
    h = water_column_height(t, w)
    pressure = pressure_gain_from_water_height(h)


    pressure += pressure_loss_from_pipe(d_large, L_supply, f, v)
    pressure += pressure_loss_from_fittings(v, n_elbows)
    
    reynolds = reynolds_number(d_large, v)
    pressure += pressure_loss_from_pipe_reduction(d_large, v, reynolds, d_small)
    
    pressure += pressure_loss_from_pipe(d_small, L_house, f, v)


    print(f"\nPressure at the house: {pressure:.1f} kilopascals")
    print(f"Pressure at the house: {kpa_to_psi(pressure):.2f} psi")

if __name__ == "__main__":
    main()