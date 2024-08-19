INITIAL_ENERGY = 100
current_energy = INITIAL_ENERGY
INITIAL_COINS = 100
current_coins = INITIAL_COINS

is_factory_open = True
handled_events = 0

working_day_events = input().split("|")

for element in working_day_events:

    element_as_list = element.split("-")
    event_name = element_as_list[0]
    event_number = int(element_as_list[1])

    if event_name == "rest":
        gained_energy = event_number
        current_energy += gained_energy

        if current_energy > 100:
            gained_energy = gained_energy - abs(current_energy - 100)
            current_energy = 100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
        handled_events += 1

    elif event_name == "order":
        earned_coins = event_number
        if current_energy >= 30:
            current_energy -= 30
            current_coins += earned_coins
            print(f"You earned {earned_coins} coins.")
            handled_events += 1
        else:
            current_energy += 50
            print("You had to rest!")
            if current_energy > INITIAL_ENERGY:
                current_energy = 100


    else:
        ingredient_to_buy = element_as_list[0]
        coins_to_be_spent = event_number

        if current_coins >= coins_to_be_spent:
            current_coins -= coins_to_be_spent
            print(f"You bought {ingredient_to_buy}.")
            handled_events += 1
        else:
            print(f"Closed! Cannot afford {ingredient_to_buy}.")
            is_factory_open = False
            break

if len(working_day_events) == handled_events: #is_factory_open:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")


