list_of_nums = input().split()

list_of_rounded_nums = [round(float(num)) for num in list_of_nums]

print(list_of_rounded_nums)