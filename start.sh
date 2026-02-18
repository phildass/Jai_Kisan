#!/bin/bash

# (J)ai Kisan - Quick Start Script
# This script helps you start the application quickly

echo "================================"
echo "(J)ai Kisan - जय किसान"
echo "Starting Application..."
echo "================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Error: Python 3 is not installed!"
    echo "Please install Python 3.7 or higher from https://www.python.org/"
    exit 1
fi

# Check if virtual environment exists, if not create it
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if requirements are installed
if ! python -c "import flask" &> /dev/null; then
    echo "📥 Installing dependencies..."
    pip install -r requirements.txt
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚙️  Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your configuration!"
fi

# Start the application
echo "🚀 Starting (J)ai Kisan application..."
echo ""
echo "Access the application at:"
echo "  - Local: http://localhost:5000"
echo "  - Network: http://$(hostname -I | awk '{print $1}'):5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================"

python app.py
