# 🚀 START HERE - Quick Setup Guide

## The Fastest Way to Get Started

### Step 1: Install Python Packages
```bash
pip install -r requirements.txt
```

### Step 2: Set Up API Keys

**🎯 EASIEST METHOD (Windows):**
1. Double-click `setup_api_keys.bat`
2. Follow the prompts to enter your API keys
3. Done! The script creates `config.py` for you

**📝 MANUAL METHOD:**
1. Get your Google Places API key from: https://console.cloud.google.com/
2. (Optional) Get your Yelp API key from: https://www.yelp.com/developers
3. Run `setup_api_keys.bat` OR create `config.py` manually

### Step 3: Test Your Setup
```bash
python test_api_keys.py
```

### Step 4: Run the Application
```bash
python app.py
```

Then open http://localhost:5000 in your browser!

---

## 📚 Need More Help?

- **Detailed API Setup:** See [SETUP_API_KEYS.md](SETUP_API_KEYS.md)
- **Full Documentation:** See [README.md](README.md)
- **Quick Reference:** See [QUICKSTART.md](QUICKSTART.md)

---

## 🆘 Common Issues

**"No API keys configured"**
→ Run `setup_api_keys.bat` or set environment variables

**"API key not valid"**
→ Check that you copied the entire key (they're long!)
→ Make sure Places API is enabled in Google Cloud Console

**"Quota exceeded"**
→ Google gives $200/month free credit
→ Wait 24 hours for quota reset

---

## ✅ Quick Checklist

- [ ] Python installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Google Places API key obtained
- [ ] API keys configured (via `setup_api_keys.bat` or manually)
- [ ] Test passed (`python test_api_keys.py`)
- [ ] Application running (`python app.py`)

---

**Ready? Let's go! 🎉**

