courses = {}

while True:
    command = input()

    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses.keys():
        courses[course_name] = [student_name]

    if student_name not in courses[course_name]:
        courses[course_name].append(student_name)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for current_value in value:
        print(f"-- {current_value}")

