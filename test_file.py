
import unittest
from main import CalorieBurnCalculator

class TestCalorieBurnCalculator(unittest.TestCase):
    def test_calculate_time_required(self):
        calculator = CalorieBurnCalculator(175, 70, 500)
        # Test with a speed where we know the expected time
        # Example: if 8 km/h should take 60 minutes to burn 500 calories, you should calculate this based on your formula
        self.assertAlmostEqual(calculator.calculate_time_required(8), 60, places=2)

    def test_calculate_speed_required(self):
        calculator = CalorieBurnCalculator(175, 70, 500)
        # Test with a time where we know the expected speed
        # Example: if 60 minutes should require 8 km/h to burn 500 calories
        self.assertAlmostEqual(calculator.calculate_speed_required(60), 8, places=2)

    def test_input_validation(self):
        # This should raise an error if the input is invalid
        with self.assertRaises(ValueError):
            CalorieBurnCalculator(0, 70, 500)  # height cannot be zero
        with self.assertRaises(ValueError):
            CalorieBurnCalculator(175, 0, 500)  # weight cannot be zero
        with self.assertRaises(ValueError):
            CalorieBurnCalculator(175, 70, -100)  # calories cannot be negative

if __name__ == '__main__':
    unittest.main()
