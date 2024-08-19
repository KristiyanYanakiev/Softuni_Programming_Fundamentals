numbers = [int(element) for element in input().split(", ")]

positive = [str(num) for num in numbers if num >= 0]
negative = [str(num) for num in numbers if num < 0]
even = [str(num) for num in numbers if num % 2 == 0]
odd = [str(num) for num in numbers if num % 2 != 0]

positive = (", ".join(positive))
negative = (", ".join(negative))
even = (", ".join(even))
odd = (", ".join(odd))

output = f"Positive: {positive}\nNegative: {negative}\nEven: {even}\nOdd: {odd}"

print(output)
