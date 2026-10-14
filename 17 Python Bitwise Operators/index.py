"""
index.py

This script demonstrates Python Bitwise Operators.
It covers AND, OR, XOR, NOT, Left Shift, and Right Shift.
"""

# ==========================================
# INITIAL VARIABLES
# ==========================================
a = 5   # Binary: 0101
b = 3   # Binary: 0011

print(f"Variables: a = {a} (Binary: {bin(a)}), b = {b} (Binary: {bin(b)})\n")

# ==========================================
# 1. BITWISE AND (&)
# ==========================================
print("=== 1. Bitwise AND (&) ===")
# Sets each bit to 1 if both bits are 1
result_and = a & b
print(f"a & b = {result_and} (Binary: {bin(result_and)})\n")

# ==========================================
# 2. BITWISE OR (|)
# ==========================================
print("=== 2. Bitwise OR (|) ===")
# Sets each bit to 1 if at least one of two bits is 1
result_or = a | b
print(f"a | b = {result_or} (Binary: {bin(result_or)})\n")

# ==========================================
# 3. BITWISE XOR (^)
# ==========================================
print("=== 3. Bitwise XOR (^) ===")
# Sets each bit to 1 if only one of two bits is 1
result_xor = a ^ b
print(f"a ^ b = {result_xor} (Binary: {bin(result_xor)})\n")

# ==========================================
# 4. BITWISE NOT (~)
# ==========================================
print("=== 4. Bitwise NOT (~) ===")
# Inverts all the bits
# Formula: ~x = -(x + 1)
result_not = ~a
print(f"~a = {result_not} (Formula: -(a + 1))\n")

# ==========================================
# 5. BITWISE LEFT SHIFT (<<)
# ==========================================
print("=== 5. Bitwise Left Shift (<<) ===")
# Shifts bits to the left
# Formula: 5 << n -> 5 * (2 ** n)
left_shift_1 = 5 << 1
left_shift_2 = 5 << 2
print(f"5 << 1 = {left_shift_1} (Formula: 5 * 2^1)")
print(f"5 << 2 = {left_shift_2} (Formula: 5 * 2^2)\n")

# ==========================================
# 6. BITWISE RIGHT SHIFT (>>)
# ==========================================
print("=== 6. Bitwise Right Shift (>>) ===")
# Shifts bits to the right
# Formula: 20 >> n -> 20 / (2 ** n)
right_shift_1 = 20 >> 1
right_shift_2 = 20 >> 2
print(f"20 >> 1 = {right_shift_1} (Formula: 20 / 2^1)")
print(f"20 >> 2 = {right_shift_2} (Formula: 20 / 2^2)\n")

# ==========================================
# SUMMARY
# ==========================================
print("=== Summary of Bitwise Operators ===")
print(f"{'Operator':<10} {'Name':<20} {'Result'}")
print("-" * 45)
print(f"{'&':<10} {'Bitwise AND':<20} {a & b}")
print(f"{'|':<10} {'Bitwise OR':<20} {a | b}")
print(f"{'^':<10} {'Bitwise XOR':<20} {a ^ b}")
print(f"{'~':<10} {'Bitwise NOT':<20} {~a}")
print(f"{'<<':<10} {'Left Shift (5 << 1)':<20} {5 << 1}")
print(f"{'>>':<10} {'Right Shift (20 >> 1)':<20} {20 >> 1}")
