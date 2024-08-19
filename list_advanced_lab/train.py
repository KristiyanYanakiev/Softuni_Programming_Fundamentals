def add(some_train: list, some_number_of_people: int):
    some_train[-1] += some_number_of_people
    return some_train

def insert(some_train: list, some_index:int, some_number_of_people:int):
    some_train[some_index] += some_number_of_people
    return some_train

def leave(some_train: list, some_index:int, some_number_of_people:int):
    some_train[some_index] -= some_number_of_people
    return some_train


train = [0] * int(input())

while True:
    command = input()
    if command == "End":
        print(train)
        break

    command_as_list = command.split()

    if "add" in command_as_list:
        number_of_people = int(command_as_list[1])
        add(train, number_of_people)

    elif "insert" in command_as_list:
        index = int(command_as_list[1])
        number_of_people = int(command_as_list[2])
        insert(train, index, number_of_people)

    elif "leave" in command_as_list:
        index = int(command_as_list[1])
        number_of_people = int(command_as_list[2])
        leave(train, index, number_of_people)


