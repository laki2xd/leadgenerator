# 📝 How to Use .env File

Guide to create and use a `.env` file for local development.

---

## ⚠️ Important Note

**Render doesn't use .env files!** 
- Render uses environment variables set in the dashboard
- `.env` files are for **local development only**
- Your `.env` file is already in `.gitignore` (won't be committed)

---

## 📋 Step 1: Create .env File

### Option A: Copy Template (Easiest)

1. **Copy the template file**
   - Copy `env.template` 
   - Rename it to `.env` (with the dot at the beginning)

### Option B: Create Manually

1. **Create new file** named `.env` in your project root
2. **Copy this content**:

```env
# Environment Variables for Lead Generator
# This file is for LOCAL DEVELOPMENT only

# Google Places API Key (Required)
GOOGLE_PLACES_API_KEY=AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y

# Apollo API Key (Optional but recommended)
APOLLO_API_KEY=Fx9l0QJ5nzZbivE2FVXgcw

# Yelp API Key (Optional)
YELP_API_KEY=

# Clearbit API Key (Optional)
CLEARBIT_API_KEY=

# ZoomInfo API Key (Optional)
ZOOMINFO_API_KEY=
```

---

## ✅ Step 2: Install python-dotenv

I've already added `python-dotenv` to `requirements.txt`. Install it:

```powershell
pip install python-dotenv
```

Or install all requirements:

```powershell
pip install -r requirements.txt
```

---

## ✅ Step 3: Code Already Updated

I've updated `app.py` to automatically load `.env` files. The code now:

1. Loads `.env` file automatically (for local development)
2. Falls back to `config.py` (if .env doesn't exist)
3. Uses environment variables (for Render/production)

**No changes needed** - it works automatically!

---

## 🚀 Step 4: Use It

### For Local Development:

1. **Create `.env` file** (see Step 1)
2. **Run your app locally**:
   ```powershell
   python app.py
   ```
3. **The app will automatically load** API keys from `.env`

### For Render Deployment:

1. **Don't upload `.env`** (it's in `.gitignore`)
2. **Set environment variables** in Render dashboard:
   - Go to: Your Service → Environment tab
   - Add: `GOOGLE_PLACES_API_KEY` = `AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y`
   - Add: `APOLLO_API_KEY` = `Fx9l0QJ5nzZbivE2FVXgcw`

---

## 📋 .env File Format

### Correct Format:

```env
KEY_NAME=value
KEY_NAME=value with spaces is fine
KEY_NAME=
```

### Rules:

- ✅ No quotes needed
- ✅ No spaces around `=`
- ✅ Empty values are OK (just `KEY_NAME=`)
- ✅ Comments start with `#`
- ✅ One key per line

### Examples:

```env
# Correct
GOOGLE_PLACES_API_KEY=AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y

# Wrong (has quotes)
GOOGLE_PLACES_API_KEY="AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y"

# Wrong (has spaces around =)
GOOGLE_PLACES_API_KEY = AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y
```

---

## 🔒 Security

### ✅ Safe:

- `.env` is in `.gitignore` - won't be committed
- Only use `.env` for local development
- Never commit `.env` to GitHub

### ⚠️ Important:

- **Render doesn't read `.env` files**
- You must set environment variables in Render dashboard
- `.env` is only for local testing

---

## ✅ Quick Checklist

- [ ] Created `.env` file in project root
- [ ] Added API keys to `.env` file
- [ ] Installed `python-dotenv`: `pip install python-dotenv`
- [ ] Tested locally: `python app.py`
- [ ] Verified `.env` is in `.gitignore` (it is!)
- [ ] Set environment variables in Render (for deployment)

---

## 🎯 Summary

**For Local Development:**
- Use `.env` file ✅
- Create `.env` from `env.template`
- Run: `python app.py`

**For Render:**
- Use Environment Variables in dashboard ✅
- Don't upload `.env` (it's ignored)
- Set variables in Render → Environment tab

---

**Your `.env` file is ready to use!** Just create it from the template above.

