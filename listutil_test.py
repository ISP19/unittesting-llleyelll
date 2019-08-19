import unittest
from listutil import *

class ListutilTest( unittest.TestCase ):

    def test_single_item_list(self):
        self.assertEqual([5], unique([5]))
        self.assertEqual([0], unique([0]))
        self.assertEqual([1], unique([1]))
        self.assertListEqual( ['hi'], unique(['hi']) )
    
    def test_unique_multiple_values(self):
        self.assertEqual(['b', 'a'], unique(['b','a','a','b','b','b','a','a']))
        self.assertEqual(['cat'], unique(['cat', 'cat', 'cat', 'cat', 'cat']))
        self.assertEqual(['cat', 'dog'], unique(['cat', 'dog', 'cat', 'cat', 'dog']))
        self.assertEqual(['a', 'b', ['a', 'a'], 'c'], unique(['a', 'b', ['a', 'a'], 'b', 'c', ['a', 'a'], 'b', 'c']))
    
    def test_unique_empty_value(self):
        self.assertEqual([], unique([]))
    
    def test_argument_not_a_list(self):
        with self.assertRaises(TypeError):
            uni = unique('a')

    def test_average_singleton_list(self):
        self.assertEqual(5, average([5]))
        self.assertEqual(1, average([1]))

    def test_average_many_values(self):
        self.assertEqual(4, average([4, 4, 4]))

    def test_average_empty_list(self):
        with self.assertRaises(ValueError):
            avg = average([])

if __name__ == "__main__":
    unittest.main()