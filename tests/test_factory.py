import pytest
from app.factory import (
    CalculationFactory,
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    perform_calculation,
    Operation
)

class TestOperations:
    """Test individual operation classes"""
    
    def test_add_operation(self):
        """Test addition operation"""
        op = AddOperation()
        assert op.calculate(5, 3) == 8
        assert op.calculate(-5, 3) == -2
        assert op.calculate(0, 0) == 0
        assert op.calculate(2.5, 3.5) == 6.0
        assert op.get_operation_name() == "Add"
    
    def test_subtract_operation(self):
        """Test subtraction operation"""
        op = SubtractOperation()
        assert op.calculate(5, 3) == 2
        assert op.calculate(-5, 3) == -8
        assert op.calculate(10, 10) == 0
        assert op.calculate(7.5, 2.5) == 5.0
        assert op.get_operation_name() == "Subtract"
    
    def test_multiply_operation(self):
        """Test multiplication operation"""
        op = MultiplyOperation()
        assert op.calculate(5, 3) == 15
        assert op.calculate(-5, 3) == -15
        assert op.calculate(0, 100) == 0
        assert op.calculate(2.5, 4) == 10.0
        assert op.get_operation_name() == "Multiply"
    
    def test_divide_operation(self):
        """Test division operation"""
        op = DivideOperation()
        assert op.calculate(10, 2) == 5
        assert op.calculate(-10, 2) == -5
        assert op.calculate(7, 2) == 3.5
        assert op.get_operation_name() == "Divide"
    
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        op = DivideOperation()
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            op.calculate(10, 0)

class TestCalculationFactory:
    """Test the calculation factory"""
    
    def test_factory_creates_add_operation(self):
        """Test factory creates addition operation"""
        op = CalculationFactory.create_operation("Add")
        assert isinstance(op, AddOperation)
        assert op.calculate(5, 3) == 8
    
    def test_factory_creates_subtract_operation(self):
        """Test factory creates subtraction operation"""
        op = CalculationFactory.create_operation("Subtract")
        assert isinstance(op, SubtractOperation)
        assert op.calculate(5, 3) == 2
    
    def test_factory_creates_multiply_operation(self):
        """Test factory creates multiplication operation"""
        op = CalculationFactory.create_operation("Multiply")
        assert isinstance(op, MultiplyOperation)
        assert op.calculate(5, 3) == 15
    
    def test_factory_creates_divide_operation(self):
        """Test factory creates division operation"""
        op = CalculationFactory.create_operation("Divide")
        assert isinstance(op, DivideOperation)
        assert op.calculate(10, 2) == 5
    
    def test_factory_invalid_operation(self):
        """Test factory raises error for invalid operation"""
        with pytest.raises(ValueError, match="Unsupported operation type"):
            CalculationFactory.create_operation("Invalid")
    
    def test_factory_get_available_operations(self):
        """Test getting available operations"""
        operations = CalculationFactory.get_available_operations()
        assert "Add" in operations
        assert "Subtract" in operations
        assert "Multiply" in operations
        assert "Divide" in operations
        assert len(operations) == 4
    
    def test_factory_register_operation(self):
        """Test registering a new operation"""
        class PowerOperation(Operation):
            def calculate(self, a: float, b: float) -> float:
                return a ** b
            def get_operation_name(self) -> str:
                return "Power"
        
        CalculationFactory.register_operation("Power", PowerOperation)
        assert "Power" in CalculationFactory.get_available_operations()
        
        op = CalculationFactory.create_operation("Power")
        assert isinstance(op, PowerOperation)
        assert op.calculate(2, 3) == 8

class TestPerformCalculation:
    """Test the convenience function for performing calculations"""
    
    def test_perform_addition(self):
        """Test performing addition"""
        result = perform_calculation(10, 5, "Add")
        assert result == 15
    
    def test_perform_subtraction(self):
        """Test performing subtraction"""
        result = perform_calculation(10, 5, "Subtract")
        assert result == 5
    
    def test_perform_multiplication(self):
        """Test performing multiplication"""
        result = perform_calculation(10, 5, "Multiply")
        assert result == 50
    
    def test_perform_division(self):
        """Test performing division"""
        result = perform_calculation(10, 5, "Divide")
        assert result == 2
    
    def test_perform_division_by_zero(self):
        """Test division by zero raises error"""
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            perform_calculation(10, 0, "Divide")
    
    def test_perform_invalid_operation(self):
        """Test invalid operation raises error"""
        with pytest.raises(ValueError, match="Unsupported operation type"):
            perform_calculation(10, 5, "InvalidOp")
    
    def test_perform_with_negative_numbers(self):
        """Test calculations with negative numbers"""
        assert perform_calculation(-10, 5, "Add") == -5
        assert perform_calculation(-10, -5, "Add") == -15
        assert perform_calculation(-10, 5, "Subtract") == -15
        assert perform_calculation(-10, 5, "Multiply") == -50
        assert perform_calculation(-10, -5, "Divide") == 2
    
    def test_perform_with_floats(self):
        """Test calculations with floating point numbers"""
        assert perform_calculation(10.5, 5.5, "Add") == 16.0
        assert perform_calculation(10.5, 5.5, "Subtract") == 5.0
        assert perform_calculation(2.5, 4.0, "Multiply") == 10.0
        assert perform_calculation(7.5, 2.5, "Divide") == 3.0
