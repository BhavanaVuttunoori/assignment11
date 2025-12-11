# Quick Setup Guide

## Prerequisites
- Python 3.11+
- PostgreSQL 15+
- Git
- Docker & Docker Compose (optional)

## Option 1: Local Development Setup

### Step 1: Clone and Setup Virtual Environment
```powershell
# Clone the repository
git clone https://github.com/yourusername/calculation-api.git
cd calculation-api

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Setup PostgreSQL Database
```powershell
# Using psql (make sure PostgreSQL is running)
psql -U postgres

# In psql:
CREATE DATABASE calculation_db;
\q
```

### Step 3: Configure Environment
```powershell
# Copy example environment file
Copy-Item .env.example .env

# Edit .env with your settings
notepad .env
```

Update `.env`:
```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/calculation_db
SECRET_KEY=your-random-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Step 4: Run the Application
```powershell
# Run with uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 5: Access the API
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Option 2: Docker Setup (Recommended)

### Step 1: Clone Repository
```powershell
git clone https://github.com/yourusername/calculation-api.git
cd calculation-api
```

### Step 2: Run with Docker Compose
```powershell
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Access the API at http://localhost:8000
```

### Step 3: Stop Services
```powershell
docker-compose down
```

---

## Running Tests

### Local Testing
```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app --cov-report=html

# Run specific test file
pytest tests/test_factory.py -v
```

### Docker Testing
```powershell
# Run tests in Docker
docker-compose run --rm app pytest tests/ -v
```

---

## GitHub Actions Setup

### Step 1: Create GitHub Repository
```powershell
# Initialize git (if not cloned)
git init
git add .
git commit -m "Initial commit"

# Add remote and push
git remote add origin https://github.com/yourusername/calculation-api.git
git branch -M main
git push -u origin main
```

### Step 2: Add Docker Hub Secrets

1. Go to your repository on GitHub
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Add the following secrets:
   - Name: `DOCKER_USERNAME`, Value: Your Docker Hub username
   - Name: `DOCKER_PASSWORD`, Value: Your Docker Hub access token

### Step 3: Verify Pipeline

1. Push changes to trigger workflow
2. Go to Actions tab in your repository
3. Watch the pipeline execute
4. Check Docker Hub for the pushed image

---

## Docker Hub Setup

### Step 1: Create Docker Hub Account
- Visit https://hub.docker.com
- Sign up or log in

### Step 2: Create Access Token
1. Go to Account Settings → Security
2. Click "New Access Token"
3. Name it (e.g., "GitHub Actions")
4. Copy the token (you won't see it again!)
5. Use this token as `DOCKER_PASSWORD` in GitHub secrets

### Step 3: Verify Deployment
After successful pipeline run:
```powershell
# Pull your image
docker pull yourusername/calculation-api:latest

# Run it
docker run -d -p 8000:8000 yourusername/calculation-api:latest
```

---

## Troubleshooting

### Issue: PostgreSQL Connection Error
**Solution:**
```powershell
# Check if PostgreSQL is running
Get-Service postgresql*

# Start PostgreSQL service
Start-Service postgresql-x64-15
```

### Issue: Python Module Not Found
**Solution:**
```powershell
# Ensure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Docker Container Won't Start
**Solution:**
```powershell
# Check logs
docker-compose logs app

# Rebuild containers
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Issue: Tests Failing Locally
**Solution:**
```powershell
# Check Python version
python --version  # Should be 3.11+

# Reinstall test dependencies
pip install pytest pytest-asyncio httpx

# Run with verbose output
pytest tests/ -vv
```

### Issue: GitHub Actions Failing
**Solution:**
1. Check workflow logs in GitHub Actions tab
2. Verify secrets are correctly set
3. Ensure PostgreSQL service is healthy
4. Check for syntax errors in workflow file

---

## Common Commands

### Development
```powershell
# Start development server
uvicorn app.main:app --reload

# Format code
black app/ tests/

# Lint code
flake8 app/ tests/

# Type checking
mypy app/
```

### Testing
```powershell
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_factory.py -v

# With coverage
pytest tests/ --cov=app --cov-report=html

# Open coverage report
start htmlcov/index.html
```

### Docker
```powershell
# Build image
docker build -t calculation-api .

# Run container
docker run -d -p 8000:8000 calculation-api

# View logs
docker logs <container_id>

# Stop container
docker stop <container_id>

# Remove container
docker rm <container_id>
```

### Docker Compose
```powershell
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild services
docker-compose build

# Run command in container
docker-compose exec app python -c "print('Hello')"
```

---

## Next Steps

1. **Test the API**: Use Swagger UI at `/docs` to test endpoints
2. **Run Tests**: Execute pytest to verify everything works
3. **Customize**: Modify the code for your specific needs
4. **Deploy**: Push to GitHub to trigger CI/CD pipeline
5. **Monitor**: Check Docker Hub for successful image deployment

---

## Support

For issues or questions:
1. Check the main README.md
2. Review the REFLECTION.md for insights
3. Check GitHub Issues
4. Review API documentation at `/docs`

---

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
