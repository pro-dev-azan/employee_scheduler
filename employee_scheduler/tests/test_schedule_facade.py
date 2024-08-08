import unittest
import pandas as pd
from facade import ScheduleFacade

class TestScheduleFacade(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'EmployeeID': [101, 101, 102],
            'Name': ['John Doe', 'John Doe', 'Jane Smith'],
            'Day': ['Monday', 'Tuesday', 'Monday'],
            'Shift': ['Morning', 'Night', 'Morning']
        })
        self.facade = ScheduleFacade('')

    def test_load_data(self):
        self.facade.schedule_data = self.data
        self.assertIsNotNone(self.facade.schedule_data)

    def test_generate_report(self):
        errors = ["Sample error"]
        self.facade.generate_report(errors)
        with open('../validation_report.txt', 'r') as file:
            content = file.read()
            self.assertIn("Sample error", content)

if __name__ == '__main__':
    unittest.main()
