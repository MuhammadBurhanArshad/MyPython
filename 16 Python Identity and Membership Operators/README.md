# Python Identity & Membership Operators

This guide covers Python Identity Operators and Membership Operators, based on the provided notes.

## 📌 Identity Operators

Identity operators are used to compare the memory locations of two objects. They check if both variables point to the same object in memory.

| Operator | Description |
| :--- | :--- |
| **`is`** | Returns `True` if both variables point to the **same object**. |
| **`is not`** | Returns `True` if both variables point to **different objects**. |

### 💡 Examples:
```python
a = [1, 2, 3]
b = a           # b points to the same object as a
c = [1, 2, 3]   # c points to a different object

print(a is b)       # True (Same object)
print(a is c)       # False (Different objects)
print(a is not c)   # True (Different objects)
```

*Note: Do not confuse `is` with `==`. The `==` operator checks if the values are equal, while `is` checks if they are the exact same object in memory.*

---

## 🔍 Membership Operators

Membership operators are used to test if a sequence (like a string, list, tuple, or dictionary) contains a specific value.

| Operator | Description |
| :--- | :--- |
| **`in`** | Returns `True` if the value **exists** in the sequence. |
| **`not in`** | Returns `True` if the value **does not exist** in the sequence. |

### 💡 Examples:
```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)       # True (Value exists)
print("mango" in fruits)        # False (Value does not exist)
print("mango" not in fruits)    # True (Value does not exist)

# Works with strings too
text = "Hello World"
print("H" in text)              # True
print("z" not in text)          # True
```
