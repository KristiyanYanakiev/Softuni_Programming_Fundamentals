number_of_messages = int(input())
output = ""

for current_message in range(number_of_messages):
    number = int(input())

    if number == 88:
        output = "Hello"
    elif number == 86:
        output = "How are you?"
    elif number != 88 and number != 86 and number < 88:
        output = "GREAT!"
    elif number > 88:
        output = "Bye."

    print(output)

