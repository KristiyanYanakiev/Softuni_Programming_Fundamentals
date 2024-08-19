to_do_list = [0] * 10

command = input()

while command != "End":
    importance, task = command.split("-")
    importance = int(importance)
    index = importance - 1
    to_do_list.pop(index)
    to_do_list.insert(index, task)
    command = input()

result = [task for task in to_do_list if task != 0]
print(result)
















