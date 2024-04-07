import unittest

class TestTriangle(unittest.TestCase):

    def test_right_triangle(self):
        a = 3
        b = 4
        c = 5
        self.assertEqual(is_right_triangle(a, b, c), True)

    def test_not_right_triangle(self):
        a = 3
        b = 4
        c = 6
        self.assertEqual(is_right_triangle(a, b, c), False)

def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2

if __name__ == '__main__':
    unittest.main()
