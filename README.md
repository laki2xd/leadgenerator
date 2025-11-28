# Company Finder - Canada & USA

A web application that allows you to search for real registered companies in Canada and USA by industry and export the results to Excel.

## Features

- 🔍 Search for companies by industry
- 🌎 Find companies in Canada and USA
- ✅ Verified registered businesses
- 📊 Export results to Excel
- 🎨 Modern, responsive UI

## Setup Instructions

### 1. Install Python Dependencies

```bash
python -m pip install -r requirements.txt
```

**Note:** If `pip` is not recognized, always use `python -m pip` instead. See [INSTALLATION_FIX.md](INSTALLATION_FIX.md) for details.

### 2. Get API Keys

**📖 For detailed step-by-step instructions, see [SETUP_API_KEYS.md](SETUP_API_KEYS.md)**

#### Quick Setup Options:

**Option A: Use the Setup Script (Easiest!)**
```bash
# Windows
setup_api_keys.bat

# This will guide you through entering your API keys
```

**Option B: Manual Setup**

#### Google Places API (Required)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the "Places API"
4. Create credentials (API Key)
5. Copy your API key

#### Yelp API (Optional but Recommended)
1. Go to [Yelp Developers](https://www.yelp.com/developers)
2. Create an app
3. Copy your API key

### 3. Set Environment Variables

**Easiest Method:** Use `setup_api_keys.bat` (Windows) - it will create `config.py` automatically!

**Or set manually:**

**Windows (PowerShell):**
```powershell
$env:GOOGLE_PLACES_API_KEY="your-google-api-key-here"
$env:YELP_API_KEY="your-yelp-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set GOOGLE_PLACES_API_KEY=your-google-api-key-here
set YELP_API_KEY=your-yelp-api-key-here
```

**Linux/Mac:**
```bash
export GOOGLE_PLACES_API_KEY="your-google-api-key-here"
export YELP_API_KEY="your-yelp-api-key-here"
```

**Or use config.py:** Copy `config.example.py` to `config.py` and add your keys there.

### 4. Test Your API Keys (Optional but Recommended)

```bash
python test_api_keys.py
```

This will verify your API keys are working correctly.

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. Open your browser and navigate to `http://localhost:5000`
2. Enter an industry name (e.g., "Technology", "Healthcare", "Manufacturing")
3. Click "Search Companies"
4. Review the results (up to 100 companies)
5. Click "Export to Excel" to download the data

## Project Structure

```
.
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   ├── style.css         # Stylesheet
│   └── script.js         # Frontend JavaScript
└── exports/              # Generated Excel files (created automatically)
```

## API Endpoints

- `GET /` - Main page
- `POST /api/search` - Search for companies
  - Body: `{ "industry": "Technology" }`
  - Returns: `{ "success": true, "count": 100, "companies": [...] }`
- `POST /api/export` - Export companies to Excel
  - Body: `{ "companies": [...] }`
  - Returns: Excel file download

## Notes

- The application uses Google Places API as the primary data source
- Yelp API is used as a secondary source if available
- Results are deduplicated based on company name and address
- Excel files are saved in the `exports/` directory
- API rate limiting is implemented to respect API quotas

## Troubleshooting

**No companies found:**
- Check that your API keys are set correctly
- Verify that the industry name is valid
- Ensure you have API quota remaining

**Export fails:**
- Make sure the `exports/` directory is writable
- Check that `openpyxl` is installed correctly

## License

This project is provided as-is for educational and personal use.

