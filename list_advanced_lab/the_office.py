employees_happiness = [int(element) for element in input().split()]
happiness_improvement_factor = int(input())

multiplied_employees_happiness = [num * happiness_improvement_factor for num in employees_happiness]

average_happiness = sum(multiplied_employees_happiness) / len(multiplied_employees_happiness)

employees_with_greater_or_equal_to_the_average_happinnes = [i for i in multiplied_employees_happiness if i >= average_happiness]

if len(employees_with_greater_or_equal_to_the_average_happinnes) >= len(multiplied_employees_happiness) / 2:
    print(f"Score: {len(employees_with_greater_or_equal_to_the_average_happinnes)}/{len(multiplied_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(employees_with_greater_or_equal_to_the_average_happinnes)}/{len(multiplied_employees_happiness)}. Employees are not happy!")

