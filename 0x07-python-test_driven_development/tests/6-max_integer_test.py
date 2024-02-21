#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class for testing max_integer()
    """

    def test_Max(self):
        self.assertEqual(max_integer([-1, -10, -100, -1000]), -1)
        self.assertEqual(max_integer([-10]), -10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(max_integer([1000, 100, 10000]), 10000)
        self.assertEqual(max_integer(["q", '1000', '009090', '8', '100']), 'q')
        self.assertEqual(max_integer([8888, 9999, 1111]), 9999)
        self.assertEqual(max_integer(['', '99', '999', 'ggg', '999']), 'ggg')
        self.assertEqual(max_integer([0, 0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([1, 100, 1000, 1000, 9]), 1000)
        self.assertEqual(max_integer([200]), 200)
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
