coffee_counter = 0
number_of_coffees_per_event = 0

while True:
    command = input()
    is_valid = False

    if command == "END":
        break

    if command == "coding" or command == "CODING":
        is_valid = True
    if command == "dog" or command == "DOG":
        is_valid = True
    if command == "cat" or command == "CAT":
        is_valid = True
    if command == "movie" or command == "MOVIE":
        is_valid = True

    if not is_valid:
        continue
    else:
        if command.isupper():
            number_of_coffees_per_event = 2
        else:
            number_of_coffees_per_event = 1

    coffee_counter += number_of_coffees_per_event

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)


