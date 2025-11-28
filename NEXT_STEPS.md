# 🚀 Next Steps - Complete Checklist

Follow these steps in order to push your code to GitHub and deploy it.

---

## ✅ Step 1: Install Git

**Status**: ⏳ Not done yet

1. **Download Git**
   - Go to: https://git-scm.com/download/win
   - Click "Download for Windows"
   - Run the installer

2. **Important Installation Options**
   - ✅ Select: **"Git from the command line and also from 3rd-party software"**
   - ✅ Select: **"Checkout Windows-style, commit Unix-style line endings"**
   - ✅ Choose: **"Nano editor"** (or Notepad++ if you have it)
   - ✅ Enable: **"Git Credential Manager"**

3. **After Installation**
   - **Close PowerShell completely**
   - **Open a new PowerShell window**
   - Test: `git --version` (should show version number)

---

## ✅ Step 2: Configure Git

**Status**: ⏳ Waiting for Git installation

Once Git is installed, run these commands in PowerShell:

```powershell
git config --global user.name "laki2xd"
git config --global user.email "ggboymc@gmail.com"
```

**Verify:**
```powershell
git config --global user.name
git config --global user.email
```

---

## ✅ Step 3: Create GitHub Account

**Status**: ⏳ Check if you have an account

1. **If you don't have a GitHub account:**
   - Go to: https://github.com
   - Click "Sign up"
   - Username: `laki2xd` (or your choice)
   - Email: `ggboymc@gmail.com`
   - Create account and verify email

2. **If you already have an account:**
   - Log in at: https://github.com
   - Make sure you can access it

---

## ✅ Step 4: Create GitHub Repository

**Status**: ⏳ Waiting for previous steps

1. **Go to GitHub**
   - Log in to https://github.com
   - Click the **"+"** icon (top right)
   - Select **"New repository"**

2. **Repository Settings**
   - **Repository name**: `lead-generator` (or your choice)
   - **Description**: "Lead Generator - Find B2B companies in Canada & USA"
   - **Visibility**: 
     - ✅ **Public** (free, code is visible)
     - ⚠️ **Private** (free for personal accounts)
   - **DO NOT** check:
     - ❌ "Add a README file"
     - ❌ "Add .gitignore"
     - ❌ "Choose a license"
   - Click **"Create repository"**

3. **Copy the Repository URL**
   - GitHub will show you a page with setup instructions
   - **Copy the HTTPS URL** - it looks like:
     ```
     https://github.com/laki2xd/lead-generator.git
     ```
   - Save this URL - you'll need it!

---

## ✅ Step 5: Initialize Git in Your Project

**Status**: ⏳ Waiting for Git installation

Open PowerShell in your project folder and run:

```powershell
# Navigate to your project (if not already there)
cd "C:\Users\user\Desktop\Website\Lead Generator"

# Initialize git repository
git init

# Check status
git status
```

You should see a list of files that will be added.

**Important**: Make sure `config.py` is NOT in the list (it's in `.gitignore` - good!)

---

## ✅ Step 6: Add Files and Commit

**Status**: ⏳ Waiting for previous steps

```powershell
# Add all files (except those in .gitignore)
git add .

# Verify config.py is NOT being added
git status

# Make your first commit
git commit -m "Initial commit - Lead Generator Flask app"
```

---

## ✅ Step 7: Connect to GitHub and Push

**Status**: ⏳ Waiting for previous steps

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values:

```powershell
# Add GitHub as remote (use YOUR repository URL from Step 4)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Example if your username is laki2xd and repo is lead-generator:
# git remote add origin https://github.com/laki2xd/lead-generator.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**First time pushing?**
- GitHub will ask for credentials:
  - **Username**: Your GitHub username (e.g., `laki2xd`)
  - **Password**: Use a **Personal Access Token** (see Step 8)

---

## ✅ Step 8: Create Personal Access Token

**Status**: ⏳ Do this before pushing

GitHub requires a token instead of password:

1. **Go to GitHub Settings**
   - Click your profile picture (top right)
   - Click **"Settings"**
   - Scroll down → **"Developer settings"**
   - Click **"Personal access tokens"** → **"Tokens (classic)"**
   - Click **"Generate new token"** → **"Generate new token (classic)"**

2. **Configure Token**
   - **Note**: "Git Push Token" (or any name)
   - **Expiration**: Choose duration (90 days recommended)
   - **Scopes**: Check ✅ **repo** (all repo permissions)
   - Click **"Generate token"**

3. **Copy Token**
   - ⚠️ **IMPORTANT**: Copy the token NOW (you won't see it again!)
   - It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - Save it somewhere safe!

4. **Use Token When Pushing**
   - When Git asks for password, paste the token instead
   - Username: Your GitHub username
   - Password: The token you just copied

---

## ✅ Step 9: Verify Push Success

1. **Refresh GitHub**
   - Go to your repository page
   - You should see all your files!

2. **Verify config.py is NOT there**
   - Check that `config.py` is NOT visible
   - ✅ This is correct - API keys should never be on GitHub!

---

## ✅ Step 10: Deploy to Render

**Status**: ⏳ After code is on GitHub

Once your code is successfully on GitHub:

1. **Read**: `RENDER_DEPLOY.md` for detailed instructions
2. **Go to**: https://render.com
3. **Create account** with GitHub
4. **Create Web Service** from your repository
5. **Add environment variables** (API keys)
6. **Add persistent disk** (for exports)
7. **Deploy!**

---

## 🎯 Current Status

- [ ] Git installed
- [ ] Git configured
- [ ] GitHub account created
- [ ] GitHub repository created
- [ ] Git initialized in project
- [ ] Files committed
- [ ] Code pushed to GitHub
- [ ] Deployed to Render

---

## 🆘 Need Help?

**Git not working?**
- Make sure you closed and reopened PowerShell after installation
- Try restarting your computer

**Can't push to GitHub?**
- Use Personal Access Token, not password
- Check repository URL is correct
- Verify you have internet connection

**config.py showing on GitHub?**
- ⚠️ Security risk! Remove it immediately
- Check `.gitignore` includes `config.py`

---

## 📞 Quick Commands Reference

```powershell
# Check Git version
git --version

# Configure Git (one-time)
git config --global user.name "laki2xd"
git config --global user.email "ggboymc@gmail.com"

# Initialize repository
git init

# Add files
git add .

# Commit
git commit -m "Your message"

# Connect to GitHub
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push
git push -u origin main
```

---

**Ready to start?** Begin with Step 1 - Install Git!

