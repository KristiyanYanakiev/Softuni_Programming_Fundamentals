import sys

number_of_electrons = int(input())
list_of_shells = []

while True:
    for current_shelf in range(1, sys.maxsize + 1):
        max_num_of_electrons_for_current_shell = 2 * current_shelf ** 2

        if number_of_electrons >= max_num_of_electrons_for_current_shell:
            list_of_shells.append(max_num_of_electrons_for_current_shell)
            number_of_electrons -= max_num_of_electrons_for_current_shell
        else:
            list_of_shells.append(number_of_electrons)
            number_of_electrons -= number_of_electrons

        if number_of_electrons == 0:
            break
    break

print(list_of_shells)


