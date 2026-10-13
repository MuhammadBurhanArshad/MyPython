"""
index.py

This script demonstrates the use of Python Sets, covering
uniqueness, lack of indexing, methods, operations, and comparisons.
"""

# ==========================================
# INITIAL SETUP
# ==========================================
fruits = {"apple", "banana", "cherry", "apple", 10}
print(f"Initial Set (note: duplicate 'apple' and mixed types): {fruits}\n")
# Note: Sets automatically remove duplicates, so "apple" appears only once.


# ==========================================
# 1. KEY POINTS DEMONSTRATION
# ==========================================
print("=== 1. Key Points ===")
print(f"Unique Values: {set([1, 2, 2, 3, 3, 3])}") # Duplicates removed
print(f"Unordered (no indexing): Cannot use fruits[0]\n")


# ==========================================
# 2. PRINTING A SET
# ==========================================
print("=== 2. Printing a Set ===")
# We can't print single value as we did for list & tuple
# print(fruits[0]) # <-- This will cause a TypeError

# We can print set via loop as:
print("Looping through set:")
for item in fruits:
    print(f" - {item}")

# OR print the whole set
print(f"Print whole set: {fruits}\n")


# ==========================================
# 3. CHECKING EXISTENCE
# ==========================================
print("=== 3. Checking Existence ===")
# For checking existence from set:
print(f"Is 'banana' in fruits? {'banana' in fruits}")
print(f"Is 'mango' in fruits? {'mango' in fruits}\n")


# ==========================================
# 4. SET METHODS (ADDING & UPDATING)
# ==========================================
print("=== 4. Adding and Updating ===")

# add(): to add value in set
fruits.add("orange")
print(f"After add('orange'): {fruits}")

# update(): works like to update or merge list or set
more_fruits = {"cherry", "mango"}
fruits.update(more_fruits)
print(f"After update(more_fruits): {fruits}\n")


# ==========================================
# 5. SET METHODS (REMOVING)
# ==========================================
print("=== 5. Removing Items ===")

# remove(): Works to remove value from set.
# gives error when not found
fruits.remove("mango")
print(f"After remove('mango'): {fruits}")

# discard(): remove value without error for non existing
fruits.discard("banana") # No error even if 'banana' is not there
fruits.discard("watermelon") # No error for non-existing item
print(f"After discard('banana') and discard('watermelon'): {fruits}")

# pop(): remove the random value (Because set are unordered)
popped_item = fruits.pop()
print(f"After pop() [Removed '{popped_item}']: {fruits}\n")


# ==========================================
# 6. SET OPERATIONS METHODS
# ==========================================
print("=== 6. Set Operations ===")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {set_a.union(set_b)}")
print(f"Intersection: {set_a.intersection(set_b)}")
print(f"Difference (A - B): {set_a.difference(set_b)}")
print(f"Symmetric Difference: {set_a.symmetric_difference(set_b)}\n")


# ==========================================
# 7. SET COMPARISON METHODS
# ==========================================
print("=== 7. Set Comparison ===")

set_c = {1, 2}
set_d = {1, 2, 3, 4}

print(f"Set C: {set_c}")
print(f"Set D: {set_d}")
print(f"Is C a subset of D? {set_c.issubset(set_d)}")
print(f"Is D a superset of C? {set_d.issuperset(set_c)}")
print(f"Are C and D disjoint? {set_c.isdisjoint(set_d)}\n")


# ==========================================
# 8. BUILT-IN FUNCTIONS
# ==========================================
print("=== 8. Built-in Functions ===")

numbers = {10, 5, 25, 8}
print(f"Numbers Set: {numbers}")
print(f"len(set): {len(numbers)}")
print(f"max(set): {max(numbers)}")
print(f"min(set): {min(numbers)}")

# set(): Converting a list to a set (removes duplicates)
my_list = [1, 2, 2, 3, 4]
converted_set = set(my_list)
print(f"set(list): {converted_set}\n")


# ==========================================
# 9. COPYING AND CLEARING
# ==========================================
print("=== 9. Copying and Clearing ===")

# copy(): to make a copy of set
fruits_new = fruits.copy()
print(f"Copied Set: {fruits_new}")

# clear(): for empty the whole set.
fruits.clear()
print(f"After clear(): {fruits}")
