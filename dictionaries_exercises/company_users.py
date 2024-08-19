def id_available(some_dict: dict, some_key: str, some_id: str) -> True or False:
    if some_id in some_dict[some_key]:
        return False
    else:
        return True


company_users = {}

while True:
    command = input()
    if command == "End":
        break

    company_name, employee_id = command.split(" -> ")

    if company_name not in company_users.keys():
        company_users[company_name] = [employee_id]
    else:
        if id_available(company_users, company_name, employee_id):
            company_users[company_name].append(employee_id)

for key, value in company_users.items():
    print(key)
    for element in value:
        print(f"-- {element}")

