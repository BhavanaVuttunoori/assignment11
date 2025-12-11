# Quick Reference Card

## 🚀 Quick Start Commands

### Setup
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Copy environment file
Copy-Item .env.example .env
```

### Run Application
```powershell
# Local development
uvicorn app.main:app --reload

# Using helper script
.\start_app.ps1

# With Docker
docker-compose up -d
```

### Run Tests
```powershell
# All tests
pytest tests/ -v

# With coverage
pytest tests/ -v --cov=app --cov-report=html

# Using helper script
.\run_tests.ps1

# Specific test file
pytest tests/test_factory.py -v
```

---

## 🌐 URLs

| Service | URL |
|---------|-----|
| API Root | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| Health Check | http://localhost:8000/health |

---

## 📋 API Endpoints Quick Reference

### Calculations
```http
POST   /calculations          # Create calculation
GET    /calculations          # List all calculations
GET    /calculations/{id}     # Get specific calculation
PUT    /calculations/{id}     # Update calculation
DELETE /calculations/{id}     # Delete calculation
```

### Users
```http
POST   /users                 # Create user
GET    /users                 # List all users
GET    /users/{id}            # Get specific user
```

---

## 💻 Example API Requests

### Create Calculation
```json
POST /calculations
{
  "a": 10,
  "b": 5,
  "type": "Add",
  "user_id": 1
}
```

### Create User
```json
POST /users
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepass123"
}
```

---

## 🏭 Factory Pattern Operations

| Operation | Class | Example |
|-----------|-------|---------|
| Add | `AddOperation` | 10 + 5 = 15 |
| Subtract | `SubtractOperation` | 10 - 5 = 5 |
| Multiply | `MultiplyOperation` | 10 × 5 = 50 |
| Divide | `DivideOperation` | 10 ÷ 5 = 2 |

---

## 🐳 Docker Commands

### Docker Compose
```powershell
docker-compose up -d          # Start services
docker-compose down           # Stop services
docker-compose logs -f        # View logs
docker-compose ps             # List services
docker-compose restart app    # Restart app
```

### Docker
```powershell
docker build -t calc-api .    # Build image
docker run -p 8000:8000 calc-api  # Run container
docker ps                     # List containers
docker logs <container_id>    # View logs
docker stop <container_id>    # Stop container
```

---

## 🧪 Test Commands

```powershell
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_factory.py -v
pytest tests/test_schemas.py -v
pytest tests/test_integration.py -v

# Run with coverage
pytest tests/ --cov=app --cov-report=term-missing

# Run specific test function
pytest tests/test_factory.py::TestOperations::test_add_operation -v

# Run tests matching pattern
pytest tests/ -k "add" -v
```

---

## 📊 Project Structure

```
app/
├── main.py          # FastAPI application
├── database.py      # Database configuration
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
└── factory.py       # Factory pattern

tests/
├── test_factory.py      # Factory tests
├── test_schemas.py      # Schema tests
└── test_integration.py  # API tests
```

---

## 🔧 Troubleshooting

### Database Connection Error
```powershell
# Check PostgreSQL service
Get-Service postgresql*
Start-Service postgresql-x64-15
```

### Module Not Found
```powershell
# Reinstall dependencies
pip install -r requirements.txt
```

### Port Already in Use
```powershell
# Find process using port 8000
netstat -ano | findstr :8000
# Kill process (replace PID)
taskkill /PID <PID> /F
```

### Docker Issues
```powershell
# Rebuild without cache
docker-compose build --no-cache
# Remove all containers and volumes
docker-compose down -v
```

---

## 📝 Common Git Commands

```powershell
# Initialize repository
git init
git add .
git commit -m "Initial commit"

# Add remote
git remote add origin <url>
git push -u origin main

# Check status
git status
git log --oneline

# Create branch
git checkout -b feature/new-feature

# Pull latest changes
git pull origin main
```

---

## 🔐 Environment Variables

Required in `.env` file:
```env
DATABASE_URL=postgresql://user:pass@localhost:5432/calc_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📦 GitHub Secrets Required

For CI/CD pipeline:
- `DOCKER_USERNAME` - Docker Hub username
- `DOCKER_PASSWORD` - Docker Hub access token

---

## 🎯 Testing Checklist

- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] Coverage > 90%
- [ ] No errors in logs
- [ ] API endpoints respond correctly
- [ ] Database migrations work
- [ ] Docker containers start successfully

---

## 📚 Useful Links

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Pytest Docs](https://docs.pytest.org/)
- [Docker Docs](https://docs.docker.com/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

---

## 💡 Pro Tips

1. **Use helper scripts**: `start_app.ps1` and `run_tests.ps1`
2. **Check health endpoint**: `/health` for quick status
3. **Use Swagger UI**: `/docs` for interactive testing
4. **View logs**: `docker-compose logs -f` for debugging
5. **Test incrementally**: Run tests after each change
6. **Use virtual env**: Always activate before working

---

## 🎓 Key Concepts

- **Factory Pattern**: Creates objects without specifying exact class
- **ORM**: Object-Relational Mapping with SQLAlchemy
- **Validation**: Input checking with Pydantic
- **Testing**: Unit tests (isolated) + Integration tests (full system)
- **CI/CD**: Automated testing and deployment
- **Containerization**: Consistent environments with Docker

---

**Print this card for quick reference while working! 📋**
