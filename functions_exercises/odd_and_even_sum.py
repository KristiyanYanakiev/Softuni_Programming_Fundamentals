def sum_of_even_and_digit(num):
    num_as_string = str(num)

    even_digits = [int(element) for element in num_as_string if int(element) % 2 == 0]
    odd_digits = [int(element) for element in num_as_string if int(element) % 2 != 0]

    sum_of_even = sum(even_digits)
    sum_of_odd = sum(odd_digits)

    return f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}"


number = int(input())
print(sum_of_even_and_digit(number))



