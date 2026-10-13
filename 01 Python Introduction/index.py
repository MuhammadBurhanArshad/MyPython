"""
index.py (01 Python Introduction)

This script demonstrates the basic concepts covered in the Introduction to Python notes.
It covers features, basic syntax, and simulates the use of popular libraries.
"""

# 1. Python Introduction & Basic Features
# -----------------------------------------
# Python is an interpreted, high-level, dynamically-typed language.
# We don't need to declare variable types.

print("=== 1. Python Features Demonstration ===")

# Dynamically Typed
my_variable = 42
print(f"Variable value: {my_variable}, Type: {type(my_variable)}")

my_variable = "Now I'm a string!"
print(f"Variable value: {my_variable}, Type: {type(my_variable)}")

# High-level and Easy to Learn
# Simple syntax with built-in functions
name = "Guido van Rossum"
year = 1991
print(f"Python was developed by {name} in {year}.\n")


# 2. Usages & Automation
# ------------------------
print("=== 2. Automation & Scripting Example ===")

# A simple automation task: calculating squares of numbers
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers] # List comprehension (a Pythonic feature)
print(f"Original numbers: {numbers}")
print(f"Squares (via automation): {squares}\n")


# 3. Popular Libraries (Simulated Imports)
# ------------------------------------------
print("=== 3. Popular Libraries Overview ===")

# Web Development
# import django
# import flask
print("[Web Dev] Django, Flask - Used for building web applications.")

# Game Development
# import pygame
print("[Game Dev] Pygame - Used for creating 2D games.")

# Desktop GUIs
# import tkinter
print("[Desktop GUI] Tkinter, Qt, wxPython - Used for desktop applications.")

# Data Science
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
print("[Data Science] Pandas, NumPy, Matplotlib - Used for data analysis.")

# AI & ML
# import tensorflow as tf
# import torch
# from sklearn import ...
print("[AI & ML] Scikit-learn, TensorFlow, PyTorch - Used for AI models.")

# IoT & Embedded
# import micropython
print("[IoT & Embedded] MicroPython, Raspberry Pi - Used for hardware projects.\n")


# 4. Conclusion
# --------------
print("=== 4. Conclusion ===")
print("Python's simplicity, large standard library, and vast ecosystem of")
print("third-party libraries make it the perfect language for beginners and experts alike.")
