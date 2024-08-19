list_of_numbers_for_the_beggars = [int(element) for element in input().split(", ")]
count_of_beggars = int(input())
sums = []

for current_index in range(count_of_beggars):
    current_beggar_sum = 0
    for index in range(current_index, len(list_of_numbers_for_the_beggars), count_of_beggars):
        current_beggar_sum += list_of_numbers_for_the_beggars[index]

    sums.append(current_beggar_sum)

print(sums)












