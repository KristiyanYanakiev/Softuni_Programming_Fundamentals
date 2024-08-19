collection_of_items = input().split("|")
budget = int(input())
starting_budget = budget
TICKET_FOR_FRANCE_PRICE = 150
proceed_to_purchase = None
list_with_new_item_prices = []
total_budget_after_selling_the_items = 0

for element in collection_of_items:

    element_as_list = element.split("->")
    item = element_as_list[0]
    item_price = float(element_as_list[1])

    if item == "Clothes" and item_price <= 50.00 and budget >= item_price:
        proceed_to_purchase = True
    elif item == "Shoes" and item_price <= 35.00 and budget >= item_price:
        proceed_to_purchase = True
    elif item == "Accessories" and item_price <= 20.50 and budget >= item_price:
        proceed_to_purchase = True
    else:
        proceed_to_purchase = False

    if proceed_to_purchase:
        budget -= item_price
        item_new_price = item_price * 0.4 + item_price
        list_with_new_item_prices.append(item_new_price)
        total_budget_after_selling_the_items += item_new_price

total_budget_after_selling_the_items += budget
profit = total_budget_after_selling_the_items - starting_budget

list_with_new_item_prices = [f"{price:.2f}" for price in list_with_new_item_prices]

list_with_new_item_prices_as_string = ""

for x in list_with_new_item_prices:
    list_with_new_item_prices_as_string += f"{x} "

print(list_with_new_item_prices_as_string)
print(f"Profit: {profit:.2f}")

if total_budget_after_selling_the_items >= TICKET_FOR_FRANCE_PRICE:
    print("Hello, France!")
else:
    print("Not enough money.")


