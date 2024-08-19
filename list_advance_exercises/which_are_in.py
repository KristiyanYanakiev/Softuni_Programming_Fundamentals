first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []

for current_element in first_sequence:
    for element in second_sequence:
        if current_element in element:
            substrings.append(current_element)
            break

print(substrings)
