import re

places_on_the_map = input()
list_of_valid_places = []
travel_points = 0

pattern = r"([\/\=])([A-Z][A-Za-z]{2,})\1"

valid_places = re.finditer(pattern, places_on_the_map)

for valid_place in valid_places:
    travel_points += len(valid_place.group(2))
    list_of_valid_places.append(valid_place.group(2))

print(f"Destinations: {', '.join(list_of_valid_places)}")
print(f"Travel Points: {travel_points}")
