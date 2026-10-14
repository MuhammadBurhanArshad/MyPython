"""
index.py

This script demonstrates Python Identity Operators and Membership Operators.
It covers 'is', 'is not', 'in', and 'not in'.
"""

# ==========================================
# 1. IDENTITY OPERATORS
# ==========================================
print("=== 1. Identity Operators ===")

# Creating a list (mutable object)
list_a = [10, 20, 30]
list_b = list_a           # list_b points to the same object as list_a
list_c = [10, 20, 30]     # list_c is a separate object with the same values

# 'is': Returns True if both variables point to same object
print(f"list_a is list_b: {list_a is list_b}")   # True
print(f"list_a is list_c: {list_a is list_c}")   # False

# 'is not': Returns True if both variables point to different object
print(f"list_a is not list_b: {list_a is not list_b}")  # False
print(f"list_a is not list_c: {list_a is not list_c}")  # True

# Note: For immutable objects like small integers and strings,
# Python may reuse the same object in memory for optimization.
x = 10
y = 10
print(f"x is y (for small ints): {x is y}")  # True (due to integer caching)
print()


# ==========================================
# 2. MEMBERSHIP OPERATORS
# ==========================================
print("=== 2. Membership Operators ===")

fruits = ["apple", "banana", "cherry"]
print(f"List of fruits: {fruits}")

# 'in': Returns True if value exists
print(f"'banana' in fruits: {'banana' in fruits}")     # True
print(f"'mango' in fruits: {'mango' in fruits}")       # False

# 'not in': Returns True if value does not exist
print(f"'mango' not in fruits: {'mango' not in fruits}") # True
print(f"'apple' not in fruits: {'apple' not in fruits}") # False
print()

# Membership operators work with other iterables too:

# String
text = "Python Programming"
print(f"'Python' in text: {'Python' in text}")         # True
print(f"'Java' not in text: {'Java' not in text}")     # True

# Dictionary (checks keys by default)
student = {"name": "Burhan", "age": 22}
print(f"'name' in student: {'name' in student}")       # True
print(f"'Burhan' in student: {'Burhan' in student}")   # False (checks keys, not values)
