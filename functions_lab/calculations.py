def calculation(operation, num1, num2):
    if operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 // num2
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2


operation = input()
number1 = int(input())
number2 = int(input())

print(calculation(operation, number1, number2))



