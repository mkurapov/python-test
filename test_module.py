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

    def testNormalCircle(self):
        cir = Circle(7)
        self.assertEqual(round(cir.getArea(),2), 153.94)

    def testNullParametersRec(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(None, None)

    def testNullParametersPar(self):
        with self.assertRaises(ValueError):
            par = Parallelogram(None, None)

    def testNullParametersTri(self):
        with self.assertRaises(ValueError):
            tri = Triangle(None, None)

    def testNullParametersCir(self):
        with self.assertRaises(ValueError):
            cir = Circle(None)

    def testNegParameterRec(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(-5, 0)

    def testNegParametersPar(self):
        with self.assertRaises(ValueError):
            par = Parallelogram(0, -3)

    def testNegParametersTri(self):
        with self.assertRaises(ValueError):
            tri = Triangle(0, -5)

    def testNegParametersCir(self):
        with self.assertRaises(ValueError):
            cir = Circle(-5)

if __name__ == '__main__':
    unittest.main()
