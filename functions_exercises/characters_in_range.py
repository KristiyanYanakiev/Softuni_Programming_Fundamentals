def chars_in_range(start_of_range, end_of_range):
    result = ""
    for current_chars in range(ord(start_of_range) + 1, ord(end_of_range)):
        result += f"{chr(current_chars)} "
    return result[:-1]


start = input()
end = input()

print(chars_in_range(start, end))

