COFFEE_PRICE = 1.50
WATER_PRICE = 1.00
COKE_PRICE = 1.40
SNACKS_PRICE = 2.00

def total_price(order, quantity):
    result = 0
    if order == "coffee":
        result = quantity * COFFEE_PRICE
    elif order == "coke":
        result = quantity * COKE_PRICE
    elif order == "water":
        result = quantity * WATER_PRICE
    elif order == "snacks":
        result = quantity * SNACKS_PRICE

    return f"{result:.2f}"

user_order = input()
product_quantity = int(input())

print(total_price(user_order, product_quantity))
