n = int(input())

dict_of_plants = {}

for _ in range(n):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = int(plant_info[1])

    if plant not in dict_of_plants.keys():
        dict_of_plants[plant] = {"rarity": 0, "rating": 0.00}
    dict_of_plants[plant]["rarity"] = rarity



while True:
    command = input()

    if command == "Exhibition":
        break

    command_as_list = command.split(":")
    action = command_as_list[0]

    if action == "Rate":
        second_part = command_as_list[1].split(" - ")
        current_plant = second_part[0][1::]

        rating = int(second_part[1])

        if current_plant in dict_of_plants.keys():
            if dict_of_plants[current_plant]["rating"] == 0:
                dict_of_plants[current_plant]["rating"] = rating
            else:
                average_rating = (dict_of_plants[current_plant]["rating"] + rating) / 2
                dict_of_plants[current_plant]["rating"] = average_rating
        else:
            print("error")


    elif action == "Update":
        second_part = command_as_list[1].split(" - ")
        current_plant = second_part[0][1::]

        if current_plant in dict_of_plants.keys():

            new_rarity = int(second_part[1])
            dict_of_plants[current_plant]["rarity"] = new_rarity
        else:
            print("error")


    elif action == "Reset":
        second_part = command_as_list[1].split(" - ")
        current_plant = second_part[0][1::]

        if current_plant in dict_of_plants.keys():

            dict_of_plants[current_plant]["rating"] = 0.00

        else:
            print("error")



print(f"Plants for the exhibition:")
for key, value in dict_of_plants.items():
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['rating']:.2f}")








