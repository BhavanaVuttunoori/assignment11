# 🚀 Getting Started - Quick Start Guide

## Welcome! Start Here 👋

This guide will get your Calculation API up and running in **under 10 minutes**.

---

## ⚡ Option 1: Docker (Fastest - Recommended)

### Prerequisites
- Docker Desktop installed
- Internet connection

### Steps

1. **Open PowerShell in project directory**
```powershell
cd "c:\Users\vuttunoori bhavana\Desktop\web api ass 11"
```

2. **Start everything**
```powershell
docker-compose up -d
```

3. **Verify it's running**
```powershell
docker-compose ps
# Both services should show "Up"
```

4. **Access the API**
- Open browser to: http://localhost:8000/docs
- You should see the Swagger UI

5. **Test an endpoint**
- In Swagger UI, expand `POST /calculations`
- Click "Try it out"
- Use this example:
```json
{
  "a": 10,
  "b": 5,
  "type": "Add"
}
```
- Click "Execute"
- You should get a 201 response with result: 15

**Done! ✅** Your API is running!

---

## ⚡ Option 2: Local Python (More Control)

### Prerequisites
- Python 3.11+
- PostgreSQL 15+

### Steps

1. **Open PowerShell in project directory**
```powershell
cd "c:\Users\vuttunoori bhavana\Desktop\web api ass 11"
```

2. **Run the helper script**
```powershell
.\start_app.ps1
```

This will:
- Create virtual environment
- Install dependencies
- Check for .env file
- Start the application

3. **Access the API**
- Open browser to: http://localhost:8000/docs

**Done! ✅** Your API is running!

---

## 🧪 Running Tests

### Quick Test

**Using helper script:**
```powershell
.\run_tests.ps1
```

**Manual:**
```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html
```

### Expected Results
- All tests pass (100+)
- Coverage > 90%
- No errors

---

## 🐛 Troubleshooting

### "Docker command not found"
**Solution**: Install Docker Desktop from https://www.docker.com/products/docker-desktop

### "PostgreSQL connection failed"
**Solution**: 
```powershell
# Check if PostgreSQL is running
Get-Service postgresql*

# Start if needed
Start-Service postgresql-x64-15
```

### "Module not found"
**Solution**:
```powershell
# Reinstall dependencies
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### "Port 8000 already in use"
**Solution**:
```powershell
# Find process
netstat -ano | findstr :8000

