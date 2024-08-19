def is_palindrome(num_as_string):

    if num_as_string == num_as_string[::-1]:
        return True
    return False


list_of_integers = input().split(", ")

for element in list_of_integers:
    print(is_palindrome(element))

