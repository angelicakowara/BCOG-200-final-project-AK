"""Example case + math/logic included
-user input: 
  Weight: 75 kg
  Desired Calories to Burn: 300
  Speed: 8 km/h

-assume MET value of 8 for 8km/hr

-calculate calories burned per minute
  Calories per minute=(8 METs×75 kg×3.5)/200
  Calories per minute=(2100/200) =10.5 calories/minute

-calculate time required 
time required = 300 calories / (10.5 calories/minute) = 28.6 minutes 

-return time required to the user 
"""
import unittest
from main import CalorieBurnCalculator

class TestCalorieBurnCalculator(unittest.TestCase):
    def test_calculate_time_required(self):
        calculator = CalorieBurnCalculator(175, 70, 500)
        self.assertAlmostEqual(calculator.calculate_time_required(8), 60, places=2)

    def test_calculate_speed_required(self):
        calculator = CalorieBurnCalculator(175, 70, 500)
        self.assertAlmostEqual(calculator.calculate_speed_required(60), 8, places=2)

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            CalorieBurnCalculator(0, 70, 500)  # height cannot be zero
        with self.assertRaises(ValueError):
            CalorieBurnCalculator(175, 0, 500)  # weight cannot be zero
        with self.assertRaises(ValueError):
            CalorieBurnCalculator(175, 70, -100)  # calories cannot be negative

if __name__ == '__main__':
    unittest.main()
