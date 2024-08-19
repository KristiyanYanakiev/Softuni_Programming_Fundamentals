sequence_of_integers = [int(i) for i in input().split()]
summed_value_of_removed_elements = 0
def decrease_and_increase(some_value, some_list_of_integers):
    result = []
    for element in some_list_of_integers:
        if element <= some_value:
            element += some_value
            result.append(element)
        elif element > some_value:
            element -= some_value
            result.append(element)

    return result


while sequence_of_integers:
    index = int(input())
    if index < 0:
        searched_value = sequence_of_integers[0]
        summed_value_of_removed_elements += searched_value
        sequence_of_integers.pop(0)
        sequence_of_integers.insert(0, sequence_of_integers[-1])
        sequence_of_integers = decrease_and_increase(searched_value, sequence_of_integers)

    elif index > len(sequence_of_integers) - 1:
        searched_value = sequence_of_integers[-1]
        summed_value_of_removed_elements += searched_value
        sequence_of_integers.pop(-1)
        sequence_of_integers.append(sequence_of_integers[0])
        sequence_of_integers = decrease_and_increase(searched_value, sequence_of_integers)

    else:
        value = sequence_of_integers[index]
        summed_value_of_removed_elements += value
        sequence_of_integers.pop(index)
        sequence_of_integers = decrease_and_increase(value, sequence_of_integers)

print(summed_value_of_removed_elements)

