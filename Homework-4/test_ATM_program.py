import unittest
from unittest import mock
from ATM_program import pin_validated, withdrawal_validated


class MyTestCase(unittest.TestCase):
    def test_pin_is_correct(self):
        expected = True
        result = pin_validated('1234')
        self.assertEqual(expected, result)  # add assertion here

    def test_pin_contains_chars(self):
        expected = False
        result = pin_validated('12fg')
        self.assertEqual(expected, result)

    def test_withdrawal_lower_than_amount(self):
        expected = True
        result = pin_validated('56')
        self.assertEqual(expected, result)

    def test_withdrawal_negative(self):
        expected = False
        result = pin_validated('-456')
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
