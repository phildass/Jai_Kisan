#!/bin/bash

# (J)ai Kisan - Deployment Verification Script
# This script checks if the deployment is configured correctly

echo "================================"
echo "(J)ai Kisan - Deployment Check"
echo "================================"
echo ""

ISSUES=0

# Check Python version
echo "📋 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    echo "✓ Python found: $PYTHON_VERSION"
    
    # Extract version number and check if it's 3.7 or higher
    VERSION_NUM=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
    if python3 -c "import sys; exit(0 if sys.version_info >= (3, 7) else 1)"; then
        echo "✓ Python version is 3.7 or higher"
    else
        echo "❌ Python version is too old. Need 3.7 or higher."
        ISSUES=$((ISSUES + 1))
    fi
else
    echo "❌ Python 3 not found. Please install Python 3.7 or higher."
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Check if pip is installed
echo "📋 Checking pip..."
if command -v pip3 &> /dev/null; then
    PIP_VERSION=$(pip3 --version 2>&1)
    echo "✓ pip found: $PIP_VERSION"
else
    echo "❌ pip not found. Please install pip."
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Check if requirements.txt exists
echo "📋 Checking project files..."
if [ -f "requirements.txt" ]; then
    echo "✓ requirements.txt found"
else
    echo "❌ requirements.txt not found"
    ISSUES=$((ISSUES + 1))
fi

if [ -f "app.py" ]; then
    echo "✓ app.py found"
else
    echo "❌ app.py not found"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Check if .env file exists
echo "📋 Checking environment configuration..."
if [ -f ".env" ]; then
    echo "✓ .env file exists"
    
    # Check for required variables
    if grep -q "SECRET_KEY" .env; then
        echo "✓ SECRET_KEY configured"
    else
        echo "⚠️  SECRET_KEY not found in .env"
    fi
    
    if grep -q "DATABASE_URI" .env; then
        echo "✓ DATABASE_URI configured"
    else
        echo "⚠️  DATABASE_URI not found in .env"
    fi
else
    echo "⚠️  .env file not found. Copy from .env.example"
    if [ -f ".env.example" ]; then
        echo "   Run: cp .env.example .env"
    fi
fi
echo ""

# Check if dependencies are installed
echo "📋 Checking Python dependencies..."
if python3 -c "import flask" 2>/dev/null; then
    echo "✓ Flask installed"
else
    echo "❌ Flask not installed. Run: pip install -r requirements.txt"
    ISSUES=$((ISSUES + 1))
fi

if python3 -c "import flask_sqlalchemy" 2>/dev/null; then
    echo "✓ Flask-SQLAlchemy installed"
else
    echo "❌ Flask-SQLAlchemy not installed. Run: pip install -r requirements.txt"
    ISSUES=$((ISSUES + 1))
fi

if python3 -c "import flask_login" 2>/dev/null; then
    echo "✓ Flask-Login installed"
else
    echo "❌ Flask-Login not installed. Run: pip install -r requirements.txt"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Check port availability
echo "📋 Checking port availability..."
if [ -f ".env" ]; then
    PORT=$(grep "^PORT=" .env | cut -d '=' -f2)
    if [ -z "$PORT" ]; then
        PORT=5000
    fi
else
    PORT=5000
fi

if command -v lsof &> /dev/null; then
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
        echo "⚠️  Port $PORT is already in use"
        echo "   Either stop the process using it or change PORT in .env"
    else
        echo "✓ Port $PORT is available"
    fi
else
    echo "ℹ️  Cannot check port (lsof not installed)"
fi
echo ""

# Production deployment checks
if [ -f ".env" ] && grep -q "FLASK_ENV=production" .env; then
    echo "📋 Production deployment checks..."
    
    # Check if Gunicorn is installed
    if command -v gunicorn &> /dev/null; then
        echo "✓ Gunicorn installed"
    else
        echo "⚠️  Gunicorn not installed. For production, run: pip install gunicorn"
    fi
    
    # Check if Nginx is installed
    if command -v nginx &> /dev/null; then
        echo "✓ Nginx installed"
    else
        echo "⚠️  Nginx not installed. For production with domain, install nginx"
    fi
    
    echo ""
fi

# Summary
echo "================================"
echo "Summary"
echo "================================"
if [ $ISSUES -eq 0 ]; then
    echo "✓ All critical checks passed!"
    echo ""
    echo "You can start the application with:"
    echo "  ./start.sh"
    echo "  OR"
    echo "  python3 app.py"
    echo ""
    echo "For production deployment, see DEPLOYMENT.md"
else
    echo "❌ Found $ISSUES issue(s) that need to be fixed"
    echo ""
    echo "Please address the issues above before starting the application."
    echo "See SETUP.md and TROUBLESHOOTING.md for help."
fi
echo ""
echo "जय किसान! (Victory to the Farmers!)"
