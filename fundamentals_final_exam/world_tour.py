string_with_stops = input()

def add_stop(some_string_with_stops, some_index, some_string_to_be_inserted):
    result = some_string_with_stops[0:index] + some_string_to_be_inserted + string_with_stops[index::]
    return result

def remove(some_string_with_stops, some_start_index, some_end_index):
    result = some_string_with_stops[0:some_start_index] + string_with_stops[some_end_index + 1::]
    return result

def switch(some_string_with_stops, some_old_string, some_new_string):
    result = some_string_with_stops = some_string_with_stops.replace(some_old_string, some_new_string)
    return result

while True:
    command = input()

    if command == "Travel":
        break

    if "::" in command:
        command_as_list = command.split("::")
    else:
        command_as_list = command.split(":")
        action = command_as_list[0]

        if action == "Add Stop":
            index = int(command_as_list[1])
            if index < len(string_with_stops):
                string_to_be_inserted = command_as_list[2]
                string_with_stops = add_stop(string_with_stops, index, string_to_be_inserted)
            print(string_with_stops)

        elif action == "Remove Stop":
            start_index = int(command_as_list[1])
            end_index = int(command_as_list[2])
            if start_index < len(string_with_stops) and end_index < len(string_with_stops):
                string_with_stops = remove(string_with_stops, start_index, end_index)
            print(string_with_stops)

        elif action == "Switch":
            old_string = command_as_list[1]
            new_string = command_as_list[2]
            if old_string in string_with_stops:
                string_with_stops = switch(string_with_stops, old_string, new_string)
            print(string_with_stops)

print(f"Ready for world tour! Planned stops: {string_with_stops}")


