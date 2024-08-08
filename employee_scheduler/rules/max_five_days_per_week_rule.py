from .base_rule import ValidationRule

class MaxFiveDaysPerWeekRule(ValidationRule):
    def validate(self, data):
        errors = []
        days_worked_per_week = data.groupby('EmployeeID')['Day'].nunique()
        for emp_id, days_count in days_worked_per_week.items():
            if days_count > 5:
                name = data[data['EmployeeID'] == emp_id]['Name'].iloc[0]
                errors.append(f"EmployeeID: {emp_id}, Name: {name} - Worked more than 5 days in the week.")
        return errors
