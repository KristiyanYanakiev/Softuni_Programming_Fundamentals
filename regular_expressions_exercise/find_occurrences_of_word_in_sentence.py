import re

string = input()
word = input()

pattern = rf"\b{word}\b"

matches = re.findall(pattern, string, re.IGNORECASE)

print(len(matches))
