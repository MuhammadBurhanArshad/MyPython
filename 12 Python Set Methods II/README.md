# Python Set Methods II

This guide is a continuation of Python Set Methods, covering creation methods, set operations (union, intersection, difference), comparison methods, and built-in functions.

## 📌 Creating a Set

We can create a set using curly braces or the `set()` constructor.

```python
# Method 1: Using curly braces
x = {"HTML", "CSS", "JS"}

# Method 2: Using the set() constructor (e.g., from a tuple)
x = set(("HTML", "CSS", "JS"))
```

---

## 🔄 Set Operations Methods

These methods are used to perform mathematical set operations. Many have equivalent operators.

| Method | Operator Equivalent | Description |
| :--- | :--- | :--- |
| **`union()`** | `\|` | Used for merging two sets. Returns a set containing all elements from both. |
| **`intersection()`** | `&` | Used to intersect sets. Returns common elements in both sets. |
| **`difference()`** | `-` | To find the difference in sets. Returns elements in the first set but not the second. |
| **`symmetric_difference()`** | `^` | Takes the difference from both sets (elements in exactly one set). |

### Examples:
```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))                 # {1, 2, 3, 4, 5}
print(A | B)                      # Same as above

print(A.intersection(B))          # {3}
print(A & B)                      # Same as above

print(A.difference(B))            # {1, 2}
print(A - B)                      # Same as above

print(A.symmetric_difference(B))  # {1, 2, 4, 5}
print(A ^ B)                      # Same as above
```

---

## ⚖️ Set Comparison Methods

| Method | Description |
| :--- | :--- |
| **`issubset()`** | Checks if the set is a subset of another set. Returns `True` if all items in the set exist in the specified set. |
| **`issuperset()`** | The vice versa of subset. Checks if the set is a superset of another set. Returns `True` if all items in the specified set exist in the set. |
| **`isdisjoint()`** | If both sets are completely different (no common elements), it returns `True`. |

### Examples:
```python
A = {1, 2}
B = {1, 2, 3, 4}
C = {5, 6}

print(A.issubset(B))      # True
print(B.issuperset(A))    # True
print(A.isdisjoint(C))    # True
```

---

## ⚙️ Built-in Functions

| Function | Description |
| :--- | :--- |
| **`set()`** | Converts a list (or other iterable) into a set. |
| **`len()`** | Used to check the length (number of items) of the set. |
| **`max()`** | To find the maximum value in the set. |
| **`min()`** | To find the minimum value in the set. |

### Examples:
```python
numbers = [1, 2, 2, 3]
my_set = set(numbers)  # Converts list to set, removes duplicates
print(my_set)          # {1, 2, 3}

fruits = {"apple", "banana", "cherry"}
print(len(fruits))     # 3
print(max(fruits))     # cherry (alphabetically)
print(min(fruits))     # apple
```
