def password_validator(password):
    is_valid = True
    if not len(password) in range(6,11):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    counter_of_digits = 0
    for char in password:
        if char.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


users_password = input()
(password_validator(users_password))