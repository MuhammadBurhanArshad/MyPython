"""
index.py

This script demonstrates the Python If Elif Statement.
It shows how to check multiple conditions in sequence.
"""

# ==========================================
# 1. BASIC IF-ELIF-ELSE EXAMPLE
# ==========================================
print("=== 1. Basic If-Elif-Else ===")

time = 15

if time < 10:
    print("Good Morning")
elif time < 20:
    print("Good Day")
else:
    print("Good Night")

print()


# ==========================================
# 2. MULTIPLE ELIF CONDITIONS (GRADING SYSTEM)
# ==========================================
print("=== 2. Grading System ===")

marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

print(f"Marks: {marks}")
print()


# ==========================================
# 3. IF-ELIF WITH USER INPUT
# ==========================================
print("=== 3. User Input Example ===")

color = input("Enter a traffic light color (red/yellow/green): ").lower()

if color == "red":
    print("Stop!")
elif color == "yellow":
    print("Get ready to stop.")
elif color == "green":
    print("Go!")
else:
    print("Invalid color entered.")

print()


# ==========================================
# 4. IF-ELIF WITHOUT ELSE
# ==========================================
print("=== 4. If-Elif without Else ===")
# The 'else' block is optional. If no condition matches, nothing happens.

day = "Saturday"

if day == "Saturday":
    print("It's the weekend!")
elif day == "Sunday":
    print("It's the weekend!")

# If day was "Monday", nothing would print here because there is no 'else'.
print()


# ==========================================
# 5. PRACTICAL EXAMPLE: POSITIVE/NEGATIVE/ZERO
# ==========================================
print("=== 5. Practical Example: Number Check ===")

num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is Zero.")
    
print()


# ==========================================
# SUMMARY
# ==========================================
print("=== Summary ===")
print("Use 'if' for the first condition.")
print("Use 'elif' for secondary conditions (can be used multiple times).")
print("Use 'else' as a default fallback when all else fails.")
