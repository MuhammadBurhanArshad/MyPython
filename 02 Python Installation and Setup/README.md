# Python Installation & Setup

This guide covers the installation and setup process for Python and the necessary tools to start coding, based on initial learning notes.

## 📌 Overview of Steps

To set up a complete Python development environment, follow these steps:
1. **Download and install Python** (from the official website).
2. **Download and install VS Code Editor** (a lightweight but powerful code editor).
3. **Install the Python Package (Extension) in VS Code** (to add language support).

## ✅ Checking Python Version

After installing Python, you can verify the installation by opening your terminal or command prompt and typing:

```bash
python --version
```

*Note: On some systems (especially macOS/Linux), you may need to use `python3 --version`.*

---

## 💻 OS-Specific Installation Guide

### 🪟 Windows
1. Go to [python.org/downloads](https://www.python.org/downloads/).
2. Download the latest Windows installer (64-bit recommended).
3. Run the installer.
4. **Important:** Check the box that says **"Add Python to PATH"** at the bottom of the installer window.
5. Click "Install Now" and wait for the process to complete.

### 🍏 macOS
**Option A: Official Installer**
1. Go to [python.org/downloads](https://www.python.org/downloads/).
2. Download the macOS installer package.
3. Run the `.pkg` file and follow the installation instructions.

**Option B: Homebrew (Recommended for developers)**
Open Terminal and run:
```bash
brew install python3
```

### 🐧 Linux (Ubuntu/Debian)
Open your terminal and run the following commands:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 🐧 Linux (Fedora/RHEL)
Open your terminal and run:
```bash
sudo dnf install python3 python3-pip
```

---

## 🛠️ VS Code Setup

1. **Download VS Code:** Go to [code.visualstudio.com](https://code.visualstudio.com/) and download the installer for your operating system.
2. **Install VS Code:** Run the installer and follow the prompts.
3. **Install the Python Extension:**
   - Open VS Code.
   - Click on the **Extensions** icon in the sidebar (or press `Ctrl+Shift+X`).
   - Search for **"Python"** (published by Microsoft).
   - Click **Install**.
4. **Select Interpreter:**
   - Open a Python file (like `index.py`).
   - Click on the Python version in the bottom-right corner of the status bar (or press `Ctrl+Shift+P` and type `Python: Select Interpreter`).
   - Choose the Python version you installed.
