"""
index.py

This script demonstrates the Python If Statement.
It shows how to check a condition and execute code based on the result.
"""

print("=== 1. Basic If Statement ===")

x = 15

# Check if x is greater than 10
if x > 10:
    print(f"x = {x} -> x is Greater than 10")

print()


# ==========================================
# 2. If Statement with User Input
# ==========================================
print("=== 2. If Statement with User Input ===")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")

print()


# ==========================================
# 3. If Statement with Strings
# ==========================================
print("=== 3. If Statement with Strings ===")

name = "Burhan"

if name == "Burhan":
    print(f"Hello, {name}! Welcome back.")

print()


# ==========================================
# 4. If Statement with Multiple Conditions (and/or)
# ==========================================
print("=== 4. If Statement with Logical Operators ===")

marks = 85
attendance = 90

# Check if student passed AND has good attendance
if marks >= 50 and attendance >= 75:
    print(f"Marks: {marks}, Attendance: {attendance}%")
    print("Result: PASSED with good attendance!")

print()


# ==========================================
# 5. If Statement with Boolean Variable
# ==========================================
print("=== 5. If Statement with Boolean ===")

is_logged_in = True

if is_logged_in:
    print("User is logged in. Showing dashboard.")

print()


# ==========================================
# 6. Nested If Statement
# ==========================================
print("=== 6. Nested If Statement ===")

num = 25

if num > 0:
    print(f"{num} is a positive number.")
    if num % 2 == 0:
        print(f"{num} is also an even number.")
    else:
        print(f"{num} is an odd number.")

print()


# ==========================================
# 7. If Statement with `in` Operator
# ==========================================
print("=== 7. If Statement with 'in' Operator ===")

fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is available in the list.")

print()


# ==========================================
# 8. If Statement with `not` Operator
# ==========================================
print("=== 8. If Statement with 'not' Operator ===")

is_raining = False

if not is_raining:
    print("It's not raining. You can go outside!")

print()


# ==========================================
# SUMMARY
# ==========================================
print("=== Summary ===")
print("The 'if' statement checks a condition.")
print("If the condition is True, the indented code block executes.")
print("If the condition is False, the code block is skipped.")
