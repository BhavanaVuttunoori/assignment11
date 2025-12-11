from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db, init_db
from app.models import Calculation, User
from app.schemas import (
    CalculationCreate, 
    CalculationRead, 
    CalculationUpdate,
    UserCreate,
    UserRead
)
from app.factory import perform_calculation
from passlib.context import CryptContext

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI(
    title="Calculation API",
    description="API for performing and storing calculations with Factory Pattern",
    version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    """Initialize database on startup"""
    init_db()

@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to Calculation API",
        "version": "1.0.0",
        "endpoints": {
            "calculations": "/calculations",
            "users": "/users",
            "docs": "/docs"
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# User endpoints
@app.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    # Check if user already exists
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )
    
    # Hash password
    hashed_password = pwd_context.hash(user.password)
    
    # Create new user
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@app.get("/users", response_model=List[UserRead])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all users"""
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get a specific user by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user

# Calculation endpoints
@app.post("/calculations", response_model=CalculationRead, status_code=status.HTTP_201_CREATED)
def create_calculation(calculation: CalculationCreate, db: Session = Depends(get_db)):
    """
    Create a new calculation
    
    Accepts operands a and b, and a calculation type (Add, Subtract, Multiply, Divide).
    Uses the Factory Pattern to perform the calculation and stores the result.
    """
    # Validate user_id if provided
    if calculation.user_id:
        user = db.query(User).filter(User.id == calculation.user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {calculation.user_id} not found"
            )
    
    try:
        # Use factory pattern to perform calculation
        result = perform_calculation(calculation.a, calculation.b, calculation.type)
        
        # Create calculation record
        db_calculation = Calculation(
            a=calculation.a,
            b=calculation.b,
            type=calculation.type,
            result=result,
            user_id=calculation.user_id
        )
        
        db.add(db_calculation)
        db.commit()
        db.refresh(db_calculation)
        
        return db_calculation
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/calculations", response_model=List[CalculationRead])
def list_calculations(
    skip: int = 0, 
    limit: int = 100, 
    user_id: int = None,
    db: Session = Depends(get_db)
):
    """List all calculations, optionally filtered by user_id"""
    query = db.query(Calculation)
    
    if user_id:
        query = query.filter(Calculation.user_id == user_id)
    
    calculations = query.offset(skip).limit(limit).all()
    return calculations

@app.get("/calculations/{calculation_id}", response_model=CalculationRead)
def get_calculation(calculation_id: int, db: Session = Depends(get_db)):
    """Get a specific calculation by ID"""
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()
    
    if not calculation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Calculation not found"
        )
    
    return calculation

@app.put("/calculations/{calculation_id}", response_model=CalculationRead)
def update_calculation(
    calculation_id: int,
    calculation_update: CalculationUpdate,
    db: Session = Depends(get_db)
):
    """Update a calculation and recalculate result"""
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()
    
    if not calculation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Calculation not found"
        )
    
    # Update fields if provided
    if calculation_update.a is not None:
        calculation.a = calculation_update.a
    if calculation_update.b is not None:
        calculation.b = calculation_update.b
    if calculation_update.type is not None:
        calculation.type = calculation_update.type
    
    try:
        # Recalculate result
        calculation.result = perform_calculation(calculation.a, calculation.b, calculation.type)
        
        db.commit()
        db.refresh(calculation)
        
        return calculation
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.delete("/calculations/{calculation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_calculation(calculation_id: int, db: Session = Depends(get_db)):
    """Delete a calculation"""
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()
    
    if not calculation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Calculation not found"
        )
    
    db.delete(calculation)
    db.commit()
    
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
