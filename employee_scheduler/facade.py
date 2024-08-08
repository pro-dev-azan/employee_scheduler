import pandas as pd
from validator import Validator
from rules.one_shift_per_day_rule import OneShiftPerDayRule

class ScheduleFacade:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.schedule_data = None
        self.validator = Validator()

    def load_data(self):
        try:
            self.schedule_data = pd.read_csv(self.csv_file)
            self.schedule_data['Day'] = self.schedule_data['Day'].str.capitalize()
            self.schedule_data['Shift'] = self.schedule_data['Shift'].str.capitalize()
        except FileNotFoundError:
            print(f"File {self.csv_file} not found.")
            raise
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def setup_validation(self):
        self.validator.add_rule(OneShiftPerDayRule())

    def run_validation(self):
        errors = self.validator.validate(self.schedule_data)
        self.generate_report(errors)

    def generate_report(self, errors):
        with open('../validation_report.txt', 'w') as report_file:
            if errors:
                for error in errors:
                    report_file.write(error + "\n")
            else:
                report_file.write("No validation errors found.\n")
