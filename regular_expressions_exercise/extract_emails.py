import re

string = input()

pattern = r"\s(([a-z0-9]+[\-\.\_a-z0-9]*)@([a-z\-]+)(\.[a-z]+)+)\b"

# pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"

# matches = re.findall(pattern, string)
# for match in matches:
#     print(match[0])


matches = re.search(pattern, string)





