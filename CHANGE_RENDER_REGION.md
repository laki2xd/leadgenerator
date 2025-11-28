# 🌍 How to Change Region in Render

Guide to change your Render service region for better performance or compliance.

---

## 📍 Where to Change Region

### Option 1: During Service Creation (New Services)

If you're creating a new service:

1. **Create New Service**
   - Go to Render Dashboard → "New +" → "Web Service"
   - Connect your repository

2. **Find Region Setting**
   - In the service creation form
   - Look for **"Region"** dropdown
   - Usually near the top, below "Name" and "Environment"

3. **Select Region**
   - Choose from available regions:
     - **Oregon (US West)** - Default, good for US West Coast
     - **Ohio (US East)** - Good for US East Coast
     - **Frankfurt (EU)** - Good for Europe
     - **Singapore (Asia)** - Good for Asia-Pacific
     - **Sydney (Australia)** - Good for Australia

4. **Create Service**
   - Continue with other settings
   - Click "Create Web Service"

---

### Option 2: Change Existing Service Region

**Important**: You cannot directly change the region of an existing service in Render. You have two options:

#### **Option A: Create New Service in New Region** (Recommended)

1. **Create New Service**
   - Go to Render Dashboard → "New +" → "Web Service"
   - Connect the same repository
   - Select the **new region** you want
   - Use same settings (environment variables, disk, etc.)

2. **Update Domain/URL**
   - Your new service will have a new URL
   - Update any bookmarks or links
   - Optionally set up custom domain

3. **Delete Old Service** (Optional)
   - Once new service is working
   - Delete old service to avoid charges

#### **Option B: Contact Render Support**

1. **Contact Support**
   - Go to: Render Dashboard → Help/Support
   - Request region change for existing service
   - They may be able to migrate it

---

## 🌐 Available Regions

Render offers these regions:

| Region | Location | Best For |
|--------|----------|----------|
| **Oregon** | US West | US West Coast, Default |
| **Ohio** | US East | US East Coast |
| **Frankfurt** | Europe | European users |
| **Singapore** | Asia | Asia-Pacific users |
| **Sydney** | Australia | Australian users |

---

## 🎯 Which Region Should You Choose?

### Choose Based on Your Users:

- **Most users in US**: Choose **Oregon** or **Ohio**
- **Most users in Europe**: Choose **Frankfurt**
- **Most users in Asia**: Choose **Singapore**
- **Most users in Australia**: Choose **Sydney**
- **Global users**: Choose **Oregon** (default, good worldwide)

### For Your Lead Generator App:

Since you're searching for companies in **Canada & USA**, I recommend:
- **Oregon (US West)** - Good for both US and Canada
- **Ohio (US East)** - Also good, slightly closer to East Coast

---

## 📋 Step-by-Step: Create New Service in Different Region

If you want to change your existing service's region:

### Step 1: Note Your Current Settings

Before creating new service, note:
- Environment variables (API keys)
- Disk configuration
- Start command: `gunicorn app:app`
- Build command: `pip install -r requirements.txt`

### Step 2: Create New Service

1. **Go to Render Dashboard**
   - https://render.com
   - Click "New +" → "Web Service"

2. **Connect Repository**
   - Select: "Build and deploy from a Git repository"
   - Connect: `laki2xd/leadgenerator`
   - Or: "Public Git repository" → Enter: `https://github.com/laki2xd/leadgenerator`

3. **Configure Settings**
   - **Name**: `lead-generator` (or your choice)
   - **Region**: **Select your desired region** ← Important!
   - **Branch**: `main`
   - **Root Directory**: (leave empty)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

4. **Add Environment Variables**
   - Click "Advanced" or scroll to "Environment Variables"
   - Add:
     - `GOOGLE_PLACES_API_KEY` = `AIzaSyAhjUqCRHZH0rJgeKUYChIv2hJXVne_77Y`
     - `APOLLO_API_KEY` = `Fx9l0QJ5nzZbivE2FVXgcw`

5. **Add Disk** (Optional)
   - Go to "Disks" section
   - Click "Add Disk"
   - Name: `exports-disk`
   - Mount Path: `/opt/render/project/src/exports`
   - Size: `1 GB`

6. **Create Service**
   - Click "Create Web Service"
   - Wait for deployment

### Step 3: Update Domain (If Using Custom Domain)

If you had a custom domain:
1. Go to new service → Settings → Custom Domains
2. Add your domain
3. Update DNS records if needed

### Step 4: Test New Service

1. Visit your new service URL
2. Test search functionality
3. Verify everything works

### Step 5: Delete Old Service (Optional)

Once new service is working:
1. Go to old service → Settings
2. Scroll to bottom → "Delete Service"
3. Confirm deletion

---

## ⚠️ Important Notes

### Region Change Considerations:

1. **New URL**: Your service will have a new URL
   - Old: `https://leadgenerator-0vdk.onrender.com`
   - New: `https://leadgenerator-xxxx.onrender.com` (different ID)

2. **Data Migration**: 
   - Environment variables: Copy manually
   - Disk data: Not automatically migrated (if you have exports, download them first)

3. **Downtime**:
   - Brief downtime while switching
   - Can run both services simultaneously during transition

4. **Cost**: 
   - Free tier: Same limits regardless of region
   - Paid tiers: Same pricing

---

## 🔄 Using render.yaml (Automatic)

Your `render.yaml` doesn't specify a region, so Render uses default (Oregon).

To specify region in `render.yaml`, add:

```yaml
services:
  - type: web
    name: lead-generator
    region: oregon  # or: ohio, frankfurt, singapore, sydney
    env: python
    # ... rest of config
```

Then deploy - Render will use the specified region.

---

## ✅ Quick Checklist

- [ ] Decided on new region
- [ ] Noted current environment variables
- [ ] Created new service in new region
- [ ] Added environment variables to new service
- [ ] Added disk to new service (if needed)
- [ ] Tested new service
- [ ] Updated any bookmarks/links
- [ ] Deleted old service (optional)

---

## 🆘 Troubleshooting

### Can't Find Region Setting
- Make sure you're creating a NEW service
- Region is only available during creation
- Check if you're on the right page (Web Service creation)

### New Service Not Working
- Verify environment variables are added
- Check build logs for errors
- Ensure start command is correct: `gunicorn app:app`

### Want to Keep Same URL
- Use custom domain
- Set up domain on new service
- Update DNS if needed

---

**Recommendation**: For Canada & USA searches, **Oregon** or **Ohio** are both good choices. Oregon is the default and works well.

