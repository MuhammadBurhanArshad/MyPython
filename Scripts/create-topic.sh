#!/bin/bash

# ==========================================
# create_topic.sh
# Creates a new Python topic folder with
# README.md and index.py, opens BOTH files
# in nano for editing, then executes index.py.
# ==========================================

# Check if folder name is provided
if [ -z "$1" ]; then
    echo "❌ Error: Please provide a folder name."
    echo "Usage: ./create_topic.sh <folder_name>"
    exit 1
fi

FOLDER_NAME="$1"

# Create the folder
mkdir -p "$FOLDER_NAME"
echo "📁 Folder created: $FOLDER_NAME"

# Create the README.md file (empty template)
README_FILE="$FOLDER_NAME/README.md"
cat > "$README_FILE" << 'EOF_README'
# Python Topic Name

Write your notes, definitions, and examples here.

## 📌 Key Points
- Point 1
- Point 2

## 💡 Example
Use fenced code blocks in your markdown for examples.
EOF_README
echo "📄 Created: $README_FILE"

# Create the index.py file (empty template)
PY_FILE="$FOLDER_NAME/index.py"
cat > "$PY_FILE" << 'EOF_PY'
"""
index.py

Description: 
"""

# Write your Python code here
print("Hello, Python!")
EOF_PY
echo "🐍 Created: $PY_FILE"

# Open the README.md file in nano for editing
echo ""
echo "📝 Step 1: Opening README.md in nano editor..."
echo "   (Save with CTRL+O, Enter, then Exit with CTRL+X)"
echo ""
sleep 1
nano "$README_FILE"

# Open the Python file in nano for editing
echo ""
echo "📝 Step 2: Opening index.py in nano editor..."
echo "   (Save with CTRL+O, Enter, then Exit with CTRL+X)"
echo ""
sleep 1
nano "$PY_FILE"

# Execute the Python file
echo ""
echo "🚀 Running $PY_FILE..."
echo "=========================================="
python3 "$PY_FILE"
echo "=========================================="
echo "✅ Done! Both files created and index.py executed."
