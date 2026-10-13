# Python Tuple Methods

This guide covers the built-in methods and universal functions available for Python Tuples. 

A **Tuple** is like a list, but with two key differences:
1. It uses **round brackets `()`** instead of square brackets.
2. It is **immutable** (cannot be changed after creation).

Because tuples are immutable, they have fewer methods than lists. However, they still support several useful operations.

---

## 📌 Tuple Methods

Tuples have only two built-in methods:

| Method | Description |
| :--- | :--- |
| **`count()`** | Returns the number of times a specified value appears in the tuple. |
| **`index()`** | Searches the tuple for a specified value and returns the position of where it was found. |

### Examples:
```python
fruits = ("apple", "Banana", "apple")

# count(): Used to show count (existence)
print(fruits.count("apple"))  # Output: 2

# index(): Index finding of value
print(fruits.index("Banana")) # Output: 1
```

---

## 🌐 Universal Methods

These built-in functions are universal and work with tuples (as well as lists and other iterables).

| Function | Description |
| :--- | :--- |
| **`len(tuple)`** | Returns the length (number of items) of the tuple. |
| **`max(tuple)`** | Returns the largest item in the tuple. |
| **`min(tuple)`** | Returns the smallest item in the tuple. |
| **`tuple(iterable)`** | Converts an iterable (like a list) into a tuple. |

### Examples:
```python
numbers = (10, 5, 25, 8)

print(len(numbers))  # Output: 4
print(max(numbers))  # Output: 25
print(min(numbers))  # Output: 5

# Converting a list to a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)      # Output: (1, 2, 3)
```

---

## 🪆 Nested Tuples

We can also create nested tuples (a tuple inside another tuple).

```python
nested_tuple = ((10, 20), (30, 40), (50, 60))
```

---

## 📊 Quick Summary

| Feature | Tuple |
| :--- | :--- |
| **Syntax** | `()` |
| **Mutability** | Immutable |
| **Methods** | `count()`, `index()` |
| **Universal Functions** | `len()`, `max()`, `min()`, `tuple()` |
