"""
index.py

This script demonstrates the methods and universal functions available for Python Tuples.
It covers count(), index(), len(), max(), min(), and nested tuples.
"""

# ==========================================
# INITIAL SETUP
# ==========================================

# Creating a tuple using round brackets ()
fruits = ("apple", "Banana", "apple", "cherry")
print(f"Initial Tuple: {fruits}\n")


# ==========================================
# 1. TUPLE METHODS
# ==========================================
print("=== 1. Tuple Methods ===")

# count(): Used to show count (existence) of a value
apple_count = fruits.count("apple")
print(f"Count of 'apple': {apple_count}")

# index(): Used to find the index of a value
# If duplicates exist, it returns the first occurrence
banana_index = fruits.index("Banana")
print(f"Index of 'Banana': {banana_index}\n")


# ==========================================
# 2. UNIVERSAL METHODS
# ==========================================
print("=== 2. Universal Methods ===")

# len(): Get the length of the tuple
length = len(fruits)
print(f"Length of tuple: {length}")

# max(): Find the maximum value (alphabetically, for strings)
max_val = max(fruits)
print(f"Max value: {max_val}")

# min(): Find the minimum value (alphabetically, for strings)
min_val = min(fruits)
print(f"Min value: {min_val}\n")

# tuple(): Convert a list (or other iterable) to a tuple
my_list = ["red", "green", "blue"]
converted_tuple = tuple(my_list)
print(f"Converted List to Tuple: {converted_tuple}\n")


# ==========================================
# 3. NESTED TUPLES
# ==========================================
print("=== 3. Nested Tuples ===")

# Creating a nested tuple
nested_tuple = ((10, 20), (30, 40), (50, 60))
print(f"Nested Tuple: {nested_tuple}")

# Accessing elements inside a nested tuple
print(f"First inner tuple: {nested_tuple[0]}")
print(f"Second element of the first inner tuple: {nested_tuple[0][1]}")


# ==========================================
# 4. TUPLE IMMUTABILITY
# ==========================================
print("\n=== 4. Immutability Check ===")
print("Tuples are immutable. Attempting to change an item will raise an error.")
# Uncommenting the line below will cause a TypeError:
# fruits[0] = "mango" 
