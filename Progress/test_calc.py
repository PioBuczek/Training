import unittest
from for_fun import calc_BMI


class TestBMIcalculator(unittest.TestCase):
    def test_underweight(self):
        result = calc_BMI(50, 1.80)
        self.assertEqual(result, "Your BMI is 15.432, you are underweight")

    def test_good_weight(self):
        result = calc_BMI(70, 1.80)
        self.assertEqual(result, "Your BMI is 21.605, you are good weight")

    def test_fat(self):
        result = calc_BMI(90, 1.80)
        self.assertEqual(result, "Your BMI is 27.778, you are fat")


if __name__ == "__main__":
    unittest.main()
