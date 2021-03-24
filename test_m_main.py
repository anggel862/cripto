import unittest
import os
from main import *
    
class TestBlocksFill(unittest.TestCase):

    def test_g(self):
        self.assertEqual(g('001011110'+'000101000111'),'001001011010')
    
    #def test_addZerosUntilMultiple12(self):
    #    self.assertEqual(addZerosUntilMultiple12('100'),'000000000100')
    
    def test_addZerosUntilMultiple(self):
        self.assertEqual(addZerosUntilMultiple('100',12),'000000000100')
    
    def test_addOneToEachSubseq(self):
        self.assertEqual(addOneToEachSubseq('000011000111110000000000',r=9),'100001100101111100100000000')



if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("Exception SystemExit occurred!")