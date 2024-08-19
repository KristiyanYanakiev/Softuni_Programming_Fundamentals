number_of_lines = int(input())
list_of_nums = []
even_list = []
odd_list = []
negative_list = []
positive_list = []

for num in range(number_of_lines):

        number = int(input())
        list_of_nums.append(number)

for element in list_of_nums:
    if element >= 0:
        positive_list.append(element)
    else:
        negative_list.append(element)

    if element % 2 == 0:
        even_list.append(element)
    else:
        odd_list.append(element)

command = input()

if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
elif command == "positive":
    print(positive_list)



