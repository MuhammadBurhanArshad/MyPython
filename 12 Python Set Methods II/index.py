"""
index.py

This script demonstrates Set creation, Set Operations (Union, Intersection, Difference),
Set Comparisons (Subset, Superset, Disjoint), and Built-in Functions.
"""

# ==========================================
# 1. CREATING A SET
# ==========================================
print("=== 1. Creating a Set ===")

# Using curly braces
set_1 = {"HTML", "CSS", "JS"}
print(f"Using curly braces: {set_1}")

# Using set() constructor
set_2 = set(("HTML", "CSS", "JS"))
print(f"Using set() constructor: {set_2}\n")


# ==========================================
# 2. SET OPERATIONS METHODS
# ==========================================
print("=== 2. Set Operations ===")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(f"Set A: {A}")
print(f"Set B: {B}\n")

# union(): used for merging two sets.
print(f"Union (A.union(B)): {A.union(B)}")
print(f"Union (A | B)     : {A | B}")

# intersection(): used to intersect sets.
print(f"Intersection (A.intersection(B)): {A.intersection(B)}")
print(f"Intersection (A & B)            : {A & B}")

# difference(): to find difference in sets.
print(f"Difference (A.difference(B)): {A.difference(B)}")
print(f"Difference (A - B)          : {A - B}")

# symmetric_difference(): take difference from set.
print(f"Symmetric Difference (A.symmetric_difference(B)): {A.symmetric_difference(B)}")
print(f"Symmetric Difference (A ^ B)                    : {A ^ B}\n")


# ==========================================
# 3. SET COMPARISON METHODS
# ==========================================
print("=== 3. Set Comparison ===")

set_a = {1, 2}
set_b = {1, 2, 3, 4}
set_c = {5, 6}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}\n")

# issubset(): to check if the set is subset or not.
print(f"Is A a subset of B? (A.issubset(B)): {set_a.issubset(set_b)}")

# issuperset(): As vice versa of subset (check superset)
print(f"Is B a superset of A? (B.issuperset(A)): {set_b.issuperset(set_a)}")

# isdisjoint(): if both set are different so it returns true.
print(f"Are A and C disjoint? (A.isdisjoint(C)): {set_a.isdisjoint(set_c)}\n")


# ==========================================
# 4. BUILT-IN FUNCTIONS
# ==========================================
print("=== 4. Built-in Functions ===")

# set(): convert list into set
numbers_list = [1, 2, 2, 3, 4, 4]
converted_set = set(numbers_list)
print(f"Converted list to set: {converted_set}")

fruits = {"apple", "banana", "cherry"}

# len(): Used to check length
length = len(fruits)
print(f"Length of fruits set: {length}")

# max() & min(): to find max and min
max_val = max(fruits)
min_val = min(fruits)
print(f"Max value in fruits: {max_val}")
print(f"Min value in fruits: {min_val}")
