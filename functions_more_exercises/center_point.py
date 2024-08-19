import math
from math import floor


def find_the_point_closest_to_the_center(some_x1, some_y1, some_x2, some_y2):
    point_one = abs(some_x1) + abs(some_y1)
    point_two = abs(some_x2) + abs(some_y2)

    if point_one <= point_two:
        return f"{floor(some_x1), floor(some_y1)}"
    else:
        return f"{floor(some_x2), floor(some_y2)}"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(find_the_point_closest_to_the_center(x1, y1, x2, y2))

