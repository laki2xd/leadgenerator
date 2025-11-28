@echo off
echo Company Finder - Starting Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
python -m pip install -r requirements.txt

echo.
echo ========================================
echo IMPORTANT: Set your API keys!
echo ========================================
echo.
echo Set environment variables:
echo   set GOOGLE_PLACES_API_KEY=your-key-here
echo   set YELP_API_KEY=your-key-here
echo.
echo Press any key to continue...
pause

REM Run the application
echo.
echo Starting Flask application...
echo Open http://localhost:5000 in your browser
echo.
cd /d "%~dp0"
python app.py

pause

