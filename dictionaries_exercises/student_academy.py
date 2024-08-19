pair_of_rows = int(input())
grades = {}


for current_row in range(pair_of_rows):
    student_name = input()
    grade = float(input())
    if student_name not in grades.keys():
        grades[student_name] = grade
    else:
        grades[student_name] += grade
        average_grade = grades[student_name] / 2
        grades[student_name] = average_grade


for key, value in grades.items():
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")
