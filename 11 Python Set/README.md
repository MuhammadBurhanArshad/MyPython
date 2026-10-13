# Python Set

This guide covers the fundamentals of Python Sets. A set is a collection of data that stores multiple values using curly brackets `{}`.

## 📌 Key Points to Remember

- **Unique Values:** Stores unique values only (duplicates are not allowed).
- **Automatic Duplication Removal:** Duplicate values are automatically removed upon creation.
- **Unordered:** Sets are unordered, meaning there is **no indexing**. You cannot access items by index.
- **Mutable:** Sets are mutable (can add or remove items).
- **Heterogeneous:** Can contain different data types (integers, strings, etc., as long as they are hashable).

---

## 🛠 Set Methods

| Method | Description |
| :--- | :--- |
| **`add()`** | To add a single value to the set. |
| **`update()`** | Works like update or merge (adds multiple items from another iterable). |
| **`remove()`** | Removes a value from the set. *Gives error if not found.* |
| **`discard()`** | Removes a value without error if the value does not exist. |
| **`pop()`** | Removes a random value (because sets are unordered). |
| **`clear()`** | Empty the whole set. |
| **`copy()`** | To make a copy of the set. |

---

## 🔄 Set Operations Methods

| Method | Description |
| :--- | :--- |
| **`union()`** | Returns a set containing all elements from both sets. |
| **`intersection()`** | Returns a set containing common elements. |
| **`difference()`** | Returns elements in the first set but not in the second. |
| **`difference_update()`** | Removes the items in this set that are also included in another set. |
| **`symmetric_difference()`** | Returns elements that are in exactly one of the sets. |

---

## ⚖️ Set Comparison Methods

| Method | Description |
| :--- | :--- |
| **`issubset()`** | Returns True if all items in the set exist in the specified set. |
| **`issuperset()`** | Returns True if all items in the specified set exist in the set. |
| **`isdisjoint()`** | Returns True if two sets have no intersection. |
| **`intersection_update()`** | Removes the items in this set that are not present in other specified sets. |

---

## ⚙️ Built-in Functions

These built-in Python functions can be used with sets:
- **`len(set)`**: Returns the number of items in the set.
- **`max(set)`**: Returns the maximum value.
- **`min(set)`**: Returns the minimum value.
- **`set()`**: Creates a set or converts an iterable to a set.

---

## 📝 Implementation & Examples

### 1. Printing a Set
We **cannot** print a single value using an index (like we did for lists and tuples) because sets are unordered.
```python
fruits = {"apple", "banana", "cherry"}

# We can print the whole set at once
print(fruits)

# Or we can print via loop
for item in fruits:
    print(item)
```

### 2. Checking Existence
```python
print("banana" in fruits)
```

### 3. Adding and Updating
```python
# add(): Add a single value
fruits.add("orange")

# update(): Merge another set
more_fruits = {"cherry", "mango"}
fruits.update(more_fruits)
```

### 4. Removing Items
```python
# remove(): Gives error if not found
fruits.remove("mango")

# discard(): No error if not found
fruits.discard("banana")

# pop(): Removes a random item (because unordered)
fruits.pop()

# clear(): Empties the whole set
fruits.clear()
```

### 5. Copying a Set
```python
fruits_new = fruits.copy()
```
