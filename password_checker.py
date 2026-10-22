def password_checker(password):
    rules = 0

    if len(password) >= 8:
        rules += 1

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*":
            has_special = True

    if has_uppercase and has_lowercase:
        rules += 1
    if has_digit:
        rules += 1  
    if has_special:
        rules += 1

    if rules == 4:
        return "strong"
    if rules >= 2:
        return "medium"
    return "weak"

print(password_checker("Password123!"))  # strong
print