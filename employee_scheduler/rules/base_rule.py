from abc import ABC, abstractmethod

class ValidationRule(ABC):
    @abstractmethod
    def validate(self, data):
        pass
