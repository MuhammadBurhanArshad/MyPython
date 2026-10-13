"""
index.py

This script serves as a quick verification tool for your Python installation and setup.
Once you have followed the README.md instructions, run this file to ensure everything is working correctly.
"""

import sys
import platform

def check_installation():
    print("=" * 50)
    print("🚀 Python Installation Verification Script")
    print("=" * 50)
    
    # 1. Check Python Version
    print(f"✅ Python is installed!")
    print(f"   Version: {sys.version.split()[0]}")
    
    # 2. Check Operating System
    print(f"✅ Operating System detected: {platform.system()} {platform.release()}")
    
    # 3. Check Interpreter Path
    print(f"✅ Python Executable Path: {sys.executable}")
    
    # 4. Verify VS Code Setup
    print("\n📝 VS Code Setup Checklist:")
    print("   1. Download and install VS Code Editor.")
    print("   2. Install the 'Python' extension by Microsoft.")
    print("   3. Select the correct Python Interpreter in VS Code.")
    
    print("\n" + "=" * 50)
    print("🎉 Setup Complete! You are ready to start coding in Python.")
    print("=" * 50)

if __name__ == "__main__":
    check_installation()
