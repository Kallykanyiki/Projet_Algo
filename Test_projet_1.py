import unittest
import math
from Implementation001 import *


class TestGeometricform(unittest.TestCase):
    def test_Rectangle(self):
        Rectangle = Rectangle(4,8)
        self.assertEqual(Rectangle.périmètre(), 12)
        self.assertEqual(Rectangle.surface(), 10)

    def test_Cercle(self):
        Cercle = Cercle(5)
        self.assertEqual(Cercle.périmètre(), 2*pi*5)
        self.assertEqual(Cercle.surface(), pi*5**2)

    def test_Triangle(self):
        Triangle = Triangle(4,6,5)
        self.assertEqual(Triangle.périmètre(), 10)
        self.assertEqual(Triangle.surface(), 9)

    def test_Carré(self):
        Carré = Carré(6)
        self.assertEqual(Carré.périmètre(), 20)
        self.assertEqual(Carré.surface(), 30)

    def test_TriangleRectangle(self):
        TriangleRectangle = TriangleRectangle(3,6)
        self.assertEqual(TriangleRectangle.périmètre(), 10)
        self.assertEqual(TriangleRectangle.surface(), 8)

if __name__ == '__main__':
    unittest.main()
    