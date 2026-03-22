import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import passgen

class TestPassgenFunctions(unittest.TestCase):

    def test_generate_password_length(self):
        # Test that the generated password length matches the requested length.
        result = passgen.generate_password(12, [True, True, True, True])
        self.assertEqual(len(result), 12)
        self.assertIsInstance(result, str)

    def test_generate_password_empty_pool(self):
        # Test that the function raises a ValueError if no character types are selected.
        with self.assertRaises(ValueError):
            passgen.generate_password(8, [False, False, False, False])

    def test_assess_strength_strong(self):
        # Test the password strength evaluator for a 'Strong' classification.
        # (12+ characters, including uppercase, lowercase, digits, and symbols)
        result = passgen.assess_password_strength("VeryStrong123!")
        self.assertEqual(result, "Strong")

    def test_assess_strength_weak(self):
        # Test the password strength evaluator for a 'Weak' classification.
        result = passgen.assess_password_strength("123")
        self.assertEqual(result, "Weak")


if __name__ == "__main__":
    unittest.main()