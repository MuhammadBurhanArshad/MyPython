# Python Bitwise Operators

This guide covers Python Bitwise Operators. Bitwise operators deal with binary data and are used to perform bit-level operations on integers.

## 📌 What are Bitwise Operators?

- Bitwise operators deal in **binary** via `bin()` and use bitwise operators.
- Bitwise et input and output in binary via simple rules of operators.
- They operate on the individual bits of integer values.

---

## 🛠 Types of Bitwise Operators

| Operator | Name | Description | Formula / Rule |
| :--- | :--- | :--- | :--- |
| **`&`** | Bitwise AND | Sets each bit to 1 if **both** bits are 1. | `a & b` |
| **`\|`** | Bitwise OR | Sets each bit to 1 if **at least one** of two bits is 1. | `a \| b` |
| **`^`** | Bitwise XOR | Sets each bit to 1 if **only one** of two bits is 1. | `a ^ b` |
| **`~`** | Bitwise NOT | Inverts all the bits. | `~x = -(x + 1)` |
| **`<<`** | Bitwise Left Shift | Shifts bits to the **left**. | `5 << n → 5 * (2 ** n)` |
| **`>>`** | Bitwise Right Shift | Shifts bits to the **right**. | `20 >> n → 20 / (2 ** n)` |

---

## 📝 Detailed Explanation

### 1. Bitwise AND (`&`)
Sets each bit to 1 if both bits are 1.
```python
a = 5   # Binary: 0101
b = 3   # Binary: 0011
# Result: 0001 (Decimal 1)
print(a & b)  # Output: 1
```

### 2. Bitwise OR (`|`)
Sets each bit to 1 if at least one of the two bits is 1.
```python
a = 5   # Binary: 0101
b = 3   # Binary: 0011
# Result: 0111 (Decimal 7)
print(a | b)  # Output: 7
```

### 3. Bitwise XOR (`^`)
Sets each bit to 1 if only one of the two bits is 1.
```python
a = 5   # Binary: 0101
b = 3   # Binary: 0011
# Result: 0110 (Decimal 6)
print(a ^ b)  # Output: 6
```

### 4. Bitwise NOT (`~`)
Inverts all the bits. The formula is `~x = -(x + 1)`.
```python
x = 5
print(~x)  # Output: -6
```

### 5. Bitwise Left Shift (`<<`)
Shifts bits to the left. Equivalent to multiplying by 2 raised to the power of the shift amount.
**Formula:** `5 << n → 5 * (2 ** n)`
```python
print(5 << 1)  # Output: 10 (5 * 2^1)
print(5 << 2)  # Output: 20 (5 * 2^2)
```

### 6. Bitwise Right Shift (`>>`)
Shifts bits to the right. Equivalent to dividing by 2 raised to the power of the shift amount.
**Formula:** `20 >> n → 20 / (2 ** n)`
```python
print(20 >> 1)  # Output: 10 (20 / 2^1)
print(20 >> 2)  # Output: 5  (20 / 2^2)
```
