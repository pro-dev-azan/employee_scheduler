import unittest
import pandas as pd
from rules.max_five_days_per_week_rule import MaxFiveDaysPerWeekRule


class TestMaxFiveDaysPerWeekRule(unittest.TestCase):
    def setUp(self):
        self.rule = MaxFiveDaysPerWeekRule()

    def test_validate_within_limit(self):
        data = pd.DataFrame(
            {
                "EmployeeID": [101, 101, 102, 102, 102],
                "Name": [
                    "John Doe",
                    "John Doe",
                    "Jane Smith",
                    "Jane Smith",
                    "Jane Smith",
                ],
                "Day": ["Monday", "Tuesday", "Monday", "Tuesday", "Wednesday"],
                "Shift": ["Morning", "Morning", "Morning", "Morning", "Morning"],
            }
        )

        errors = self.rule.validate(data)
        self.assertEqual(errors, [])

    def test_validate_exceed_limit(self):
        data = pd.DataFrame(
            {
                "EmployeeID": [101, 101, 101, 101, 101, 101, 102],
                "Name": ["John Doe"] * 6 + ["Jane Smith"],
                "Day": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Sunday",
                    "Monday",
                ],
                "Shift": ["Morning"] * 6 + ["Afternoon"],
            }
        )

        errors = self.rule.validate(data)
        self.assertEqual(len(errors), 1)
        self.assertIn("Worked more than 5 days in the week.", errors[0])


if __name__ == "__main__":
    unittest.main()
