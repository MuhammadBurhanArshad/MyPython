# Python Dictionary Methods

This guide covers the built-in methods and universal functions available for Python Dictionaries, based on the provided notes.

## 📌 Dictionary Methods

A dictionary comes with several built-in methods to manipulate and retrieve data.

| Method | Description |
| :--- | :--- |
| **`get()`** | Used to get a value from a key. |
| **`keys()`** | To get all the keys. |
| **`values()`** | To get all the values. |
| **`items()`** | Separates and returns key & value as tuples. |
| **`fromkeys()`** | Create a new dictionary from a sequence of keys. |
| **`pop()`** | Removes the specified key from the dictionary. |
| **`popitem()`** | Automatically removes and returns the last key-value pair. |
| **`clear()`** | Empties the whole dictionary. |
| **`update()`** | To update and add key-value pairs. |
| **`copy()`** | To copy the dictionary. |
| **`setdefault()`** | To assign a default value if the key does not exist. |

### Universal Functions
These built-in Python functions can be used with dictionaries:
- **`len(dict)`**: Returns the number of keys in the dictionary.
- **`str(dict)`**: Converts the dictionary into a string representation.

---

## 📝 Example & Implementation

### 1. `get()`
Used to safely retrieve a value. It can also provide a default fallback value if the key is missing.
```python
student.get("name")
student.get("city", "Not Found")
```

### 2. `keys()` and `items()`
```python
# Get all keys
student.keys()

# Get all key-value pairs
student.items()
```

### 3. `fromkeys()`
Creates a new dictionary from a list of keys, optionally assigning a default value to all.
```python
keys = ["name", "age"]
dict.fromkeys(keys)
dict.fromkeys(keys, "Unknown")
```

### 4. `pop()` and `popitem()`
```python
# Remove a specific key
student.pop("age")

# Remove the last inserted item
student.popitem()
```

### 5. `update()`
Used to add multiple key-value pairs or update existing ones.
```python
student.update({"age": 25})
student.update(city="Khi")
```

### 6. `copy()` and `setdefault()`
```python
# Copy the dictionary
new_student = student.copy()

# Assign default value if key doesn't exist
student.setdefault("name", "Unknown")
```

### 7. `clear()`
```python
# Empty the entire dictionary
student.clear()
```
