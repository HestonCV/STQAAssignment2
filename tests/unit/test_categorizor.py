import unittest
from bmi_calculator.categorizor import categorize_bmi

class TestBMICategorizer(unittest.TestCase):
    def test_categorize_bmi_underweight_boundary(self):
        bmi = 18.4  # Just below the lower boundary of Normal weight
        category = categorize_bmi(bmi)
        self.assertEqual(category, "Underweight")

        bmi = 18.5  # On the lower boundary of Normal weight
        category = categorize_bmi(bmi)
        self.assertEqual(category, "Normal Weight")

    def test_categorize_bmi_normal_weight_boundary(self):
        bmi = 24.9  # On the upper boundary of Normal weight
        category = categorize_bmi(bmi)
        self.assertEqual(category, "Normal Weight")

        bmi = 25.0  # Just above the upper boundary of Normal weight
        category = categorize_bmi(bmi)
        self.assertEqual(category, "Overweight")

    def test_categorize_bmi_overweight_boundary(self):
        bmi = 29.9  # On the upper boundary of Overweight
        category = categorize_bmi(bmi)
        self.assertEqual(category, "Overweight")

        bmi = 30.0  # On the lower boundary of Obese
        category = categorize_bmi(bmi)
        self.assertEqual(category, "Obese")

if __name__ == '__main__':
    unittest.main()