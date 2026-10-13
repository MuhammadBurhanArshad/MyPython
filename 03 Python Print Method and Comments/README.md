# Python Print Method & Comments

This guide covers the basics of outputting text to the console using the `print()` function and writing comments in Python, based on initial learning notes.

## 📌 File Extension
In Python, we use the **`.py`** extension for Python files (e.g., `index.py`, `main.py`).

---

## 🖨️ Print Command
We use the `print()` method to output any text, variable, or value to the console.

*Note: In Python, `print` must be written in **lowercase**. `Print` (with a capital P) will cause an error.*

### Common Print Examples:
| Code | Output | Description |
|------|--------|-------------|
| `print("Hello World")` | `Hello World` | Using double quotes |
| `print('Hello World')` | `Hello World` | Using single quotes |
| `print("Hello", "World")` | `Hello World` | Printing multiple arguments (comma adds a space) |
| `print(25)` | `25` | Printing a number (integer) |

---

## 💬 Comments
Comments are lines of code that are ignored by the Python interpreter. They are used to explain code, make notes, or temporarily disable code.

### Single-Line Comments
For a single-line comment, we write a **`#`** symbol before the line.

**Example:**
```python
# This is a single-line comment
print("Hello")  # This is also a comment (inline)
```

### Multi-Line Comments
For multi-line comments, we wrap the text in triple quotes: **`""" """`**.

**Example:**
```python
"""
This is a multi-line comment.
It can span across several lines.
Python ignores this block entirely.
"""
print("Hello World")
```
