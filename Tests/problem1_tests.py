import unittest
from Problems import sum_of_multiples_3_and_5_below_given_number


class MyTestCase(unittest.TestCase):
    def test_sum_of_multiples(self):
        self.assertEqual(sum_of_multiples_3_and_5_below_given_number(10), 23)  # add assertion here
        self.assertEqual(sum_of_multiples_3_and_5_below_given_number(5), 3)
        self.assertEqual(sum_of_multiples_3_and_5_below_given_number(6), 8)
        self.assertEqual(sum_of_multiples_3_and_5_below_given_number(7), 14)


if __name__ == '__main__':
    unittest.main()
