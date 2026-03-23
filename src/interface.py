import os

def show_welcome_message() -> None:
    """
    Display the program title and short instructions to the user.
    :param data: none
    :return: welcome message
    """
    print("Welcome to the password generator! Please, abide to the following instructions.")


def get_password_length() -> int:
    """
    Ask the user for the desired password length.
    :param data: none
    :return: return user specified length
    """
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_character_set_choices() -> list[bool]:
    """
    Ask the user which character groups should be included.
    :param data: none
    :return: return user specified character set
    """
    def ask_yes_no(prompt: str) -> bool:
        while True:
            answer = input(prompt).strip().lower()
            if answer in ("y", "yes"):
                return True
            if answer in ("n", "no"):
                return False
            print("Please answer with yes/y or no/n.")

    include_uppercase = ask_yes_no("Include uppercase letters? (y/n): ")
    include_lowercase = ask_yes_no("Include lowercase letters? (y/n): ")
    include_digits = ask_yes_no("Include digits? (y/n): ")
    include_special = ask_yes_no("Include special characters? (y/n): ")

    return [include_uppercase, include_lowercase, include_digits, include_special]

def display_generated_password(password: str) -> None:
    """
    Show the generated password to the user.
    :param data: generated password
    :return: display generated password on screen
    """
    print(f"Generated password: {password}")


def display_password_strength(strength: str) -> None:
    """
    Show the result of the password strength assessment.
    :param data: password strength
    :return: display password strength on screen
    """
    print(f"Password strength: {strength}")

def ask_to_continue() -> bool:
    """
    Ask whether the user wants to generate another password.
    :param data: none
    :return: whether to continue program execution
    """
    while True:
        answer = input("Do you want to generate another password? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with yes/y or no/n.")

def reset_output_file(output_file: str) -> None:
    """
    Clear the contents of the output file so a new run starts with an empty file.
    :param data: Path to file
    :return: none
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("")


def append_password_to_text(password: str, strength: str, output_file: str) -> None:
    """
    Append the generated password and its strength to the output file.
    :param data: Password, Strength, Path to file
    :return: none
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "a", encoding="utf-8") as file:
        file.write(f"Password: {password}   :   {strength}\n")