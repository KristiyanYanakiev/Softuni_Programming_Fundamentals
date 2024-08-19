sequence_of_numbers = [int(element) for element in input().split()]

while True:
    command = input()

    if command == "Finish":
        break

    command_as_list = command.split()


    if "Add" in command_as_list:
        value = int(command_as_list[1])
        sequence_of_numbers.append(value)

    elif "Remove" in command_as_list:
        value = int(command_as_list[1])
        if value in sequence_of_numbers:
            sequence_of_numbers.remove(value)
        else:
            continue

    elif "Replace" in command_as_list:
        value = int(command_as_list[1])
        replacement_value = int(command_as_list[2])
        if value in sequence_of_numbers:
            replacement_index = sequence_of_numbers.index(value)
            sequence_of_numbers[replacement_index] = replacement_value
        else:
            continue

    elif "Collapse" in command_as_list:
        value = int(command_as_list[1])
        for num in sequence_of_numbers[::-1]:
            if num < value:
                sequence_of_numbers.remove(num)

sequence_of_numbers_as_string = [str(number) for number in sequence_of_numbers]
result = " ".join(sequence_of_numbers_as_string)

print(result)
