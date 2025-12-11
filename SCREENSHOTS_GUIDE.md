# Screenshot Guide for Submission

This guide will help you capture all required screenshots for the Module 11 assignment submission.

---

## 📸 Required Screenshots

### 1. GitHub Actions Workflow Success

**What to show**: Successful CI/CD pipeline execution

**Steps**:
1. Navigate to your GitHub repository
2. Click on the "Actions" tab at the top
3. Select the most recent workflow run
4. Wait for all jobs to complete (green checkmarks)
5. Take a screenshot showing:
   - ✅ All three jobs completed successfully:
     - "Run Tests" job
     - "Build and Push Docker Image" job
     - "Security Scan" job
   - Workflow name and run number
   - Timestamp of execution
   - Your repository name

**Filename**: `01_github_actions_success.png`

---

### 2. Docker Hub Deployment

**What to show**: Successfully deployed Docker image on Docker Hub

**Steps**:
1. Log in to https://hub.docker.com
2. Navigate to your `calculation-api` repository
3. Take a screenshot showing:
   - Repository name
   - Latest tag visible
   - Image size
   - Last updated timestamp
   - Number of pulls (if any)
   - Tags section showing:
     - `latest`
     - `main-<sha>`
     - `main` (if present)

**Filename**: `02_docker_hub_deployment.png`

**Optional**: Take a second screenshot showing the image details:
- Click on the `latest` tag
- Show the layers and image information

**Optional Filename**: `02b_docker_image_details.png`

---

### 3. Test Coverage Report

**What to show**: High test coverage percentage

**Steps**:
1. Open PowerShell in your project directory
2. Activate virtual environment:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
3. Run tests with coverage:
   ```powershell
   pytest tests/ -v --cov=app --cov-report=html
   ```
4. Open the coverage report:
   ```powershell
   start htmlcov/index.html
   ```
5. Take a screenshot showing:
   - Overall coverage percentage (should be 90%+)
   - Module breakdown with coverage for each file:
     - `app/factory.py`
     - `app/schemas.py`
     - `app/main.py`
     - `app/models.py`
     - `app/database.py`
   - Statements, Missing, and Coverage columns
   - Date generated

**Filename**: `03_test_coverage.png`

**Optional**: Click on `app/factory.py` and take a screenshot showing:
- Line-by-line coverage
- Green highlighting for covered lines
- Red highlighting for missed lines (if any)

**Optional Filename**: `03b_detailed_coverage.png`

---

### 4. API Documentation (Swagger UI)

**What to show**: Complete API with all endpoints documented

**Steps**:
1. Start the application:
   ```powershell
   .\start_app.ps1
   ```
   OR
   ```powershell
   docker-compose up -d
   ```
2. Navigate to: http://localhost:8000/docs
3. Take a screenshot showing:
   - All endpoint groups:
     - Root endpoints (/, /health)
     - User endpoints (/users)
     - Calculation endpoints (/calculations)
   - FastAPI/Swagger UI header
   - API title and version

**Filename**: `04_api_documentation.png`

**Optional**: Expand one of the POST endpoints and take a screenshot showing:
- Request body schema
- Response schema
- Try it out button
- Example values

**Optional Filename**: `04b_endpoint_details.png`

---

### 5. Successful Test Execution (Optional but Recommended)

**What to show**: Tests running successfully in terminal

**Steps**:
1. Run the test script:
   ```powershell
   .\run_tests.ps1
   ```
   OR
   ```powershell
   pytest tests/ -v
   ```
2. Take a screenshot showing:
   - All tests passing (green)
   - Test count (100+ tests)
   - No failures or errors
   - Execution time
   - Coverage summary at the bottom

**Filename**: `05_test_execution.png`

---

### 6. Database Schema (Optional but Impressive)

**What to show**: Database tables and relationships

**Steps**:
1. Connect to your PostgreSQL database using pgAdmin or DBeaver
2. Navigate to the `calculation_db` database
3. Take a screenshot showing:
   - Tables: `users` and `calculations`
   - Table structures with columns
   - Foreign key relationship between tables

**Filename**: `06_database_schema.png`

---

### 7. Docker Compose Running (Optional)

**What to show**: Application running in Docker containers

