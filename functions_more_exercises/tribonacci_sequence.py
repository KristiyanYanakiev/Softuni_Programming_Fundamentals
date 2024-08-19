# def tribunacci(signature, n):
#     while len(signature) < n:
#         signature.append(sum(signature[-3:]))
#     signature_as_string = [str(element) for element in signature]
#     return " ".join(signature_as_string)
# first_three_numbers = [1, 1, 2]
# number = int(input())
#
# print(tribunacci(first_three_numbers, number))

number = int(input())

def tribonacci_sequence(def_num):
    sequence = [1]
    for i in range(1, def_num):
        if len(sequence) < 3:
            sequence.append(i)
        else:
            sequence.append(sum(sequence[-3:]))
    return ' '.join([str(num) for num in sequence])

print(tribonacci_sequence(number))