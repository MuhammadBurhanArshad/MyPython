#!/bin/bash

# ==========================================
# create_topic.sh
# Creates a new Python topic folder with
# EMPTY README.md and index.py files,
# opens both in nano for editing,
# then executes index.py.
# ==========================================

# Check if folder name is provided
if [ -z "$1" ]; then
    echo "❌ Error: Please provide a folder name."
    echo "Usage: ./create_topic.sh <folder_name>"
    exit 1
fi

FOLDER_NAME="../$1"

# Create the folder
mkdir -p "$FOLDER_NAME"
echo "📁 Folder created: $FOLDER_NAME"

# Create empty README.md file
README_FILE="$FOLDER_NAME/README.md"
touch "$README_FILE"
echo "📄 Created empty: $README_FILE"

# Create empty index.py file
PY_FILE="$FOLDER_NAME/index.py"
touch "$PY_FILE"
echo "🐍 Created empty: $PY_FILE"

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
