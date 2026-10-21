"""
index.py

This script demonstrates the Python Nested If Statement.
It includes a voting eligibility check and mini-programs
for an e-commerce checkout and an ATM withdrawal.
"""

# ==========================================
# 1. BASIC NESTED IF EXAMPLE (VOTING)
# ==========================================
print("=== 1. Basic Nested If (Voting) ===")

age = 20
is_citizen = True

if age >= 18:
    # This block only runs if age >= 18
    if is_citizen:
        print("Eligible to vote.")
    else:
        print("Must be a Citizen to vote.")
else:
    print("Must be at least 18 for vote.")

print()


# ==========================================
# 2. MINI-PROGRAM: ONLINE STORE CHECKOUT
# ==========================================
print("=== 2. Mini-Program: Online Store ===")

is_logged_in = True
cart_items = 3

if is_logged_in:
    print("Welcome back!")
    # Inner if checks cart contents
    if cart_items > 0:
        print(f"Proceed to checkout with {cart_items} items.")
    else:
        print("Your cart is empty. Add items to checkout.")
else:
    print("Please log in to continue.")

print()


# ==========================================
# 3. MINI-PROGRAM: ATM WITHDRAWAL
# ==========================================
print("=== 3. Mini-Program: ATM Withdrawal ===")

stored_pin = 1234
account_balance = 500.00
withdraw_amount = 250.00

entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin == stored_pin:
    print("PIN accepted.")
    
    # Inner if checks balance
    if withdraw_amount <= account_balance:
        account_balance -= withdraw_amount
        print(f"Withdrawal successful. Please take your cash: ${withdraw_amount:.2f}")
        print(f"Remaining balance: ${account_balance:.2f}")
    else:
        print(f"Error: Insufficient funds. Your current balance is ${account_balance:.2f}.")
        
else:
    print("Error: Incorrect PIN. Access denied.")

print()


# ==========================================
# 4. MINI-PROGRAM: SCHOLARSHIP ELIGIBILITY
# ==========================================
print("=== 4. Mini-Program: Scholarship Check ===")

gpa = 3.8
extracurriculars = True

if gpa >= 3.5:
    print("High GPA achieved.")
    # Inner check for extracurriculars
    if extracurriculars:
        print("Congratulations! You qualify for the full scholarship.")
    else:
        print("You qualify for the partial scholarship. Consider joining a club.")
else:
    print("GPA is below 3.5. You do not meet the minimum requirement for this scholarship.")

print()


# ==========================================
# SUMMARY
# ==========================================
print("=== Summary ===")
print("Nested 'if' statements are used when you need to check a condition")
print("only AFTER another condition has been proven to be True.")
