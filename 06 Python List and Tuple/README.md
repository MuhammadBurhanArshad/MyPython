# Python List & Tuple

This guide covers the fundamentals of two important Python data structures: **Lists** and **Tuples**. Both are used to store multiple items in a single variable, but they have key differences.

---

## 📋 List

A **List** is used to store data for multiple items in a single variable without any type restriction. It is an ordered, mutable (changeable) collection.

### 🔹 Accessing Items in a List
- **Using Index:** For accessing a single value in a List, we use the index (starting from `0`).
  ```python
  x = ["HTML", "CSS", "JS"]
  print(x[1])  # Output: CSS
  ```
- **Updating Items:** Since lists are mutable, you can change an item using its index.
  ```python
  x[1] = "Python"
  ```
- **Reverse Indexing:** You can also use reverse indexing to access items from the last (starting from `-1`).
- **Slicing (Range):** For getting a range of values, we can use slicing.
  ```python
  x[1:3]  # Returns items from index 1 to 2
  ```

### 🔹 Unpacking a List
We can get values out from a list and assign them directly to variables.
```python
data = ["Sandeep", 25, 75.50, True]
name, age, marks, married = data
```

---

## 📦 Tuple

A **Tuple** is like a list, but it is **immutable** (cannot be changed after creation). We use **round brackets `()`** to define a tuple.

### 🔹 Key Characteristics of Tuples
- **Immutable:** Once created, elements cannot be added, removed, or changed.
- **Allows Duplicates:** Tuples can contain duplicate values.
- **Faster than Lists:** Tuples are generally faster than lists in terms of performance.
- **Use Case:** Use a tuple when the data should not change.

### 🔹 Accessing Items in a Tuple
You can access values in a tuple just like a list, using index or reverse indexing.
```python
fruits = ("Apple", "Banana")
print(fruits[0])  # Output: Apple
```
*Note: While tuples don't support item assignment (like `fruits[0] = "Mango"`), they support other list operations like indexing, slicing, and concatenation.*

---

## 📊 List vs Tuple (Summary)

| Feature          | List (`[]`)                  | Tuple (`()`)                 |
|------------------|------------------------------|------------------------------|
| **Mutability**   | Mutable (Changeable)         | Immutable (Unchangeable)     |
| **Syntax**       | Square brackets `[]`         | Round brackets `()`          |
| **Speed**        | Slower                       | Faster                       |
| **Duplicates**   | Allowed                      | Allowed                      |
| **Use Case**     | Data that changes over time  | Data that should not change  |
