@echo off
echo ========================================
echo   Installing Dependencies
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found!
python --version
echo.

echo Installing required packages...
echo This may take a few minutes...
echo.

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo You can now run the application with:
echo   python app.py
echo.
pause

