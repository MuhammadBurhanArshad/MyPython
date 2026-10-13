"""
index.py

This script demonstrates the use of Lists and Tuples in Python,
covering indexing, slicing, unpacking, mutability, and key differences.
"""

# ==========================================
# 1. PYTHON LIST
# ==========================================

print("=== 1. Python List ===")

# A list stores multiple data types in a single variable
x = ["HTML", "CSS", "JS"]
print(f"Original List: {x}")

# Accessing a single value using index (0-based)
print(f"Item at index 1: {x[1]}")

# Modifying an item in the list (Lists are mutable)
x[1] = "Python"
print(f"After modification: {x}")

# Accessing from the last using reverse indexing
print(f"Last item: {x[-1]}")

# Using range/slicing (x[1:3] gives items from index 1 to 2)
print(f"Sliced List [1:3]: {x[1:3]}")

# Unpacking a list into variables
data = ["Sandeep", 25, 75.50, True]
name, age, marks, married = data
print(f"\nUnpacked Data -> Name: {name}, Age: {age}, Marks: {marks}, Married: {married}")

print("-" * 40)

# ==========================================
# 2. PYTHON TUPLE
# ==========================================

print("=== 2. Python Tuple ===")

# Tuple is like a list but we use round brackets ()
# Tuples are immutable (cannot be changed after creation)
fruits = ("Apple", "Banana")
print(f"Original Tuple: {fruits}")

# Accessing values using index
print(f"Item at index 0: {fruits[0]}")

# Tuples allow duplicates
duplicate_tuple = ("Apple", "Banana", "Apple")
print(f"Tuple with duplicates: {duplicate_tuple}")

# Tuples are faster than Lists
# Attempting to change a tuple will cause an error:
# fruits[0] = "Mango"  # <-- This will raise a TypeError

# Use a tuple when data should not change
# Tuple could be used as list (supports indexing, slicing, etc.)
print(f"Last item in tuple: {fruits[-1]}")

print("-" * 40)

# ==========================================
# 3. SUMMARY
# ==========================================

print("=== 3. Key Notes ===")
print("List : Mutable (Changeable), uses []")
print("Tuple: Immutable (Unchangeable), uses ()")
