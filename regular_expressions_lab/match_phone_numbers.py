import re

phone_numbers = input()

pattern = r"\+359([\s\-])2\1\d{3}\1\d{4}\b"

matches = re.finditer(pattern, phone_numbers)

for match in matches:
    print(match.group(), end=", ")

