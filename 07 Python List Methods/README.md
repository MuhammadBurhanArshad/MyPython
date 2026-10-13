# Python List Methods

This guide covers the built-in methods available for Python Lists. Lists are mutable sequences, meaning they can be modified after creation using various methods.

## 📌 List Methods Overview

The List in Python comes up with the following built-in methods:

| Category | Methods |
| :--- | :--- |
| **Adding Items** | `append()`, `insert()`, `extend()` |
| **Removing Items** | `remove()`, `pop()`, `clear()` |
| **Utility/Info** | `copy()`, `index()`, `count()`, `sort()`, `reverse()` |

### Other General Functions (Built-in)
These built-in functions can be used with any sequence, including lists:
- `len(list)` : Get the length of the list.
- `max(list)` : Find the maximum value.
- `min(list)` : Find the minimum value.
- `list(seq)` : Convert a sequence (like a tuple) into a list.

---

## 📝 Example Usage

Let's assume we have a base list: `fruits = ["Apple", "Banana", "Cherry"]`

### ➕ Adding Values
* **`append()`**: Used to add a value at the **end** of the list.
  ```python
  fruits.append("Mango")
  # Result: ["Apple", "Banana", "Cherry", "Mango"]
  ```

* **`insert()`**: Used to add a value at a **specified index**.
  ```python
  fruits.insert(0, "Orange")
  # Result: ["Orange", "Apple", "Banana", "Cherry", "Mango"]
  ```

* **`extend()`**: Allows extending/merging two lists.
  ```python
  veg = ["Carrot", "Potato"]
  fruits.extend(veg)
  # Result: ["Orange", "Apple", "Banana", "Cherry", "Mango", "Carrot", "Potato"]
  ```

### ➖ Removing Values
* **`remove()`**: Takes the value to directly remove it.
  ```python
  fruits.remove("Banana")
  # Result: ["Orange", "Apple", "Cherry", "Mango"]
  ```

* **`pop()`**: Used to remove the last value (or a value at a specific index).
  ```python
  fruits.pop()        # Removes the last item
  fruits.pop(1)       # Removes item at index 1
  ```

* **`clear()`**: Used to clear the whole list.
  ```python
  fruits.clear()
  # Result: []
  ```

### 🔄 Sorting & Reversing
* **`sort()`**: Used to sort the list in ascending order (default).
  ```python
  fruits.sort()
  fruits.sort(reverse=False)  # Explicit ascending
  fruits.sort(reverse=True)   # Descending
  ```

* **`reverse()`**: Used to reverse the order of the list.
  ```python
  fruits.reverse()
  ```

### 📋 Utility Methods
* **`copy()`**: Used to copy the list (creates a shallow copy).
  ```python
  x = fruits.copy()
  x = list(fruits)  # Alternative using list() constructor
  x = fruits[:]     # Alternative using slicing
  ```

* **`index()`**: Used to find the index of an item. Can specify start and end indices.
  ```python
  x = fruits.index("grapes")
  x = fruits.index("mango", 2, 6)  # Search between index 2 and 6
  ```

* **`count()`**: Used to count the existence of a specific item.
  ```python
  x = fruits.count("cherry")
  ```

* **`len()`**: Universal method to get the length of the list.
  ```python
  x = len(fruits)
  ```

* **`max()` / `min()`**: To find out the maximum and minimum values.
  ```python
  fruits_max = max(fruits)
  fruits_min = min(fruits)
  ```
