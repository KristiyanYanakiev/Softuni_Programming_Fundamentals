products = {}

while True:
    line = input().split()

    if line[0] == "buy":
        break

    product = line[0]
    price = float(line[1])
    quantity = int(line[2])

    if product not in products.keys():
        products[product] = [price, quantity]
    else:
        products[product][1] += quantity
        products[product][0] = price

for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")

