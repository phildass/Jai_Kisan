@echo off
REM (J)ai Kisan - Quick Start Script for Windows
REM This script helps you start the application quickly on Windows

echo ================================
echo (J)ai Kisan - जय किसान
echo Starting Application...
echo ================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python is not installed!
    echo Please install Python 3.7 or higher from https://www.python.org/
    pause
    exit /b 1
)

REM Check if virtual environment exists, if not create it
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if requirements are installed
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo 📥 Installing dependencies...
    pip install -r requirements.txt
)

REM Check if .env file exists
if not exist ".env" (
    echo ⚙️  Creating .env file from template...
    copy .env.example .env
    echo ⚠️  Please edit .env file with your configuration!
)

REM Start the application
echo 🚀 Starting (J)ai Kisan application...
echo.
echo Access the application at:
echo   - Local: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ================================

python app.py
