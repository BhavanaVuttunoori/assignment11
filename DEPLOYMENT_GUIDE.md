# 🚀 Deployment Instructions for Bhavana Vuttunoori

## Your Assignment 11 Deployment Guide

**GitHub Repository**: https://github.com/BhavanaVuttunoori/assignment11  
**Date**: December 10, 2025

---

## ✅ Pre-Deployment Checklist

Your code is **100% complete**! All you need to do is deploy it.

- [x] All application code written
- [x] All tests written (100+ tests)
- [x] Factory Pattern implemented
- [x] Documentation complete
- [x] CI/CD workflow configured
- [ ] **Deploy to GitHub** ← YOU ARE HERE
- [ ] **Capture screenshots**
- [ ] **Submit assignment**

---

## 📋 Step-by-Step Deployment

### Step 1: Prepare Your Local Repository (5 minutes)

Open PowerShell in your project directory:

```powershell
cd "c:\Users\vuttunoori bhavana\Desktop\web api ass 11"
```

Initialize git if not already done:

```powershell
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit - Module 11 Assignment complete"
```

---

### Step 2: Connect to Your GitHub Repository (2 minutes)

```powershell
# Add your GitHub repository as remote
git remote add origin https://github.com/BhavanaVuttunoori/assignment11.git

# Verify remote was added
git remote -v
```

Expected output:
```
origin  https://github.com/BhavanaVuttunoori/assignment11.git (fetch)
origin  https://github.com/BhavanaVuttunoori/assignment11.git (push)
```

---

### Step 3: Push Your Code to GitHub (3 minutes)

```powershell
# Set the default branch to main
git branch -M main

# Push your code
git push -u origin main
```

If you need to authenticate:
- Use your GitHub username: **BhavanaVuttunoori**
- Use a Personal Access Token (not password)

