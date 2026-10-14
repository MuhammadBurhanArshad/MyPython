# Python If Statement

This guide covers the fundamentals of the `if` statement in Python, based on the provided notes.

## 📌 What is an If Statement?

The `if` statement is used to check a condition and returns `True` or `False`. It executes a block of code only if the condition evaluates to `True`.

---

## 📝 Syntax

The basic syntax of an `if` statement is:

```python
if condition:
    # Code Statements
```

- **`if`**: The keyword that starts the statement.
- **`condition`**: An expression that evaluates to `True` or `False`.
- **`:` (colon)**: Marks the end of the condition and the beginning of the code block.
- **Indentation**: The code inside the `if` block must be indented (usually 4 spaces).

---

## 💡 Example

Here is a simple example that checks if `x` is greater than 10:

```python
x = 15

if x > 10:
    print("x is Greater")
```

**Output:**
```
x is Greater
```

### Explanation:
1. `x = 15` assigns the value 15 to `x`.
2. `if x > 10:` checks if `x` is greater than 10.
3. Since 15 is greater than 10, the condition is `True`.
4. The indented `print` statement executes.

---

## 🔄 Comparison Operators Used in `if`

| Operator | Description |
| :--- | :--- |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## 📚 Related Topics

The notes also indicate **`xx) Python If Else Statement`** as a continuation, which covers handling the `False` condition.
