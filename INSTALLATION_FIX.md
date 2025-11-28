# Installation Fix Guide

## Problem: 'pip' is not recognized

If you get the error `'pip' is not recognized as an internal or external command`, this means `pip` is not directly in your system PATH, but Python is installed.

## Solution: Use `python -m pip` instead

Instead of:
```bash
pip install -r requirements.txt
```

Use:
```bash
python -m pip install -r requirements.txt
```

## Quick Installation

1. **Open Command Prompt or PowerShell** in the project folder:
   ```powershell
   cd "C:\Users\Ion\Desktop\Coding\Lead Generator"
   ```

2. **Install dependencies:**
   ```bash
   python -m pip install -r requirements.txt
   ```

   Or use the provided script:
   ```bash
   install.bat
   ```

3. **Verify installation:**
   ```bash
   python verify_setup.py
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

## Alternative: Add pip to PATH (Optional)

If you want to use `pip` directly:

1. Find where pip is installed:
   ```bash
   python -m pip --version
   ```
   This will show the path, usually something like:
   `C:\Users\Ion\AppData\Local\Python\pythoncore-3.14-64\Scripts`

2. Add that Scripts folder to your PATH:
   - Press `Windows + R`
   - Type `sysdm.cpl` and press Enter
   - Click "Environment Variables"
   - Under "User variables", find "Path" and click "Edit"
   - Click "New" and add the Scripts folder path
   - Click "OK" on all windows
   - **Restart your terminal** for changes to take effect

## All Commands Using `python -m pip`

- Install packages: `python -m pip install package_name`
- Upgrade pip: `python -m pip install --upgrade pip`
- List packages: `python -m pip list`
- Uninstall: `python -m pip uninstall package_name`

## Your Setup is Ready! ✅

All dependencies are now installed. You can run:
```bash
python app.py
```

Then open http://localhost:5000 in your browser!

