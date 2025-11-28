# Quick Start Guide

## Step 1: Install Python
Make sure you have Python 3.7+ installed. Download from [python.org](https://www.python.org/downloads/)

## Step 2: Get API Keys

### Google Places API (Required)
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select existing)
3. Enable "Places API" from the API Library
4. Go to "Credentials" → "Create Credentials" → "API Key"
5. Copy your API key
6. (Optional) Restrict the API key to Places API for security

### Yelp API (Optional but Recommended)
1. Visit [Yelp Developers](https://www.yelp.com/developers)
2. Click "Create App"
3. Fill in the form and create your app
4. Copy your API key

## Step 3: Set API Keys

### Option A: Environment Variables (Recommended)

**Windows PowerShell:**
```powershell
$env:GOOGLE_PLACES_API_KEY="your-key-here"
$env:YELP_API_KEY="your-key-here"
```

**Windows Command Prompt:**
```cmd
set GOOGLE_PLACES_API_KEY=your-key-here
set YELP_API_KEY=your-key-here
```

**Linux/Mac:**
```bash
export GOOGLE_PLACES_API_KEY="your-key-here"
export YELP_API_KEY="your-key-here"
```

### Option B: Config File
1. Copy `config.example.py` to `config.py`
2. Edit `config.py` and add your API keys
3. Never commit `config.py` to version control!

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

Or use the provided scripts:
- **Windows:** Double-click `run.bat`
- **Linux/Mac:** Run `chmod +x run.sh && ./run.sh`

## Step 5: Run the Application

```bash
python app.py
```

Or use the provided scripts:
- **Windows:** `run.bat`
- **Linux/Mac:** `./run.sh`

## Step 6: Use the Application

1. Open your browser and go to `http://localhost:5000`
2. Enter an industry (e.g., "Technology", "Healthcare", "Manufacturing")
3. Click "Search Companies"
4. Wait for results (may take 10-30 seconds)
5. Click "Export to Excel" to download

## Troubleshooting

### "No API keys configured" error
- Make sure you set the environment variables in the same terminal window where you run the app
- Or create a `config.py` file with your keys

### "Only found X companies" message
- Try a more specific industry name
- Some industries may have fewer registered companies
- Check your API quota/limits

### Export fails
- Make sure `openpyxl` is installed: `pip install openpyxl`
- Check that the `exports/` folder is writable

### API quota exceeded
- Google Places API has free tier limits
- Consider upgrading your API plan
- Wait for quota reset (usually daily)

## Example Industries to Try

- Technology
- Healthcare
- Manufacturing
- Finance
- Real Estate
- Retail
- Construction
- Food & Beverage
- Automotive
- Education

## Need Help?

Check the full README.md for more detailed information.

