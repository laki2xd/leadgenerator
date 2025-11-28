#!/bin/bash

echo "Company Finder - Starting Application..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 from https://www.python.org/"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "========================================"
echo "IMPORTANT: Set your API keys!"
echo "========================================"
echo ""
echo "Set environment variables:"
echo "  export GOOGLE_PLACES_API_KEY=your-key-here"
echo "  export YELP_API_KEY=your-key-here"
echo ""
read -p "Press Enter to continue..."

# Run the application
echo ""
echo "Starting Flask application..."
echo "Open http://localhost:5000 in your browser"
echo ""
python app.py

