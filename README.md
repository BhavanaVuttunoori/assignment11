# Calculation API - Module 11 Assignment

[![CI/CD Pipeline](https://github.com/yourusername/calculation-api/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/yourusername/calculation-api/actions/workflows/ci-cd.yml)

A RESTful API for performing and storing calculations using FastAPI, SQLAlchemy, and the Factory Pattern. This project demonstrates modern software development practices including automated testing, CI/CD pipelines, and containerization.

## 🚀 Features

- **SQLAlchemy ORM**: Database models for Users and Calculations
- **Pydantic Validation**: Robust input validation and serialization
- **Factory Pattern**: Extensible calculation operations (Add, Subtract, Multiply, Divide)
- **RESTful API**: Full CRUD operations for calculations and users
- **PostgreSQL Database**: Production-ready database with proper relationships
- **Comprehensive Testing**: Unit and integration tests with pytest
- **CI/CD Pipeline**: Automated testing and Docker deployment with GitHub Actions
- **Docker Support**: Containerized application with docker-compose
- **Security**: Password hashing with bcrypt

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [API Documentation](#api-documentation)
- [Factory Pattern Implementation](#factory-pattern-implementation)
- [Database Schema](#database-schema)
- [CI/CD Pipeline](#cicd-pipeline)
- [Docker Hub](#docker-hub)
- [Learning Outcomes](#learning-outcomes)

## 📁 Project Structure

```
calculation-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   └── factory.py           # Factory pattern implementation
├── tests/
│   ├── __init__.py
│   ├── test_factory.py      # Unit tests for factory pattern
│   ├── test_schemas.py      # Unit tests for Pydantic schemas
│   └── test_integration.py  # Integration tests with database
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # GitHub Actions workflow
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── .env.example
├── .gitignore
└── README.md
```

## 🔧 Requirements

- Python 3.11+
- PostgreSQL 15+
- Docker & Docker Compose (optional)
- Git

## 📦 Installation

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/calculation-api.git
cd calculation-api
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your database credentials
```

5. **Set up PostgreSQL database**
```bash
# Create database
createdb calculation_db

# Or using psql
psql -U postgres
CREATE DATABASE calculation_db;
```

### Docker Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/calculation-api.git
cd calculation-api
```

2. **Run with Docker Compose**
```bash
docker-compose up -d
```

The application will be available at `http://localhost:8000`

## 🚀 Running the Application

### Local Development

```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Using Docker

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down
```

### Access the API

- **API Base URL**: http://localhost:8000
- **Interactive Docs (Swagger)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc

## 🧪 Running Tests

### Run All Tests

```bash
# Using pytest
pytest tests/ -v

# With coverage report
pytest tests/ -v --cov=app --cov-report=term-missing --cov-report=html
```

### Run Specific Test Files

```bash
# Unit tests for factory pattern
pytest tests/test_factory.py -v

# Unit tests for schemas
pytest tests/test_schemas.py -v

# Integration tests
pytest tests/test_integration.py -v
```

### Run Tests with Docker

```bash
# Run tests in Docker container
docker-compose run --rm app pytest tests/ -v
```

### View Coverage Report

After running tests with coverage, open `htmlcov/index.html` in your browser:
```bash
# On Windows
start htmlcov/index.html

# On macOS
open htmlcov/index.html

# On Linux
xdg-open htmlcov/index.html
```

## 📚 API Documentation

### Calculation Endpoints

#### Create Calculation
```http
POST /calculations
Content-Type: application/json

{
  "a": 10.5,
  "b": 5.2,
  "type": "Add",
  "user_id": 1
}
```

**Supported Operations:**
- `Add` - Addition
- `Subtract` - Subtraction
- `Multiply` - Multiplication
- `Divide` - Division (validates against zero divisor)

#### List Calculations
```http
GET /calculations?skip=0&limit=100&user_id=1
```

#### Get Calculation
```http
GET /calculations/{calculation_id}
```

#### Update Calculation
```http
PUT /calculations/{calculation_id}
Content-Type: application/json

{
  "a": 20,
  "type": "Multiply"
}
```

#### Delete Calculation
```http
DELETE /calculations/{calculation_id}
```

### User Endpoints

#### Create User
```http
POST /users
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

#### List Users
```http
GET /users?skip=0&limit=100
```

#### Get User
```http
GET /users/{user_id}
```

## 🏭 Factory Pattern Implementation

The Factory Pattern is implemented to handle different calculation operations dynamically:

### Key Components

1. **Abstract Operation Class**: Defines the interface for all operations
2. **Concrete Operation Classes**: Implement specific calculations (Add, Subtract, Multiply, Divide)
3. **Factory Class**: Creates appropriate operation instances based on type
4. **Registry Pattern**: Allows dynamic registration of new operations

### Example Usage

```python
from app.factory import CalculationFactory, perform_calculation

# Using the factory
operation = CalculationFactory.create_operation("Add")
result = operation.calculate(10, 5)  # Returns 15

# Using the convenience function
result = perform_calculation(10, 5, "Multiply")  # Returns 50

# Register custom operation
class PowerOperation(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a ** b
    def get_operation_name(self) -> str:
        return "Power"

CalculationFactory.register_operation("Power", PowerOperation)
```

### Benefits

- **Extensibility**: Easy to add new operations without modifying existing code
- **Separation of Concerns**: Business logic separated from data access
- **Testability**: Each operation can be tested independently
- **Type Safety**: Ensures valid operation types at runtime

## 🗄️ Database Schema

### Users Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key, Auto Increment |
| username | String | Unique, Not Null, Indexed |
| email | String | Unique, Not Null, Indexed |
| hashed_password | String | Not Null |
| created_at | DateTime | Default: UTC Now |

### Calculations Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key, Auto Increment |
| a | Float | Not Null |
| b | Float | Not Null |
| type | String | Not Null (Add, Subtract, Multiply, Divide) |
| result | Float | Nullable |
| created_at | DateTime | Default: UTC Now |
| user_id | Integer | Foreign Key (users.id), Nullable |

### Relationships
- One-to-Many: User → Calculations
- A user can have multiple calculations
- A calculation can optionally belong to a user

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Test Stage**
   - Sets up Python 3.11 environment
   - Spins up PostgreSQL container
   - Installs dependencies with caching
   - Runs unit tests for factory and schemas
   - Runs integration tests against PostgreSQL
   - Generates coverage reports

2. **Build and Push Stage** (on main branch)
   - Builds Docker image
   - Tags with branch name, commit SHA, and latest
   - Pushes to Docker Hub
   - Uses build cache for optimization

3. **Security Scan Stage**
   - Runs Trivy vulnerability scanner
   - Uploads results to GitHub Security tab

### Required GitHub Secrets

Add these secrets to your repository settings:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub access token

### Viewing Pipeline Results

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. Select the latest workflow run
4. View detailed logs for each job

## 🐳 Docker Hub

### Pull the Image

```bash
docker pull bhavanav/assignment11:latest
```

### Run the Container

```bash
docker run -d \
  -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:password@host:5432/db \
  -e SECRET_KEY=your-secret-key \
  bhavanav/assignment11:latest
```

### Docker Hub Repository

**Link**: https://hub.docker.com/r/bhavanav/assignment11

## 📊 Learning Outcomes

This project demonstrates the following Course Learning Outcomes (CLOs):

### CLO3: Create Python applications with automated testing
- ✅ Comprehensive unit tests for factory pattern
- ✅ Schema validation tests with Pydantic
- ✅ Integration tests with database operations
- ✅ Test fixtures and mocking

### CLO4: Set up GitHub Actions for CI
- ✅ Automated testing on push and pull requests
- ✅ PostgreSQL service containers
- ✅ Automated Docker builds and deployment
- ✅ Artifact uploads (coverage reports)

### CLO9: Apply containerization techniques
- ✅ Multi-stage Dockerfile
- ✅ Docker Compose for local development
- ✅ Environment variable management
- ✅ Service orchestration with health checks

### CLO11: Integrate with SQL databases
- ✅ SQLAlchemy ORM models
- ✅ Foreign key relationships
- ✅ Database migrations support (via Alembic)
- ✅ Connection pooling and session management

### CLO12: Serialize/deserialize JSON with Pydantic
- ✅ Input validation schemas (CalculationCreate, UserCreate)
- ✅ Output serialization schemas (CalculationRead, UserRead)
- ✅ Custom validators for business logic
- ✅ Type safety with Python type hints

### CLO13: Implement secure authentication
- ✅ Password hashing with bcrypt
- ✅ Secure password storage
- ✅ Email validation with regex
- ✅ User authentication foundation

## 🎯 Testing Strategy

### Unit Tests (65 tests)

**Factory Tests** (`test_factory.py`)
- Individual operation classes (Add, Subtract, Multiply, Divide)
- Factory creation and operation selection
- Error handling (division by zero, invalid operations)
- Custom operation registration
- Edge cases (negative numbers, floats)

**Schema Tests** (`test_schemas.py`)
- Pydantic validation rules
- Division by zero validation
- Email and password validation
- Type enumeration
- Optional fields

### Integration Tests (35+ tests)

**API Endpoint Tests** (`test_integration.py`)
- CRUD operations for calculations
- CRUD operations for users
- User-calculation relationships
- Error handling and validation
- Database transactions
- Query filtering

## 🛠️ Development

### Code Quality

```bash
# Format code with black
black app/ tests/

# Lint with flake8
flake8 app/ tests/

# Type checking with mypy
mypy app/
```

### Database Migrations

```bash
# Initialize Alembic (if not done)
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Author

**Bhavana Vuttunoori**
- GitHub: [@BhavanaVuttunoori](https://github.com/BhavanaVuttunoori)
- Student ID: Module 11 Assignment

## 🙏 Acknowledgments

- FastAPI documentation
- SQLAlchemy ORM guide
- Pydantic validation documentation
- GitHub Actions community
- Course instructors and TAs

## 📞 Support

For questions or issues:
1. Check the [GitHub Issues](https://github.com/BhavanaVuttunoori/assignment11/issues)
2. Review the API documentation at `/docs`
3. Contact the repository maintainer

---

**Note**: This project was created as part of Module 11 assignment for demonstrating calculation model implementation with Factory Pattern, automated testing, and CI/CD pipelines.
