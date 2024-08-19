from math import ceil

number_of_people = int(input())
capacity = int(input())

number_of_courses_needed = ceil(number_of_people / capacity)

print(number_of_courses_needed)

# number_of_people = int(input())
# capacity = int(input())
# number_of_courses = 0
#
# while number_of_people > 0:
#     number_of_people -= capacity
#     number_of_courses += 1
#
# print(number_of_courses)
