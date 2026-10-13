"""
index.py

This script demonstrates the use of variables in Python, covering
naming rules, dynamic typing, multiple assignments, and concatenation.
"""

# ==========================================
# 1. VARIABLES BASICS
# ==========================================

# A variable is like a bucket that stores a value
name = "Burhan"
print(name)  # Output: Burhan

# Note: print() must be lowercase. 'Print' will cause an error.
# Print(name)  # <-- This would cause an error


# ==========================================
# 2. VARIABLE NAMING RULES
# ==========================================

# Valid variable names
my_variable = "Uses underscore"
_variable = "Starts with underscore"
variable1 = "Contains number at the end"
var_1 = "Contains number in the middle"
CamelCase = "No case restriction (case-sensitive)"

print(my_variable)
print(_variable)
print(variable1)
print(var_1)
print(CamelCase)

# Invalid variable names (Uncommenting these will cause errors)
# 1variable = "Cannot start with a number"
# my variable = "Cannot contain spaces"
# for = "Cannot be a keyword"


# ==========================================
# 3. DYNAMIC TYPING (OVERWRITING)
# ==========================================

# Variable can be overwritten easily, irrespective of data types
data = 10
print(f"Data: {data}, Type: {type(data)}")

data = "Now I am a string"
print(f"Data: {data}, Type: {type(data)}")


# ==========================================
# 4. MULTIPLE VARIABLE ASSIGNMENTS
# ==========================================

# Assigning different values to different variables
a, b, c = 10, 20, 30
print(f"a = {a}, b = {b}, c = {c}")

# Assigning the same value to multiple variables
x = y = z = 100
print(f"x = {x}, y = {y}, z = {z}")


# ==========================================
# 5. CONCATENATION (USING + AND ,)
# ==========================================

first_name = "Muhammad"
last_name = "Burhan"

# Using the + operator (requires strings to be joined manually)
full_name_plus = first_name + " " + last_name
print("Using +: " + full_name_plus)

# Using the , operator (automatically adds a space)
print("Using ,:", first_name, last_name)


# ==========================================
# 6. DATA TYPES (BONUS)
# ==========================================

string_var = "Hello"
int_var = 25
float_var = 3.14
bool_var = True

print("\n--- Data Types ---")
print(f"String: {string_var} | Type: {type(string_var)}")
print(f"Integer: {int_var} | Type: {type(int_var)}")
print(f"Float: {float_var} | Type: {type(float_var)}")
print(f"Boolean: {bool_var} | Type: {type(bool_var)}")
