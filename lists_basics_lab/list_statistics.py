number_of_lines = int(input())

list_positives = []
list_negatives = []

for current_number in range(number_of_lines):
    num = int(input())

    if num >= 0:
        list_positives.append(num)
    else:
        list_negatives.append(num)

print(list_positives)
print(list_negatives)
print(f"Count of positives: {len(list_positives)}\nSum of negatives: {sum(list_negatives)}")
