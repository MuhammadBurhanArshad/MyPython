"""
index.py

This script demonstrates Python Conditional Expressions (Ternary Operators).
It includes basic one-liners and mini-programs.
"""

# ==========================================
# 1. BASIC ADULT/MINOR CHECK
# ==========================================
print("=== 1. Basic Adult/Minor Check ===")

age = 20
# variable = value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"

print(f"Age: {age}")
print(f"Status: {status}\n")


# ==========================================
# 2. EVEN OR ODD CHECK
# ==========================================
print("=== 2. Even or Odd Check ===")

num = 10
result = "Even" if num % 2 == 0 else "Odd"

print(f"Number: {num}")
print(f"Result: {result}\n")


# ==========================================
# 3. MULTI-CONDITIONAL (NESTED TERNARY)
# ==========================================
print("=== 3. Multi-Conditional (Grading) ===")

marks = 85
# Result = "A" if condition1 else "B" if condition2 else "C"
grade = "A" if marks >= 90 else "B" if marks >= 80 else "C"

print(f"Marks: {marks}")
print(f"Grade: {grade}\n")


# ==========================================
# 4. MINI-PROGRAM: FREE SHIPPING CHECK
# ==========================================
print("=== 4. Mini-Program: Free Shipping ===")

cart_total = 45.00
# Shipping is 0 if cart is >= 50, otherwise it's 5.99
shipping_fee = 0 if cart_total >= 50 else 5.99

print(f"Cart Total: ${cart_total:.2f}")
print(f"Shipping Fee: ${shipping_fee:.2f}")
print(f"Total to Pay: ${cart_total + shipping_fee:.2f}\n")


# ==========================================
# 5. MINI-PROGRAM: PASSWORD VALIDATION
# ==========================================
print("=== 5. Mini-Program: Password Check ===")

password = "Secret123"
# Check if length is at least 8 characters
strength = "Strong" if len(password) >= 8 else "Weak"

print(f"Password entered: {'*' * len(password)}")
print(f"Password Strength: {strength}\n")


# ==========================================
# 6. MINI-PROGRAM: LOGIN STATUS
# ==========================================
print("=== 6. Mini-Program: Login Status ===")

is_logged_in = False
# If logged in, say "Welcome Back", else "Please Log In"
message = "Welcome Back!" if is_logged_in else "Please Log In"

print(f"Message: {message}\n")


# ==========================================
# SUMMARY
# ==========================================
print("=== Summary ===")
print("Conditional Expressions (Ternary operators) are used for")
print("simple if-else logic on a single line to keep code concise.")
