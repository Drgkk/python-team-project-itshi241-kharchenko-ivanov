import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import interface

class TestInterfaceFunctions(unittest.TestCase):

    def test_show_welcome_message(self):
        # Tests that the welcome message function prints something to the screen.
        with patch("builtins.print") as mocked_print:
            interface.show_welcome_message()
            mocked_print.assert_called()

    def test_get_password_length(self):
        # Tests that the password length function returns an integer from user input.
        with patch("builtins.input", return_value="12"):
            result = interface.get_password_length()
            self.assertIsInstance(result, int)

    def test_get_character_set_choices(self):
        # Tests that the character set choice function returns a list.
        with patch("builtins.input", side_effect=["y", "n", "y", "n"]):
            result = interface.get_character_set_choices()
            self.assertIsInstance(result, list)

    def test_display_generated_password(self):
        # Tests that the generated password function displays the password.
        with patch("builtins.print") as mocked_print:
            interface.display_generated_password("Abc123!")
            mocked_print.assert_called()

    def test_display_password_strength(self):
        # Tests that the password strength function displays the strength result.
        with patch("builtins.print") as mocked_print:
            interface.display_password_strength("Strong")
            mocked_print.assert_called()

    def test_ask_to_continue(self):
        # Tests that the continue function returns a boolean value.
        with patch("builtins.input", return_value="y"):
            result = interface.ask_to_continue()
            self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main()
