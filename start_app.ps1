# Start Application Script
# This script helps start the application locally on Windows

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Calculation API - Startup Script" -ForegroundColor Cyan
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

# Check if .env exists
if (-Not (Test-Path ".env")) {
    Write-Host ""
    Write-Host "WARNING: .env file not found!" -ForegroundColor Red
    Write-Host "Copying .env.example to .env..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host ""
    Write-Host "Please edit .env file with your database credentials:" -ForegroundColor Yellow
    Write-Host "  DATABASE_URL=postgresql://user:password@localhost:5432/calculation_db" -ForegroundColor White
    Write-Host ""
    $continue = Read-Host "Continue with default settings? (y/n)"
    if ($continue -ne "y") {
        Write-Host "Please configure .env and run this script again." -ForegroundColor Yellow
        exit
    }
}

Write-Host ""
Write-Host "==================================" -ForegroundColor Green
Write-Host "Starting Application" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green
Write-Host ""
Write-Host "Application will be available at:" -ForegroundColor Cyan
Write-Host "  - API: http://localhost:8000" -ForegroundColor White
Write-Host "  - Swagger Docs: http://localhost:8000/docs" -ForegroundColor White
Write-Host "  - ReDoc: http://localhost:8000/redoc" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start the application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
