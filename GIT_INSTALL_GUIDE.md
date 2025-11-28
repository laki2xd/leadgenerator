# 🔧 Git Installation Options Guide

When installing Git on Windows, here are the **important options** to select:

---

## 📋 Step-by-Step Installation Options

### **Step 1: Select Components**
✅ **Keep defaults** - All default options are fine:
- ✅ Git Bash Here
- ✅ Git GUI Here
- ✅ Associate .git* configuration files with the default text editor
- ✅ Associate .sh files to be run with Bash

### **Step 2: Choosing the default editor used by Git** ⚠️ IMPORTANT
**Recommended**: Select **"Nano editor"** or **"Notepad++"** (if installed)
- ✅ **Nano editor** - Simple, beginner-friendly
- ✅ **Notepad++** - If you have it installed
- ⚠️ Avoid "Vim" unless you know how to use it (it's confusing for beginners)

**Why it matters**: This is what opens when Git needs you to write commit messages.

### **Step 3: Adjusting your PATH environment** ⚠️ VERY IMPORTANT
**Select**: ✅ **"Git from the command line and also from 3rd-party software"**

This is the **most important option**! It allows you to use `git` commands in PowerShell.

**Options explained:**
- ✅ **"Git from the command line and also from 3rd-party software"** ← **CHOOSE THIS**
- ❌ "Git from the command line only" - Works but less flexible
- ❌ "Use Git and optional Unix tools from the Command Prompt" - Not needed
- ❌ "Use Git Bash only" - Won't work in PowerShell

### **Step 4: Choosing HTTPS transport backend**
**Recommended**: ✅ **"Use the OpenSSL library"** (default)

This is fine for GitHub and most services.

### **Step 5: Configuring the line ending conversions** ⚠️ IMPORTANT
**Select**: ✅ **"Checkout Windows-style, commit Unix-style line endings"**

**Why**: 
- Windows uses `CRLF` line endings
- Linux/Mac use `LF` line endings
- This setting automatically converts them, preventing issues

**Options:**
- ✅ **"Checkout Windows-style, commit Unix-style line endings"** ← **CHOOSE THIS**
- ⚠️ "Checkout as-is, commit as-is" - Can cause issues
- ⚠️ "Checkout as-is, commit Unix-style" - Less common

### **Step 6: Configuring the terminal emulator**
**Select**: ✅ **"Use Windows' default console window"** (default)

This works fine with PowerShell.

### **Step 7: Configuring extra options**
✅ **Keep defaults**:
- ✅ Enable file system caching
- ✅ Enable Git Credential Manager
- ✅ Enable symbolic links

**Git Credential Manager** is especially useful - it stores your GitHub credentials securely.

### **Step 8: Configuring experimental options**
**Leave unchecked** - These are experimental features you don't need.

---

## ✅ Recommended Settings Summary

Here's what to select:

| Step | Option | Selection |
|------|--------|-----------|
| Components | All defaults | ✅ Keep defaults |
| Default Editor | Editor choice | ✅ **Nano** or **Notepad++** |
| PATH Environment | Command line access | ✅ **Git from command line and 3rd-party software** ⭐ |
| HTTPS Transport | Backend | ✅ Use OpenSSL library |
| Line Endings | Conversion | ✅ **Checkout Windows-style, commit Unix-style** ⭐ |
| Terminal Emulator | Console | ✅ Use Windows' default console |
| Extra Options | Credential Manager | ✅ Enable Git Credential Manager |
| Experimental | Features | ❌ Leave unchecked |

---

## 🎯 Quick Install Checklist

When installing, make sure you:

- [ ] ✅ Select **"Git from the command line and also from 3rd-party software"**
- [ ] ✅ Select **"Checkout Windows-style, commit Unix-style line endings"**
- [ ] ✅ Enable **Git Credential Manager**
- [ ] ✅ Choose **Nano** or **Notepad++** as editor (not Vim)

---

## 🔍 After Installation

1. **Close and reopen PowerShell** (important!)
2. **Verify installation**:
   ```powershell
   git --version
   ```
   Should show: `git version 2.x.x`

3. **Configure Git** (one-time):
   ```powershell
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

---

## 🆘 Troubleshooting

### "git: command not found" after installation
- **Solution**: Close and reopen PowerShell
- If still not working, restart your computer

### Wrong editor opens
- **Solution**: Change it later:
  ```powershell
  git config --global core.editor "notepad"
  ```

### Line ending warnings
- **Solution**: Already handled if you selected "Checkout Windows-style, commit Unix-style"

---

## 💡 Pro Tips

1. **Git Credential Manager** will save your GitHub token, so you won't need to enter it every time
2. **Nano editor** is easier than Vim for beginners
3. You can change most settings later with `git config` commands

---

**Most Important**: Select **"Git from the command line and also from 3rd-party software"** - this is critical!

