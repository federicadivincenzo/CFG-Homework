import unittest
from assessment import add, subtract, divide, multiply, isEven


## SYNTAX : test_function_valid/invalid_what


class MyTestCase(unittest.TestCase):
    #VALID
    def test_add_valid(self):
        expected = 5
        actual = add(3, 2)
        self.assertEqual(expected, actual)

    def test_divide_valid(self):
        expected = 5
        actual = divide(10, 2)
        self.assertEqual(expected, actual)

    #INVALID
    def test_divide_invalid_divide_by_zero(self):
        while self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    # INVALID
    def test_divide_invalid_string(self):
        while self.assertRaises(TypeError):
            divide('string', 'string')

    def test_isEven_valid(self):
        self.assertTrue(isEven(2))

    def test_isEven_invalid_odd(self):
        self.assertFalse(isEven(3))

if __name__ == '__main__':
    unittest.main()
