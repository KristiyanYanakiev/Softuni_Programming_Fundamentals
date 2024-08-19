countries = input().split(", ")
capitals = input().split(", ")

# dict = {}

# for current_index in range(len(countries)):
#     dict[countries[current_index]] = capitals[current_index]

# dict = dict(zip(countries, capitals))

dict = {countries[current_index]:capitals[current_index] for current_index in range(len(capitals))}

for key, value in dict.items():
    print(f"{key} -> {value}")
