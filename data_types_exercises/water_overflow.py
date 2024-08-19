water_tank_capacity_in_litters = 255

number_of_lines = int(input())

total_of_filled_water = 0

for current_pour in range(number_of_lines):
    current_water_amount = int(input())
    if total_of_filled_water + current_water_amount > water_tank_capacity_in_litters:
        print("Insufficient capacity!")
        continue
    total_of_filled_water += current_water_amount

print(total_of_filled_water)




