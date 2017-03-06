import unittest

from Rectangle import Rectangle
from Parallelogram import Parallelogram
from Triangle import Triangle
from Circle import Circle
from Shape import Shape

class ShapesTestMethods(unittest.TestCase):
    def testNormalRectangle(self):
        rec = Rectangle(5,5)
        self.assertEqual(rec.getArea(), 25)

    def testNormalParallelorgram(self):
        par = Parallelogram(35,2)
        self.assertEqual(par.getArea(), 70)

    def testNormalTriangle(self):
        tri = Triangle(35,2)
        self.assertEqual(tri.getArea(), 35)

    def testNormalCircleRadius(self):
        cir = Circle(7)
        self.assertEqual(round(cir.getArea(),2), 153.94)

    def testNullParametersRec(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(None, None)

    def testNullParametersPar(self):
        with self.assertRaises(ValueError):
            par = Parallelogram(None, None)

if __name__ == '__main__':
    unittest.main()
