g_max = ["", "", -1.0]
g_min = ["", "", 999.0]
y_stats = [0, 0, -1.0, 999.0] 
c_stats = [0, 0, -1.0, 999.0] 
user_year = input("Enter the year of interest: ")
user_country = input("Enter the country of interest: ")

with open("life-expectancy.csv") as f:
    next(f)
    for line in f:
        parts = line.strip().split(",")
        name, year, val = parts[0], parts[2], float(parts[3])
        if val > g_max[2]: g_max = [name, year, val]
        if val < g_min[2]: g_min = [name, year, val]
        if year == user_year:
            y_stats[0] += val
            y_stats[1] += 1
            if val > y_stats[2]: y_stats[2] = val
            if val < y_stats[3]: y_stats[3] = val
        if name.lower() == user_country.lower():
            c_stats[0] += val
            c_stats[1] += 1
            if val > c_stats[2]: c_stats[2] = val
            if val < c_stats[3]: c_stats[3] = val
print(f"\nOverall max: {g_max[2]} from {g_max[0]} in {g_max[1]}")
print(f"Overall min: {g_min[2]} from {g_min[0]} in {g_min[1]}")

if y_stats[1] > 0:
    print(f"\nFor the year {user_year}:")
    print(f"Average: {y_stats[0] / y_stats[1]:.2f}")
    print(f"Max: {y_stats[2]}\nMin: {y_stats[3]}")
if c_stats[1] > 0:
    print(f"\nFor the country {user_country.capitalize()}:")
    print(f"Average: {c_stats[0] / c_stats[1]:.2f}")
    print(f"Max: {c_stats[2]}\nMin: {c_stats[3]}")