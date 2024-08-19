import re

string = input()
while string:
    matches = re.findall(r"\d+", string)
    if matches:
        print(" ".join(matches), end=" ")

    string = input()
