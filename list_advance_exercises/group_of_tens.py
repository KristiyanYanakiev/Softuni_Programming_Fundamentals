sequence_of_numbers_as_string = input().split(", ")
sequence_of_numbers_as_int = [int(i) for i in sequence_of_numbers_as_string]

current_group = 10
list_of_numbers = []

while sequence_of_numbers_as_int:
    list_of_numbers = [num for num in sequence_of_numbers_as_int if num <= current_group]
    sequence_of_numbers_as_int = [x for x in sequence_of_numbers_as_int if x not in list_of_numbers]
    print(f"Group of {current_group}'s: {list_of_numbers}")
    current_group += 10

