number_of_lines = int(input())
word = input()
list = []

for string in range(number_of_lines):
    user_string = input()
    list.append(user_string)

filtered_list = []

for current_string in list:
    if word in current_string:
        filtered_list.append(current_string)

print(list)
print(filtered_list)
