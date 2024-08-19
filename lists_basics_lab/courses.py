number_of_lines = int(input())
course_list = []

for current_course in range(number_of_lines):
    course_name = input()
    course_list.append(course_name)

print(course_list)
