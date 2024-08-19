# number_of_strings = int(input())
#
# is_pure = True
#
# for current_string in range(number_of_strings):
#     string = input()
#
#     if "," in string or "." in string or "_" in string:
#         is_pure = False
#
#     if is_pure:
#         print(f"{string} is pure.")
#     else:
#         print(f"{string} is not pure!")


number_of_strings = int(input())
not_pure_characters = [",", ".", "_"]

for current_string in range(number_of_strings):
    is_pure = True
    string = input()
    for char in not_pure_characters:
        if char in string:
            is_pure = False

    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")

