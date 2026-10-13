"""
index.py

This script demonstrates the various built-in methods available for Python Lists.
It covers adding, removing, sorting, copying, and other utility methods.
"""

# ==========================================
# INITIAL SETUP
# ==========================================
fruits = ["Apple", "Banana", "Cherry", "Mango"]
print(f"Initial List: {fruits}\n")

# ==========================================
# 1. ADDING VALUES
# ==========================================
print("=== 1. Adding Values ===")

# append(): Add value at the end
fruits.append("Grapes")
print(f"After append('Grapes'): {fruits}")

# insert(): Add value at a specified index
fruits.insert(0, "Orange")
print(f"After insert(0, 'Orange'): {fruits}")

# extend(): Merge another list
veg = ["Carrot", "Potato"]
fruits.extend(veg)
print(f"After extend(veg): {fruits}\n")


# ==========================================
# 2. REMOVING VALUES
# ==========================================
print("=== 2. Removing Values ===")

# remove(): Remove by value
fruits.remove("Banana")
print(f"After remove('Banana'): {fruits}")

# pop(): Remove last value or specific index
popped_item = fruits.pop()
print(f"After pop() [Removed '{popped_item}']: {fruits}")

fruits.pop(1) # Removes item at index 1
print(f"After pop(1): {fruits}")

# clear(): Clear the whole list
# We will demonstrate clear() at the very end to not lose our data
print()


# ==========================================
# 3. SORTING & REVERSING
# ==========================================
print("=== 3. Sorting & Reversing ===")

# sort(): Sort the list
fruits.sort()
print(f"After sort(): {fruits}")

# reverse(): Reverse the list
fruits.reverse()
print(f"After reverse(): {fruits}\n")


# ==========================================
# 4. UTILITY & INFORMATION
# ==========================================
print("=== 4. Utility & Information ===")

# copy(): Copy the list
fruits_copy = fruits.copy()
print(f"Copied List (fruits_copy): {fruits_copy}")

# index(): Find the index of an item
# Let's add a duplicate to test count() properly
fruits.append("Apple")
index_of_apple = fruits.index("Apple")
print(f"Index of 'Apple': {index_of_apple}")

# count(): Count existence of an item
count_apple = fruits.count("Apple")
print(f"Count of 'Apple': {count_apple}")

# len(): Get the length
length = len(fruits)
print(f"Length of list: {length}")

# max() & min(): Find maximum and minimum values
# (Note: Works best with homogeneous lists of numbers or strings)
max_val = max(fruits)
min_val = min(fruits)
print(f"Max value: {max_val}")
print(f"Min value: {min_val}\n")


# ==========================================
# 5. CLEARING THE LIST
# ==========================================
print("=== 5. Clearing the List ===")

# clear(): Removes all items
fruits.clear()
print(f"After clear(): {fruits}")
print(f"Length after clear(): {len(fruits)}")
