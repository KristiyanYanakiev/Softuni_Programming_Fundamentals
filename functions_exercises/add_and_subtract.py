def sum_numbers(num1, num2):
    return num1 + num2

def subtract(sum, num3):
    return sum - num3

def add_and_subtract(first_number, second_number, third_number):
    sum_of_first_and_second_number = sum_numbers(first_number, second_number)
    result = subtract(sum_of_first_and_second_number, third_number)
    print(result)

number1 = int(input())
number2 = int(input())
number3 = int(input())

add_and_subtract(number1, number2, number3)



