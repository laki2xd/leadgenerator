# 🔧 Fix: Website Showing 0 Companies

Your website at https://leadgenerator-0vdk.onrender.com/ is loading but searches return 0 results.

## 🔍 Root Cause

The most likely issue is **API keys not configured** in Render environment variables.

Looking at your code (line 910 in app.py):
- If `GOOGLE_PLACES_API_KEY` is not set, searches will return 0 companies
- The search function requires at least Google Places API key to work

## ✅ Solution: Add Environment Variables in Render

### Step 1: Go to Render Dashboard

1. Log in to https://render.com
2. Click on your service: **"leadgenerator"** (or whatever you named it)

### Step 2: Add Environment Variables

1. Click **"Environment"** tab (left sidebar)
2. Click **"Add Environment Variable"**

3. **Add GOOGLE_PLACES_API_KEY:**
   - **Key**: `GOOGLE_PLACES_API_KEY`
   - **Value**: `AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y`
   - Click **"Save"**

4. **Add APOLLO_API_KEY (optional but recommended):**
   - **Key**: `APOLLO_API_KEY`
   - **Value**: `Fx9l0QJ5nzZbivE2FVXgcw`
   - Click **"Save"**

### Step 3: Redeploy

After adding environment variables:

1. Render should **auto-redeploy** (watch the logs)
2. If not, go to **"Manual Deploy"** → **"Deploy latest commit"**
3. Wait for deployment to complete (2-5 minutes)

### Step 4: Test

1. Visit: https://leadgenerator-0vdk.onrender.com/
2. Try searching for: **"Manufacturing"** or **"Warehouse"**
3. Should now find companies!

## 🔍 How to Verify Environment Variables Are Set

1. Go to: Render Dashboard → Your Service → **"Environment"** tab
2. You should see:
   ```
   GOOGLE_PLACES_API_KEY    ••••••••••••••••
   APOLLO_API_KEY            •••••••••••••••
   ```
3. Values are hidden (dots) for security - that's normal

## 🆘 If Still Not Working

### Check Render Logs

1. Go to: Your Service → **"Logs"** tab
2. Look for errors like:
   - `No API keys configured`
   - `ModuleNotFoundError`
   - `API quota exceeded`
   - `REQUEST_DENIED`

### Common Issues:

1. **"No API keys configured"**
   - → Environment variables not added
   - → Fix: Add them in Environment tab

2. **"API quota exceeded"**
   - → Google Places API free tier limit reached
   - → Fix: Check Google Cloud Console, wait for quota reset

3. **"REQUEST_DENIED"**
   - → API key is invalid or restricted
   - → Fix: Verify API key is correct, check Google Cloud Console

4. **"ModuleNotFoundError"**
   - → Missing dependency
   - → Fix: Check `requirements.txt` includes all packages

## ✅ Quick Checklist

- [ ] `GOOGLE_PLACES_API_KEY` added in Render Environment tab
- [ ] `APOLLO_API_KEY` added (optional but recommended)
- [ ] Service redeployed after adding variables
- [ ] No errors in Render logs
- [ ] Test search works

## 🎯 Expected Behavior After Fix

- Search should find 10-100 companies
- Results show company names, addresses, phone numbers
- Export to Excel works
- Progress bar shows search status

---

**Most Important**: Add `GOOGLE_PLACES_API_KEY` environment variable in Render, then redeploy!

