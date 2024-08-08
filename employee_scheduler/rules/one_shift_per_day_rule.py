from .base_rule import ValidationRule


class OneShiftPerDayRule(ValidationRule):
    def validate(self, data):
        errors = []
        multiple_shifts_per_day = data.groupby(["EmployeeID", "Day"]).size()
        for (emp_id, day), count in multiple_shifts_per_day.items():
            if count > 1:
                name = data[data["EmployeeID"] == emp_id]["Name"].iloc[0]
                errors.append(
                    f"EmployeeID: {emp_id}, Name: {name} - Worked more than one shift on {day}."
                )
        return errors
