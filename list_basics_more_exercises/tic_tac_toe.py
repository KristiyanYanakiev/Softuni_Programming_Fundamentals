first_line = [int(element) for element in input().split(" ")]
second_line = [int(s) for s in input().split(" ")]
third_line = [int(x) for x in input().split(" ")]

first = False
second = False

is_there_a_matching = False

#horizontal:
if first_line[0] == first_line[1] and first_line[1] == first_line[2]:
    is_there_a_matching = True
    if first_line[0] == 1:
        first = True
    elif first_line[0] == 2:
        second = True
elif second_line[0] == second_line[1] and second_line[1] == second_line[2]:
    is_there_a_matching = True
    if second_line[0] == 1:
        first = True
    elif second_line[0] == 2:
        second = True
elif third_line[0] == third_line[1] and third_line[1] == third_line[2]:
    is_there_a_matching = True
    if third_line[0] == 1:
        first = True
    elif third_line[0] == 2:
        second = True

#vertical:
elif first_line[0] == second_line[0] and second_line[0] == third_line[0]:
    is_there_a_matching = True
    if first_line[0] == 1:
        first = True
    elif first_line[0] == 2:
        second = True
elif first_line[1] == second_line[1] and second_line[1] == third_line[1]:
    is_there_a_matching = True
    if first_line[1] == 1:
        first = True
    elif first_line[1] == 2:
        second = True
elif first_line[2] == second_line[2] and second_line[2] == third_line[2]:
    is_there_a_matching = True
    if first_line[2] == 1:
        first = True
    elif first_line[2] == 2:
        second = True

#diagonal
elif first_line[0] == second_line[1] and second_line[1] == third_line[2]:
    is_there_a_matching = True
    if first_line[0] == 1:
        first = True
    elif first_line[0] == 2:
        second = True
elif first_line[2] == second_line[1] and second_line[1] == third_line[0]:
    is_there_a_matching = True
    if first_line[2] == 1:
        first = True
    elif first_line[2] == 2:
        second = True

if is_there_a_matching:
    if first:
        print("First player won")
    elif second:
        print("Second player won")
    else:
        print("Draw!")
else:
    print("Draw!")






