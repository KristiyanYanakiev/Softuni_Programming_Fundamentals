list_of_numbers = [int(num) for num in input().split(" ")]
amount_of_numbers_to_be_removed = int(input())


for _ in range(amount_of_numbers_to_be_removed):
    smallest_num = min(list_of_numbers)
    list_of_numbers.remove(smallest_num)

list_as_string = ""

for element in list_of_numbers:
    list_as_string += f"{element}, "

result = list_as_string[:-2]

print(result)












