# Python Data Types

This guide covers the fundamental data types in Python. The type of a value determines what kind of data it is and what operations can be performed on it.

## 📌 Basic Data Types

A data type is essentially the "type of value" assigned to a variable.

| Value Example                 | Data Type      |
|-------------------------------|----------------|
| `x = "Hello World"`           | **String** (`str`) |
| `x = 25`                      | **Integer** (`int`) |
| `x = 25.35`                   | **Float** (`float`) |
| `x = True`                    | **Boolean** (`bool`) |
| `x = ["HTML", "CSS"]`         | **List** (`list`) |
| `x = ("HTML", "CSS")`         | **Tuple** (`tuple`) |
| `x = {"first": "Jane", "age": 20}` | **Dictionary** (`dict`) |
| `x = {"red", "green"}`        | **Set** (`set`) |

---

## ➕ Some Other Data Types in Python

Python also includes more specialized data types for specific tasks.

| Value Example                       | Data Type          |
|-------------------------------------|--------------------|
| `x = 4 + 6j`                        | **Complex** (`complex`) |
| `x = range(5)`                      | **Range** (`range`) |
| `x = frozenset([1, 2, 3])`          | **Frozenset** (`frozenset`) |
| `x = None`                          | **None** (`NoneType`) |
| `x = b'Hello'`                      | **Bytes** (`bytes`) |
| `x = bytearray([65, 66, 67])`       | **Bytearray** (`bytearray`) |
| `x = memoryview(bytes([65, 66, 67]))` | **Memoryview** (`memoryview`) |

---

## 📂 Category-wise Data Types

Python data types can be grouped into the following categories:

| Category       | Data Types Included                          |
|----------------|----------------------------------------------|
| **Numeric**    | `int`, `float`, `complex`                    |
| **Boolean**    | `bool`                                       |
| **Text**       | `str`                                        |
| **Sequence**   | `list`, `tuple`, `range`                     |
| **Mapping**    | `dict`                                       |
| **Set**        | `set`, `frozenset`                           |
| **Binary**     | `bytes`, `bytearray`, `memoryview`           |
| **Special**    | `NoneType` (`None`)                          |

---

## 🔍 Checking Data Type

To find out the data type of any value or variable in Python, we can use the built-in **`type()`** method.

**Example:**
```python
x = 25
print(type(x))  # Output: <class 'int'>
```
