# ✅ Verify Git Installation

Git needs PowerShell to be restarted to work. Follow these steps:

---

## Step 1: Close and Reopen PowerShell

**Important**: After installing Git, you MUST close and reopen PowerShell!

1. **Close this PowerShell window completely**
2. **Open a NEW PowerShell window**:
   - Press `Windows Key + X`
   - Select "Windows PowerShell" or "Terminal"
   - Or search "PowerShell" in Start menu

---

## Step 2: Verify Git Works

In the NEW PowerShell window, run:

```powershell
git --version
```

**Expected output**: `git version 2.x.x` (or similar)

If you see an error, try:
- Restart your computer
- Or check Git installation path is in system PATH

---

## Step 3: Verify Configuration

Check your Git configuration:

```powershell
git config --global user.name
git config --global user.email
```

**Expected output**:
- `laki2xd`
- `ggboymc@gmail.com`

If these are blank or wrong, configure them:

```powershell
git config --global user.name "laki2xd"
git config --global user.email "ggboymc@gmail.com"
```

---

## Step 4: Navigate to Your Project

```powershell
cd "C:\Users\user\Desktop\Website\Lead Generator"
```

---

## Step 5: Initialize Git Repository

```powershell
git init
```

You should see: `Initialized empty Git repository in...`

---

## Step 6: Check Status

```powershell
git status
```

You should see a list of files. **Important**: Make sure `config.py` is NOT in the list (it should be ignored).

---

## ✅ Once Git is Working

After you've verified Git works in a new PowerShell window, let me know and I'll help you:
1. Add files to Git
2. Make your first commit
3. Create GitHub repository
4. Push your code

---

## 🆘 Troubleshooting

### "git: command not found" after reopening PowerShell
- **Solution**: Restart your computer
- Or manually add Git to PATH (usually `C:\Program Files\Git\cmd`)

### Configuration shows wrong name/email
- **Solution**: Run the config commands again:
  ```powershell
  git config --global user.name "laki2xd"
  git config --global user.email "ggboymc@gmail.com"
  ```

---

**Next**: After Git is verified, we'll initialize your repository and push to GitHub!

