from interface import show_welcome_message, get_password_length, get_character_set_choices, display_generated_password, display_password_strength, ask_to_continue
from passgen import generate_password, assess_password_strength


show_welcome_message()

while True:
    length = get_password_length()
    choices = get_character_set_choices()

    password = generate_password(length, choices)

    strength = assess_password_strength(password)
    display_generated_password(password)
    display_password_strength(strength)

    if not ask_to_continue():
        print("Goodbye!")
        break