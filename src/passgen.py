from random import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

def generate_password(length: int, character_pool: list[bool]) -> str:
    """
    Generate a random password.
    :param data: password length, pool of allowed characters
    :return: return generated password
    """
    selected_options = ""
    for index, is_included in enumerate(character_pool):
        match index:
            case 0 if is_included:
                selected_options += ascii_uppercase
            case 1 if is_included:
                selected_options += ascii_lowercase
            case 2 if is_included:
                selected_options += digits
            case 3 if is_included:
                selected_options += punctuation

    if not selected_options:
        raise ValueError("Error: Character pool is empty. Please select at least one option!")

    return "".join(choice(selected_options) for _ in range(length))


def assess_password_strength(password: str) -> str:
    """
    Evaluate the password strength.
    :param data: password
    :return: return password strength assessment ("Weak", "Medium", "Strong")
    """
    length_score = len(password) >= 12  
    has_upper = any(ch in ascii_uppercase for ch in password)
    has_lower = any(ch in ascii_lowercase for ch in password)
    has_digit = any(ch in digits for ch in password)
    has_symbol = any(ch in punctuation for ch in password)

    categories = sum([has_upper, has_lower, has_digit, has_symbol])

    if len(password) < 6 or categories < 2:
        return "Weak"
    elif length_score and categories >= 3:
        return "Strong"
    else:
        return "Medium"