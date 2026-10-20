# Python If Elif Statement

This guide covers the `if-elif-else` statement in Python, based on the provided notes.

## 📌 What is an If Elif Statement?

The `elif` (else if) statement is used to check **secondary conditions** when the initial `if` condition is `False`. 

It allows you to check multiple conditions in sequence. Python evaluates conditions from top to bottom, and as soon as it finds a `True` condition, it executes that block and skips the rest.

---

## 📝 Syntax

```python
if condition1:
    # Statements
elif condition2:
    # Statements
else:
    # Statements
```

### Key Points:
- **`if`** must come first.
- **`elif`** can be implemented **multiple times** (you can have as many `elif` blocks as you need).
- **`else`** is optional and acts as the default fallback if none of the `if` or `elif` conditions are met.

---

## 💡 Example & Implementation

Here is a simple program that greets the user based on the time of day:

```python
time = 15

if time < 10:
    print("Good Morning")
elif time < 20:
    print("Good Day")
else:
    print("Good Night")
```

**Output:**
```
Good Day
```

### Step-by-Step Explanation:
1. `time = 15` assigns the value 15.
2. `if time < 10:` checks if 15 is less than 10. (False)
3. It moves to the next condition: `elif time < 20:` checks if 15 is less than 20. (True)
4. Since the condition is True, it prints `"Good Day"`.
5. The program skips the `else` block because a condition was already met.
