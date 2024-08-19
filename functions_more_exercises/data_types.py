def data_type_configurator(some_data_type, some_data):
    if some_data_type == "int":
        result = 2 * int(data)
    elif some_data_type == "real":
        result = f"{1.5 * float(some_data):.2f}"
    else:
        result = f"${some_data}$"
    return result


data_type = input()
data = input()
print(data_type_configurator(data_type, data))

