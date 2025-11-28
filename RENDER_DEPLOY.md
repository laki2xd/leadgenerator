# 🚀 Quick Deploy to Render (Recommended)

Render is the **best option** for this Flask app because it supports:
- ✅ Persistent file storage (for exports)
- ✅ Long-running requests (no timeout issues)
- ✅ Free tier available
- ✅ Easy setup

## Step-by-Step Guide

### 1. Prepare Your Code

Make sure your code is ready:
- ✅ All files committed to Git
- ✅ `config.py` is NOT committed (it's in `.gitignore`)
- ✅ `requirements.txt` includes `gunicorn`

### 2. Push to GitHub

If you haven't already, push your code to GitHub:

```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### 3. Create Render Account

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with GitHub (recommended)

### 4. Create New Web Service

1. Click "New +" → "Web Service"
2. Click "Connect account" if prompted
3. Select your repository: `Lead Generator`
4. Click "Connect"

### 5. Configure Your Service

Fill in these settings:

**Basic Settings:**
- **Name**: `lead-generator` (or your choice)
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main` (or your default branch)

**Build & Deploy:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

**Plan:**
- Select **Free** (or paid for better performance)

### 6. Add Environment Variables

Scroll down to "Environment Variables" and click "Add Environment Variable" for each:

1. **GOOGLE_PLACES_API_KEY**
   - Key: `GOOGLE_PLACES_API_KEY`
   - Value: (paste your key from config.py)

2. **APOLLO_API_KEY** (if you have it)
   - Key: `APOLLO_API_KEY`
   - Value: (paste your key)

3. **YELP_API_KEY** (optional)
   - Key: `YELP_API_KEY`
   - Value: (paste your key or leave empty)

4. **CLEARBIT_API_KEY** (optional)
   - Key: `CLEARBIT_API_KEY`
   - Value: (paste your key or leave empty)

5. **ZOOMINFO_API_KEY** (optional)
   - Key: `ZOOMINFO_API_KEY`
   - Value: (paste your key or leave empty)

### 7. Add Persistent Disk (Important!)

This allows exports to persist:

1. Scroll to "Disks" section
2. Click "Add Disk"
3. Configure:
   - **Name**: `exports-disk`
   - **Mount Path**: `/opt/render/project/src/exports`
   - **Size**: `1 GB` (or more if needed)
4. Click "Save"

### 8. Deploy!

1. Scroll to bottom
2. Click "Create Web Service"
3. Wait 5-10 minutes for first deployment
4. Watch the logs for progress

### 9. Access Your App

Once deployed:
- Your app URL: `https://lead-generator.onrender.com` (or your custom name)
- Click the URL to open your app!

### 10. Set Up Custom Domain (Optional)

1. Go to "Settings" → "Custom Domains"
2. Add your domain
3. Follow DNS setup instructions

---

## 🔄 Updating Your App

After making changes:

```bash
git add .
git commit -m "Update app"
git push origin main
```

Render will automatically redeploy!

---

## 📊 Monitoring

- **Logs**: Click "Logs" tab to see real-time logs
- **Metrics**: View CPU, memory, and request stats
- **Events**: See deployment history

---

## 🆘 Troubleshooting

### App won't start
- Check logs for errors
- Verify all environment variables are set
- Ensure `gunicorn` is in requirements.txt

### Exports not saving
- Verify disk is mounted correctly
- Check disk mount path matches: `/opt/render/project/src/exports`
- Ensure disk has space

### API errors
- Verify API keys are correct
- Check API quotas/limits
- Review logs for specific error messages

### Slow performance
- Free tier sleeps after 15 min inactivity
- First request after sleep takes ~30 seconds
- Consider paid tier for always-on

---

## 💰 Pricing

**Free Tier:**
- 750 hours/month
- Sleeps after 15 min inactivity
- 512 MB RAM
- Perfect for testing/small projects

**Starter ($7/month):**
- Always on
- 512 MB RAM
- Better for production

**Standard ($25/month):**
- Always on
- 2 GB RAM
- Best for production

---

## ✅ Success Checklist

- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Web service created
- [ ] Environment variables added
- [ ] Persistent disk added
- [ ] App deployed successfully
- [ ] App accessible via URL
- [ ] Test search functionality
- [ ] Test export functionality

---

**Need help?** Check Render docs: https://render.com/docs

