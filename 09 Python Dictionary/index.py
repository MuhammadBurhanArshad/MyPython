"""
index.py

This script demonstrates the use of Python Dictionaries, covering
creation, accessing values, adding/updating, looping, and key existence checks.
"""

# ==========================================
# 1. DICTIONARY BASICS
# ==========================================

print("=== 1. Dictionary Basics ===")

# A dictionary is a key-value pair
student = {
    "name": "Burhan",
    "age": 22
}

# Printing the whole dictionary
print(f"Whole Dictionary: {student}")

# Accessing a single value using its key
print(f"Single Value (name): {student['name']}\n")


# ==========================================
# 2. KEY POINTS TO REMEMBER
# ==========================================

print("=== 2. Key Points ===")
# 1. Keys must be unique
# 2. Keys can be strings, numbers, tuples, etc.
# 3. Values can be of any data type
# 4. Dictionaries are mutable (changeable)
# 5. Access values using keys
print("Dictionaries store unique key-value pairs and are mutable.\n")


# ==========================================
# 3. ADDING AND UPDATING VALUES
# ==========================================

print("=== 3. Adding and Updating ===")

# Adding a new key-value pair
student["gender"] = "male"
print(f"After adding 'gender': {student}")

# Updating an existing value
student["age"] = 23
print(f"After updating 'age': {student}\n")


# ==========================================
# 4. CREATING A DICTIONARY WITH dict()
# ==========================================

print("=== 4. Using dict() constructor ===")

# Creating a dictionary using the dict() constructor
student2 = dict(
    name="John",
    age=20
)
print(f"Dictionary created with dict(): {student2}\n")


# ==========================================
# 5. LOOPING THROUGH A DICTIONARY
# ==========================================

print("=== 5. Looping through Dictionary ===")

# Using .values() to get values
print("Values:")
for value in student.values():
    print(f" - {value}")

# Using .items() to get key and value
print("\nKeys and Values:")
for key, value in student.items():
    print(f" - {key}: {value}")
print()


# ==========================================
# 6. CHECKING KEY EXISTENCE
# ==========================================

print("=== 6. Key Existence ===")

# Checking if a key exists using 'in'
if "name" in student:
    print("Key Found: 'name' exists in the dictionary.")

if "salary" not in student:
    print("Key Not Found: 'salary' does not exist in the dictionary.")
