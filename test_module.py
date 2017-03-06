import unittest

from Rectangle import Rectangle
from Parallelogram import Parallelogram
from Triangle import Triangle
from Circle import Circle
from Shape import Shape

class TestStringMethods(unittest.TestCase):
    def testNormalRectangle(self):
        rec = Rectangle(5,5)
        self.assertEqual(rec.getArea(), 25)
)    

if __name__ == '__main__':
    unittest.main()
