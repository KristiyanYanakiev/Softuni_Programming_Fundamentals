first_char_index = int(input())
second_char_index = int(input())

for current_char in range(first_char_index, second_char_index + 1):
    print(chr(current_char), end=" ")

