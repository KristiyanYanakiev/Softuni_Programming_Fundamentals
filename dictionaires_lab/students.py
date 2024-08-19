student_list = []
course_to_search = ""

while True:
    command = input().split(":")

    if len(command) == 1:
        break

    name, id, course = command

    student_list.append({"name": name, "id": id, "course": course})


course_to_search = command[0]

for current_dict in student_list:
    if course_to_search.startswith(current_dict["course"][0:3]):
        print(f"{current_dict['name']} - {int(current_dict['id'])}")




