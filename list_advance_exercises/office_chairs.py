number_of_rooms = int(input())
total_free_chairs = 0
total_visitors = 0
total_used_chairs = 0
total_needed = 0

for current_room in range(1, number_of_rooms + 1):
    chair_info = input()
    number_of_chairs = len(chair_info.split()[0])
    number_of_visitors = int(chair_info.split()[1])
    total_visitors += number_of_visitors


    if number_of_visitors > number_of_chairs:
        print(f"{number_of_visitors - number_of_chairs} more chairs needed in room {current_room}")
        total_needed += number_of_visitors - number_of_chairs
    else:
        total_free_chairs += number_of_chairs - number_of_visitors

if total_free_chairs >= total_needed:
    print(f"Game On, {total_free_chairs} free chairs left")











