import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import passgen

class TestFile2Functions(unittest.TestCase):

    def test_generate_password(self):
        # Tests that the password generator returns a string.
        result = passgen.generate_password(8, ["a", "b", "1", "!"])
        self.assertIsInstance(result, str)

    def test_assess_password_strength(self):
        # Tests that the strength checker returns a string value.
        result = passgen.assess_password_strength("Abc123!@#")
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()