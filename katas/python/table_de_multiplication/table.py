#!usr/bin/python
#-*-coding:utf-8 -*
import unittest

class TestTableDeMultiplication(unittest.TestCase):

    def testTrueTrue(self):
        self.assertEqual(True,True)

    def testMultiply(self):
        self.assertEqual(multiply(1),0)


if __name__=='__main__':
    unittest.main()
