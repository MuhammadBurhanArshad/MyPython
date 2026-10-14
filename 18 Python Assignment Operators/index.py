"""
index.py

This script demonstrates Python Assignment Operators.
It covers all arithmetic and bitwise assignment operators.
"""

print("=== 1. Basic Assignment (=) ===")
x = 5
print(f"x = 5 -> x = {x}\n")

print("=== 2. Add and Assign (+=) ===")
x = 5
x += 3  # Equivalent to x = x + 3
print(f"x += 3 -> x = {x}\n")

print("=== 3. Subtract and Assign (-=) ===")
x = 5
x -= 3  # Equivalent to x = x - 3
print(f"x -= 3 -> x = {x}\n")

print("=== 4. Multiply and Assign (*=) ===")
x = 5
x *= 3  # Equivalent to x = x * 3
print(f"x *= 3 -> x = {x}\n")

print("=== 5. Divide and Assign (/=) ===")
x = 6
x /= 3  # Equivalent to x = x / 3
print(f"x /= 3 -> x = {x} (Note: returns float)\n")

print("=== 6. Floor Divide and Assign (//=) ===")
x = 10
x //= 3  # Equivalent to x = x // 3
print(f"x //= 3 -> x = {x}\n")

print("=== 7. Modulus and Assign (%=) ===")
x = 10
x %= 3  # Equivalent to x = x % 3
print(f"x %= 3 -> x = {x}\n")

print("=== 8. Exponentiate and Assign (**=) ===")
x = 2
x **= 3  # Equivalent to x = x ** 3
print(f"x **= 3 -> x = {x}\n")

print("=== 9. Bitwise AND and Assign (&=) ===")
x = 5
x &= 3  # Equivalent to x = x & 3
print(f"x &= 3 -> x = {x}\n")

print("=== 10. Bitwise OR and Assign (|=) ===")
x = 5
x |= 3  # Equivalent to x = x | 3
print(f"x |= 3 -> x = {x}\n")

print("=== 11. Bitwise XOR and Assign (^=) ===")
x = 5
x ^= 3  # Equivalent to x = x ^ 3
print(f"x ^= 3 -> x = {x}\n")

print("=== 12. Left Shift and Assign (<<=) ===")
x = 5
x <<= 1  # Equivalent to x = x << 1
print(f"x <<= 1 -> x = {x}\n")

print("=== 13. Right Shift and Assign (>>=) ===")
x = 20
x >>= 1  # Equivalent to x = x >> 1
print(f"x >>= 1 -> x = {x}\n")
