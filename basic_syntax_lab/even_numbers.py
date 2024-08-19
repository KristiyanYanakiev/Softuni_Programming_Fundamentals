number_of_lines = int(input())

for current_number in range(number_of_lines):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        exit()

print("All numbers are even.")
