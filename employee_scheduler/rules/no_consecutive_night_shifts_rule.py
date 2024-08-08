from .base_rule import ValidationRule


class NoConsecutiveNightShiftsRule(ValidationRule):
    def validate(self, data):
        errors = []
        day_order = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        day_mapping = {day: index for index, day in enumerate(day_order)}
        data["DayIndex"] = data["Day"].map(day_mapping)
        sorted_data = data.sort_values(by=["EmployeeID", "DayIndex"])
        night_shifts = sorted_data[sorted_data["Shift"] == "Night"]
        grouped = night_shifts.groupby("EmployeeID")

        for emp_id, group in grouped:
            group = group.sort_values(by="DayIndex")

            for i in range(len(group) - 1):
                if group.iloc[i]["DayIndex"] + 1 == group.iloc[i + 1]["DayIndex"]:
                    name = group.iloc[i]["Name"]
                    errors.append(
                        f"EmployeeID: {emp_id}, Name: {name} - Worked the night shift on consecutive days."
                    )
                    break

        return errors
