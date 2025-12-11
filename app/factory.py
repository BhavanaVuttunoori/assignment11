from abc import ABC, abstractmethod
from typing import Dict, Type

class Operation(ABC):
    """Abstract base class for calculation operations"""
    
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        """Perform the calculation and return the result"""
        pass
    
    @abstractmethod
    def get_operation_name(self) -> str:
        """Return the name of the operation"""
        pass

class AddOperation(Operation):
    """Addition operation"""
    
    def calculate(self, a: float, b: float) -> float:
        return a + b
    
    def get_operation_name(self) -> str:
        return "Add"

class SubtractOperation(Operation):
    """Subtraction operation"""
    
    def calculate(self, a: float, b: float) -> float:
        return a - b
    
    def get_operation_name(self) -> str:
        return "Subtract"

class MultiplyOperation(Operation):
    """Multiplication operation"""
    
    def calculate(self, a: float, b: float) -> float:
        return a * b
    
    def get_operation_name(self) -> str:
        return "Multiply"

class DivideOperation(Operation):
    """Division operation"""
    
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    def get_operation_name(self) -> str:
        return "Divide"

class CalculationFactory:
    """Factory class to create appropriate calculation operations"""
    
    # Registry of available operations
    _operations: Dict[str, Type[Operation]] = {
        "Add": AddOperation,
        "Subtract": SubtractOperation,
        "Multiply": MultiplyOperation,
        "Divide": DivideOperation,
    }
    
    @classmethod
    def create_operation(cls, operation_type: str) -> Operation:
        """
        Create and return an operation instance based on the type
        
        Args:
            operation_type: String representing the operation type
            
        Returns:
            An instance of the appropriate Operation subclass
            
        Raises:
            ValueError: If the operation type is not supported
        """
        operation_class = cls._operations.get(operation_type)
        
        if operation_class is None:
            available_operations = ", ".join(cls._operations.keys())
            raise ValueError(
                f"Unsupported operation type: {operation_type}. "
                f"Available operations: {available_operations}"
            )
        
        return operation_class()
    
    @classmethod
    def get_available_operations(cls) -> list:
        """Return a list of available operation types"""
        return list(cls._operations.keys())
    
    @classmethod
    def register_operation(cls, operation_name: str, operation_class: Type[Operation]):
        """
        Register a new operation type
        
        Args:
            operation_name: Name of the operation
            operation_class: Class implementing the Operation interface
        """
        if not issubclass(operation_class, Operation):
            raise TypeError(f"{operation_class} must be a subclass of Operation")
        cls._operations[operation_name] = operation_class

def perform_calculation(a: float, b: float, operation_type: str) -> float:
    """
    Convenience function to perform a calculation using the factory
    
    Args:
        a: First operand
        b: Second operand
        operation_type: Type of operation to perform
        
    Returns:
        Result of the calculation
    """
    operation = CalculationFactory.create_operation(operation_type)
    return operation.calculate(a, b)