# Kill it (replace 1234 with actual PID)
taskkill /PID 1234 /F
```

---

## 📚 What to Do Next

### 1. Explore the API (5 minutes)
- Open http://localhost:8000/docs
- Try the different endpoints:
  - POST /calculations (create calculation)
  - GET /calculations (list all)
  - POST /users (create user)
  - GET /health (health check)

### 2. Read the Documentation (10 minutes)
- Start with `README.md` for full overview
- Check `QUICK_REFERENCE.md` for commands
- Review `REFLECTION.md` for insights

### 3. Review the Code (15 minutes)
- `app/factory.py` - See the Factory Pattern
- `app/schemas.py` - Check validation logic
- `app/models.py` - View database models
- `tests/test_factory.py` - Understand testing

### 4. Run Tests (5 minutes)
```powershell
.\run_tests.ps1
```

### 5. Prepare for Submission (30 minutes)
- Follow `SUBMISSION_CHECKLIST.md`
- Capture screenshots (see `SCREENSHOTS_GUIDE.md`)
- Set up GitHub repository
- Configure Docker Hub

---

## 🎯 Your First API Call

### Using Swagger UI (Easiest)
1. Go to http://localhost:8000/docs
2. Click on `POST /calculations`
3. Click "Try it out"
4. Enter:
```json
{
  "a": 15,
  "b": 3,
  "type": "Multiply"
}
```
5. Click "Execute"
6. See result: 45

### Using PowerShell
```powershell
$body = @{
    a = 15
    b = 3
    type = "Multiply"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/calculations" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"
```

### Using curl
```powershell
curl -X POST "http://localhost:8000/calculations" `
    -H "Content-Type: application/json" `
    -d '{"a":15,"b":3,"type":"Multiply"}'
```

---

## 📊 Understanding the Project

### Architecture
```
User Request
    ↓
FastAPI (app/main.py)
    ↓
Pydantic Validation (app/schemas.py)
    ↓
Factory Pattern (app/factory.py)
    ↓
SQLAlchemy Models (app/models.py)
    ↓
PostgreSQL Database
```

### Key Files to Know
- **app/main.py**: All API endpoints
- **app/factory.py**: Factory Pattern implementation
- **app/schemas.py**: Input/output validation
- **app/models.py**: Database tables
- **tests/**: All tests

---

## 🎓 Learning Path

### Day 1: Understanding
- [ ] Read README.md
- [ ] Run the application
- [ ] Test API endpoints
- [ ] Review factory.py code

### Day 2: Testing
- [ ] Run all tests
- [ ] Review test files
- [ ] Check coverage report
- [ ] Understand test patterns

### Day 3: DevOps
- [ ] Set up GitHub repo
- [ ] Configure GitHub Actions
- [ ] Set up Docker Hub
- [ ] Push and deploy

### Day 4: Submission
- [ ] Capture screenshots
- [ ] Complete reflection
- [ ] Verify everything works
- [ ] Submit assignment

---

## 🔗 Important URLs

| Service | URL | Purpose |
|---------|-----|---------|
| API Root | http://localhost:8000 | Base API |
| Swagger Docs | http://localhost:8000/docs | Interactive API docs |
| ReDoc | http://localhost:8000/redoc | Alternative docs |
| Health Check | http://localhost:8000/health | Status check |

---

## 🆘 Getting Help

### Documentation Files
1. **README.md** - Complete documentation
2. **SETUP.md** - Installation guide
3. **QUICK_REFERENCE.md** - Command reference
4. **REFLECTION.md** - Detailed insights
5. **SUBMISSION_CHECKLIST.md** - Submission prep

### Online Resources
- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://docs.sqlalchemy.org/
- Pytest: https://docs.pytest.org/

### Common Issues
Check the "Troubleshooting" section in README.md

---

## ✅ Quick Verification

After setup, verify everything works:

```powershell
# 1. Check application is running
curl http://localhost:8000/health

# 2. Run tests
pytest tests/ -v

# 3. Check Docker containers (if using Docker)
docker-compose ps
```

All should return success! ✅

---

## 🎉 Success Indicators

You're ready to proceed when:
- ✅ API responds at http://localhost:8000
- ✅ Swagger UI loads at /docs
- ✅ All tests pass
- ✅ No error messages in logs
- ✅ Can create a calculation via API

---

## 📝 Next Steps Checklist

- [ ] Application running successfully
- [ ] Tested at least one endpoint
- [ ] Tests pass (ran `run_tests.ps1`)
- [ ] Read README.md overview
- [ ] Reviewed code structure
- [ ] Ready to start development/testing

---

## 💡 Pro Tips

1. **Use the helper scripts**: `start_app.ps1` and `run_tests.ps1` save time
2. **Keep Swagger UI open**: Best way to test endpoints
3. **Watch the logs**: `docker-compose logs -f app`
4. **Test after changes**: Run tests frequently
5. **Read the reflection**: Lots of helpful insights

---

## 🚀 Ready to Go!

You're all set! The project is:
- ✅ Fully implemented
- ✅ Thoroughly tested
- ✅ Well documented
- ✅ Ready to deploy

### What you have:
- Complete FastAPI application
- Factory Pattern implementation
- 100+ tests with 92%+ coverage
- CI/CD pipeline ready
- Docker deployment ready
- Comprehensive documentation

### What you need to do:
1. Set up GitHub repository
2. Configure GitHub Actions secrets
3. Set up Docker Hub account
4. Push code and trigger deployment
5. Capture screenshots
6. Submit assignment

**Estimated time to deployment**: 1-2 hours

---

## 🎯 Your Mission

**Goal**: Successfully deploy and submit Module 11 assignment

**Steps**:
1. ✅ Get application running (YOU ARE HERE!)
2. Test and verify functionality
3. Set up GitHub repository
4. Configure CI/CD
5. Deploy to Docker Hub
6. Capture screenshots
7. Submit assignment

**You've got this! 🚀**

---

**Need immediate help?** 
- Check TROUBLESHOOTING section in README.md
- Review SETUP.md for detailed setup
- Follow QUICK_REFERENCE.md for commands

**Ready for submission?**
- Follow SUBMISSION_CHECKLIST.md
- Use SCREENSHOTS_GUIDE.md for captures
- Review PROJECT_SUMMARY.md for overview

---

**Let's build something great! 💪**
