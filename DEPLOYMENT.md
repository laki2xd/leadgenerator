# Deployment Guide

This guide covers deploying your Lead Generator Flask application to various platforms.

## 🚀 Recommended: Render (Free Tier Available)

Render is the best option for Flask apps with file storage needs.

### Steps:

1. **Create a Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Connect Your Repository**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository

3. **Configure Settings**
   - **Name**: `lead-generator` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (or paid for more resources)

4. **Add Environment Variables**
   Click "Environment" and add:
   - `GOOGLE_PLACES_API_KEY` = (your key)
   - `YELP_API_KEY` = (your key, optional)
   - `APOLLO_API_KEY` = (your key, optional)
   - `CLEARBIT_API_KEY` = (your key, optional)
   - `ZOOMINFO_API_KEY` = (your key, optional)

5. **Add Persistent Disk (for exports)**
   - Go to "Disks" tab
   - Click "Add Disk"
   - Name: `exports-disk`
   - Mount Path: `/opt/render/project/src/exports`
   - Size: 1 GB

6. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Your app will be live at `https://your-app-name.onrender.com`

### Render Free Tier Limits:
- 750 hours/month (enough for always-on)
- Sleeps after 15 minutes of inactivity
- 512 MB RAM
- Persistent disk available

---

## 🚂 Alternative: Railway

Railway is another excellent option with a free tier.

### Steps:

1. **Create Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **New Project**
   - Click "New Project"
   - "Deploy from GitHub repo"
   - Select your repository

3. **Configure**
   - Railway auto-detects Python
   - Add environment variables in "Variables" tab:
     - `GOOGLE_PLACES_API_KEY`
     - `YELP_API_KEY` (optional)
     - `APOLLO_API_KEY` (optional)
     - etc.

4. **Deploy**
   - Railway automatically deploys
   - Get your URL from "Settings" → "Generate Domain"

### Railway Free Tier:
- $5 credit/month
- Pay-as-you-go after credit

---

## 🦅 Alternative: Fly.io

Great for Flask apps with global distribution.

### Steps:

1. **Install Fly CLI**
   ```bash
   # Windows (PowerShell)
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   ```

2. **Login**
   ```bash
   fly auth login
   ```

3. **Create App**
   ```bash
   fly launch
   ```
   - Follow prompts
   - Don't deploy yet

4. **Configure**
   - Edit `fly.toml` (created automatically)
   - Add environment variables:
   ```bash
   fly secrets set GOOGLE_PLACES_API_KEY=your-key
   fly secrets set YELP_API_KEY=your-key
   ```

5. **Deploy**
   ```bash
   fly deploy
   ```

---

## ⚠️ Netlify (Not Recommended - Limited Functionality)

**Important**: Netlify is NOT ideal for this Flask app because:
- ❌ No persistent file storage (exports won't work)
- ❌ Serverless functions have 10-second timeout (searches take longer)
- ❌ No persistent state (progress tracking won't work)

If you still want to try Netlify, you'll need to:
1. Convert Flask routes to Netlify Functions
2. Use external storage (S3) for exports
3. Use external database for progress tracking
4. Accept timeout limitations

**Better**: Use Render or Railway instead.

---

## 🔧 Pre-Deployment Checklist

Before deploying, ensure:

- [ ] `config.py` is in `.gitignore` (already done)
- [ ] API keys are NOT committed to git
- [ ] `requirements.txt` includes all dependencies
- [ ] `Procfile` exists (for Heroku/Railway)
- [ ] `runtime.txt` specifies Python version
- [ ] Test locally: `gunicorn app:app`

---

## 📝 Environment Variables Setup

All platforms require these environment variables:

**Required:**
- `GOOGLE_PLACES_API_KEY` - Your Google Places API key

**Optional:**
- `YELP_API_KEY` - Yelp API key
- `APOLLO_API_KEY` - Apollo.io API key
- `CLEARBIT_API_KEY` - Clearbit API key
- `ZOOMINFO_API_KEY` - ZoomInfo API key

**Note**: Never commit `config.py` with real API keys to git!

---

## 🐛 Troubleshooting

### "Module not found" errors
- Ensure `requirements.txt` has all dependencies
- Check that `gunicorn` is in requirements.txt

### "Port already in use"
- Render/Railway handle ports automatically
- Don't hardcode port 5000 in production

### Exports folder not working
- On Render: Add persistent disk
- On Railway: Use volume mounts
- On Fly.io: Use volumes

### API keys not working
- Verify environment variables are set correctly
- Check for typos in variable names
- Ensure no quotes around values

---

## 🎯 Quick Deploy Commands

### Render
```bash
# Just push to GitHub, Render auto-deploys
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Railway
```bash
# Railway auto-detects and deploys
git push origin main
```

### Fly.io
```bash
fly launch
fly secrets set GOOGLE_PLACES_API_KEY=your-key
fly deploy
```

---

## 📚 Additional Resources

- [Render Docs](https://render.com/docs)
- [Railway Docs](https://docs.railway.app)
- [Fly.io Docs](https://fly.io/docs)
- [Gunicorn Docs](https://gunicorn.org)

---

**Recommendation**: Start with **Render** - it's the easiest and most suitable for this Flask app!

