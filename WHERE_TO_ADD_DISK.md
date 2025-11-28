# 📍 Where to Add Persistent Disk in Render

Step-by-step guide to find the Disks section in Render dashboard.

---

## 🎯 Location: Disks Tab

The persistent disk option is in the **"Disks"** section of your Render service.

---

## 📋 Step-by-Step Instructions

### Step 1: Go to Your Web Service

1. **Log in to Render**
   - Go to https://render.com
   - Log in with your GitHub account

2. **Open Your Dashboard**
   - Click **"Dashboard"** (top navigation)
   - You'll see a list of your services

3. **Click on Your Service**
   - Find your service (e.g., "lead-generator" or whatever you named it)
   - Click on the service name to open it

### Step 2: Find the Disks Section

Once you're on your service page, look for the **"Disks"** tab. It can be in two places:

#### **Option A: Left Sidebar (Most Common)**

Look at the **left sidebar menu**. You should see tabs like:
- Overview
- Logs
- Metrics
- Environment
- **Disks** ← Click here!
- Settings
- etc.

#### **Option B: Scroll Down**

If you don't see "Disks" in the sidebar:

1. Scroll down on the service page
2. Look for sections like:
   - Environment Variables
   - **Disks** ← Look for this section
   - Settings
   - etc.

### Step 3: Add Disk

Once you find the Disks section:

1. **Click "Add Disk"** or **"Create Disk"** button
   - Usually a green or blue button
   - May say "Add Disk", "Create Disk", or "+ Add Disk"

2. **Fill in the form** that appears:
   - **Name**: `exports-disk`
   - **Mount Path**: `/opt/render/project/src/exports`
   - **Size**: `1 GB`

3. **Click "Create Disk"** or **"Save"**

---

## 🖼️ Visual Guide

### What the Disks Section Looks Like:

```
┌─────────────────────────────────────────────────┐
│  Your Service: lead-generator                   │
├─────────────────────────────────────────────────┤
│                                                  │
│  [Overview] [Logs] [Environment] [Disks] [Settings]  ← Left Sidebar
│                                                  │
│  Disks                                          │
│  ──────                                         │
│                                                  │
│  No disks attached                              │
│                                                  │
│  [+ Add Disk]  ← Click this button              │
│                                                  │
└─────────────────────────────────────────────────┘
```

### After Adding Disk:

```
┌─────────────────────────────────────────────────┐
│  Disks                                          │
│  ──────                                         │
│                                                  │
│  Name         Mount Path              Size      │
│  ────────────────────────────────────────────  │
│  exports-disk /opt/render/.../exports  1 GB    │
│                                                  │
│  [+ Add Disk]                                   │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## 🔍 Can't Find Disks Section?

### Troubleshooting:

1. **Make sure you're on the Web Service page**
   - Not the main dashboard
   - Click on your service name first

2. **Check if you're on Free Tier**
   - Free tier supports disks
   - If you don't see it, try refreshing the page

3. **Look in different places:**
   - Left sidebar tabs
   - Scroll down below Environment Variables
   - Check Settings tab (sometimes it's there)

4. **Try different views:**
   - Some Render interfaces have tabs at the top instead of sidebar
   - Look for "Disks" tab anywhere on the page

---

## 📱 Alternative: Using render.yaml

If you can't find the Disks section in the UI, you can also configure it in `render.yaml`:

Your `render.yaml` already has disk configuration! Render should automatically create it when you deploy.

Check your `render.yaml` file - it should have:
```yaml
disk:
  name: exports-disk
  mountPath: /opt/render/project/src/exports
  sizeGB: 1
```

If `render.yaml` has this, Render will create the disk automatically during deployment!

---

## ✅ Quick Checklist

- [ ] Logged into Render dashboard
- [ ] Clicked on your web service
- [ ] Found "Disks" tab (sidebar or scroll down)
- [ ] Clicked "Add Disk" button
- [ ] Filled in: Name, Mount Path, Size
- [ ] Clicked "Create Disk"

---

## 🆘 Still Can't Find It?

**Option 1: Check render.yaml**
- Your `render.yaml` file already has disk configuration
- Render should create it automatically
- Check if disk appears after deployment

**Option 2: Contact Render Support**
- Go to Render dashboard → Help/Support
- Ask: "Where do I add persistent disks?"

**Option 3: Use Render CLI**
- Install Render CLI
- Create disk via command line

---

**Most Common Location**: Left sidebar → "Disks" tab → "Add Disk" button

**If using render.yaml**: The disk should be created automatically when you deploy!

