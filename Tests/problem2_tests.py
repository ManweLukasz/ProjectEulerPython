import unittest
from Problems import sum_of_even_values_terms_fibo_sequence_below_given_value as tested_function


class TestFibFunctions(unittest.TestCase):

    def test_fib_output(self):
        self.assertEqual(tested_function(1), 0)
        self.assertEqual(tested_function(2), 2)
        self.assertEqual(tested_function(9), 10)
        self.assertEqual(tested_function(14), 10)
        self.assertEqual(tested_function(4000000), 4613732)


if __name__ == '__main__':
    unittest.main()
