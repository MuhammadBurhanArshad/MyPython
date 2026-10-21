"""
index.py

This script demonstrates the Python Match Statement.
It includes matching exact values, multiple values, guards, and wildcards.
"""

# ==========================================
# 1. MATCHING EXACT VALUES
# ==========================================
print("=== 1. Exact Values (Days) ===")

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Enter the correct week Day")

print()


# ==========================================
# 2. KEEPING SAME CASE FOR DIFFERENT VALUES
# ==========================================
print("=== 2. Multiple Values (Pipe |) ===")

command = "stop"

match command:
    case "start" | "play":
        print("Starting...")
    case "stop" | "pause":
        print("Stopping...")
    case _:
        print("Unknown command")

print()


# ==========================================
# 3. MATCHING WITH GUARDS (Conditions)
# ==========================================
print("=== 3. Guards (Age Check) ===")

age = int(input("Enter your age: "))

match age:
    case x if x < 13:
        print("Child")
    case x if x < 20:
        print("Teenager")
    case x if x < 60:
        print("Adult")
    case _:
        print("Senior Citizen")

print()


# ==========================================
# 4. WILDCARDS IN SEQUENCES (Tuples)
# ==========================================
print("=== 4. Wildcards in Tuples ===")

# Let's test two different points
point1 = (5, 20)
point2 = (10, 50)

match point1:
    case (_, 20):
        print(f"point1 {point1}: Second value is 20")
    case _:
        print(f"point1 {point1}: No Match")

match point2:
    case (_, 20):
        print(f"point2 {point2}: Second value is 20")
    case _:
        print(f"point2 {point2}: No Match")

print()


# ==========================================
# 5. MINI-PROGRAM: HTTP STATUS CODES
# ==========================================
print("=== 5. Mini-Program: HTTP Status ===")

status_code = 404

match status_code:
    case 200:
        print("200: OK - Request successful")
    case 301 | 302:
        print("3xx: Redirect - Resource moved")
    case 400:
        print("400: Bad Request - Client error")
    case 404:
        print("404: Not Found - Resource missing")
    case 500:
        print("500: Internal Server Error")
    case _:
        print("Unknown Status Code")

print()


# ==========================================
# SUMMARY
# ==========================================
print("=== Summary ===")
print("The 'match' statement is a cleaner alternative to long if-elif chains.")
print("Use 'case _:' as the default fallback.")
print("Use '|' to combine cases, and 'if' inside a case for guards.")
