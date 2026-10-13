"""
index.py

This script demonstrates how to take user input in Python,
format strings, convert data types, and handle input errors.
"""

# ==========================================
# 1. BASIC USER INPUT
# ==========================================
print("=== 1. Basic User Input ===")

# input() function allows user to enter value
# The string inside is the prompt message
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python.\n")


# ==========================================
# 2. PRINT END PARAMETER
# ==========================================
print("=== 2. Print 'end' Parameter ===")

# By default, print() adds a new line at the end.
# We can change this using the 'end' parameter.
print("This is printed on the first line.", end=" ")
print("This continues on the same line!")
print() # To add a new line after the previous print


# ==========================================
# 3. FORMATTED STRINGS (F-STRINGS)
# ==========================================
print("=== 3. Formatted Strings ===")

city = input("Enter your city: ")
# We can print formatted string using f""
print(f"My name is {name} and city is {city}.\n")


# ==========================================
# 4. TYPE CONVERSION FROM INPUT
# ==========================================
print("=== 4. Type Conversion ===")

# input() always returns a string, so we use int() to convert
width = int(input("Enter width: "))
height = int(input("Enter height: "))
area = width * height
print(f"The area of the rectangle is: {area}\n")


# ==========================================
# 5. ERROR HANDLING WITH TRY & EXCEPT
# ==========================================
print("=== 5. Error Handling ===")

# We can add try & except to handle invalid inputs
try:
    width = int(input("Enter a valid width (number): "))
    print(f"Width entered: {width}")
except ValueError:
    print("Error: Please enter a valid number!")
