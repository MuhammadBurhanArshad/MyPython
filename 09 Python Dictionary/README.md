# Python Dictionary

This guide covers the fundamentals of Python Dictionaries. A dictionary is a collection of key-value pairs, used to store data in a structured way.

## 📌 Dictionary Basics

A dictionary is defined using curly braces `{}` and consists of key-value pairs separated by colons.

**Example:**
```python
student = {
    "name": "Burhan",
    "age": 22
}
```

---

## 🔑 Key Points to Remember

- **Keys must be unique:** You cannot have two identical keys in a single dictionary.
- **Key Types:** Keys can be strings, numbers, or tuples (must be immutable types).
- **Value Types:** Values can be of any data type (strings, numbers, lists, other dictionaries, etc.).
- **Mutability:** Dictionaries are mutable (changeable). You can add, remove, or modify items after creation.
- **Accessing Values:** You access values using their specific keys, not by index.

---

## 📝 Example & Implementations

### 1. Printing Values
* **Print the whole dictionary:**
  ```python
  print(student)
  # Output: {'name': 'Burhan', 'age': 22}
  ```

* **Print a single value using its key:**
  ```python
  print(student["name"])
  # Output: Burhan
  ```

### 2. Adding and Updating Values
You can add a new key-value pair or update an existing one using the assignment operator.
```python
student["gender"] = "male"
# Output: {'name': 'Burhan', 'age': 22, 'gender': 'male'}
```

### 3. Creating a Dictionary using `dict()`
You can also create a dictionary using the `dict()` constructor with keyword arguments.
```python
student = dict(
    name = "John",
    age = 20
)
```

### 4. Looping Through a Dictionary
* **Getting values using `.values()`:**
  ```python
  for value in student.values():
      print(value)
  ```

* **Getting both keys and values using `.items()`:**
  ```python
  for key, value in student.items():
      print(f"{key}: {value}")
  ```

### 5. Checking Key Existence
You can use the `in` keyword to check if a specific key exists in the dictionary.
```python
if "name" in student:
    print("Key Found")
```

---

## 📚 Up Next: Python Dictionary Methods
The notes transition to `x) Python Dictionary Methods`, which covers functions like `get()`, `pop()`, `update()`, etc.
