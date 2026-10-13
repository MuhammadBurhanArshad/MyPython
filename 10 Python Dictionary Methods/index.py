"""
index.py

This script demonstrates the various built-in methods available for Python Dictionaries.
It covers getting values, adding/updating, removing, copying, and other utility methods.
"""

# ==========================================
# INITIAL SETUP
# ==========================================
student = {
    "name": "Burhan",
    "age": 22,
    "course": "Python"
}
print(f"Initial Dictionary: {student}\n")

# ==========================================
# 1. GETTING VALUES
# ==========================================
print("=== 1. Getting Values ===")

# get(): Used to get value from key
name = student.get("name")
print(f"get('name'): {name}")

# get() with a default fallback value
city = student.get("city", "Not Found")
print(f"get('city', 'Not Found'): {city}")

# keys(): To get all the keys
all_keys = student.keys()
print(f"keys(): {all_keys}")

# values(): To get all the values
all_values = student.values()
print(f"values(): {all_values}")

# items(): Separate and return key & value
all_items = student.items()
print(f"items(): {all_items}\n")


# ==========================================
# 2. CREATING FROM KEYS
# ==========================================
print("=== 2. fromkeys() ===")

# fromkeys(): Create new dictionary from keys.
# Without default value
new_dict_1 = dict.fromkeys(["a", "b", "c"])
print(f"fromkeys (no value): {new_dict_1}")

# With default value
new_dict_2 = dict.fromkeys(["a", "b", "c"], "Unknown")
print(f"fromkeys (with 'Unknown'): {new_dict_2}\n")


# ==========================================
# 3. UPDATING & ADDING
# ==========================================
print("=== 3. update() ===")

# update(): to update and add key value
student.update({"age": 25})
student.update(city="Khi")
print(f"After update(): {student}\n")


# ==========================================
# 4. SETDEFAULT
# ==========================================
print("=== 4. setdefault() ===")

# setdefault(): to assign default value.
# 'name' already exists, so it won't change
student.setdefault("name", "Unknown")
# 'salary' does not exist, so it will be added with the default value
student.setdefault("salary", 50000)
print(f"After setdefault(): {student}\n")


# ==========================================
# 5. COPYING
# ==========================================
print("=== 5. copy() ===")

# copy(): to copy dictionary
student_copy = student.copy()
print(f"Original: {student}")
print(f"Copied  : {student_copy}\n")


# ==========================================
# 6. REMOVING ITEMS
# ==========================================
print("=== 6. Removing Items ===")

# pop(): removes the key from dictionary
popped_age = student.pop("age")
print(f"After pop('age') [Removed {popped_age}]: {student}")

# popitem(): automatically removes and returns the last key-value pair
popped_item = student.popitem()
print(f"After popitem() [Removed {popped_item}]: {student}\n")


# ==========================================
# 7. UNIVERSAL FUNCTIONS
# ==========================================
print("=== 7. Universal Functions ===")

# len(): return the number of keys.
length = len(student)
print(f"len(): {length} keys")

# str(): to convert dictionary in string
string_representation = str(student)
print(f"str(): {string_representation} (Type: {type(string_representation)})")
print()


# ==========================================
# 8. CLEARING THE DICTIONARY
# ==========================================
print("=== 8. clear() ===")

# clear(): empty the whole dictionary
student.clear()
print(f"After clear(): {student}")
print(f"Length after clear(): {len(student)}")
