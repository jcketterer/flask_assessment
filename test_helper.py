from forex_python.converter import RatesNotAvailableError
from helper import final_amount, correct_curr_code, valid_number
from unittest import TestCase


class HelperTestCase(TestCase):
    def test_correct_number_input(self):
        """Check correct number"""

        self.assertTrue(valid_number("1"))
        self.assertTrue(valid_number("3.0"))
        self.assertTrue(valid_number(5))
        self.assertTrue(valid_number(3.0))

        self.assertFalse(valid_number("two"))
        self.assertFalse(valid_number(0))
        self.assertFalse(valid_number("0"))
        self.assertFalse(valid_number("-5"))
        self.assertFalse(valid_number(-5))

    def test_correct_code(self):
        """Checks for correct currency code entered"""

        self.assertTrue(correct_curr_code("USD"))
        self.assertTrue(correct_curr_code("EUR"))
        self.assertTrue(correct_curr_code("GBP"))

        self.assertFalse(correct_curr_code("aaa"))
        self.assertFalse(correct_curr_code("123"))
        self.assertFalse(correct_curr_code("MKJHa"))
        self.assertFalse(correct_curr_code(456))

    def test_helper(self):
        """Test full function with different letter sizing and produces correct output"""

        self.assertEqual(final_amount("USD", "USD", "5"), "US$5.00")
        self.assertEqual(final_amount("USD", "USD", 5), "US$5.00")
        self.assertIn("3.00", final_amount("EUR", "EUR", "3"))
        self.assertIn("9.99", final_amount("EUR", "EUR", "9.99"))
        self.assertRaises(RatesNotAvailableError, final_amount, "ZZZ", "USD", "5.00")
        self.assertIsInstance(final_amount("GPB", "GPB", "15"), str)
