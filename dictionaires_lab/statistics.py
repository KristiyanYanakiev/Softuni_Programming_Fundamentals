def add_new_product_or_add_quantity(some_bakery, some_product, some_quantity):
    if some_product in some_bakery:
        some_bakery[some_product] += some_quantity
    else:
        some_bakery[some_product] = some_quantity

bakery = {}

while True:
    command = input()

    if command == "statistics":
        break

    command_as_list = command.split(":")
    product = command_as_list[0]
    quantity = int(command_as_list[1])

    add_new_product_or_add_quantity(bakery, product, quantity)

print("Products in stock:")
for key, value in bakery.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(bakery)}\nTotal Quantity: {sum(bakery.values())}")




