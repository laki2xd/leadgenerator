# 🔧 Fix API Keys in Render - Step by Step

Guide to check, fix, and properly configure API keys in your Render service.

---

## 🔍 Step 1: Check Current API Keys

### How to View Your Environment Variables:

1. **Go to Render Dashboard**
   - https://render.com
   - Log in

2. **Open Your Service**
   - Click on your service: "leadgenerator" (or whatever you named it)

3. **Go to Environment Tab**
   - Click **"Environment"** tab (left sidebar)
   - Or scroll down to **"Environment Variables"** section

4. **Check What's There**
   - You should see a list of environment variables
   - Values are hidden (shown as dots) for security
   - Note which keys exist

---

## ✅ Step 2: Verify Correct API Keys

Your API keys should be:

### **Required:**
- **Key**: `GOOGLE_PLACES_API_KEY`
- **Value**: `AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y`

### **Optional (but you have it):**
- **Key**: `APOLLO_API_KEY`
- **Value**: `Fx9l0QJ5nzZbivE2FVXgcw`

---

## 🛠️ Step 3: Fix API Keys

### Option A: Edit Existing Keys

If keys exist but are wrong:

1. **Find the Key**
   - In Environment tab, find the key you want to fix
   - Click on it or click **"Edit"** button (if available)

2. **Update Value**
   - Change the value to the correct one
   - Make sure no extra spaces before/after
   - No quotes needed

3. **Save**
   - Click **"Save"** or **"Update"**

### Option B: Delete and Re-add (Recommended)

If keys are completely wrong:

1. **Delete Wrong Key**
   - Find the incorrect key
   - Click **"Delete"** or trash icon
   - Confirm deletion

2. **Add Correct Key**
   - Click **"Add Environment Variable"**
   - **Key**: `GOOGLE_PLACES_API_KEY`
   - **Value**: `AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y`
   - Click **"Save"**

3. **Repeat for Other Keys**
   - Add `APOLLO_API_KEY` = `Fx9l0QJ5nzZbivE2FVXgcw`

---

## ⚠️ Common Mistakes to Avoid

### ❌ Wrong: Adding Quotes
```
GOOGLE_PLACES_API_KEY = "AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y"
```
**Fix**: Remove quotes, just paste the key directly

### ❌ Wrong: Extra Spaces
```
GOOGLE_PLACES_API_KEY = AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y 
```
**Fix**: No spaces before or after the value

### ❌ Wrong: Wrong Key Name
```
GOOGLE_API_KEY = AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y
```
**Fix**: Must be exactly `GOOGLE_PLACES_API_KEY` (case-sensitive)

### ❌ Wrong: Missing Key
```
(No GOOGLE_PLACES_API_KEY at all)
```
**Fix**: Add the key

### ❌ Wrong: Incomplete Key
```
GOOGLE_PLACES_API_KEY = AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne
```
**Fix**: Copy the complete key from config.py

---

## 📋 Step-by-Step: Fix API Keys Properly

### Complete Fix Process:

1. **Go to Environment Tab**
   - Render Dashboard → Your Service → **"Environment"** tab

2. **Delete All Existing API Keys** (if wrong)
   - Find: `GOOGLE_PLACES_API_KEY`
   - Click **Delete** (if it exists and is wrong)
   - Find: `APOLLO_API_KEY`
   - Click **Delete** (if it exists and is wrong)

3. **Add GOOGLE_PLACES_API_KEY Correctly**
   - Click **"Add Environment Variable"**
   - **Key field**: Type exactly: `GOOGLE_PLACES_API_KEY`
     - Must be uppercase
     - Use underscores, not hyphens
     - No spaces
   - **Value field**: Paste exactly: `AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y`
     - No quotes
     - No spaces before/after
     - Complete key
   - Click **"Save"**

4. **Add APOLLO_API_KEY Correctly**
   - Click **"Add Environment Variable"** again
   - **Key field**: Type exactly: `APOLLO_API_KEY`
   - **Value field**: Paste exactly: `Fx9l0QJ5nzZbivE2FVXgcw`
   - Click **"Save"**

5. **Verify Both Keys Are There**
   - You should see:
     ```
     GOOGLE_PLACES_API_KEY    ••••••••••••••••
     APOLLO_API_KEY            •••••••••••••••
     ```
   - Values are hidden (dots) - that's normal and correct

