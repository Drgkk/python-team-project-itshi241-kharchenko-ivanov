import unittest
from unittest.mock import patch

import sys
import os
import tempfile
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

    def test_reset_output_file_clears_existing_content(self):
        #Tests that the function clears hte existing content of a specified file
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_file = os.path.join(tmp_dir, "output.txt")

            with open(output_file, "w", encoding="utf-8") as file:
                file.write("old content")

            interface.reset_output_file(output_file)

            with open(output_file, "r", encoding="utf-8") as file:
                content = file.read()

            self.assertEqual(content, "")

    def test_append_password_to_text_writes_content(tmp_path):
        #Tests that the function appends text to a file as expected
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_file = os.path.join(tmp_dir, "output.txt")

            interface.append_password_to_text("Abc123!", "Strong", output_file)

            with open(output_file, "r", encoding="utf-8") as file:
                content = file.read()

            assert content == "Password: Abc123!   :   Strong\n"   


if __name__ == "__main__":
    unittest.main()
