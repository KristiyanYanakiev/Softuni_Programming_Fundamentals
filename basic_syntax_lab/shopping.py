budget = int(input())

total_expenses = 0

while True:
    order = input()
    if order == "End":
        break

    current_product_price = int(order)
    total_expenses += current_product_price

    if total_expenses > budget:
        print("You went in overdraft!")
        exit()

print("You bought everything needed.")

