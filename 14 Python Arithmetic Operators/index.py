"""
index.py

This script demonstrates the use of Python Arithmetic Operators.
It covers addition, subtraction, multiplication, division,
floor division, modulus, and exponentiation.
"""

# ==========================================
# INITIAL VARIABLES
# ==========================================
a = 10
b = 5

print(f"Variables: a = {a}, b = {b}\n")

# ==========================================
# 1. ADDITION (+)
# ==========================================
print("=== 1. Addition (+) ===")
result = a + b
print(f"{a} + {b} = {result}\n")

# ==========================================
# 2. SUBTRACTION (-)
# ==========================================
print("=== 2. Subtraction (-) ===")
result = a - b
print(f"{a} - {b} = {result}\n")

# ==========================================
# 3. MULTIPLICATION (*)
# ==========================================
print("=== 3. Multiplication (*) ===")
result = a * b
print(f"{a} * {b} = {result}\n")

# ==========================================
# 4. DIVISION (/)
# ==========================================
print("=== 4. Division (/) ===")
# Note: Division in Python 3 always returns a float
result = a / b
print(f"{a} / {b} = {result}\n")

# ==========================================
# 5. FLOOR DIVISION (//)
# ==========================================
print("=== 5. Floor Division (//) ===")
# Note: Floor division rounds down to the nearest integer
result = 10 // 3
print(f"10 // 3 = {result}\n")

# ==========================================
# 6. MODULUS / REMAINDER (%)
# ==========================================
print("=== 6. Modulus / Remainder (%) ===")
result = 10 % 5
print(f"10 % 5 = {result}\n")

# ==========================================
# 7. EXPONENTIATION / POWER (**)
# ==========================================
print("=== 7. Exponentiation / Power (**) ===")
result = 2 ** 3
print(f"2 ** 3 = {result}\n")


# ==========================================
# PRACTICAL EXAMPLE
# ==========================================
print("=== Practical Example: Area of Circle ===")
radius = 7
pi = 3.14159
area = pi * (radius ** 2)
print(f"Radius: {radius}")
print(f"Area of Circle: {area}")
