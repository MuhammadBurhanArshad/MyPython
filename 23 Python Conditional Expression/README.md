# Python Conditional Expression

This guide covers Python Conditional Expressions (often called the ternary operator), based on the provided notes and expanded with practical examples.

## 📌 What is a Conditional Expression?

A conditional expression is a **single-line** way to write an `if-else` statement. It is also known as a **ternary operator** because it takes three operands. It allows you to assign a value to a variable based on a condition, all in one line.

---

## 📝 Syntax

```python
variable = value_if_true if condition else value_if_false
```

### How it works:
1. The `condition` is evaluated.
2. If the condition is `True`, it returns `value_if_true`.
3. If the condition is `False`, it returns `value_if_false`.

---

## 💡 Example 1: Basic Adult/Minor Check

Instead of writing a multi-line `if-else` block, we can do it in one line:

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

**Output:**
```
Adult
```

---

## 🔢 Example 2: Even or Odd Number

```python
num = 10
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result}.")
```

**Output:**
```
The number 10 is Even.
```

---

## 🎓 Example 3: Multi-Conditional (Nested Ternary)

Conditional expressions can also be nested to handle multiple conditions, though it can reduce readability if overused.

```python
marks = 85
result = "A" if marks >= 90 else "B" if marks >= 80 else "C"
print(f"Grade: {result}")
```

**Output:**
```
Grade: B
```

### Step-by-Step Explanation of Nested Ternary:
1. It checks `marks >= 90`. (False, so it moves to the `else` part).
2. The `else` part contains another condition: `"B" if marks >= 80 else "C"`.
3. It checks `marks >= 80`. Since 85 is greater than 80 (True), it returns `"B"`.

---

## 🛒 Example 4: Mini-Program - E-Commerce Free Shipping

A practical use case is determining shipping costs based on cart value.

```python
cart_total = 75
shipping_cost = 0 if cart_total >= 50 else 10

print(f"Cart Total: ${cart_total}")
print(f"Shipping Cost: ${shipping_cost}")
```

**Output:**
```
Cart Total: $75
Shipping Cost: $0
```
