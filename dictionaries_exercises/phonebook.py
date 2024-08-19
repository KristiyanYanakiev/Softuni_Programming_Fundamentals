phonebook = {}

while True:
    command = input()
    if command.isdigit():
        search_times = int(command)
        break

    name, phone_number = command.split("-")
    phonebook[name] = phone_number


for _ in range(search_times):
    name_to_search = input()

    if name_to_search in phonebook:
        print(f"{name_to_search} -> {phonebook[name_to_search]}")
    else:
        print(f"Contact {name_to_search} does not exist.")


