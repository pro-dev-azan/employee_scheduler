from rules.base_rule import ValidationRule

class Validator:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        if isinstance(rule, ValidationRule):
            self.rules.append(rule)

    def validate(self, data):
        all_errors = []
        for rule in self.rules:
            errors = rule.validate(data)
            all_errors.extend(errors)
        return all_errors
