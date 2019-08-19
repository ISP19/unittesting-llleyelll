import unittest
from listutil import *

class ListutilTest( unittest.TestCase ):

    def test_single_item_list(self):
        self.assertEqual([5], unique([5]))
        self.assertEqual([0], unique([0]))
        self.assertEqual([1], unique([1]))
        self.assertListEqual( ['hi'], unique(['hi']) )
    
    def test_multiple_ele_list(self):
        self.assertEqual(['b', 'a'], unique(['b','a','a','b','b','b','a','a']))
        self.assertEqual(['cat'], unique(['cat', 'cat', 'cat', 'cat', 'cat']))
        self.assertEqual(['cat', 'dog'], unique(['cat', 'dog', 'cat', 'cat', 'dog']))
        self.assertEqual(['a', 'b', ['a', 'a'], 'c'], unique(['a', 'b', ['a', 'a'], 'b', 'c', ['a', 'a'], 'b', 'c']))
    
    def test_empty_list(self):
        self.assertEqual([], unique([]))
    
    def test_non_type_list(self):
        with self.assertRaises(TypeError):
            uni = unique('str')

if __name__ == "__main__":
    unittest.main()