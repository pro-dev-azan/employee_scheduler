import unittest
from validator import Validator
from rules.one_shift_per_day_rule import OneShiftPerDayRule
import pandas as pd

class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_add_rule(self):
        rule = OneShiftPerDayRule()
        self.validator.add_rule(rule)
        self.assertEqual(len(self.validator.rules), 1)

    def test_validate(self):
        rule = OneShiftPerDayRule()
        self.validator.add_rule(rule)

        mock_data = pd.DataFrame({
            'EmployeeID': [101, 101],
            'Name': ['John Doe', 'John Doe'],
            'Day': ['Monday', 'Monday'],
            'Shift': ['Morning', 'Afternoon']
        })
        errors = self.validator.validate(mock_data)

        self.assertIsInstance(errors, list)

if __name__ == '__main__':
    unittest.main()
