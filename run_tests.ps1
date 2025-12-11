# Run Tests Script
# This script helps run tests locally on Windows

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Calculation API - Test Runner" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-Not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -q -r requirements.txt

Write-Host ""
Write-Host "==================================" -ForegroundColor Green
Write-Host "Running Unit Tests" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green
pytest tests/test_factory.py tests/test_schemas.py -v

Write-Host ""
Write-Host "==================================" -ForegroundColor Green
Write-Host "Running Integration Tests" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green
pytest tests/test_integration.py -v

Write-Host ""
Write-Host "==================================" -ForegroundColor Green
Write-Host "Running All Tests with Coverage" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green
pytest tests/ -v --cov=app --cov-report=term-missing --cov-report=html

Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Test Summary" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Coverage report generated: htmlcov/index.html" -ForegroundColor Yellow
Write-Host ""
Write-Host "To view coverage report, run:" -ForegroundColor Yellow
Write-Host "  start htmlcov/index.html" -ForegroundColor White
Write-Host ""
