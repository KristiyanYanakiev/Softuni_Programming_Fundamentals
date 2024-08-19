gifts = [element for element in input().split(" ")]

while True:
    command = input()

    if command == "No Money":
        break

    command_as_list = command.split(" ")
    action = command_as_list[0]
    item = command_as_list[1]

    if action == "OutOfStock":
        if item in gifts:
            searched_index = gifts.index(item)
            searched_value = gifts[searched_index]

            gifts = [element if element != searched_value else "None" for element in gifts]

    elif action == "Required":
        index = int(command_as_list[2])
        if 0 <= index < len(gifts):
            gifts[index] = item

    elif action == "JustInCase":
        gifts[-1] = item

result = [element for element in gifts if element != "None"]

final_output = " ".join(result)

print(final_output)



