team_a = []
team_b = []

for index in range(1, 12):
    team_a.append(f"A-{index}")

for index in range(1, 12):
    team_b.append(f"B-{index}")

list_of_cards = input().split(" ")

for element in list_of_cards:
    if element in team_a:
        team_a.remove(element)
    elif element in team_b:
        team_b.remove(element)

    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")




