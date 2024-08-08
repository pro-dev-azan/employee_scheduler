import pandas as pd
from validator import Validator
from rules.one_shift_per_day_rule import OneShiftPerDayRule
from rules.max_five_days_per_week_rule import MaxFiveDaysPerWeekRule
from rules.no_consecutive_night_shifts_rule import NoConsecutiveNightShiftsRule
from rules.consistent_name_rule import ConsistentNameRule


class ScheduleFacade:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.schedule_data = None
        self.validator = Validator()

    def load_data(self):
        try:
            self.schedule_data = pd.read_csv(self.csv_file)
            self.schedule_data["Day"] = self.schedule_data["Day"].str.capitalize()
            self.schedule_data["Shift"] = self.schedule_data["Shift"].str.capitalize()
        except FileNotFoundError:
            print(f"File {self.csv_file} not found.")
            raise
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def setup_validation(self):
        self.validator.add_rule(OneShiftPerDayRule())
        self.validator.add_rule(MaxFiveDaysPerWeekRule())
        self.validator.add_rule(NoConsecutiveNightShiftsRule())
        self.validator.add_rule(ConsistentNameRule())

    def run_validation(self):
        errors = self.validator.validate(self.schedule_data)
        self.generate_report(errors)

    def generate_report(self, errors):
        error_summary = {}

        for error in errors:
            parts = error.split(" - ", 1)
            if len(parts) != 2:
                continue

            header, message = parts
            if ", Name: " in header:
                emp_id, name_part = header.split(", Name: ", 1)
                name = name_part.strip()
                emp_id = emp_id.strip()
            else:
                emp_id = header.strip()
                name = None

            if emp_id not in error_summary:
                error_summary[emp_id] = {"Name": name, "Messages": []}
            error_summary[emp_id]["Messages"].append(message)

        with open("../validation_report.txt", "w") as report_file:
            for emp_id, info in error_summary.items():
                name_str = f", Name: {info['Name']}" if info["Name"] else ""
                report_file.write(f"{emp_id}{name_str}\n")
                for message in info["Messages"]:
                    report_file.write(f" - {message}\n")
                report_file.write("\n")
