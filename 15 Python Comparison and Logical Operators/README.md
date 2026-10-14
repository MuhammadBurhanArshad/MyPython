# Python Comparison & Logical Operators

This guide covers Python Comparison Operators and Logical Operators, based on the provided notes.

## 📌 Comparison Operators

Comparison operators are used to compare two values or variables. They return a Boolean value (`True` or `False`).

| Operator | Name | Example | Description |
| :--- | :--- | :--- | :--- |
| `==` | Equal to | `5 == 5` | Returns `True` if both values are equal. |
| `!=` | Not Equal to | `5 != 3` | Returns `True` if values are not equal. |
| `>` | Greater than | `10 > 5` | Returns `True` if the left value is greater. |
| `<` | Lower than | `5 < 10` | Returns `True` if the left value is smaller. |
| `>=` | Greater than or equal to | `10 >= 10` | Returns `True` if the left value is greater than or equal to the right. |
| `<=` | Less than or equal to | `5 <= 10` | Returns `True` if the left value is less than or equal to the right. |

---

## ⚙️ Logical Operators

Logical operators are used to combine conditional statements.

| Operator | Description | Rule |
| :--- | :--- | :--- |
| **`and`** | Returns `True` if **both** conditions are true. | True and True -> True |
| **`or`** | Returns `True` if **at least one** condition is true. | True or False -> True |
| **`not`** | **Reverses** the result. Returns `False` if the result is true. | not True -> False |

### 💡 Examples:
```python
# and Operator
print(True and True)   # True
print(True and False)  # False

# or Operator
print(True or False)   # True
print(False or False)  # False

# not Operator
print(not True)        # False
print(not False)       # True
```
