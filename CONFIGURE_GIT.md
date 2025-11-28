# ⚙️ How to Configure Git

After installing Git, you need to configure it with your name and email. Here's how:

---

## 📝 Step-by-Step Configuration

### Step 1: Open PowerShell

1. Press `Windows Key + X`
2. Select **"Windows PowerShell"** or **"Terminal"**
3. Or search for "PowerShell" in the Start menu

### Step 2: Run Configuration Commands

Replace `"Your Name"` and `"your.email@example.com"` with **your actual information**.

#### Configure Your Name:
```powershell
git config --global user.name "Your Name"
```

**Examples:**
```powershell
git config --global user.name "John Doe"
git config --global user.name "Sarah Smith"
```

#### Configure Your Email:
```powershell
git config --global user.email "your.email@example.com"
```

**Examples:**
```powershell
git config --global user.email "john@example.com"
git config --global user.email "sarah.smith@gmail.com"
```

**Important**: Use the **same email** you'll use for GitHub!

---

## ✅ Verify Configuration

After running both commands, verify they worked:

```powershell
git config --global user.name
git config --global user.email
```

You should see your name and email displayed.

---

## 🎯 Complete Example

Here's a complete example session:

```powershell
# Set your name
git config --global user.name "John Doe"

# Set your email
git config --global user.email "john.doe@example.com"

# Verify it worked
git config --global user.name
# Output: John Doe

git config --global user.email
# Output: john.doe@example.com
```

---

## 📋 What Each Command Does

### `git config --global user.name`
- Sets your name for **all** Git repositories on your computer
- This name appears in commit history
- Use your real name or GitHub username

### `git config --global user.email`
- Sets your email for **all** Git repositories
- Should match your GitHub account email
- Used to link commits to your GitHub account

### `--global` Flag
- Makes the setting apply to **all** repositories
- Without `--global`, it only applies to the current folder
- You only need to do this **once** per computer

---

## 🔍 View All Git Configuration

To see all your Git settings:

```powershell
git config --list
```

To see only global settings:

```powershell
git config --global --list
```

---

## ✏️ Change Configuration Later

If you need to change your name or email later:

```powershell
# Change name
git config --global user.name "New Name"

# Change email
git config --global user.email "new.email@example.com"
```

---

## 🆘 Troubleshooting

### "git: command not found"
- Git is not installed or PowerShell wasn't restarted
- Install Git, then **close and reopen PowerShell**

### "fatal: unable to read config file"
- Git is not properly installed
- Reinstall Git and restart PowerShell

### Wrong email/name showing
- Check what's configured: `git config --global user.name`
- Update if needed: `git config --global user.name "Correct Name"`

---

## 💡 Pro Tips

1. **Use the same email as GitHub** - This links your commits to your GitHub account
2. **Use your real name** - Makes it easier to identify your commits
3. **Set it once** - The `--global` flag means you only need to do this once
4. **Can be different per project** - Remove `--global` to set per-project settings

---

## ✅ Quick Checklist

- [ ] Git installed
- [ ] PowerShell opened
- [ ] Name configured: `git config --global user.name "Your Name"`
- [ ] Email configured: `git config --global user.email "your.email@example.com"`
- [ ] Verified: `git config --global user.name` shows your name
- [ ] Verified: `git config --global user.email` shows your email

---

**Next Step**: After configuring Git, you can start pushing your code to GitHub! See `GITHUB_SETUP.md` for the next steps.

