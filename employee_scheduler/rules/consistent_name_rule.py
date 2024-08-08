from .base_rule import ValidationRule

class ConsistentNameRule(ValidationRule):
    def validate(self, data):
        errors = []
        inconsistent_names = data.groupby('EmployeeID')['Name'].nunique()
        for emp_id, name_count in inconsistent_names.items():
            if name_count > 1:
                errors.append(f"EmployeeID: {emp_id} - Inconsistent Name values detected.")
        return errors
