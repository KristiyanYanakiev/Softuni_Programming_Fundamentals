def merge(some_command_as_list, some_list_of_strings):
    start_index = int(some_command_as_list[1])
    end_index = int(some_command_as_list[2])
    concatenated_string = "".join(some_list_of_strings[start_index:end_index+1])
    some_list_of_strings = [i for i in some_list_of_strings if i not in concatenated_string]
    some_list_of_strings.insert(start_index, concatenated_string)

    return some_list_of_strings





list_of_strings = input().split()
#example: ['Ivo', 'Johny', 'Tony', 'Bony', 'Mony']

while True:
    command = input()
    if command == "3:1":
        break

    command_as_list = command.split()
    if "merge" in command_as_list:
        merge(command_as_list, list_of_strings)

    elif "divide" in command_as_list:
        divide(command_as_list, list_of_strings)
