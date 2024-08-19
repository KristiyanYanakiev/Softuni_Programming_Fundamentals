import math
import sys

factor = int(input())
count = int(input())

multiples_list = []

while True:
    for number in range(factor, sys.maxsize):
        if number % factor == 0:
            multiples_list.append(number)

            if len(multiples_list) == count:
                print(multiples_list)
                exit()



