import unittest
import pandas as pd
from rules.one_shift_per_day_rule import OneShiftPerDayRule


class TestOneShiftPerDayRule(unittest.TestCase):
    def setUp(self):
        self.rule = OneShiftPerDayRule()

    def test_validate_single_shift_per_day(self):
        data = pd.DataFrame(
            {
                "EmployeeID": [101, 102, 103],
                "Name": ["John Doe", "Jane Smith", "Michael Johnson"],
                "Day": ["Monday", "Monday", "Tuesday"],
                "Shift": ["Morning", "Afternoon", "Night"],
            }
        )

        errors = self.rule.validate(data)
        self.assertEqual(errors, [])

    def test_validate_multiple_shifts_per_day(self):
        data = pd.DataFrame(
            {
                "EmployeeID": [101, 101, 102],
                "Name": ["John Doe", "John Doe", "Jane Smith"],
                "Day": ["Monday", "Monday", "Tuesday"],
                "Shift": ["Morning", "Afternoon", "Morning"],
            }
        )
        errors = self.rule.validate(data)

        self.assertEqual(len(errors), 1)
        self.assertIn("Worked more than one shift on Monday.", errors[0])


if __name__ == "__main__":
    unittest.main()
