max_number_of_stars = int(input())

for rows in range(1, max_number_of_stars + 1):
    print(rows * "*")

for columns in range(max_number_of_stars - 1, 0, -1):
    print(columns * "*")

