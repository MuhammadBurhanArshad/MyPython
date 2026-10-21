# Python Nested If Statement

This guide covers the Nested `if` statement in Python, based on the provided notes and expanded with practical examples.

## 📌 What is a Nested If Statement?

A **Nested If** statement means placing an `if` (or `if-else`) block inside another `if` block. We can use another `if` condition inside an `if` block to check secondary conditions only if the first condition is met.

---

## 📝 Syntax

```python
if condition_1:
    # Statements for condition 1
    if condition_2:
        # Statements for condition 2
    else:
        # Statements if condition 2 is False
else:
    # Statements if condition 1 is False
```

### Key Points:
- **Indentation** is crucial. The inner `if` must be indented further than the outer `if`.
- The inner `if` block is only evaluated if the outer `if` condition is `True`.

---

## 💡 Example 1: Voting Eligibility (from notes)

Here is the example from the notes checking if someone is eligible to vote:

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote.")
    else:
        print("Must be a Citizen to vote.")
else:
    print("Must be at least 18 for vote.")
```

**Output:**
```
Eligible to vote.
```

### Step-by-Step Explanation:
1. `age >= 18` is checked first. Since `age` is 20, this is `True`. We enter the outer `if`.
2. Inside, `if citizen:` is checked. Since `citizen` is `True`, it prints `"Eligible to vote."`.
3. If `citizen` were `False`, it would print `"Must be a Citizen to vote."`.
4. If `age` were less than 18, it would skip the inner block entirely and print `"Must be at least 18 for vote."`.

---

## 🛒 Example 2: Mini-Program - Online Store Checkout

This program checks if a user is logged in, and if so, verifies if their cart has items before allowing them to checkout.

```python
is_logged_in = True
cart_items = 3

if is_logged_in:
    print("Welcome back!")
    if cart_items > 0:
        print(f"Proceed to checkout with {cart_items} items.")
    else:
        print("Your cart is empty. Add items to checkout.")
else:
    print("Please log in to continue.")
```

**Output:**
```
Welcome back!
Proceed to checkout with 3 items.
```

---

## 🏧 Example 3: Mini-Program - ATM Withdrawal

This program checks if the PIN is correct, and if so, verifies if there are sufficient funds.

```python
pin = 1234
balance = 500
withdrawal_amount = 600

if pin == 1234:
    print("PIN accepted.")
    if withdrawal_amount <= balance:
        print(f"Withdrawal successful. Dispensing ${withdrawal_amount}.")
    else:
        print(f"Insufficient funds. Your balance is ${balance}.")
else:
    print("Incorrect PIN. Access denied.")
```

**Output:**
```
PIN accepted.
Insufficient funds. Your balance is $500.
```
