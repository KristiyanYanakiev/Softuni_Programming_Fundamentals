import re

line = "Update: {plant} - {new_rarity}"

pattern = r":\s|\s-\s"

new_line = re.split(pattern, line)

print(new_line)








