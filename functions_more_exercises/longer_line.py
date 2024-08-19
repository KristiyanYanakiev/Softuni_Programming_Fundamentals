from math import floor

def find_line_length_of_two_points(some_x1, some_y1, some_x2, some_y2):
    point_one = abs(some_x1) + abs(some_y1)
    point_two = abs(some_x2) + abs(some_y2)
    line_length = point_one + point_two
    return line_length

def print_the_longest_line(a, b, c, d):
    if abs(a) + abs(b) <= abs(c) + abs(d):
        result = f"{floor(a), floor(b)}{floor(c), floor(d)}"
    else:
        result = f"{floor(c), floor(d)}{floor(a), floor(b)}"

    return result




x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())


line_one_length = find_line_length_of_two_points(x1, y1, x2, y2)
line_two_length = find_line_length_of_two_points(a1, b1, a2, b2)

if line_one_length >= line_two_length:
    print(print_the_longest_line(x1, y1, x2, y2))
else:
    print(print_the_longest_line(a1, b1, a2, b2))












