"""
Python If-Else - Complete Guide (All Concepts + Tricky/Anomaly Cases)
Run this file to master conditionals for logic building and interviews
"""

# -----------------------------
# 1. Basic if
# -----------------------------
print("1. Basic if:")
a = 10
if a > 5:
    print("a is greater than 5")

# -----------------------------
# 2. if-else
# -----------------------------
print("\n2. if-else:")
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# -----------------------------
# 3. if-elif-else
# -----------------------------
print("\n3. if-elif-else:")
marks = 75
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

# -----------------------------
# 4. Shorthand if
# -----------------------------
print("\n4. Shorthand if:")
if a > 0: print("Positive")

# -----------------------------
# 5. Ternary (Shorthand if-else)
# -----------------------------
print("\n5. Ternary:")
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# -----------------------------
# 6. Logical Operators in Conditions
# -----------------------------
print("\n6. Logical Operators:")
x, y = 10, 20
if x > 5 and y > 15:
    print("Both conditions true")
if x > 5 or y < 10:
    print("At least one condition true")
if not (x > y):
    print("x is not greater than y")

# -----------------------------
# 7. Nested if
# -----------------------------
print("\n7. Nested if:")
num = 15
if num > 0:
    if num % 5 == 0:
        print("Positive and divisible by 5")

# -----------------------------
# 8. Pass Statement
# -----------------------------
print("\n8. Pass Statement:")
if True:
    pass  # placeholder
print("Pass used successfully")

# -----------------------------
# 9. Comparison Tricks
# -----------------------------
print("\n9. Comparison Tricks:")
print(1 < 5 < 10)  # chained comparison

# -----------------------------
# 10. Truthy & Falsy Values
# -----------------------------
print("\n10. Truthy/Falsy:")
if []:
    print("List is True")
else:
    print("Empty list is False")

if "hello":
    print("Non-empty string is True")

# -----------------------------
# 11. Membership in if
# -----------------------------
print("\n11. Membership:")
nums = [1,2,3]
if 2 in nums:
    print("2 exists")

# -----------------------------
# 12. Using Functions in Conditions
# -----------------------------
print("\n12. Functions in Conditions:")
def is_even(n):
    return n % 2 == 0

if is_even(4):
    print("Even number")

# -----------------------------
# 13. Important Tricky/Anomaly Cases
# -----------------------------
print("\n13. Tricky Cases:")

# Assignment vs Comparison
x = 5
# if x = 5: ❌ SyntaxError
if x == 5:
    print("Correct comparison")

# is vs ==
a = [1,2]
b = [1,2]
print("== compares value:", a == b)
print("is compares memory:", a is b)

# None comparison
val = None
if val is None:
    print("Correct None check")

# Boolean confusion
print(bool("False"))  # True

# Short-circuit behavior
print(False and print("Won't print"))
print(True or print("Won't print"))

# -----------------------------
# 14. Mini Code Challenges
# -----------------------------
print("\n14. Code Challenges:")

# Find largest of 3 numbers
a, b, c = 5, 9, 3
if a >= b and a >= c:
    print("Largest:", a)
elif b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# Check palindrome
s = "madam"
if s == s[::-1]:
    print("Palindrome")

# -----------------------------
# 15. Best Practices
# -----------------------------
print("\n15. Best Practices:")
print("Avoid deep nesting, use functions for clarity")

print("\n--- End of If-Else Mastery File ---")
