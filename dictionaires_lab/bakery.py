food_and_quantities = input().split()

bakery = {}

for current_index in range(0, len(food_and_quantities), 2):
    current_key = food_and_quantities[current_index]
    current_value = int(food_and_quantities[current_index + 1])
    bakery[current_key] = current_value

print(bakery)


