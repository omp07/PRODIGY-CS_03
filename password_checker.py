import re


def check_password_complexity(password):
    # Define regular expressions for different criteria
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password))

    # Check length
    length_ok = len(password) >= 8

    # Initialize strength
    strength = "Weak"

    # Check overall strength
    if has_uppercase and has_lowercase and has_digit and has_special and length_ok:
        strength = "Strong"
    elif (has_uppercase and has_lowercase and has_digit) or (has_uppercase and has_lowercase and has_special) or (
            has_uppercase and has_digit and has_special) or (has_lowercase and has_digit and has_special):
        strength = "Moderate"

    # Build output message
    output = "Password complexity:\n"
    output += f"- Length: {'OK' if length_ok else 'Weak'}\n"
    output += f"- Uppercase letter: {'OK' if has_uppercase else 'Not found'}\n"
    output += f"- Lowercase letter: {'OK' if has_lowercase else 'Not found'}\n"
    output += f"- Digit: {'OK' if has_digit else 'Not found'}\n"
    output += f"- Special character: {'OK' if has_special else 'Not found'}\n"
    output += f"Overall strength: {strength}"

    return output


# Example usage
print("Welcome to Password Complexity")
password = input("Enter your password: ")
result = check_password_complexity(password)
print(result)
