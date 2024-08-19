list_of_cells = input().split("#")
total_water = int(input())
valid_range = 0

total_effort_counter = 0
total_fire = 0

list_of_put_out_cells = []

for cell in list_of_cells:
    cell_as_list = cell.split(" = ")

    type_of_fire = cell_as_list[0]
    cell_value = int(cell_as_list[1])

    if type_of_fire == "High":
        valid_range = range(81, 126)
    elif type_of_fire == "Medium":
        valid_range = range(51, 81)
    elif type_of_fire == "Low":
        valid_range = range(1, 51)

    if cell_value in valid_range:
        if total_water >= cell_value:
            total_water -= cell_value
            total_effort_counter += 0.25 * cell_value
            total_fire += cell_value
            list_of_put_out_cells.append(cell_value)

    if total_water == 0:
        break

# below commented solution is giving me 90 points in Judge

output = ""
for (element) in list_of_put_out_cells:
    output += f" - {element}\n"

if output != "":
    print("Cells:")
    print(output[:-1])
print(f"Effort: {total_effort_counter:.2f}")
print(f"Total Fire: {total_fire}")

# however this one is giving me 100/100. Only difference is the for loop

# print("Cells:")
# for element in list_of_put_out_cells:
#     print(f" - {element}")
# print(f"Effort: {total_effort_counter:.2f}")
# print(f"Total Fire: {total_fire}")
