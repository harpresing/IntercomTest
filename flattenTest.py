"""Test suite for flatten.py.

Written by: Harpreet Singh
""" 

import unittest
from flatten import FlattenArray


class FlattenTest(unittest.TestCase):
    
    def test_depth_five(self):
        ob = FlattenArray()
        arr = [[[2, 3, 4], 3, 5, 7, [[2, [66], 7]], 87, 65, 47, 90]]
        flatArr = [2, 3, 4, 3, 5, 7, 2, 66, 7, 87, 65, 47, 90]
        self.assertEqual(ob.flatten(arr), flatArr)

    def test_depth_one(self):
        ob = FlattenArray()
        arr = [2, 4, 5, 6, 7]
        flatArr = arr
        self.assertEqual(ob.flatten(arr), flatArr)

    def test_empty_list(self):
        ob = FlattenArray()
        arr = []
        flatArr = []
        self.assertEqual(ob.flatten(arr), flatArr)

    def test_empty_list_depth_three(self):
        ob = FlattenArray()
        arr = [[[]]]
        flatArr = []
        self.assertEqual(ob.flatten(arr), flatArr)

    def test_list_with_negative_elements(self):
        ob = FlattenArray()
        arr = [1, -2, [3, -4, 5, [[-6]], -7, [[8, 9]]], -4]
        flatArr = [1, -2, 3, -4, 5, -6, -7, 8, 9, -4]
        self.assertEqual(ob.flatten(arr), flatArr)

    def test_list_with_elements_of_different_datatypes(self):
        ob = FlattenArray()
        arr = [[["Hakuna Matata"]], 3, -4.33, 5, [["Hello, world!"]], [7, 'b', 9], 10]
        flatArr = ["Hakuna Matata", 3, -4.33, 5, "Hello, world!", 7, 'b', 9, 10]
        self.assertEqual(ob.flatten(arr), flatArr)

if __name__ == '__main__':
    unittest.main()