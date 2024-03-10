import unittest
from unittest.mock import patch
from utils import verify_if_prime_number, verify_if_prime_number_basic
from utils import generate_fib_sequence
from utils import get_input_from_user


class MyTestCase(unittest.TestCase):

    @patch('builtins.input', side_effect=['5'])
    def test_get_input_from_user_int(self, mock_input):
        result = get_input_from_user("Podaj liczbę", int, 0)
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['5.4'])
    def test_get_input_from_user_wrong_type(self, mock_input):
        with (self.assertRaises(ValueError)):
            get_input_from_user("Podaj liczbę", int, 0)

    @patch('builtins.input', side_effect=['Adam'])
    def test_get_input_from_user_str(self, mock_input):
        result = get_input_from_user("Podaj imię", str)
        self.assertEqual(result, 'Adam')

    @patch('builtins.input', side_effect=['-4', '4'])
    @patch('builtins.print')
    def test_get_input_from_user_too_low_number(self, mock_print, mock_input):
        result = get_input_from_user("Podaj liczbę", int, 0)
        self.assertEqual(result, 4)
        mock_print.assert_called_once_with("Your number -4 is lower than 0")


    def test_prime_numbers(self):
        self.assertEqual(verify_if_prime_number(1), False)
        self.assertEqual(verify_if_prime_number(2), True)
        self.assertEqual(verify_if_prime_number(3), True)
        self.assertEqual(verify_if_prime_number(4), False)
        self.assertEqual(verify_if_prime_number(5), True)
        self.assertEqual(verify_if_prime_number(6), False)
        self.assertEqual(verify_if_prime_number(7), True)
        self.assertEqual(verify_if_prime_number(10), False)
        self.assertEqual(verify_if_prime_number(13), True)

    def test_prime_numbers_basic(self):
        self.assertEqual(verify_if_prime_number_basic(1), False)
        self.assertEqual(verify_if_prime_number_basic(2), True)
        self.assertEqual(verify_if_prime_number_basic(3), True)
        self.assertEqual(verify_if_prime_number_basic(4), False)
        self.assertEqual(verify_if_prime_number_basic(5), True)
        self.assertEqual(verify_if_prime_number_basic(6), False)
        self.assertEqual(verify_if_prime_number_basic(7), True)
        self.assertEqual(verify_if_prime_number_basic(10), False)
        self.assertEqual(verify_if_prime_number_basic(13), True)

    def test_generating_fibo_sequence(self):
        self.assertEqual(generate_fib_sequence(1),[0])
        self.assertEqual(generate_fib_sequence(2), [0, 1])
        self.assertEqual(generate_fib_sequence(3), [0, 1, 1])
        self.assertEqual(generate_fib_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


if __name__ == '__main__':
    unittest.main()
