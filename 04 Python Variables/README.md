# Python Variables

This guide covers the fundamentals of variables in Python, including naming rules, dynamic typing, multiple assignments, and concatenation, based on initial learning notes.

## 📌 What is a Variable?

A variable is like a **single bucket** that stores a value. You can call and use this value multiple times throughout your code.

**Example:**
```python
name = "Burhan"
print(name)
```
*Note: In Python, the `print` function must be written in lowercase (`print`), not capital `Print`.*

---

## 📝 Rules for Naming Variables

When naming variables in Python, follow these rules:
- ✅ **Can contain underscores** (e.g., `my_variable`).
- ✅ **Can start with an underscore** (e.g., `_private`).
- ✅ **Can contain numbers in the middle or end** (e.g., `var1`, `data2`).
- ✅ **No case restriction** (e.g., `Name` and `name` are different variables).
- ❌ **No spaces** allowed (use underscores instead).
- ❌ **Cannot be a keyword** (e.g., `if`, `for`, `while`).
- ❌ **Cannot start with a number** (e.g., `1var` is invalid).

---

## 🔄 Dynamic Typing (Overwriting)

Python is a dynamically typed language. This means a variable can be easily **overwritten** with a different data type. You do not need to declare the type explicitly.

**Example:**
```python
x = 10       # x is an integer
x = "Hello"  # x is now a string
```

---

## 📦 Multiple Variable Assignments

Python allows you to assign values to multiple variables in a single line.

### 1. Assigning different values to different variables:
```python
a, b, c = 10, 20, 30
```

### 2. Assigning the same value to multiple variables:
```python
x = y = z = 100
```

---

## 🔗 Concatenation

We use the **`+`** operator and the **`,`** separator to concatenate (join) strings and variables.

- **Using `+`:** Joins strings together. (Both operands must be strings).
- **Using `,`:** Separates arguments in the `print()` function. Python automatically adds a space between them.

**Example:**
```python
first_name = "Muhammad"
last_name = "Burhan"

# Using +
print("Full Name: " + first_name + " " + last_name)

# Using ,
print("Full Name:", first_name, last_name)
```

---

## 🔢 Data Types (Brief Mention)
Python has various built-in data types, including:
- **String** (`str`): Text, e.g., `"Hello"`
- **Integer** (`int`): Whole numbers, e.g., `10`
- **Float** (`float`): Decimal numbers, e.g., `3.14`
- **Boolean** (`bool`): True/False values
