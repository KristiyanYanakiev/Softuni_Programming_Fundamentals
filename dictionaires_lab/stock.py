def stock(some_bakery, some_products):
    for current_product in some_products:
        if current_product in some_bakery:
            print(f"We have {some_bakery[current_product]} of {current_product} left")
        else:
            print(f"Sorry, we don't have {current_product}")


food_and_quantities = input().split()

bakery = {}

for current_index in range(0, len(food_and_quantities), 2):
    current_key = food_and_quantities[current_index]
    current_value = food_and_quantities[current_index + 1]
    bakery[current_key] = current_value


products_to_search_for = input().split()

stock(bakery, products_to_search_for)