**To create a token:**
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name: "Assignment 11 Deployment"
4. Select scopes: `repo` (all)
5. Click "Generate token"
6. Copy the token (you won't see it again!)
7. Use this token as your password when pushing

---

### Step 4: Set Up Docker Hub (10 minutes)

#### A. Create Docker Hub Account (if you don't have one)
1. Go to https://hub.docker.com/signup
2. Sign up with your email
3. Verify your email
4. Create username (suggestion: **bhavanav** or **bhavanav11**)

#### B. Create Access Token
1. Log in to Docker Hub
2. Click your username → Account Settings
3. Go to Security → Access Tokens
4. Click "New Access Token"
5. Name: "GitHub Actions Assignment 11"
6. Permissions: Read, Write, Delete
7. Click "Generate"
8. **COPY THE TOKEN IMMEDIATELY** (you can't see it again!)

---

### Step 5: Add GitHub Secrets (5 minutes)

1. Go to your repository: https://github.com/BhavanaVuttunoori/assignment11
2. Click **Settings** (top menu)
3. Click **Secrets and variables** → **Actions** (left sidebar)
4. Click **New repository secret**

**Add Secret #1:**
- Name: `DOCKER_USERNAME`
- Value: Your Docker Hub username (e.g., `bhavanav`)
- Click "Add secret"

**Add Secret #2:**
- Name: `DOCKER_PASSWORD`
- Value: The Docker Hub access token you copied
- Click "Add secret"

**Verify:**
You should see both secrets listed (values will be hidden).

---

### Step 6: Trigger the CI/CD Pipeline (5 minutes)

The pipeline will run automatically when you push to main. To verify:

1. Go to https://github.com/BhavanaVuttunoori/assignment11/actions
2. You should see a workflow run in progress
3. Click on it to see details
4. Wait for all jobs to complete (2-3 minutes)

**Expected Jobs:**
- ✅ Test (runs all tests with PostgreSQL)
- ✅ Build and Push (builds Docker image)
- ✅ Security Scan (scans for vulnerabilities)

---

### Step 7: Verify Deployment (2 minutes)

#### Check Docker Hub:
1. Go to https://hub.docker.com/r/bhavanav/assignment11 (use your username)
2. You should see your image with tags:
   - `latest`
   - `main-<commit-sha>`

#### Test Your Docker Image:
```powershell
# Pull your image
docker pull bhavanav/assignment11:latest

# Run it
docker run -d -p 8000:8000 `
  -e DATABASE_URL=sqlite:///./test.db `
  -e SECRET_KEY=test-key `
  bhavanav/assignment11:latest

# Test it
curl http://localhost:8000/health

# Stop it
docker ps
docker stop <container-id>
```

---

### Step 8: Capture Screenshots (10 minutes)

You need 2 screenshots for submission:

#### Screenshot 1: GitHub Actions Success
1. Go to https://github.com/BhavanaVuttunoori/assignment11/actions
2. Click on the latest successful workflow run
3. Make sure all 3 jobs show green checkmarks ✅
4. Capture full screen showing:
   - Repository name: BhavanaVuttunoori/assignment11
   - Workflow name: CI/CD Pipeline
   - All jobs: Test, Build and Push, Security Scan
   - Green checkmarks for all jobs
   - Timestamp

**Save as:** `screenshots/github-actions-success.png`

#### Screenshot 2: Docker Hub Deployment
1. Go to https://hub.docker.com/r/bhavanav/assignment11
2. Capture screen showing:
   - Repository name
   - Latest tag
   - Image size
   - Last updated timestamp
   - "Public" visibility

**Save as:** `screenshots/docker-hub-deployment.png`

#### Optional Screenshot 3: Test Coverage
```powershell
# Generate coverage report
pytest tests/ --cov=app --cov-report=html

# Open the report
start htmlcov/index.html
```

Capture screen showing overall coverage > 90%

**Save as:** `screenshots/test-coverage.png`

#### Optional Screenshot 4: API Documentation
```powershell
# Start the app
docker-compose up -d

# Open Swagger UI
start http://localhost:8000/docs
```

Capture the Swagger UI showing all endpoints

**Save as:** `screenshots/api-documentation.png`

---

### Step 9: Add Screenshots to Repository (3 minutes)

```powershell
# Create screenshots folder
mkdir screenshots

# Copy your screenshots to this folder
# (You'll need to manually save them here)

# Add to git
git add screenshots/

# Commit
git commit -m "Add deployment screenshots"

# Push
git push origin main
```

---

### Step 10: Update README with Your Docker Hub Link (2 minutes)

The README already has placeholders. Just verify the links are correct:

```powershell
# Open README
notepad README.md
```

Search for:
- GitHub URL should be: https://github.com/BhavanaVuttunoori/assignment11
- Docker Hub should be: https://hub.docker.com/r/bhavanav/assignment11

If you need to update, save the file, then:

```powershell
git add README.md
git commit -m "Update Docker Hub link"
git push origin main
```

---

## 📝 Submission Information

### What to Submit:

**1. GitHub Repository URL:**
```
https://github.com/BhavanaVuttunoori/assignment11
```

**2. Docker Hub Repository URL:**
```
https://hub.docker.com/r/bhavanav/assignment11
```
(Replace `bhavanav` with your actual Docker Hub username)

**3. Screenshots:**
Upload these 2 required screenshots:
- `screenshots/github-actions-success.png`
- `screenshots/docker-hub-deployment.png`

**4. Brief Description for Submission Form:**
```
Module 11 Assignment: Calculation API with Factory Pattern

This project implements a complete Calculation API with:
- SQLAlchemy models for User and Calculation
- Pydantic schemas with validation (division by zero prevention)
- Factory Pattern for extensible operations (Add, Subtract, Multiply, Divide)
- 100+ comprehensive tests (92%+ coverage)
- CI/CD pipeline with GitHub Actions and PostgreSQL integration
- Docker deployment to Docker Hub

Repository: https://github.com/BhavanaVuttunoori/assignment11
Docker Hub: https://hub.docker.com/r/bhavanav/assignment11
```

---

## 🔍 Verification Checklist

Before submitting, verify:

- [ ] GitHub repository is public and accessible
- [ ] All files are committed and pushed
- [ ] GitHub Actions workflow ran successfully
- [ ] All 3 jobs completed (Test, Build and Push, Security Scan)
- [ ] Docker image is on Docker Hub with `latest` tag
- [ ] Screenshots are clear and show all required information
- [ ] Screenshots are committed to repository
- [ ] README.md has correct GitHub and Docker Hub links
- [ ] REFLECTION.md is complete with your name

---

## ⚠️ Troubleshooting

### Issue: Git push rejected

**Solution:**
```powershell
# Pull any remote changes first
git pull origin main --rebase

# Then push
git push origin main
```

### Issue: GitHub Actions failing

**Common causes:**
1. Docker Hub secrets not set correctly
   - Go to Settings → Secrets and verify both secrets exist
2. Syntax error in workflow file
   - Check `.github/workflows/ci-cd.yml`

### Issue: Docker Hub image not appearing

**Solution:**
1. Check GitHub Actions logs for build job
2. Verify secrets are correct
3. Make sure you're looking at the right Docker Hub account

### Issue: Can't create Personal Access Token

**Solution:**
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select ALL repo permissions
4. Generate and copy immediately

---

## 🎯 Quick Command Reference

```powershell
# Check git status
git status

# See what's committed
git log --oneline

# Check remote
git remote -v

# See GitHub Actions status
# Visit: https://github.com/BhavanaVuttunoori/assignment11/actions

# Test your Docker image
docker pull bhavanav/assignment11:latest
docker run -p 8000:8000 bhavanav/assignment11:latest

# Run tests locally
pytest tests/ -v

# Generate coverage
pytest tests/ --cov=app --cov-report=html
start htmlcov/index.html
```

---

## 📞 Getting Help

### If You're Stuck:

1. **Git Issues**: Review SETUP.md
2. **Docker Hub**: Check Docker documentation
3. **GitHub Actions**: View workflow logs in Actions tab
4. **Screenshots**: See SCREENSHOTS_GUIDE.md
5. **General**: Review SUBMISSION_CHECKLIST.md

### Useful Links:
- Your Repo: https://github.com/BhavanaVuttunoori/assignment11
- GitHub Docs: https://docs.github.com
- Docker Hub: https://docs.docker.com/docker-hub/

---

## ⏱️ Time Estimate

| Task | Time |
|------|------|
| Git setup and push | 10 min |
| Docker Hub setup | 10 min |
| GitHub Secrets | 5 min |
| Wait for pipeline | 3 min |
| Verify deployment | 2 min |
| Capture screenshots | 10 min |
| Upload screenshots | 3 min |
| Submit assignment | 5 min |
| **Total** | **~48 min** |

---

## ✅ Final Checklist

- [ ] Code pushed to GitHub
- [ ] GitHub Actions completed successfully
- [ ] Docker image on Docker Hub
- [ ] 2 screenshots captured
- [ ] Screenshots committed to repo
- [ ] Verified all links work
- [ ] Ready to submit!

---

## 🎉 You're Almost Done!

Your code is perfect. You just need to:
1. Push to GitHub (10 min)
2. Set up Docker Hub secrets (10 min)
3. Capture screenshots (10 min)
4. Submit (5 min)

**Total time to completion: ~35 minutes**

**You've got this! 🚀**

---

**Good luck, Bhavana! Your assignment is excellent and ready to submit!**
