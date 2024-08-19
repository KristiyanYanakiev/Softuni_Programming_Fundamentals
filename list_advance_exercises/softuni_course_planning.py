list_of_courses = input().split(", ")

def add(some_command, some_list_of_courses):
    lesson_title = some_command.split(":")[1]
    if lesson_title not in some_list_of_courses:
        some_list_of_courses.append(lesson_title)

    return some_list_of_courses

def insert(some_command, some_list_of_courses):
    lesson_title = some_command.split(":")[1]
    index = int(some_command.split(":")[2])
    if lesson_title not in some_list_of_courses:
        some_list_of_courses.insert(index, lesson_title)

    return some_list_of_courses


def remove(some_command, some_list_of_courses):
    lesson_title = some_command.split(":")[1]
    if lesson_title in some_list_of_courses:
        some_list_of_courses.remove(lesson_title)

    if f"{lesson_title}-Exercise" in some_list_of_courses:
        some_list_of_courses.remove(f"{lesson_title}-Exercise")

    return some_list_of_courses


def swap(some_command, some_list_of_courses):
    lesson_one = some_command.split(":")[1]

    lesson_two = some_command.split(":")[2]

    if lesson_one in some_list_of_courses and lesson_two in some_list_of_courses:
        index_one = some_list_of_courses.index(lesson_one)
        index_two = some_list_of_courses.index(lesson_two)
        some_list_of_courses[index_one], some_list_of_courses[index_two] = some_list_of_courses[index_two], some_list_of_courses[index_one]
        if f"{lesson_one}-Exercise" in some_list_of_courses and f"{lesson_two}-Exercise" in some_list_of_courses:
            index_exercise_one = some_list_of_courses.index(f"{lesson_one}-Exercise")
            index_exercise_two = some_list_of_courses.index(f"{lesson_two}-Exercise")
            some_list_of_courses[index_exercise_one], some_list_of_courses[index_exercise_two] = some_list_of_courses[index_exercise_two], some_list_of_courses[index_exercise_one]

        elif f"{lesson_one}-Exercise" in some_list_of_courses and f"{lesson_two}-Exercise" not in some_list_of_courses:
            insert_index = some_list_of_courses.index(lesson_one) + 1
            some_list_of_courses.remove(f"{lesson_one}-Exercise")
            some_list_of_courses.insert(insert_index, some_list_of_courses[lesson_one], f"{lesson_one}-Exercise")

        elif f"{lesson_one}-Exercise" not in some_list_of_courses and f"{lesson_two}-Exercise" in some_list_of_courses:
            insert_index = some_list_of_courses.index(lesson_two) + 1
            some_list_of_courses.remove(f"{lesson_two}-Exercise")
            some_list_of_courses.insert(insert_index, f"{lesson_two}-Exercise")

    return some_list_of_courses


def exercices(some_command, some_list_of_courses):
    lesson_title = some_command.split(":")[1]
    if lesson_title in some_list_of_courses and f"{lesson_title}-Exercise" not in some_list_of_courses:
        index = some_list_of_courses.index(lesson_title) + 1
        some_list_of_courses.insert(index, f"{lesson_title}-Exercise")
    if lesson_title not in some_list_of_courses:
        some_list_of_courses.append(lesson_title)
        some_list_of_courses.append(f"{lesson_title}-Exercise")

while True:
    command = input()

    if command == "course start":
        break

    if "Add" in command:
        add(command, list_of_courses)
    elif "Insert" in command:
        insert(command, list_of_courses)
    elif "Remove" in command:
        remove(command, list_of_courses)
    elif "Swap" in command:
        swap(command, list_of_courses)
    elif "Exercise" in command:
        exercices(command, list_of_courses)


index = 0
for current_index in range(len(list_of_courses)):
    index += 1
    print(f"{index}.{list_of_courses[current_index]}")

