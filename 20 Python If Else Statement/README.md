# Python If Else Statement

This guide covers the `if-else` statement in Python, based on the provided notes.

## 📌 What is an If Else Statement?

The `else` statement is used for the **default option** if the `if` condition does not match. It provides an alternative block of code to execute when the `if` condition is `False`.

---

## 📝 Syntax

```python
if condition:
    # Statements for True
else:
    # Statements for False
```

- **`if condition:`** Checks the condition. If `True`, executes the indented block.
- **`else:`** Executes only if the `if` condition is `False`.
- **Indentation** is required for both blocks.

---

## 💡 Example 1: Basic If-Else

```python
x = 5

if x > 10:
    print("x is Greater")
else:
    print("x is Not Greater")
```

**Output:**
```
x is Not Greater
```

### Explanation:
1. `x = 5` assigns 5 to `x`.
2. `if x > 10:` checks if `x` is greater than 10 (False).
3. Since the condition is `False`, the `else` block executes.

---

## 🔍 Example 2: Membership Operator with If-Else

We can use the membership operator (`in`) with `if-else` to check if a value exists in a sequence.

```python
numbers = [11, 22, 33, 44, 55]

if 33 in numbers:
    print("Present")
else:
    print("Not Present")
```

**Output:**
```
Present
```

---

## 🔗 Example 3: Comparison and Logical Operators Together

We can use comparison and logical operators together within the `if` condition.

```python
username = "admin"
password = "1234"
name = "Burhan"

if (username == "admin" and password == "1234"):
    print("Hello Mr.", name)
else:
    print("Hello Miss.", name)
```

**Output:**
```
Hello Mr. Burhan
```

### Key Points:
- **`and`** operator: Both conditions must be `True`.
- **`or`** operator: At least one condition must be `True`.
- Parentheses `()` are optional but help with readability.
