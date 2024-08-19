number_of_orders = int(input())
is_valid_data = False
total = 0


for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100.00:
        is_valid_data = True
    else:
        is_valid_data = False
        continue
    if 1 <= days <= 31:
        is_valid_data = True
    else:
        is_valid_data = False
        continue
    if 1 <= capsules_needed_per_day <= 2000:
        is_valid_data = True
    else:
        is_valid_data = False
        continue

    if is_valid_data:

        order_price = price_per_capsule * days * capsules_needed_per_day
        print(f"The price for the coffee is: ${order_price:.2f}")
        total += order_price


print(f"Total: ${total:.2f}")