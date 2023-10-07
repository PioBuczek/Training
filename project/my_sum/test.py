import unittest

from __init__ import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_in_minus(self):
        data = [-1, -2, -3]
        result = sum(data)
        self.assertEqual(result, -6)

    def test_str_in_list(self):
        data = [-1, 2, "3"]
        with self.assertRaises(TypeError):
            sum(data)


if __name__ == "__main__":
    unittest.main()
