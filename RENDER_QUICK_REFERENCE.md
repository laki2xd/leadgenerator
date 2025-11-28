# 🚀 Render Quick Reference - Your API Keys

Quick copy-paste reference for adding environment variables to Render.

---

## 📋 Step 6: Environment Variables to Add

Copy these from your `config.py` file and add them in Render:

### **Required:**

**GOOGLE_PLACES_API_KEY**
- **Value**: `AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y`
- Copy from: `config.py` line 5

### **Optional (but you have it):**

**APOLLO_API_KEY**
- **Value**: `Fx9l0QJ5nzZbivE2FVXgcw`
- Copy from: `config.py` line 14

### **Optional (empty - skip these):**

- `YELP_API_KEY` - Empty in your config, skip it
- `CLEARBIT_API_KEY` - Empty in your config, skip it
- `ZOOMINFO_API_KEY` - Empty in your config, skip it

---

## 📋 Step 7: Persistent Disk Settings

**Name**: `exports-disk`

**Mount Path**: `/opt/render/project/src/exports`

**Size**: `1 GB`

---

## 🎯 Quick Steps in Render Dashboard

### For Environment Variables:

1. Go to your service → **"Environment"** tab
2. Click **"Add Environment Variable"**
3. Add these two:

   ```
   Key: GOOGLE_PLACES_API_KEY
   Value: AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y
   ```

   ```
   Key: APOLLO_API_KEY
   Value: Fx9l0QJ5nzZbivE2FVXgcw
   ```

### For Persistent Disk:

1. Go to your service → **"Disks"** tab
2. Click **"Add Disk"**
3. Fill in:
   - **Name**: `exports-disk`
   - **Mount Path**: `/opt/render/project/src/exports`
   - **Size**: `1 GB`
4. Click **"Create Disk"**

---

## ✅ Checklist

- [ ] `GOOGLE_PLACES_API_KEY` added to Render
- [ ] `APOLLO_API_KEY` added to Render
- [ ] Persistent disk created
- [ ] Mount path is `/opt/render/project/src/exports`
- [ ] Disk size is 1 GB
- [ ] Service redeployed successfully

---

**That's it!** After adding these, your app will be ready to use on Render.

