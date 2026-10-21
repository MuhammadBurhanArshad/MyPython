# Python For Loop

This guide covers the `for` loop in Python. It is based on the provided notes and expanded with practical examples.

## 📌 What is a For Loop?

A `for` loop is used to iterate over a sequence (such as a list, tuple, string, or dictionary). It is used to print the whole sequence or perform an action on each item once.

---

## 📝 Basic Syntax

```python
for item in sequence:
    # Code block to execute for each item
```

---

## 🔄 Iterating Through Different Data Types

### 1. Lists and Tuples
You can iterate through lists or tuples to access each item.

```python
subjects = ["Math", "Science", "English"]

for subject in subjects:
    print(subject)
```

### 2. Dictionaries
When iterating through a dictionary, you can use `.items()` to get both the key and the value.

```python
student = {"name": "Burhan", "age": 22}

for key, v in student.items():
    print(key, ":", v)
```

---

## 🛠 Helpful Built-in Functions for Loops

### 1. `enumerate()`
The `enumerate()` function adds a counter to an iterable and returns it. It is useful when you need both the **index** and the **value**.

```python
fruits = ["Apple", "Banana", "Cherry"]

for index, fruit in enumerate(fruits):
    print(index, ":", fruit)
```

### 2. `zip()`
The `zip()` function is used to **merge sequences** (like two lists) together. It pairs the first item of the first list with the first item of the second list, and so on.

```python
students = ["Ali", "Sara", "John"]
marks = [85, 92, 78]

for name, mark in zip(students, marks):
    print(name, "scored", mark)
```

---

## 🔀 Conditions in Loops

You can include `if` statements inside a loop to filter or conditionally execute code.

```python
# Print only even numbers from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:
        print(num)
```

---

## 🏁 The `else` Clause in Loops

Python allows you to define an `else` block for a `for` loop. The `else` block executes **after the loop finishes** normally (i.e., if it wasn't stopped by a `break` statement).

```python
for num in range(1, 6):
    print(num)
else:
    print("Loop completed")
```
