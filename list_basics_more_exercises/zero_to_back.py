list_of_numbers = [int(element) for element in input().split(", ")]

list_of_numbers_without_zero = [num for num in list_of_numbers if num != 0]
list_of_zeros = [number for number in list_of_numbers if not number in list_of_numbers_without_zero]

final_list = list_of_numbers_without_zero + list_of_zeros

print(final_list)

