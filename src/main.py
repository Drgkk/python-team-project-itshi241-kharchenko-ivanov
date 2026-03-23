from interface import show_welcome_message, get_password_length, get_character_set_choices, display_generated_password, display_password_strength, ask_to_continue, reset_output_file, append_password_to_text
from passgen import generate_password, assess_password_strength

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "output.txt")

show_welcome_message()
reset_output_file(OUTPUT_FILE)

while True:
    length = get_password_length()
    choices = get_character_set_choices()

    password = generate_password(length, choices)

    strength = assess_password_strength(password)
    display_generated_password(password)
    display_password_strength(strength)
    append_password_to_text(password, strength, OUTPUT_FILE)

    if not ask_to_continue():
        print("Goodbye!")
        break