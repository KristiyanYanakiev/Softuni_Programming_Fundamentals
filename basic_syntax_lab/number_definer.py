number = float(input())
output = ""

if number == 0:
    output = "zero"
elif number > 0:
    output = "positive"
else:
    output = "negative"

if abs(number) < 1 and number != 0:
    output = f"small {output}"
elif abs(number) > 1000000:
    output = f"large {output}"

print(output)

