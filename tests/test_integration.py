import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models import User, Calculation

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    """Override database dependency for testing"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def test_db():
    """Create test database tables"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(test_db):
    """Create test client"""
    return TestClient(app)

class TestRootEndpoints:
    """Test root and health endpoints"""
    
    def test_read_root(self, client):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "endpoints" in data
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}

class TestUserEndpoints:
    """Test user CRUD endpoints"""
    
    def test_create_user(self, client):
        """Test creating a new user"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        response = client.post("/users", json=user_data)
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == "testuser"
        assert data["email"] == "test@example.com"
        assert "id" in data
        assert "hashed_password" not in data  # Password should not be returned
    
    def test_create_duplicate_user(self, client):
        """Test that creating duplicate user fails"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        # Create first user
        response1 = client.post("/users", json=user_data)
        assert response1.status_code == 201
        
        # Try to create duplicate
        response2 = client.post("/users", json=user_data)
        assert response2.status_code == 400
        assert "already registered" in response2.json()["detail"]
    
    def test_create_user_invalid_email(self, client):
        """Test creating user with invalid email"""
        user_data = {
            "username": "testuser",
            "email": "invalid-email",
            "password": "testpassword123"
        }
        response = client.post("/users", json=user_data)
        assert response.status_code == 422
    
    def test_list_users(self, client):
        """Test listing users"""
        # Create some users
        users = [
            {"username": "user1", "email": "user1@test.com", "password": "pass123456"},
            {"username": "user2", "email": "user2@test.com", "password": "pass123456"}
        ]
        for user in users:
            client.post("/users", json=user)
        
        # List users
        response = client.get("/users")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
    
    def test_get_user(self, client):
        """Test getting a specific user"""
        # Create user
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        create_response = client.post("/users", json=user_data)
        user_id = create_response.json()["id"]
        
        # Get user
        response = client.get(f"/users/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == user_id
        assert data["username"] == "testuser"
    
    def test_get_nonexistent_user(self, client):
        """Test getting non-existent user"""
        response = client.get("/users/9999")
        assert response.status_code == 404

class TestCalculationEndpoints:
    """Test calculation CRUD endpoints"""
    
    def test_create_calculation_add(self, client):
        """Test creating addition calculation"""
        calc_data = {
            "a": 10,
            "b": 5,
            "type": "Add"
        }
        response = client.post("/calculations", json=calc_data)
        assert response.status_code == 201
        data = response.json()
        assert data["a"] == 10
        assert data["b"] == 5
        assert data["type"] == "Add"
        assert data["result"] == 15
        assert "id" in data
    
    def test_create_calculation_subtract(self, client):
        """Test creating subtraction calculation"""
        calc_data = {
            "a": 10,
            "b": 5,
            "type": "Subtract"
        }
        response = client.post("/calculations", json=calc_data)
        assert response.status_code == 201
        data = response.json()
        assert data["result"] == 5
    
    def test_create_calculation_multiply(self, client):
        """Test creating multiplication calculation"""
        calc_data = {
            "a": 10,
            "b": 5,
            "type": "Multiply"
        }
        response = client.post("/calculations", json=calc_data)
        assert response.status_code == 201
        data = response.json()
        assert data["result"] == 50
    
    def test_create_calculation_divide(self, client):
        """Test creating division calculation"""
        calc_data = {
            "a": 10,
            "b": 5,
            "type": "Divide"
        }
        response = client.post("/calculations", json=calc_data)
        assert response.status_code == 201
        data = response.json()
        assert data["result"] == 2
    
    def test_create_calculation_divide_by_zero(self, client):
        """Test that division by zero is rejected"""
        calc_data = {
            "a": 10,
            "b": 0,
            "type": "Divide"
        }
        response = client.post("/calculations", json=calc_data)
        assert response.status_code == 422
    
    def test_create_calculation_invalid_type(self, client):
        """Test creating calculation with invalid type"""
        calc_data = {
            "a": 10,
            "b": 5,
            "type": "InvalidType"
        }
        response = client.post("/calculations", json=calc_data)
        assert response.status_code == 422
    
    def test_create_calculation_with_user(self, client):
        """Test creating calculation with user association"""
        # Create user first
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        user_response = client.post("/users", json=user_data)
        user_id = user_response.json()["id"]
        
        # Create calculation
        calc_data = {
            "a": 10,
            "b": 5,
            "type": "Add",
            "user_id": user_id
        }
        response = client.post("/calculations", json=calc_data)
        assert response.status_code == 201
        data = response.json()
        assert data["user_id"] == user_id
    
    def test_create_calculation_invalid_user(self, client):
        """Test creating calculation with non-existent user"""
        calc_data = {
            "a": 10,
            "b": 5,
            "type": "Add",
            "user_id": 9999
        }
        response = client.post("/calculations", json=calc_data)
        assert response.status_code == 404
    
    def test_list_calculations(self, client):
        """Test listing calculations"""
        # Create some calculations
        calcs = [
            {"a": 10, "b": 5, "type": "Add"},
            {"a": 20, "b": 10, "type": "Subtract"}
        ]
        for calc in calcs:
            client.post("/calculations", json=calc)
        
        # List calculations
        response = client.get("/calculations")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
    
    def test_list_calculations_by_user(self, client):
        """Test listing calculations filtered by user"""
        # Create user
        user_response = client.post("/users", json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass123"
        })
        user_id = user_response.json()["id"]
        
        # Create calculations
        client.post("/calculations", json={"a": 10, "b": 5, "type": "Add", "user_id": user_id})
        client.post("/calculations", json={"a": 20, "b": 10, "type": "Add"})
        
        # List by user
        response = client.get(f"/calculations?user_id={user_id}")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["user_id"] == user_id
    
    def test_get_calculation(self, client):
        """Test getting a specific calculation"""
        # Create calculation
        calc_data = {"a": 10, "b": 5, "type": "Add"}
        create_response = client.post("/calculations", json=calc_data)
        calc_id = create_response.json()["id"]
        
        # Get calculation
        response = client.get(f"/calculations/{calc_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == calc_id
        assert data["result"] == 15
    
    def test_get_nonexistent_calculation(self, client):
        """Test getting non-existent calculation"""
        response = client.get("/calculations/9999")
        assert response.status_code == 404
    
    def test_update_calculation(self, client):
        """Test updating a calculation"""
        # Create calculation
        calc_data = {"a": 10, "b": 5, "type": "Add"}
        create_response = client.post("/calculations", json=calc_data)
        calc_id = create_response.json()["id"]
        
        # Update calculation
        update_data = {"a": 20}
        response = client.put(f"/calculations/{calc_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["a"] == 20
        assert data["result"] == 25  # 20 + 5
    
    def test_update_calculation_type(self, client):
        """Test updating calculation type"""
        # Create calculation
        calc_data = {"a": 10, "b": 5, "type": "Add"}
        create_response = client.post("/calculations", json=calc_data)
        calc_id = create_response.json()["id"]
        
        # Update type
        update_data = {"type": "Multiply"}
        response = client.put(f"/calculations/{calc_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["type"] == "Multiply"
        assert data["result"] == 50  # 10 * 5
    
    def test_delete_calculation(self, client):
        """Test deleting a calculation"""
        # Create calculation
        calc_data = {"a": 10, "b": 5, "type": "Add"}
        create_response = client.post("/calculations", json=calc_data)
        calc_id = create_response.json()["id"]
        
        # Delete calculation
        response = client.delete(f"/calculations/{calc_id}")
        assert response.status_code == 204
        
        # Verify deletion
        get_response = client.get(f"/calculations/{calc_id}")
        assert get_response.status_code == 404
    
    def test_delete_nonexistent_calculation(self, client):
        """Test deleting non-existent calculation"""
        response = client.delete("/calculations/9999")
        assert response.status_code == 404

class TestCalculationWithNegativeNumbers:
    """Test calculations with negative numbers"""
    
    def test_negative_addition(self, client):
        """Test addition with negative numbers"""
        response = client.post("/calculations", json={
            "a": -10,
            "b": 5,
            "type": "Add"
        })
        assert response.status_code == 201
        assert response.json()["result"] == -5
    
    def test_negative_multiplication(self, client):
        """Test multiplication with negative numbers"""
        response = client.post("/calculations", json={
            "a": -10,
            "b": 5,
            "type": "Multiply"
        })
        assert response.status_code == 201
        assert response.json()["result"] == -50

class TestCalculationWithFloats:
    """Test calculations with floating point numbers"""
    
    def test_float_addition(self, client):
        """Test addition with floats"""
        response = client.post("/calculations", json={
            "a": 10.5,
            "b": 5.3,
            "type": "Add"
        })
        assert response.status_code == 201
        assert abs(response.json()["result"] - 15.8) < 0.01
    
    def test_float_division(self, client):
        """Test division with floats"""
        response = client.post("/calculations", json={
            "a": 7.5,
            "b": 2.5,
            "type": "Divide"
        })
        assert response.status_code == 201
        assert response.json()["result"] == 3.0
