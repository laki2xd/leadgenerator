# 📦 Push Your Code to GitHub - Complete Guide

This guide will walk you through pushing your Lead Generator code to GitHub so you can deploy it to Render.

---

## Step 1: Install Git

### Option A: Download Git for Windows (Recommended)

1. **Download Git**
   - Go to https://git-scm.com/download/win
   - Download the latest version (64-bit)
   - Run the installer

2. **Installation Settings**
   - Click "Next" through most screens
   - **Important**: Choose "Git from the command line and also from 3rd-party software"
   - Use default options for everything else
   - Click "Install"

3. **Verify Installation**
   - Open a **new** PowerShell window (close and reopen)
   - Run: `git --version`
   - You should see something like: `git version 2.x.x`

### Option B: Install via Winget (Windows Package Manager)

If you have winget installed:

```powershell
winget install --id Git.Git -e --source winget
```

---

## Step 2: Configure Git (One-time setup)

Open PowerShell and run these commands (replace with your info):

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Example:**
```powershell
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
```

---

## Step 3: Create GitHub Account (if you don't have one)

1. Go to https://github.com
2. Click "Sign up"
3. Enter your email, password, and username
4. Verify your email
5. Complete the setup

---

## Step 4: Create a New Repository on GitHub

1. **Log in to GitHub**
   - Go to https://github.com
   - Log in with your account

2. **Create New Repository**
   - Click the **"+"** icon in the top right
   - Select **"New repository"**

3. **Repository Settings**
   - **Repository name**: `lead-generator` (or your choice)
   - **Description**: "Lead Generator - Find B2B companies in Canada & USA"
   - **Visibility**: 
     - ✅ **Public** (free, anyone can see code)
     - ⚠️ **Private** (free for personal accounts, but API keys should still be in .gitignore)
   - **DO NOT** check "Add a README file" (we already have files)
   - **DO NOT** add .gitignore or license (we already have them)
   - Click **"Create repository"**

4. **Copy the Repository URL**
   - GitHub will show you a page with setup instructions
   - **Copy the HTTPS URL** (looks like: `https://github.com/yourusername/lead-generator.git`)
   - You'll need this in the next step!

---

## Step 5: Initialize Git in Your Project

Open PowerShell in your project folder (`C:\Users\user\Desktop\Website\Lead Generator`) and run:

```powershell
# Navigate to your project (if not already there)
cd "C:\Users\user\Desktop\Website\Lead Generator"

# Initialize git repository
git init

# Check what files will be added
git status
```

---

## Step 6: Add Files to Git

**Important**: Make sure `config.py` is NOT committed (it contains your API keys!)

```powershell
# Add all files (except those in .gitignore)
git add .

# Verify config.py is NOT being added
git status
```

You should see `config.py` is NOT listed (it's in `.gitignore` - good!).

---

## Step 7: Make Your First Commit

```powershell
git commit -m "Initial commit - Lead Generator Flask app"
```

---

## Step 8: Connect to GitHub and Push

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name:

```powershell
# Add GitHub as remote (replace with YOUR repository URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Example:
# git remote add origin https://github.com/johndoe/lead-generator.git

# Rename default branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**First time pushing?**
- GitHub will ask for your username and password
- **Username**: Your GitHub username
- **Password**: Use a **Personal Access Token** (see below)

---

## Step 9: Create Personal Access Token (for password)

GitHub no longer accepts passwords. You need a token:

1. **Go to GitHub Settings**
   - Click your profile picture → **Settings**
   - Scroll down → **Developer settings**
   - Click **Personal access tokens** → **Tokens (classic)**
   - Click **Generate new token** → **Generate new token (classic)**

2. **Configure Token**
   - **Note**: "Git Push Token" (or any name)
   - **Expiration**: Choose duration (90 days recommended)
   - **Scopes**: Check ✅ **repo** (all repo permissions)
   - Click **Generate token**

3. **Copy Token**
   - ⚠️ **IMPORTANT**: Copy the token NOW (you won't see it again!)
   - It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

4. **Use Token as Password**
   - When Git asks for password, paste the token instead
   - Username: Your GitHub username
   - Password: The token you just copied

---

## Step 10: Verify Push Success

1. **Refresh GitHub**
   - Go to your repository page on GitHub
   - You should see all your files!

2. **Verify config.py is NOT there**
   - Check that `config.py` is NOT visible (it's in `.gitignore`)
   - ✅ This is correct - API keys should never be on GitHub!

---

## ✅ Success Checklist

- [ ] Git installed
- [ ] Git configured with name and email
- [ ] GitHub account created
- [ ] Repository created on GitHub
- [ ] Git initialized in project folder
- [ ] Files added to git
- [ ] First commit made
- [ ] Remote repository connected
- [ ] Code pushed to GitHub
- [ ] Files visible on GitHub
- [ ] config.py NOT visible (good!)

---

## 🔄 Updating Your Code Later

After making changes:

```powershell
# Navigate to project folder
cd "C:\Users\user\Desktop\Website\Lead Generator"

# Check what changed
git status

# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push
```

---

## 🆘 Troubleshooting

### "git: command not found"
- Git is not installed or not in PATH
- Install Git (Step 1)
- Restart PowerShell after installation

### "fatal: not a git repository"
- You're not in the project folder
- Run: `cd "C:\Users\user\Desktop\Website\Lead Generator"`

### "fatal: remote origin already exists"
- Repository already connected
- To change: `git remote set-url origin NEW_URL`

### "Authentication failed"
- Use Personal Access Token instead of password
- See Step 9 above

### "config.py is showing on GitHub"
- ⚠️ **SECURITY RISK!**
- Remove it: `git rm --cached config.py`
- Commit: `git commit -m "Remove config.py"`
- Push: `git push`
- Verify `.gitignore` includes `config.py`

### "Permission denied"
- Check your GitHub username is correct
- Use Personal Access Token, not password
- Verify token has `repo` scope

---

## 📚 Quick Reference Commands

```powershell
# Check status
git status

# Add all files
git add .

# Commit changes
git commit -m "Your message"

# Push to GitHub
git push

# View commit history
git log

# Check remote URL
git remote -v
```

---

## 🎯 Next Steps After Pushing

Once your code is on GitHub:

1. ✅ **Deploy to Render** - Follow `RENDER_DEPLOY.md`
2. ✅ **Add Environment Variables** - Add API keys in Render dashboard
3. ✅ **Test Your App** - Visit your Render URL

---

**Need help?** Check GitHub docs: https://docs.github.com

