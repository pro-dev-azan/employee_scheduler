from abc import ABC, abstractmethod


class ValidationRule(ABC):
    """
    Abstract base class for all validation rules.
    
    ValidationRule class uses the `ABC` (Abstract Base Class) module to define a common interface for all validation rules.
    The `validate` method must be implemented by any subclass. This ensures that each specific rule will 
    follow a consistent interface and can be processed by the `Validator` without knowing the details of 
    each rule's implementation.
    """

    @abstractmethod
    def validate(self, data):
        pass
