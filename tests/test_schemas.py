import pytest
from pydantic import ValidationError
from app.schemas import (
    CalculationCreate,
    CalculationRead,
    CalculationUpdate,
    CalculationType,
    UserCreate,
    UserRead
)
from datetime import datetime

class TestCalculationType:
    """Test calculation type enumeration"""
    
    def test_valid_calculation_types(self):
        """Test all valid calculation types"""
        assert CalculationType.ADD.value == "Add"
        assert CalculationType.SUBTRACT.value == "Subtract"
        assert CalculationType.MULTIPLY.value == "Multiply"
        assert CalculationType.DIVIDE.value == "Divide"

class TestCalculationCreate:
    """Test CalculationCreate schema"""
    
    def test_valid_calculation_create(self):
        """Test creating valid calculation"""
        calc = CalculationCreate(a=10.5, b=5.2, type=CalculationType.ADD)
        assert calc.a == 10.5
        assert calc.b == 5.2
        assert calc.type == "Add"
        assert calc.user_id is None
    
    def test_calculation_create_with_user_id(self):
        """Test creating calculation with user_id"""
        calc = CalculationCreate(a=10, b=5, type=CalculationType.MULTIPLY, user_id=1)
        assert calc.user_id == 1
    
    def test_calculation_create_all_types(self):
        """Test creating calculations with all operation types"""
        for calc_type in CalculationType:
            if calc_type != CalculationType.DIVIDE:
                calc = CalculationCreate(a=10, b=5, type=calc_type)
                assert calc.type == calc_type.value
    
    def test_division_by_zero_validation(self):
        """Test that division by zero is caught"""
        with pytest.raises(ValidationError, match="Division by zero is not allowed"):
            CalculationCreate(a=10, b=0, type=CalculationType.DIVIDE)
    
    def test_division_with_nonzero_divisor(self):
        """Test that division with non-zero divisor is valid"""
        calc = CalculationCreate(a=10, b=5, type=CalculationType.DIVIDE)
        assert calc.b == 5
    
    def test_invalid_calculation_type(self):
        """Test that invalid calculation type raises error"""
        with pytest.raises(ValidationError):
            CalculationCreate(a=10, b=5, type="InvalidType")
    
    def test_missing_required_fields(self):
        """Test that missing required fields raise error"""
        with pytest.raises(ValidationError):
            CalculationCreate(a=10)  # Missing b and type
        
        with pytest.raises(ValidationError):
            CalculationCreate(b=5, type=CalculationType.ADD)  # Missing a
    
    def test_negative_numbers(self):
        """Test calculations with negative numbers"""
        calc = CalculationCreate(a=-10, b=5, type=CalculationType.ADD)
        assert calc.a == -10
        assert calc.b == 5

class TestCalculationRead:
    """Test CalculationRead schema"""
    
    def test_calculation_read_from_dict(self):
        """Test creating CalculationRead from dictionary"""
        data = {
            "id": 1,
            "a": 10.5,
            "b": 5.2,
            "type": "Add",
            "result": 15.7,
            "created_at": datetime.utcnow(),
            "user_id": 1
        }
        calc = CalculationRead(**data)
        assert calc.id == 1
        assert calc.a == 10.5
        assert calc.b == 5.2
        assert calc.type == "Add"
        assert calc.result == 15.7
        assert calc.user_id == 1
    
    def test_calculation_read_without_user_id(self):
        """Test CalculationRead without user_id"""
        data = {
            "id": 1,
            "a": 10,
            "b": 5,
            "type": "Add",
            "result": 15,
            "created_at": datetime.utcnow()
        }
        calc = CalculationRead(**data)
        assert calc.user_id is None

class TestCalculationUpdate:
    """Test CalculationUpdate schema"""
    
    def test_update_single_field(self):
        """Test updating single field"""
        update = CalculationUpdate(a=20)
        assert update.a == 20
        assert update.b is None
        assert update.type is None
    
    def test_update_multiple_fields(self):
        """Test updating multiple fields"""
        update = CalculationUpdate(a=20, b=10, type=CalculationType.MULTIPLY)
        assert update.a == 20
        assert update.b == 10
        assert update.type == "Multiply"
    
    def test_update_with_no_fields(self):
        """Test creating update with no fields"""
        update = CalculationUpdate()
        assert update.a is None
        assert update.b is None
        assert update.type is None

class TestUserCreate:
    """Test UserCreate schema"""
    
    def test_valid_user_create(self):
        """Test creating valid user"""
        user = UserCreate(
            username="johndoe",
            email="john@example.com",
            password="securepass123"
        )
        assert user.username == "johndoe"
        assert user.email == "john@example.com"
        assert user.password == "securepass123"
    
    def test_username_too_short(self):
        """Test that short username raises error"""
        with pytest.raises(ValidationError):
            UserCreate(username="ab", email="test@test.com", password="password123")
    
    def test_invalid_email(self):
        """Test that invalid email raises error"""
        with pytest.raises(ValidationError):
            UserCreate(username="johndoe", email="invalid-email", password="password123")
    
    def test_password_too_short(self):
        """Test that short password raises error"""
        with pytest.raises(ValidationError):
            UserCreate(username="johndoe", email="john@test.com", password="12345")

class TestUserRead:
    """Test UserRead schema"""
    
    def test_user_read_from_dict(self):
        """Test creating UserRead from dictionary"""
        data = {
            "id": 1,
            "username": "johndoe",
            "email": "john@example.com",
            "created_at": datetime.utcnow()
        }
        user = UserRead(**data)
        assert user.id == 1
        assert user.username == "johndoe"
        assert user.email == "john@example.com"
        assert isinstance(user.created_at, datetime)
