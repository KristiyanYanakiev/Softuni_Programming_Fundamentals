n = int(input())

for current_char in range(0, n):
    for second_char in range(0, n):
        for third_char in range(0, n):
            print(f"{chr(97 + current_char)}{chr(97 + second_char)}{chr(97 + third_char)}")