---

## 🔄 Step 4: Redeploy After Fixing

After fixing API keys:

1. **Render Should Auto-Redeploy**
   - Render usually redeploys automatically when you change environment variables
   - Watch the "Logs" tab for deployment progress

2. **If Not Auto-Redeploying**
   - Go to: **"Manual Deploy"** tab
   - Click **"Deploy latest commit"**
   - Wait 2-5 minutes

3. **Check Deployment**
   - Go to **"Logs"** tab
   - Look for "Deploy successful" message
   - Check for any errors

---

## ✅ Step 5: Verify It's Fixed

### Test Your Website:

1. **Visit Your Site**
   - Go to: https://leadgenerator-0vdk.onrender.com/

2. **Test Search**
   - Try searching for: "Manufacturing" or "Warehouse"
   - Should now find companies (not 0 results)

3. **Check Browser Console** (Optional)
   - Press F12 → Console tab
   - Look for errors
   - Should see successful API calls

---

## 🔍 How to Verify Keys Are Correct

### Check Render Logs:

1. **Go to Logs Tab**
   - Your Service → **"Logs"** tab

2. **Look for These Errors:**

   **If you see:**
   ```
   No API keys configured
   ```
   → Keys not added or wrong names

   **If you see:**
   ```
   REQUEST_DENIED
   ```
   → API key is invalid or wrong value

   **If you see:**
   ```
   OVER_QUERY_LIMIT
   ```
   → API key is correct but quota exceeded

   **If you see:**
   ```
   ModuleNotFoundError
   ```
   → Not an API key issue, missing dependency

---

## 📋 Correct API Key Format

### What It Should Look Like in Render:

```
Environment Variables
┌─────────────────────────────────────┐
│ Key                          Value  │
├─────────────────────────────────────┤
│ GOOGLE_PLACES_API_KEY       ••••••  │
│ APOLLO_API_KEY              ••••••  │
└─────────────────────────────────────┘
```

### Key Requirements:

✅ **Key Name**: Exact match, case-sensitive
- `GOOGLE_PLACES_API_KEY` ✅
- `google_places_api_key` ❌
- `GOOGLE-PLACES-API-KEY` ❌

✅ **Value**: Complete key, no quotes, no spaces
- `AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y` ✅
- `"AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y"` ❌
- ` AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y ` ❌

---

## 🆘 Troubleshooting

### Keys Not Saving

**Problem**: Can't save environment variables

**Solutions**:
- Make sure you're on the correct service
- Check you have permission (owner/admin)
- Try refreshing the page
- Check for typos in key name

### Keys Saved But Not Working

**Problem**: Keys are there but search still returns 0 results

**Solutions**:
1. **Redeploy**: Manual Deploy → Deploy latest commit
2. **Check Logs**: Look for API errors
3. **Verify Values**: Make sure keys are complete (no truncation)
4. **Test API Keys**: Verify keys work in Google Cloud Console

### Can't Find Environment Tab

**Problem**: Don't see Environment tab

**Solutions**:
- Make sure you're on the Web Service page (not dashboard)
- Scroll down - might be below other sections
- Try refreshing the page
- Check you're the owner/admin

---

## ✅ Final Checklist

After fixing API keys:

- [ ] `GOOGLE_PLACES_API_KEY` exists in Environment tab
- [ ] Key name is exactly `GOOGLE_PLACES_API_KEY` (uppercase, underscores)
- [ ] Value is complete key (no quotes, no spaces)
- [ ] `APOLLO_API_KEY` exists (if using)
- [ ] Service redeployed after changes
- [ ] No errors in logs
- [ ] Search works on website (finds companies)

---

## 🎯 Quick Fix Summary

**If API keys are wrong:**

1. Go to: Render Dashboard → Your Service → **Environment** tab
2. Delete wrong keys (if any)
3. Add correct keys:
   - `GOOGLE_PLACES_API_KEY` = `AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y`
   - `APOLLO_API_KEY` = `Fx9l0QJ5nzZbivE2FVXgcw`
4. Save each key
5. Wait for auto-redeploy (or manually deploy)
6. Test your website

---

**Need help?** Tell me what you see in the Environment tab and I'll help you fix it!

