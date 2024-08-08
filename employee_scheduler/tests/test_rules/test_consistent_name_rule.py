import unittest
import pandas as pd
from rules.consistent_name_rule import ConsistentNameRule


class TestConsistentNameRule(unittest.TestCase):
    def setUp(self):
        self.rule = ConsistentNameRule()

    def test_validate_consistent_names(self):
        data = pd.DataFrame(
            {
                "EmployeeID": [101, 101, 102, 102],
                "Name": ["John Doe", "John Doe", "Jane Smith", "Jane Smith"],
                "Day": ["Monday", "Tuesday", "Monday", "Tuesday"],
                "Shift": ["Morning", "Morning", "Morning", "Morning"],
            }
        )

        errors = self.rule.validate(data)
        self.assertEqual(errors, [])

    def test_validate_inconsistent_names(self):
        data = pd.DataFrame(
            {
                "EmployeeID": [101, 101, 102],
                "Name": ["John Doe", "Jane Doe", "Jane Smith"],
                "Day": ["Monday", "Tuesday", "Monday"],
                "Shift": ["Morning", "Morning", "Morning"],
            }
        )

        errors = self.rule.validate(data)
        self.assertEqual(len(errors), 1)
        self.assertIn("EmployeeID: 101 - Inconsistent Name values detected.", errors[0])


if __name__ == "__main__":
    unittest.main()
