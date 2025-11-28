# 🔧 Render: Add Environment Variables & Persistent Disk

Step-by-step guide for steps 6 and 7 of Render deployment.

---

## ✅ Step 6: Add Environment Variables (API Keys)

Environment variables store your API keys securely. Render will use these instead of `config.py`.

### How to Add Environment Variables:

1. **Go to Your Render Dashboard**
   - Log in to https://render.com
   - Click on your web service (e.g., "lead-generator")

2. **Navigate to Environment Tab**
   - In your service dashboard, click **"Environment"** tab (left sidebar)
   - Or scroll down to the **"Environment Variables"** section

3. **Add Each API Key**

   Click **"Add Environment Variable"** for each key:

   #### **Required: Google Places API Key**
   - **Key**: `GOOGLE_PLACES_API_KEY`
   - **Value**: Paste your key from `config.py` (starts with `AIzaSy...`)
   - Click **"Save"**

   #### **Optional: Apollo API Key**
   - **Key**: `APOLLO_API_KEY`
   - **Value**: Paste your key from `config.py` (if you have one)
   - Click **"Save"**

   #### **Optional: Yelp API Key**
   - **Key**: `YELP_API_KEY`
   - **Value**: Paste your key from `config.py` (if you have one)
   - Click **"Save"**

   #### **Optional: Clearbit API Key**
   - **Key**: `CLEARBIT_API_KEY`
   - **Value**: Paste your key from `config.py` (if you have one)
   - Click **"Save"**

   #### **Optional: ZoomInfo API Key**
   - **Key**: `ZOOMINFO_API_KEY`
   - **Value**: Paste your key from `config.py` (if you have one)
   - Click **"Save"**

4. **Verify All Variables Added**
   - You should see all your environment variables listed
   - Values are hidden (shown as dots) for security
   - Make sure all required keys are there

### 📋 Quick Checklist:

- [ ] `GOOGLE_PLACES_API_KEY` added
- [ ] `APOLLO_API_KEY` added (if you have it)
- [ ] `YELP_API_KEY` added (if you have it)
- [ ] `CLEARBIT_API_KEY` added (if you have it)
- [ ] `ZOOMINFO_API_KEY` added (if you have it)

### ⚠️ Important Notes:

- **No quotes needed**: Just paste the key value directly
- **Case sensitive**: Use exact key names (all uppercase)
- **No spaces**: Don't add spaces before/after the value
- **Copy from config.py**: Your keys are in `C:\Users\user\Desktop\Website\Lead Generator\config.py`

---

## ✅ Step 7: Add Persistent Disk (for Exports)

The persistent disk allows your `exports/` folder to persist between deployments and restarts.

### Why You Need This:

- Without a disk: Exported Excel files disappear when the app restarts
- With a disk: Exported files are saved permanently

### How to Add Persistent Disk:

1. **Go to Your Service Dashboard**
   - In Render, click on your web service
   - Look for **"Disks"** tab in the left sidebar
   - Or scroll down to find **"Disks"** section

2. **Add New Disk**
   - Click **"Add Disk"** or **"Create Disk"** button
   - A form will appear

3. **Configure Disk Settings**

   Fill in these values:

   - **Name**: `exports-disk`
     - This is just a label for your reference

   - **Mount Path**: `/opt/render/project/src/exports`
     - ⚠️ **IMPORTANT**: This must be exact!
     - This tells Render where to mount the disk
     - Your app expects exports in the `exports/` folder

   - **Size**: `1 GB` (or more if needed)
     - 1 GB is usually enough for many Excel files
     - You can increase later if needed
     - Free tier allows up to 1 GB

4. **Save Disk**
   - Click **"Create Disk"** or **"Save"**
   - Render will create and attach the disk

5. **Verify Disk is Attached**
   - You should see `exports-disk` listed in the Disks section
   - Status should show as "Attached" or "Active"
   - The mount path should be visible

### 📋 Disk Configuration Summary:

```
Name: exports-disk
Mount Path: /opt/render/project/src/exports
Size: 1 GB
```

### ⚠️ Important Notes:

- **Mount Path is Critical**: Must be `/opt/render/project/src/exports`
- **Case Sensitive**: Use exact path (lowercase)
- **Restart Required**: After adding disk, Render will restart your service
- **First Deploy**: If you add disk before first deploy, it will be ready from the start

---

## 🔄 After Adding Environment Variables & Disk

1. **Render Will Auto-Redeploy**
   - After adding environment variables, Render may restart your service
   - After adding disk, Render will restart your service
   - This is normal - wait for deployment to complete

2. **Check Deployment Logs**
   - Go to **"Logs"** tab
   - Watch for any errors
   - Look for "Deploy successful" message

3. **Test Your App**
   - Visit your Render URL (e.g., `https://lead-generator.onrender.com`)
   - Try searching for companies
   - Try exporting to Excel
   - Verify exports are saved

---

## 🆘 Troubleshooting

### Environment Variables Not Working

**Problem**: App says "No API keys configured"

**Solutions**:
- Check variable names are exact (case-sensitive)
- Verify values were copied correctly (no extra spaces)
- Make sure you clicked "Save" after adding each variable
- Check logs for specific error messages

### Disk Not Working

**Problem**: Exports folder is empty or files disappear

**Solutions**:
- Verify mount path is exact: `/opt/render/project/src/exports`
- Check disk is "Attached" in Disks section
- Restart your service after adding disk
- Check disk has available space

### Can't Find Disks Section

**Problem**: Don't see "Disks" tab

**Solutions**:
- Make sure you're on the Web Service page (not dashboard)
- Scroll down - Disks section might be below Environment Variables
- Free tier supports disks - you should see the option
- Try refreshing the page

---

## 📸 Visual Guide Reference

### Environment Variables Section:
```
Environment Variables
┌─────────────────────────────────────┐
│ Key                          Value  │
├─────────────────────────────────────┤
│ GOOGLE_PLACES_API_KEY       ••••••  │
│ APOLLO_API_KEY              ••••••  │
│ YELP_API_KEY                ••••••  │
└─────────────────────────────────────┘
[+ Add Environment Variable]
```

### Disks Section:
```
Disks
┌─────────────────────────────────────────────┐
│ Name         Mount Path              Size   │
├─────────────────────────────────────────────┤
│ exports-disk /opt/render/.../exports  1 GB  │
└─────────────────────────────────────────────┘
[+ Add Disk]
```

---

## ✅ Final Checklist

Before deploying, make sure:

- [ ] All environment variables added (at least `GOOGLE_PLACES_API_KEY`)
- [ ] Persistent disk created
- [ ] Disk mount path is correct: `/opt/render/project/src/exports`
- [ ] Disk size is set (1 GB minimum)
- [ ] Service is ready to deploy

---

## 🎯 Next Steps

After completing steps 6 and 7:

1. ✅ Environment variables added
2. ✅ Persistent disk added
3. **Deploy your service** (if not already deployed)
4. **Test your app** at your Render URL
5. **Verify exports work** by downloading an Excel file

---

**Need help?** Check Render docs: https://render.com/docs or your service logs for specific errors.

