import unittest
import pandas as pd
from facade import ScheduleFacade


class TestScheduleFacade(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame(
            {
                "EmployeeID": [101, 101, 102],
                "Name": ["John Doe", "John Doe", "Jane Smith"],
                "Day": ["Monday", "Tuesday", "Monday"],
                "Shift": ["Morning", "Night", "Morning"],
            }
        )
        self.facade = ScheduleFacade("")

    def test_load_data(self):
        self.facade.schedule_data = self.data
        self.assertIsNotNone(self.facade.schedule_data)

    def test_generate_report(self):
        errors = [
            "EmployeeID: 101, Name: John Doe - Worked more than one shift on Monday.",
            "EmployeeID: 101, Name: John Doe - Worked more than 5 days in the week.",
            "EmployeeID: 102, Name: Jon Ali - Inconsistent Name values detected.",
        ]
        self.facade.generate_report(errors)

        with open("../validation_report.txt", "r") as file:
            content = file.read()

        expected_content = (
            "EmployeeID: 101, Name: John Doe\n"
            " - Worked more than one shift on Monday.\n"
            " - Worked more than 5 days in the week.\n\n"
            "EmployeeID: 102, Name: Jon Ali\n"
            " - Inconsistent Name values detected.\n\n"
        )

        self.assertEqual(content, expected_content)


if __name__ == "__main__":
    unittest.main()