**Steps**:
1. Run:
   ```powershell
   docker-compose up -d
   docker-compose ps
   ```
2. Take a screenshot showing:
   - Both containers running (calculation_app and calculation_db)
   - Status: Up
   - Ports mapped (5432 and 8000)

**Filename**: `07_docker_compose_status.png`

---

## 📁 Organizing Your Screenshots

### Create a Screenshots Folder

```powershell
# In your project directory
New-Item -ItemType Directory -Path "screenshots" -Force
```

### Move Screenshots

Place all screenshots in the `screenshots/` folder:
```
screenshots/
├── 01_github_actions_success.png
├── 02_docker_hub_deployment.png
├── 03_test_coverage.png
├── 04_api_documentation.png
├── 05_test_execution.png (optional)
├── 06_database_schema.png (optional)
└── 07_docker_compose_status.png (optional)
```

---

## 📝 Screenshot Checklist

Before submission, verify you have:

### Required Screenshots
- [ ] GitHub Actions workflow success (01)
- [ ] Docker Hub deployment (02)
- [ ] Test coverage report (03)
- [ ] API documentation (04)

### Optional Screenshots (Recommended)
- [ ] Test execution in terminal (05)
- [ ] Database schema (06)
- [ ] Docker compose status (07)

### Quality Checks
- [ ] All screenshots are clear and readable
- [ ] Text is legible (not too small)
- [ ] Important information is visible
- [ ] Timestamps are shown
- [ ] No sensitive information exposed (passwords, tokens)

---

## 🎨 Screenshot Best Practices

### Resolution
- Minimum: 1280x720
- Recommended: 1920x1080
- Format: PNG (preferred) or JPEG

### What to Include
- Full browser window (for web screenshots)
- Terminal output (for CLI screenshots)
- Timestamp or date visible
- Clear labels or annotations if needed

### What to Avoid
- Personal information
- API keys or secrets
- Unrelated tabs or windows
- Cluttered desktop background

### Tools
**Windows**:
- Snipping Tool (Win + Shift + S)
- Snip & Sketch
- ShareX (advanced)

**Screenshot Annotations**:
- Windows Photos app
- Paint
- ShareX
- Greenshot

---

## 📤 Adding Screenshots to GitHub

After capturing screenshots:

```powershell
# Add screenshots folder to git
git add screenshots/

# Commit
git commit -m "Add submission screenshots"

# Push to GitHub
git push origin main
```

---

## 📋 Screenshot Descriptions for Submission

When submitting, include these descriptions:

### 1. GitHub Actions Success
> "Screenshot showing successful execution of CI/CD pipeline with all jobs completed: automated testing with PostgreSQL container, Docker image building, and security scanning."

### 2. Docker Hub Deployment
> "Screenshot demonstrating successful deployment of the calculation-api Docker image to Docker Hub, showing the latest tag, image size, and last updated timestamp."

### 3. Test Coverage Report
> "HTML coverage report showing 92%+ overall test coverage across all application modules, with detailed breakdown of statements and missing lines."

### 4. API Documentation
> "Swagger UI documentation showing all implemented API endpoints including calculation CRUD operations, user management, and utility endpoints."

---

## ⚠️ Common Issues

### Issue: GitHub Actions not showing
**Solution**: Make sure you've pushed your code and triggered the workflow

### Issue: Docker Hub image not visible
**Solution**: Check that GitHub secrets are configured and the workflow completed

### Issue: Coverage report not generating
**Solution**: Install pytest-cov: `pip install pytest-cov`

### Issue: API docs not loading
**Solution**: Ensure the application is running: `uvicorn app.main:app --reload`

---

## ✅ Final Verification

Before submitting, confirm:

1. [ ] All required screenshots captured
2. [ ] Screenshots are clear and readable
3. [ ] No sensitive information visible
4. [ ] Screenshots added to `screenshots/` folder
5. [ ] Folder committed to GitHub
6. [ ] README includes note about screenshots
7. [ ] Each screenshot filename is descriptive

---

## 📞 Need Help?

If you encounter issues capturing screenshots:
1. Review the SETUP.md for application startup
2. Check the README.md for testing instructions
3. Ensure all services are running properly
4. Verify network connectivity for external services

---

**Good luck with your submission! 🎉**
