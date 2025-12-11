from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum

class CalculationType(str, Enum):
    """Enumeration for calculation types"""
    ADD = "Add"
    SUBTRACT = "Subtract"
    MULTIPLY = "Multiply"
    DIVIDE = "Divide"

class CalculationCreate(BaseModel):
    """Schema for creating a new calculation"""
    a: float = Field(..., description="First operand")
    b: float = Field(..., description="Second operand")
    type: CalculationType = Field(..., description="Type of calculation: Add, Subtract, Multiply, or Divide")
    user_id: Optional[int] = Field(None, description="Optional user ID")

    @model_validator(mode='after')
    def validate_division_by_zero(self):
        """Ensure divisor is not zero for division operations"""
        if self.type == CalculationType.DIVIDE and self.b == 0:
            raise ValueError('Division by zero is not allowed')
        return self

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "a": 10.5,
                "b": 5.2,
                "type": "Add",
                "user_id": 1
            }
        }

class CalculationRead(BaseModel):
    """Schema for reading calculation data"""
    id: int
    a: float
    b: float
    type: str
    result: Optional[float] = None
    created_at: datetime
    user_id: Optional[int] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "a": 10.5,
                "b": 5.2,
                "type": "Add",
                "result": 15.7,
                "created_at": "2023-11-24T10:30:00",
                "user_id": 1
            }
        }

class CalculationUpdate(BaseModel):
    """Schema for updating a calculation"""
    a: Optional[float] = None
    b: Optional[float] = None
    type: Optional[CalculationType] = None

    class Config:
        use_enum_values = True

class UserCreate(BaseModel):
    """Schema for creating a new user"""
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    password: str = Field(..., min_length=6)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john@example.com",
                "password": "securepassword123"
            }
        }

class UserRead(BaseModel):
    """Schema for reading user data"""
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "john@example.com",
                "created_at": "2023-11-24T10:30:00"
            }
        }
