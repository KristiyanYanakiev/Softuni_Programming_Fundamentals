number_of_comments = int(input())
parking = {}

for current_command in range(number_of_comments):
    command = input().split()

    action = command[0]
    username = command[1]


    if action == "register":
        license_plate_number = command[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif action == "unregister":
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")


for key, value in parking.items():
    print(f"{key} => {value}")


