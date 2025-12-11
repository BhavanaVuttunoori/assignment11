# Calculation API - Module 11 Assignment

The Assignment 11 deliverable is a fully tested FastAPI calculation service with Factory Pattern implementation, packaged for local development, Docker usage, and CI/CD. This README documents how the project is structured, what was implemented, and how to reproduce the results.

## Project Highlights

Built with FastAPI and SQLAlchemy to expose calculation operations through REST endpoints with database persistence.
Factory Pattern implementation in app/factory.py with extensible operation registry for Add, Subtract, Multiply, and Divide operations.
Robust Pydantic validation in app/schemas.py with explicit error handling (division by zero, email format, password strength).
Comprehensive automated test suite covering unit and integration scenarios (100+ tests with pytest).
SQLAlchemy ORM models with proper relationships between Users and Calculations tables.
Continuous Integration via GitHub Actions to test with PostgreSQL, build Docker images, and run security scans.
Containerized delivery: public Docker image available at bhavanavuttunoori/calculation-api.

## Getting Started

### 1. Setup Environment

```bash
cd assignment11
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the Application Locally

```bash
uvicorn app.main:app --reload
```

Navigate to http://localhost:8000/docs for the Swagger UI or hit REST endpoints directly (e.g. POST http://localhost:8000/calculations).

## Docker Usage

### Build Locally (optional)

```bash
docker build -t calculation-api .
docker run -p 8000:8000 -e DATABASE_URL=sqlite:///./test.db -e SECRET_KEY=test-key calculation-api
```

### Pull Prebuilt Image

```bash
docker pull bhavanavuttunoori/calculation-api:latest
docker run -p 8000:8000 -e DATABASE_URL=sqlite:///./test.db -e SECRET_KEY=test-key bhavanavuttunoori/calculation-api:latest
```

### Using Docker Compose

```bash
docker-compose up -d
```

The application will be available at http://localhost:8000 with PostgreSQL database.

## Testing Strategy

Unit Tests (tests/test_factory.py): verify factory pattern operations and extensibility.
Unit Tests (tests/test_schemas.py): verify Pydantic validation rules and error handling.
Integration Tests (tests/test_integration.py): exercise each API route through FastAPI's test client with database operations.

Run the full suite:

```bash
pytest tests/ -v
```

Run with coverage:

```bash
pytest tests/ --cov=app --cov-report=term-missing --cov-report=html
```

View coverage report:

```bash
start htmlcov/index.html  # Windows
```

## Project Structure

```
assignment11/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application with all endpoints
│   ├── database.py          # Database configuration and session management
│   ├── models.py            # SQLAlchemy ORM models (User, Calculation)
│   ├── schemas.py           # Pydantic validation schemas
│   └── factory.py           # Factory pattern implementation
├── tests/
│   ├── __init__.py
│   ├── test_factory.py      # Unit tests for factory operations
│   ├── test_schemas.py      # Unit tests for Pydantic schemas
│   └── test_integration.py  # Integration tests with database
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # GitHub Actions CI/CD pipeline
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── .env.example
└── README.md
```

## API Endpoints

### Calculation Operations

Create Calculation:
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

List Calculations:
```http
GET /calculations?skip=0&limit=100&user_id=1
```

Get Calculation:
```http
GET /calculations/{calculation_id}
```

Update Calculation:
```http
PUT /calculations/{calculation_id}
Content-Type: application/json

{
  "a": 20,
  "type": "Multiply"
}
```

Delete Calculation:
```http
DELETE /calculations/{calculation_id}
```

### User Operations

Create User:
```http
POST /users
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

List Users:
```http
GET /users?skip=0&limit=100
```

Get User:
```http
GET /users/{user_id}
```

## Factory Pattern Implementation

The Factory Pattern in app/factory.py provides extensible calculation operations:

Abstract Operation class defines the interface for all operations.
Concrete operation classes (AddOperation, SubtractOperation, MultiplyOperation, DivideOperation) implement specific calculations.
CalculationFactory uses a registry pattern to create appropriate operation instances.
Easy to extend by registering new operations without modifying existing code.

Example usage:

```python
from app.factory import CalculationFactory, perform_calculation

# Using the factory
operation = CalculationFactory.create_operation("Add")
result = operation.calculate(10, 5)  # Returns 15

# Using the convenience function
result = perform_calculation(10, 5, "Multiply")  # Returns 50
```

## Database Schema

Users Table:
- id (Integer, Primary Key)
- username (String, Unique, Indexed)
- email (String, Unique, Indexed)
- hashed_password (String)
- created_at (DateTime)

Calculations Table:
- id (Integer, Primary Key)
- a (Float)
- b (Float)
- type (String: Add, Subtract, Multiply, Divide)
- result (Float)
- created_at (DateTime)
- user_id (Integer, Foreign Key to users.id)

Relationship: One User can have many Calculations.

## Continuous Integration

The repository includes a GitHub Actions workflow (.github/workflows/ci-cd.yml) that runs on every push:

Test Job:
- Set up Python 3.11
- Start PostgreSQL 15 service container
- Install dependencies with caching
- Run unit tests (test_factory.py, test_schemas.py)
- Run integration tests with PostgreSQL (test_integration.py)
- Generate and upload coverage reports

