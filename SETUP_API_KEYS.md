# Complete API Setup Guide

## Step 1: Get Google Places API Key (REQUIRED)

### 1.1 Create Google Cloud Account
1. Go to https://console.cloud.google.com/
2. Sign in with your Google account (or create one if needed)

### 1.2 Create a New Project
1. Click the project dropdown at the top
2. Click "New Project"
3. Enter a project name (e.g., "Company Finder")
4. Click "Create"
5. Wait for the project to be created, then select it

### 1.3 Enable Places API
1. In the left sidebar, go to "APIs & Services" → "Library"
2. Search for "Places API"
3. Click on "Places API"
4. Click "Enable"

### 1.4 Create API Key
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "API Key"
3. Copy your API key (it will look like: `AIzaSy...`)
4. **IMPORTANT:** Click "Restrict Key" to secure it:
   - Under "API restrictions", select "Restrict key"
   - Check "Places API"
   - Click "Save"

### 1.5 Set Up Billing (Required for Places API)
1. Go to "Billing" in the left menu
2. Click "Link a billing account"
3. Add a payment method (Google gives $200 free credit monthly)
4. The free tier covers most usage for this app

---

## Step 2: Get Yelp API Key (OPTIONAL but Recommended)

### 2.1 Create Yelp Developer Account
1. Go to https://www.yelp.com/developers
2. Click "Create App" or "Get Started"
3. Sign in with your Yelp account (or create one)

### 2.2 Create an App
1. Fill in the form:
   - App Name: "Company Finder"
   - Industry: Select any
   - Use Case: "Personal Project" or "Learning"
2. Accept the terms
3. Click "Create App"

### 2.3 Get Your API Key
1. You'll see your API Key (it's a long string)
2. Copy it immediately (you can view it again later)

---

## Step 3: Set Environment Variables on Windows

### Method 1: Using PowerShell (Recommended - Temporary)

Open PowerShell in the project folder and run:

```powershell
# Set Google Places API Key
$env:GOOGLE_PLACES_API_KEY="YOUR_GOOGLE_API_KEY_HERE"

# Set Yelp API Key (optional)
$env:YELP_API_KEY="YOUR_YELP_API_KEY_HERE"

# Verify they're set
echo $env:GOOGLE_PLACES_API_KEY
echo $env:YELP_API_KEY
```

**Note:** These variables only last for the current PowerShell session. When you close PowerShell, you'll need to set them again.

### Method 2: Using Command Prompt (Temporary)

Open Command Prompt and run:

```cmd
set GOOGLE_PLACES_API_KEY=YOUR_GOOGLE_API_KEY_HERE
set YELP_API_KEY=YOUR_YELP_API_KEY_HERE
```

### Method 3: Set Permanently in Windows (Recommended for Long-term Use)

1. Press `Windows + R`
2. Type `sysdm.cpl` and press Enter
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Variable name: `GOOGLE_PLACES_API_KEY`
6. Variable value: Your API key
7. Click "OK"
8. Repeat for `YELP_API_KEY`
9. **Restart your terminal/IDE** for changes to take effect

### Method 4: Using the Setup Script (Easiest!)

I've created a helper script for you. See `setup_api_keys.bat` below.

---

## Step 4: Alternative - Use Config File

If you prefer not to use environment variables:

1. Copy `config.example.py` to `config.py`
2. Open `config.py` in a text editor
3. Replace the placeholder values with your actual API keys:
   ```python
   GOOGLE_PLACES_API_KEY = 'AIzaSy...your-actual-key...'
   YELP_API_KEY = 'your-actual-yelp-key'
   ```
4. Save the file
5. **Never commit `config.py` to git!** (It's already in .gitignore)

---

## Step 5: Test Your Setup

1. Make sure your API keys are set (use one of the methods above)
2. Run the application:
   ```bash
   python app.py
   ```
3. Open http://localhost:5000 in your browser
4. Try searching for "Technology" companies
5. If you see companies, your setup is working!

---

## Troubleshooting

### "No API keys configured" error
- Make sure you set the variables in the SAME terminal where you run `python app.py`
- Or use the `config.py` method instead
- Verify your keys don't have extra spaces or quotes

### "API key not valid" error
- Check that you copied the entire key (they're long!)
- Make sure Places API is enabled in Google Cloud Console
- Verify billing is set up for Google Cloud

### "Quota exceeded" error
- Google Places API has free tier limits
- Wait 24 hours for quota reset
- Or upgrade your Google Cloud billing plan

### Keys not persisting
- If using PowerShell/CMD, variables reset when you close the window
- Use Method 3 (permanent Windows variables) or `config.py` for persistence

---

## Security Tips

1. **Never share your API keys** publicly
2. **Never commit** `config.py` to version control (already in .gitignore)
3. **Restrict your Google API key** to only Places API
4. **Monitor usage** in Google Cloud Console to prevent unexpected charges
5. Google gives $200/month free credit, which is usually enough

---

## Quick Reference

**Google Places API:**
- Console: https://console.cloud.google.com/google/maps-apis
- Documentation: https://developers.google.com/maps/documentation/places/web-service

**Yelp API:**
- Dashboard: https://www.yelp.com/developers
- Documentation: https://www.yelp.com/developers/documentation/v3

**Test your keys:**
```powershell
# In PowerShell, test Google Places API
$key = $env:GOOGLE_PLACES_API_KEY
Invoke-WebRequest "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Toronto&key=$key"
```

If you see JSON data, your key works!

