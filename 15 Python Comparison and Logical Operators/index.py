"""
index.py

This script demonstrates Python Comparison Operators and Logical Operators.
It covers equal to, not equal to, greater than, less than, and logical and/or/not.
"""

# ==========================================
# INITIAL VARIABLES
# ==========================================
a = 10
b = 5
c = 10

print(f"Variables: a = {a}, b = {b}, c = {c}\n")

# ==========================================
# 1. COMPARISON OPERATORS
# ==========================================
print("=== 1. Comparison Operators ===")

# Equal to (==)
print(f"a == c (10 == 10): {a == c}")

# Not Equal to (!=)
print(f"a != b (10 != 5): {a != b}")

# Greater than (>)
print(f"a > b (10 > 5): {a > b}")

# Lower than (<)
print(f"b < a (5 < 10): {b < a}")

# Greater than or equal to (>=)
print(f"a >= c (10 >= 10): {a >= c}")

# Less than or equal to (<=)
print(f"b <= a (5 <= 10): {b <= a}\n")


# ==========================================
# 2. LOGICAL OPERATORS
# ==========================================
print("=== 2. Logical Operators ===")

x = True
y = False

# 'and' operator: Returns True if both conditions are true
print(f"x and y (True and False): {x and y}")
print(f"x and True (True and True): {x and True}")

# 'or' operator: Returns True if at least one condition is true
print(f"x or y (True or False): {x or y}")
print(f"y or False (False or False): {y or False}")

# 'not' operator: Reverses the result
print(f"not x (not True): {not x}")
print(f"not y (not False): {not y}\n")


# ==========================================
# 3. COMBINING COMPARISON AND LOGICAL OPERATORS
# ==========================================
print("=== 3. Combined Example ===")

age = 25
has_license = True

# Check if person is eligible to drive
# Condition: Age must be 18 or above AND must have a license
is_eligible = (age >= 18) and (has_license == True)
print(f"Age: {age}, Has License: {has_license}")
print(f"Is eligible to drive? {is_eligible}")