Build and Push Job (main branch only):
- Build Docker image
- Tag with branch name, commit SHA, and latest
- Push to Docker Hub (bhavanavuttunoori/calculation-api)

Security Scan Job:
- Run Trivy vulnerability scanner
- Upload results to GitHub Security tab

### Required GitHub Secrets

DOCKER_USERNAME: Your Docker Hub username
DOCKER_PASSWORD: Your Docker Hub access token

## Assignment Instructions & Deliverables

Objective: Implement and test a Calculation Model with Factory Pattern, including SQLAlchemy models, Pydantic schemas, comprehensive tests, and CI/CD pipeline.

### Implementation Checklist

SQLAlchemy models for User and Calculation with proper relationships.
Pydantic schemas with validation (division by zero, email format, password strength).
Factory Pattern with extensible operation registry.
100+ comprehensive tests covering unit and integration scenarios.
FastAPI application with full CRUD operations.
GitHub Actions workflow with PostgreSQL integration.
Docker containerization with docker-compose support.
Comprehensive documentation.

### Submission Package

GitHub repository: https://github.com/BhavanaVuttunoori/assignment11
Docker Hub image: https://hub.docker.com/r/bhavanavuttunoori/calculation-api
Screenshots demonstrating:
- Successful GitHub Actions workflow
- Docker Hub deployment
- Test coverage report
- API documentation (Swagger UI)

### Grading Guidelines

Criterion: SQLAlchemy Models
- User and Calculation models with proper fields and relationships
- Foreign key constraints and indexes

Criterion: Pydantic Schemas
- Input validation schemas (CalculationCreate, UserCreate)
- Output serialization schemas (CalculationRead, UserRead)
- Custom validators for business logic

Criterion: Factory Pattern
- Abstract Operation base class
- Concrete operation implementations
- Factory with registry pattern
- Extensibility demonstration

Criterion: Testing
- 100+ unit and integration tests
- Factory pattern tests
- Schema validation tests
- API endpoint tests with database
- 90%+ code coverage

Criterion: CI/CD Pipeline
- GitHub Actions workflow configuration
- PostgreSQL service container integration
- Docker build and push automation
- Security scanning

Criterion: Documentation
- Comprehensive README with setup instructions
- API documentation via Swagger
- Code comments and docstrings
- Reflection document

## Helpful Commands

| Task | Command |
|------|---------|
| Install dependencies | pip install -r requirements.txt |
| Run application | uvicorn app.main:app --reload |
| Run all tests | pytest tests/ -v |
| Run tests with coverage | pytest tests/ --cov=app --cov-report=html |
| Run unit tests only | pytest tests/test_factory.py tests/test_schemas.py -v |
| Run integration tests only | pytest tests/test_integration.py -v |
| Build Docker image | docker build -t calculation-api . |
| Run with Docker Compose | docker-compose up -d |
| Stop Docker Compose | docker-compose down |
| View container logs | docker logs -f assignment11_app_1 |
| Format code | black app/ tests/ |
| Lint code | flake8 app/ tests/ |

## Submission Tips

Commit frequently with meaningful messages describing each feature.
Keep .env or secrets out of version control (use .gitignore).
Verify all tests pass locally before pushing.
Ensure GitHub Actions workflow completes successfully.
Capture required screenshots showing green checkmarks in Actions tab.
Verify Docker image is publicly accessible on Docker Hub.

## Learning Outcomes

CLO3: Create Python applications with automated testing
- Comprehensive unit tests for factory pattern and schemas
- Integration tests with database operations
- Test fixtures and mocking
- 100+ tests with 90%+ coverage

CLO4: Set up GitHub Actions for CI
- Automated testing on push and pull requests
- PostgreSQL service containers
- Automated Docker builds and deployment
- Coverage report uploads

CLO9: Apply containerization techniques
- Multi-stage Dockerfile for optimization
- Docker Compose for local development
- Environment variable management
- Service orchestration with health checks

CLO11: Integrate with SQL databases
- SQLAlchemy ORM models with relationships
- Foreign key constraints
- Database session management
- PostgreSQL in production, SQLite for testing

CLO12: Serialize/deserialize JSON with Pydantic
- Input validation schemas with custom validators
- Output serialization with from_attributes
- Type safety with Python type hints
- Enum-based type validation

CLO13: Implement secure authentication
- Password hashing with bcrypt
- Secure password storage
- Email validation with regex patterns
- User authentication foundation

## Author

Bhavana Vuttunoori
GitHub: https://github.com/BhavanaVuttunoori
Repository: https://github.com/BhavanaVuttunoori/assignment11

## Acknowledgments

FastAPI documentation and community examples.
SQLAlchemy ORM patterns and best practices.
Pydantic validation framework.
GitHub Actions workflow templates.
Course instructors for project guidance.

## Support

For questions or issues:
1. Check the GitHub Issues: https://github.com/BhavanaVuttunoori/assignment11/issues
2. Review the API documentation at http://localhost:8000/docs
3. Contact the repository maintainer

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Note: This project was created as part of Module 11 assignment for demonstrating calculation model implementation with Factory Pattern, automated testing, comprehensive validation, and CI/CD pipelines.
