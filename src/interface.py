def show_welcome_message() -> None:
    """
    Display the program title and short instructions to the user.
    :param data: none
    :return: welcome message
    """
    raise NotImplementedError("Interface function not implemented yet.")


def get_password_length() -> int:
    """
    Ask the user for the desired password length.
    :param data: none
    :return: return user specified length
    """
    raise NotImplementedError("Interface function not implemented yet.")

def get_character_set_choices() -> list[bool]:
    """
    Ask the user which character groups should be included.
    :param data: none
    :return: return user specified character set
    """
    raise NotImplementedError("Interface function not implemented yet.")

def display_generated_password(password: str) -> None:
    """
    Show the generated password to the user.
    :param data: generated password
    :return: display generated password on screen
    """
    raise NotImplementedError("Interface function not implemented yet.")


def display_password_strength(strength: str) -> None:
    """
    Show the result of the password strength assessment.
    :param data: password strength
    :return: display password strength on screen
    """
    raise NotImplementedError("Interface function not implemented yet.")

def ask_to_continue() -> bool:
    """
    Ask whether the user wants to generate another password.
    :param data: none
    :return: whether to continue program execution
    """
    raise NotImplementedError("Interface function not implemented yet.")
