import re

def check_password_strength(password):
    # Criteria checks
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[@$!%*?&]", password) is None

    # Count errors
    errors = sum([length_error, digit_error, uppercase_error, lowercase_error, special_char_error])

    # Strength rating
    if errors == 0:
        return "Strong Password"
    elif errors <= 2:
        return "Moderate Password"
    else:
        return "Weak Password"

# Get user input
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
