import unittest
from listutil import *
from random import randint

class ListutilTest( unittest.TestCase ):

    def test_single_item_list(self):
        # ['hi'] will return ['hi']
        self.assertEqual([5], unique([5]))
        self.assertEqual([0], unique([0]))
        self.assertEqual([1], unique([1]))
        self.assertListEqual( ['hi'], unique(['hi']) )
    
    def test_multiple_ele_list(self):
        # should return the one duplicate of the same element with the smae order
        self.assertEqual(['b', 'a'], unique(['b','a','a','b','b','b','a','a']))
        self.assertEqual(['cat'], unique(['cat', 'cat', 'cat', 'cat', 'cat']))
        self.assertEqual(['cat', 'dog'], unique(['cat', 'dog', 'cat', 'cat', 'dog']))
        self.assertEqual(['a', 'b', ['a', 'a'], 'c'], unique(['a', 'b', ['a', 'a'], 'b', 'c', ['a', 'a'], 'b', 'c']))
    
    def test_huge_list(self):
        # list of 1000 random number in range 1 to 50
        huge_list = [randint(1, 50) for i in range(1000)]
        self.assertEqual(sorted(list(range(1, 51))), sorted(unique(huge_list)))
    
    def test_empty_list(self):
        # result should be [] 
        self.assertEqual([], unique([]))
    
    def test_non_type_list(self):
        # should raise TypeError exception 
        with self.assertRaises(TypeError):
            uni = unique('str')

if __name__ == "__main__":
    unittest.main()