"""
index.py

This script demonstrates the different data types available in Python.
It covers basic types, advanced types, and how to check the type of a variable.
"""

# ==========================================
# 1. BASIC DATA TYPES
# ==========================================

print("=== 1. Basic Data Types ===")

# String (Text)
x = "Hello World"
print(f"Value: {x} | Type: {type(x)}")

# Integer (Whole Number)
x = 25
print(f"Value: {x} | Type: {type(x)}")

# Float (Decimal Number)
x = 25.35
print(f"Value: {x} | Type: {type(x)}")

# Boolean (True/False)
x = True
print(f"Value: {x} | Type: {type(x)}")

# List (Ordered, Mutable collection)
x = ["HTML", "CSS"]
print(f"Value: {x} | Type: {type(x)}")

# Tuple (Ordered, Immutable collection)
x = ("HTML", "CSS")
print(f"Value: {x} | Type: {type(x)}")

# Dictionary (Key-Value pairs)
x = {"first": "Jane", "age": 20}
print(f"Value: {x} | Type: {type(x)}")

# Set (Unordered, Unique elements)
x = {"red", "green"}
print(f"Value: {x} | Type: {type(x)}")


# ==========================================
# 2. SOME OTHER DATA TYPES
# ==========================================

print("\n=== 2. Other Data Types ===")

# Complex Number
x = 4 + 6j
print(f"Value: {x} | Type: {type(x)}")

# Range (Sequence of numbers)
x = range(5)
print(f"Value: {x} | Type: {type(x)}")

# Frozenset (Immutable version of a set)
x = frozenset([1, 2, 3])
print(f"Value: {x} | Type: {type(x)}")

# None (Represents absence of value)
x = None
print(f"Value: {x} | Type: {type(x)}")

# Bytes (Immutable sequence of bytes)
x = b'Hello'
print(f"Value: {x} | Type: {type(x)}")

# Bytearray (Mutable sequence of bytes)
x = bytearray([65, 66, 67])
print(f"Value: {x} | Type: {type(x)}")

# Memoryview (Memory view of an object)
x = memoryview(bytes([65, 66, 67]))
print(f"Value: {x} | Type: {type(x)}")


# ==========================================
# 3. CATEGORY WISE DATA TYPES (COMMENTED)
# ==========================================

print("\n=== 3. Category Reference ===")
print("Numeric  : int, float, complex")
print("Boolean  : bool")
print("Text     : str")
print("Sequence : list, tuple, range")
print("Mapping  : dict")
print("Set      : set, frozenset")
print("Binary   : bytes, bytearray, memoryview")
print("Special  : NoneType (None)")


# ==========================================
# 4. CHECKING DATA TYPE WITH type()
# ==========================================

print("\n=== 4. Using type() method ===")
# We can use the type() function to verify the type of any variable
my_variable = "Python"
print(f"The type of '{my_variable}' is {type(my_variable)}")
