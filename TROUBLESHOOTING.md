# 🔧 Troubleshooting Render Deployment

Guide to fix common issues with your deployed website.

---

## 🆘 What's Not Working?

Please tell me:
1. **What error do you see?** (Error message, blank page, etc.)
2. **Where is it happening?** (Homepage, search, export, etc.)
3. **What's the URL?** (Your Render URL)

---

## 🔍 Common Issues & Fixes

### Issue 1: "Application Error" or Blank Page

**Possible Causes:**
- Build failed
- Start command incorrect
- Missing dependencies
- Port configuration issue

**How to Fix:**

1. **Check Build Logs**
   - Go to Render dashboard → Your service → **"Logs"** tab
   - Look for error messages (red text)
   - Common errors:
     - `ModuleNotFoundError` - Missing dependency
     - `Port already in use` - Port issue
     - `Command not found` - Wrong start command

2. **Verify Start Command**
   - Should be: `gunicorn app:app`
   - Check: Settings → Start Command

3. **Check Build Command**
   - Should be: `pip install -r requirements.txt`
   - Check: Settings → Build Command

---

### Issue 2: "No API keys configured"

**Symptoms:**
- Page loads but shows "No API keys configured"
- Search doesn't work

**How to Fix:**

1. **Check Environment Variables**
   - Go to: Your service → **"Environment"** tab
   - Verify these exist:
     - `GOOGLE_PLACES_API_KEY`
     - `APOLLO_API_KEY` (if you added it)
   - Check values are correct (no extra spaces)

2. **Redeploy After Adding Variables**
   - After adding environment variables, Render should auto-redeploy
   - If not, go to: **"Manual Deploy"** → **"Deploy latest commit"**

---

### Issue 3: Search Not Working / Timeout

**Symptoms:**
- Search button does nothing
- "Searching..." forever
- Timeout errors

**Possible Causes:**
- API keys not set
- API quota exceeded
- Network issues
- Long-running requests

**How to Fix:**

1. **Check API Keys**
   - Verify environment variables are set
   - Test API keys locally first

2. **Check API Quotas**
   - Google Places API: Check Google Cloud Console
   - Apollo API: Check Apollo dashboard
   - Free tiers have limits

3. **Check Logs**
   - Look for API errors in Render logs
   - Check for "quota exceeded" or "unauthorized" errors

---

### Issue 4: Export Not Working

**Symptoms:**
- Export button doesn't work
- Files not saving
- "Export failed" error

**Possible Causes:**
- Disk not mounted
- Disk path incorrect
- Permissions issue

**How to Fix:**

1. **Verify Disk is Attached**
   - Go to: Your service → **"Disks"** tab
   - Check disk exists and is "Attached"
   - Mount path: `/opt/render/project/src/exports`

2. **Check Disk Path in Code**
   - Your code should use: `exports/` folder
   - Render mounts disk to: `/opt/render/project/src/exports`
   - Make sure they match

---

### Issue 5: "502 Bad Gateway" or "503 Service Unavailable"

**Symptoms:**
- Page shows 502/503 error
- Service appears down

**How to Fix:**

1. **Check Service Status**
   - Render dashboard → Your service
   - Status should be "Live" (green)
   - If "Stopped" or "Error", check logs

2. **Check Logs**
   - Look for startup errors
   - Check if app crashed
   - Look for Python errors

3. **Restart Service**
   - Go to: Settings → **"Manual Deploy"**
   - Click **"Deploy latest commit"**

---

### Issue 6: CORS Errors

**Symptoms:**
- Browser console shows CORS errors
- API requests fail
- "Access-Control-Allow-Origin" errors

**How to Fix:**

- Your code already has `CORS(app)` - should be fine
- If errors persist, check Render logs

---

## 🔍 How to Check Logs

1. **Go to Render Dashboard**
   - https://render.com
   - Click your service

2. **Open Logs Tab**
   - Click **"Logs"** in left sidebar
   - Or scroll to "Logs" section

3. **Look for Errors**
   - Red text = errors
   - Yellow text = warnings
   - Check recent logs (most recent at bottom)

4. **Common Error Messages:**
   ```
   ModuleNotFoundError: No module named 'X'
   → Missing dependency in requirements.txt
   
   Port 10000 already in use
   → Port conflict (rare on Render)
   
   Application failed to respond
   → App crashed or wrong start command
   
   No API keys configured
   → Environment variables not set
   ```

---

## ✅ Quick Checklist

Run through this checklist:

- [ ] Service status is "Live" (green)
- [ ] Build completed successfully (check logs)
- [ ] Start command is: `gunicorn app:app`
- [ ] Build command is: `pip install -r requirements.txt`
- [ ] Environment variables are set:
  - [ ] `GOOGLE_PLACES_API_KEY`
  - [ ] `APOLLO_API_KEY` (if using)
- [ ] Disk is attached (if using exports)
- [ ] No errors in logs
- [ ] API keys are valid (test locally)

---

## 🛠️ Debugging Steps

### Step 1: Check Service Status
- Render dashboard → Your service
- Is it "Live" or showing an error?

### Step 2: Check Build Logs
- Click "Logs" tab
- Scroll to build section
- Look for errors during `pip install`

### Step 3: Check Runtime Logs
- Scroll to runtime logs (after build)
- Look for errors when starting
- Check for Python tracebacks

### Step 4: Test Locally First
- Make sure it works on `localhost:5000`
- If local works but Render doesn't, it's a deployment issue

### Step 5: Verify Configuration
- Check all settings match recommendations
- Verify environment variables
- Confirm disk is attached

---

## 📞 Need More Help?

**Share these details:**
1. Your Render URL
2. Error message (if any)
3. What happens when you visit the site
4. Recent logs (copy/paste errors)

**Or check:**
- Render logs for specific errors
- Browser console (F12) for frontend errors
- Network tab for failed requests

---

## 🎯 Most Common Fixes

1. **Add missing environment variables**
2. **Fix start command** (`gunicorn app:app`)
3. **Check build logs** for missing dependencies
4. **Redeploy** after making changes
5. **Verify API keys** are correct

---

**Tell me what error you're seeing and I'll help you fix it!**

