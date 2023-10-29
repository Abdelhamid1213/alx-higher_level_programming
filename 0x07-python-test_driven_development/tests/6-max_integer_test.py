#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_unordered_list(self):
        unordered_list = [5, 4, 13, 7]
        self.assertEqual(max_integer(unordered_list), 13)

    def test_ordered_list(self):
        ordered_list = [0, 3, 5, 7]
        self.assertEqual(max_integer(ordered_list), 7)

    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_no_arguments(self):
        self.assertEqual(max_integer(), None)

    def test_str_list(self):
        str_list = ["one", "two", "nine"]
        self.assertEqual(max_integer(str_list), "two")

    def test_str(self):
        str = "abcdzef"
        self.assertEqual(max_integer(str), "z")

if __name__ == '__main__':
    unittest.main()
