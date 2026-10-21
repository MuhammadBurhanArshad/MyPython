# Python Match Statement

This guide covers the `match` statement in Python (introduced in Python 3.10). It is based on the provided notes and expanded with practical examples.

## 📌 What is a Match Statement?

The `match` statement is used to mention match patterns according to an expression. It is Python's equivalent to the **`switch-case`** statement found in other programming languages (like C++, Java, or PHP).

It provides a more readable and powerful way to handle multiple conditional branches compared to long `if-elif-else` chains.

---

## 📝 Syntax

```python
match expression:
    case pattern1:
        # Code Block
    case pattern2:
        # Code Block
    case _:
        # Default Code Block
```

- **`match`**: The keyword followed by the variable or expression you want to check.
- **`case`**: Defines a specific pattern to match against.
- **`_` (underscore)**: The wildcard character. It acts as the default case if no other patterns match.

---

## 🎯 What Can It Match?

The `match` statement is very flexible and can match:
- Exact values (`case 1:`, `case "apple":`)
- Multiple values (`case 1 | 2 | 3:`)
- Variables (capturing the value)
- Lists and Tuples
- Dictionaries
- Conditions (using **guards**)

---

## 💡 Example 1: Matching Exact Values (Days of the Week)

```python
day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Enter the correct week Day")
```
**Output:** `Monday`

### Keeping Same Case for Different Values
You can combine multiple patterns using the pipe `|` symbol:
```python
match day:
    case 1 | 2 | 3:
        print("Start of the week")
```

---

## 🛡️ Example 2: Guards (Adding Conditions to Cases)

A **guard** is an `if` statement added to a `case` to add an extra condition that must be met for the case to match.

```python
age = 25

match age:
    case x if x < 13:
        print("Child")
    case x if x < 20:
        print("Teenager")
    case x if x < 60:
        print("Adult")
    case _:
        print("Senior Citizen")
```
**Output:** `Adult`

---

## 📦 Example 3: Wildcards in Sequences

The wildcard `_` can be used inside lists or tuples to represent "any value" at that position.

```python
point = (5, 20)

match point:
    case (_, 20):
        print("Second value is 20")
    case _:
        print("No Match")
```
**Output:** `Second value is 20`
