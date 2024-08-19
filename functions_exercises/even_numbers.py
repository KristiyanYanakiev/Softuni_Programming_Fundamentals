def is_even(num):
    if num % 2 == 0:
        return True
    return False


list_of_numbers = [int(element) for element in input().split()]

list_of_even = list(filter(is_even, list_of_numbers))

print(list_of_even)