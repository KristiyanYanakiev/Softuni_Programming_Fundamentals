list_of_nums = [int(num) for num in input().split(", ")]

list_of_even_nums_indexes = []

for current_index in range(len(list_of_nums)):
    if list_of_nums[current_index] % 2 == 0:
        list_of_even_nums_indexes.append(current_index)


print(list_of_even_nums_indexes)

