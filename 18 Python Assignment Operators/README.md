# Python Assignment Operators

This guide covers Python Assignment Operators. These operators are used to assign values to variables, often combining an arithmetic or bitwise operation with the assignment.

## 📌 What are Assignment Operators?

Assignment operators are used to assign values to variables. The most common is the simple `=` operator.

| Operator | Example | Equivalent To | Description |
| :--- | :--- | :--- | :--- |
| **`=`** | `x = 5` | `x = 5` | Assign value |
| **`+=`** | `x += 3` | `x = x + 3` | Add and assign |
| **`-=`** | `x -= 3` | `x = x - 3` | Subtract and assign |
| **`*=`** | `x *= 3` | `x = x * 3` | Multiply and assign |
| **`/=`** | `x /= 3` | `x = x / 3` | Divide and assign |
| **`%=`** | `x %= 3` | `x = x % 3` | Modulus and assign |
| **`//=`** | `x //= 3` | `x = x // 3` | Floor divide and assign |
| **`**=`** | `x **= 3` | `x = x ** 3` | Exponentiate and assign |
| **`&=`** | `x &= 3` | `x = x & 3` | Bitwise AND and assign |
| **`\|=`** | `x \|= 3` | `x = x \| 3` | Bitwise OR and assign |
| **`^=`** | `x ^= 3` | `x = x ^ 3` | Bitwise XOR and assign |
| **`>>=`** | `x >>= 3` | `x = x >> 3` | Right Shift and assign |
| **`<<=`** | `x <<= 3` | `x = x << 3` | Left Shift and assign |

---

## 📝 Example Implementation

### 1. Basic Assignment (`=`)
```python
x = 5  # Assigns 5 to x
```

### 2. Add and Assign (`+=`)
```python
x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8
```

### 3. Subtract and Assign (`-=`)
```python
x = 5
x -= 3  # Equivalent to x = x - 3
print(x)  # Output: 2
```

### 4. Multiply and Assign (`*=`)
```python
x = 5
x *= 3  # Equivalent to x = x * 3
print(x)  # Output: 15
```

### 5. Divide and Assign (`/=`)
```python
x = 6
x /= 3  # Equivalent to x = x / 3
print(x)  # Output: 2.0 (always returns float)
```

### 6. Floor Divide and Assign (`//=`)
```python
x = 10
x //= 3  # Equivalent to x = x // 3
print(x)  # Output: 3
```

### 7. Modulus and Assign (`%=`)
```python
x = 10
x %= 3  # Equivalent to x = x % 3
print(x)  # Output: 1
```

### 8. Exponentiate and Assign (`**=`)
```python
x = 2
x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 8
```

### 9. Bitwise Assignment Operators
```python
x = 5
x &= 3   # Equivalent to x = x & 3 (Bitwise AND)
print(x)  # Output: 1

x = 5
x |= 3   # Equivalent to x = x | 3 (Bitwise OR)
print(x)  # Output: 7

x = 5
x ^= 3   # Equivalent to x = x ^ 3 (Bitwise XOR)
print(x)  # Output: 6

x = 5
x <<= 1  # Equivalent to x = x << 1 (Left Shift)
print(x)  # Output: 10

x = 20
x >>= 1  # Equivalent to x = x >> 1 (Right Shift)
print(x)  # Output: 10
```
