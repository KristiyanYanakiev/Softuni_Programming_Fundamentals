string = input()

occurrences = {}

for char in string:
    if char != " ":
        if char not in occurrences.keys():
            occurrences[char] = 0
        occurrences[char] += 1

for character, occurrence in occurrences.items():
    print(f"{character} -> {occurrence}")

