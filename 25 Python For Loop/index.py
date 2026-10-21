"""
index.py

This script demonstrates the Python For Loop.
It covers iterating through lists, tuples, dictionaries,
using enumerate(), zip(), conditions inside loops, and the else clause.
"""

# ==========================================
# 1. BASIC FOR LOOP (LIST)
# ==========================================
print("=== 1. Basic For Loop (List) ===")

subjects = ["Math", "Science", "English"]

for subject in subjects:
    print(f"Subject: {subject}")

print()


# ==========================================
# 2. FOR LOOP WITH DICTIONARY
# ==========================================
print("=== 2. For Loop with Dictionary ===")

student = {"name": "Burhan", "age": 22, "course": "Python"}

# Using .items() to get key and value
for key, v in student.items():
    print(f"{key}: {v}")

print()


# ==========================================
# 3. USING ENUMERATE()
# ==========================================
print("=== 3. Using enumerate() ===")

fruits = ["Apple", "Banana", "Cherry"]

# returns index as well
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print()


# ==========================================
# 4. USING ZIP() TO MERGE SEQUENCES
# ==========================================
print("=== 4. Using zip() ===")

students = ["Ali", "Sara", "John"]
marks = [85, 92, 78]

# Merge sequences
for name, mark in zip(students, marks):
    print(f"{name} scored {mark}")

print()


# ==========================================
# 5. CONDITION IN LOOP
# ==========================================
print("=== 5. Condition Inside Loop (Even Numbers) ===")

# Print only even numbers from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:
        print(num, end=" ")
print("\n")


# ==========================================
# 6. ELSE CLAUSE IN LOOP
# ==========================================
print("=== 6. Else Clause in Loop ===")

# We can define else part in loop as well to print after the loop
for num in range(1, 6):
    print(num, end=" ")
else:
    print("\nLoop completed")

print()


# ==========================================
# MINI-PROGRAM: MULTIPLICATION TABLE
# ==========================================
print("=== Mini-Program: Multiplication Table ===")

table_num = 5
print(f"Multiplication Table for {table_num}:")

for i in range(1, 11):
    result = table_num * i
    print(f"{table_num} x {i} = {result}")

print()


# ==========================================
# MINI-PROGRAM: VOWEL COUNTER
# ==========================================
print("=== Mini-Program: Vowel Counter ===")

text = "Python Programming"
vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print(f"Text: '{text}'")
print(f"Number of vowels: {count}")
