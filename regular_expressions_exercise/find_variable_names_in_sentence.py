import re

string = input()
pattern = r"\b_([A-Za-z0-9]+\b)"

valid_names = re.findall(pattern, string)

print(valid_names)


