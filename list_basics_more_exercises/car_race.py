sequence_of_numbers = [element for element in input().split()]

finish_line = len(sequence_of_numbers) // 2

left_total_time = 0
right_total_time = 0

for x in sequence_of_numbers[:finish_line]:
    left_total_time += int(x)

    if int(x) == 0:
        left_total_time -= 0.2 * left_total_time

for y in sequence_of_numbers[:finish_line:-1]:
    right_total_time += int(y)

    if int(y) == 0:
        right_total_time -= 0.2 * right_total_time


winner = ""
total_time = 0

if left_total_time < right_total_time:
    winner = "left"
    total_time = left_total_time
elif left_total_time > right_total_time:
    winner = "right"
    total_time = right_total_time


print(f"The winner is {winner} with total time: {total_time:.1f}")




