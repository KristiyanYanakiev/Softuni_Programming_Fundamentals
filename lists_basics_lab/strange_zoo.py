list = []

for current_string in range(3):
    string = input()
    list.append(string)

list[0], list[1], list[2] = list[2], list[1], list[0]

print(list)

