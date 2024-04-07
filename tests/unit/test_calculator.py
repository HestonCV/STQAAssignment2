import unittest
from bmi_calculator.calculator import calculate_bmi


class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi_normal_weight(self):
        # Test case for normal weight
        height = 69  # 5 feet 9 inches
        weight = 150     # 150 pounds
        expected_bmi = 22.68  # Expected BMI value for normal weight

        actual_bmi = calculate_bmi(height, weight)
        self.assertAlmostEqual(actual_bmi, expected_bmi, places=2)

    def test_calculate_bmi_underweight(self):
        # Test case for underweight
        height = 72  # 6 feet 0 inches
        weight = 120     # 120 pounds
        expected_bmi = 16.67  # Expected BMI value for underweight

        actual_bmi = calculate_bmi(height, weight)
        self.assertAlmostEqual(actual_bmi, expected_bmi, places=2)

    def test_calculate_bmi_overweight(self):
        # Test case for overweight
        height = 65  # 5 feet 5 inches
        weight = 175     # 200 pounds
        expected_bmi = 29.82  # Expected BMI value for overweight

        actual_bmi = calculate_bmi(height, weight)
        self.assertAlmostEqual(actual_bmi, expected_bmi, places=2)

    def test_calculate_bmi_obese(self):
        # Test case for obese
        height = 70  # 5 feet 10 inches
        weight = 250      # 250 pounds
        expected_bmi = 36.73  # Expected BMI value for obese

        actual_bmi = calculate_bmi(height, weight)
        self.assertAlmostEqual(actual_bmi, expected_bmi, places=2)


if __name__ == '__main__':
    unittest.main()
