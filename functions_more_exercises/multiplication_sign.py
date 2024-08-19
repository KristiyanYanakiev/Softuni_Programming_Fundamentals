def multiplication_sign(num1, num2, num3):
    num_list = [num1, num2, num3]

    negative_counter = 0

    for element in num_list:
        if element < 0:
            negative_counter += 1

    if 0 in num_list:
        return "zero"
    elif negative_counter == 1 or negative_counter == 3:
        return "negative"
    elif negative_counter == 0 or negative_counter == 2:
        return "positive"



number_one = int(input())
number_two = int(input())
number_three = int(input())
print(multiplication_sign(number_one, number_two, number_three))
