n = int(input())

for current_number in range(1, n + 1):

    sum_of_digits = 0
    for digit in str(current_number):
        sum_of_digits += int(digit)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True
    else:
        is_special = False

    print(f"{current_number} -> {is_special}")
