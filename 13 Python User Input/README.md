# Python User Input

This guide covers how to accept input from the user in Python using the `input()` function, format output, and handle invalid input gracefully.

## 📌 The `input()` Function

The `input()` function allows the user to enter a value from the console. It reads the input as a **string** by default.

### Basic Usage:
```python
name = input("Enter your name: ")
```
*The string inside the parentheses (`"Enter your name: "`) is an optional message displayed to the user, prompting them for input.*

---

## 🖨️ Additional Print Parameters

We have another parameter (argument) for the `print()` function to tell what should be at the end of the output. This is done using the `end` parameter.

- **By default:** `print()` adds a new line (`\n`) at the end.
- **Custom end:** We can change this behavior.

**Example:**
```python
print("message", end=" ")
```
*Here, the `end` parameter is set to a space (`" "`), so the next print statement will continue on the same line.*

---

## 📝 Formatted Strings (f-strings)

We can print formatted strings easily using f-strings. This allows us to embed variables directly inside a string using curly braces `{}`.

**Example:**
```python
name = "Burhan"
city = "Karachi"
print(f"My name is {name} and city {city}")
```

---

## 🔄 Type Conversion from Input

Since `input()` always returns a string, we need to convert it to the required data type (e.g., integer, float) if we want to perform mathematical operations.

**Example:**
```python
width = int(input("Enter width: "))
```

---

## 🛡️ Error Handling with `try` & `except`

When converting input types, users might enter invalid data (e.g., typing "abc" instead of a number). To prevent the program from crashing, we can use `try` and `except` blocks.

**Example:**
```python
try:
    width = int(input("Enter width: "))
except ValueError:
    print("Please enter a valid value")
```
*If the user enters something that cannot be converted to an integer, a `ValueError` is raised, and the code inside the `except` block executes instead of crashing.*
