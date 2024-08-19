def loading_bar(some_number):
    if some_number == 100:
        output = f"100% Complete!"
        list = [10 * "%"]
        list_as_string = "".join(list)
        list_as_string = f"[{list_as_string}]"
        return f"{output}\n{list_as_string}"

    else:
        number_of_different_signs = some_number // 10
        list = [number_of_different_signs * "%" + (10 - number_of_different_signs) * "."]
        list_as_string = "".join(list)
        list_as_string = f"[{list_as_string}]"
        return f"{some_number}% {list_as_string}\nStill loading..."

number = int(input())
print(loading_bar(number))
