while True:
    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    double_char_string = ""

    for current_char in command:
        double_char_string += current_char * 2

    print(double_char_string)

