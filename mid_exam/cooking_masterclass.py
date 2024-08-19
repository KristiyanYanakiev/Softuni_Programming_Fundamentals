from math import ceil

budget = float(input())
number_of_students = int(input())

price_per_package_of_flour = float(input())
price_per_one_egg = float(input())
price_per_one_apron = float(input())

expenses_for_eggs = number_of_students * 10 * price_per_one_egg

number_of_packages_of_apron = ceil(number_of_students + number_of_students * 0.20)
expenses_for_apron = number_of_packages_of_apron * price_per_one_apron

expenses_for_flour = 0

for current_student in range(1, number_of_students + 1):
    if current_student % 5 == 0:
        continue
    expenses_for_flour += price_per_package_of_flour

total_expenses = expenses_for_apron + expenses_for_flour + expenses_for_eggs

if total_expenses <= budget:
    print(f"Items purchased for {total_expenses:.2f}$.")
else:
    print(f"{total_expenses - budget:.2f}$ more needed.")

