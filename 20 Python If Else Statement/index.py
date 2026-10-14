"""
index.py

This script demonstrates the Python If Else Statement.
It covers basic if-else, membership operators, and logical operators.
"""

# ==========================================
# 1. BASIC IF-ELSE
# ==========================================
print("=== 1. Basic If-Else ===")

x = 5

if x > 10:
    print(f"x = {x} -> x is Greater than 10")
else:
    print(f"x = {x} -> x is Not Greater than 10")

print()


# ==========================================
# 2. IF-ELSE WITH MEMBERSHIP OPERATOR
# ==========================================
print("=== 2. If-Else with 'in' Operator ===")

numbers = [11, 22, 33, 44, 55]

if 33 in numbers:
    print("33 is Present in the list")
else:
    print("33 is Not Present in the list")

# Check for a value that is not in the list
if 99 in numbers:
    print("99 is Present in the list")
else:
    print("99 is Not Present in the list")

print()


# ==========================================
# 3. IF-ELSE WITH COMPARISON & LOGICAL OPERATORS
# ==========================================
print("=== 3. If-Else with Logical Operators ===")

username = "admin"
password = "1234"
name = "Burhan"

if (username == "admin" and password == "1234"):
    print(f"Hello Mr. {name}")
else:
    print(f"Hello Miss. {name}")

print()


# ==========================================
# 4. IF-ELSE WITH USER INPUT
# ==========================================
print("=== 4. If-Else with User Input ===")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

print()


# ==========================================
# 5. IF-ELSE WITH `or` OPERATOR
# ==========================================
print("=== 5. If-Else with 'or' Operator ===")

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print(f"{day} is a Weekend!")
else:
    print(f"{day} is a Working Day.")

print()


# ==========================================
# 6. IF-ELSE WITH NEGATIVE CONDITION
# ==========================================
print("=== 6. If-Else with Negative Condition ===")

is_raining = False

if is_raining:
    print("Take an umbrella.")
else:
    print("No need for an umbrella.")

print()


# ==========================================
# 7. PRACTICAL EXAMPLE: EVEN OR ODD
# ==========================================
print("=== 7. Practical Example: Even or Odd ===")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

print()


# ==========================================
# SUMMARY
# ==========================================
print("=== Summary ===")
print("The 'if' block executes when the condition is True.")
print("The 'else' block executes when the condition is False.")
print("'else' is the default option for the 'if' condition.")
