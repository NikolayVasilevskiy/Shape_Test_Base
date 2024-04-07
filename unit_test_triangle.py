import unittest
import math

class TestTriangle(unittest.TestCase):

    def test_area_of_triangle(self):
        a = 3
        b = 4
        c = 5
        expected_area = 6
        self.assertEqual(area_of_triangle(a, b, c), expected_area)

def area_of_triangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

if __name__ == '__main__':
    unittest.main()