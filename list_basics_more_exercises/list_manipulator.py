def exchange_index(list_of_nums, some_command_as_list):
    index = int(some_command_as_list[1])
    if index > len(list_of_nums) - 1 or index < 0:
        print("Invalid index")
    else:
        list_of_nums = list_of_nums[index+1:] + list_of_nums[:index+1]
        return list_of_nums


def max_even(list_of_nums, some_command_as_list):
    even_nums_list = [i for i in list_of_nums if i % 2 == 0]
    if len(even_nums_list) == 0:
        print("No matches")
    else:
        max_even_num = max(even_nums_list)
        if even_nums_list.count(max_even_num) >= 2:
            for element in list_of_nums[::-1]:
                if element == max_even_num:
                    print(list_of_nums.index(element))
                    break
        else:
            print(list_of_nums.index(max_even_num))


def max_odd(list_of_nums, some_command_as_list):
    odd_nums_list = [i for i in list_of_nums if i % 2 != 0]
    if len(odd_nums_list) == 0:
        print("No matches")
    else:
        max_odd_num = max(odd_nums_list)
        if odd_nums_list.count(max_odd_num) >= 2:
            for element in list_of_nums[::-1]:
                if element == max_odd_num:
                    print(list_of_nums.index(element))
                    break
        else:
            print(list_of_nums.index(max_odd_num))


def min_even(list_of_nums, some_command_as_list):
    even_nums_list = [i for i in list_of_nums if i % 2 == 0]
    if len(even_nums_list) == 0:
        print("No matches")
    else:
        min_even_num = min(even_nums_list)
        if even_nums_list.count(min_even_num) >= 2:
            for element in list_of_nums[::-1]:
                if element == min_even_num:
                    print(list_of_nums.index(element))
                    break
        else:
            print(list_of_nums.index(min_even_num))


def min_odd(list_of_nums, some_command_as_list):
    odd_nums_list = [i for i in list_of_nums if i % 2 != 0]
    if len(odd_nums_list) == 0:
        print("No matches")
    else:
        min_odd_num = min(odd_nums_list)
        if odd_nums_list.count(min_odd_num) >= 2:
            for element in list_of_nums[::-1]:
                if element == min_odd_num:
                    print(list_of_nums.index(element))
                    break
        else:
            print(list_of_nums.index(min_odd_num))

def first_count_even(list_of_nums, some_command_as_list):
    count = int(some_command_as_list[1])
    if count > len(list_of_nums):
        print("Invalid count")
    else:
        even_nums = []
        for element in list_of_nums:
            if element % 2 == 0:
                even_nums.append(element)
            if len(even_nums) == count:
                print(even_nums)
                break
            else:
                print(even_nums)

def first_count_odd(list_of_nums, some_command_as_list):
    count = int(some_command_as_list[1])
    if count > len(list_of_nums):
        print("Invalid count")
    else:
        odd_nums = []
        for element in list_of_nums:
            if element % 2 != 0:
                odd_nums.append(element)
            if len(odd_nums) == count:
                print(odd_nums)
                break
            else:
                print(odd_nums)


def last_count_even(list_of_nums, some_command_as_list):
    count = int(some_command_as_list[1])
    if count > len(list_of_nums):
        print("Invalid count")
    else:
        even_nums = []
        for element in list_of_nums[::-1]:
            if element % 2 == 0:
                even_nums.append(element)
            if len(even_nums) == count:
                print(even_nums)
                break
            else:
                print(even_nums)

def last_count_odd(list_of_nums, some_command_as_list):
    count = int(some_command_as_list[1])
    if count > len(list_of_nums):
        print("Invalid count")
    else:
        odd_nums = []
        for element in list_of_nums[::-1]:
            if element % 2 != 0:
                odd_nums.append(element)
            if len(odd_nums) == count:
                print(odd_nums)
                break
            else:
                print(odd_nums)



list_of_numbers = [int(num) for num in input().split()]

while True:
    command = input()

    if command == "end":
        break

    command_as_list = command.split()

    if command_as_list[0] == "exchange":
        exchange_index(list_of_numbers, command_as_list)
        list_of_numbers = exchange_index(list_of_numbers, command_as_list)
    elif command_as_list[0] == "max" and command_as_list[1] == "even":
        max_even(list_of_numbers, command_as_list)
    elif command_as_list[0] == "max" and command_as_list[1] == "odd":
        max_odd(list_of_numbers, command_as_list)
    elif command_as_list[0] == "min" and command_as_list[1] == "even":
        min_even(list_of_numbers, command_as_list)
    elif command_as_list[0] == "min" and command_as_list[1] == "odd":
        min_odd(list_of_numbers, command_as_list)
    elif command_as_list[0] == "first" and command_as_list[2] == "even":
        first_count_even(list_of_numbers, command_as_list)
    elif command_as_list[0] == "first" and command_as_list[2] == "odd":
        first_count_odd(list_of_numbers, command_as_list)
    elif command_as_list[0] == "last" and command_as_list[2] == "even":
        last_count_even(list_of_numbers, command_as_list)
    elif command_as_list[0] == "last" and command_as_list[2] == "odd":
        last_count_odd(list_of_numbers, command_as_list)

print(list_of_numbers)


