import unittest

from bigcalc_manual import add_strings, sub_strings, mul_strings, div_strings


class TestBigCalcManual(unittest.TestCase):
    def test_addition_large(self):
        num1 = '1234567890' * 100
        num2 = '9876543210' * 100
        expected = str(int(num1) + int(num2))
        self.assertEqual(add_strings(num1, num2), expected)

    def test_subtraction_large(self):
        num1 = '9876543210' * 100
        num2 = '1234567890' * 100
        expected = str(int(num1) - int(num2))
        self.assertEqual(sub_strings(num1, num2), expected)

    def test_multiplication_large(self):
        num1 = '9' * 1000
        num2 = '8' * 1000
        expected = str(int(num1) * int(num2))
        self.assertEqual(mul_strings(num1, num2), expected)

    def test_division_large(self):
        num1 = '9' + '0' * 999
        num2 = '1' + '0' * 999
        expected = str(int(num1) // int(num2))
        self.assertEqual(div_strings(num1, num2), expected)


if __name__ == '__main__':
    unittest.main()
