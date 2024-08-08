import unittest
import pandas as pd
from rules.no_consecutive_night_shifts_rule import NoConsecutiveNightShiftsRule

class TestNoConsecutiveNightShiftsRule(unittest.TestCase):

    def setUp(self):
        self.rule = NoConsecutiveNightShiftsRule()

    def test_validate_no_consecutive_nights(self):
        data = pd.DataFrame({
            'EmployeeID': [101, 101, 102, 102],
            'Name': ['John Doe', 'John Doe', 'Jane Smith', 'Jane Smith'],
            'Day': ['Monday', 'Wednesday', 'Monday', 'Tuesday'],
            'Shift': ['Morning', 'Night', 'Morning', 'Night']
        })
        
        errors = self.rule.validate(data)
        self.assertEqual(errors, [])

    def test_validate_consecutive_nights(self):
        data = pd.DataFrame({
            'EmployeeID': [101, 101],
            'Name': ['John Doe', 'John Doe'],
            'Day': ['Monday', 'Tuesday'],
            'Shift': ['Night', 'Night']
        })

        errors = self.rule.validate(data)
        self.assertEqual(len(errors), 1)
        self.assertIn("Worked the night shift on consecutive days.", errors[0])

if __name__ == '__main__':
    unittest.main()
