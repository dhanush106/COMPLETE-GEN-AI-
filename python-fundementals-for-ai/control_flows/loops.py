"""
Python Loops - Complete Guide (All Concepts + Tricky/Anomaly Cases)
Run this file to master loops for logic building and interviews
"""

# -----------------------------
# 1. for loop basics
# -----------------------------
print("1. For Loop:")
for i in range(5):
    print(i, end=" ")
print()

# -----------------------------
# 2. while loop basics
# -----------------------------
print("\n2. While Loop:")
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()

# -----------------------------
# 3. Looping through collections
# -----------------------------
print("\n3. Looping Collections:")
lst = [1,2,3]
for x in lst:
    print(x)

# -----------------------------
# 4. enumerate()
# -----------------------------
print("\n4. Enumerate:")
for idx, val in enumerate(lst):
    print(idx, val)

# -----------------------------
# 5. break statement
# -----------------------------
print("\n5. Break:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

# -----------------------------
# 6. continue statement
# -----------------------------
print("\n6. Continue:")
for i in range(5):
    if i == 2:
        continue
    print(i, end=" ")
print()

# -----------------------------
# 7. else with loops
# -----------------------------
print("\n7. Loop else:")
for i in range(3):
    print(i)
else:
    print("Loop finished")

# -----------------------------
# 8. Nested loops
# -----------------------------
print("\n8. Nested Loops:")
for i in range(3):
    for j in range(2):
        print(i, j)

# -----------------------------
# 9. List comprehension
# -----------------------------
print("\n9. List Comprehension:")
squares = [x*x for x in range(5)]
print(squares)

# -----------------------------
# 10. while True loop
# -----------------------------
print("\n10. While True (with break):")
i = 0
while True:
    print(i)
    i += 1
    if i == 3:
        break

# -----------------------------
# 11. range variations
# -----------------------------
print("\n11. Range Variations:")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

# -----------------------------
# 12. Iterating strings
# -----------------------------
print("\n12. String Iteration:")
for ch in "hello":
    print(ch)

# -----------------------------
# 13. Important Tricky Cases
# -----------------------------
print("\n13. Tricky Cases:")

# Modifying list while iterating
lst = [1,2,3,4]
for x in lst:
    if x == 2:
        lst.remove(x)
print("Modified list:", lst)

# Infinite loop risk
# while True:
#     pass

# break skips else
for i in range(3):
    if i == 1:
        break
else:
    print("This will not print")

# variable leakage
for i in range(3):
    pass
print("i still exists:", i)

# -----------------------------
# 14. Mini Problems
# -----------------------------
print("\n14. Mini Problems:")

# Sum of numbers
s = 0
for i in range(5):
    s += i
print("Sum:", s)

# Reverse a string
s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print("Reverse:", rev)

# -----------------------------
# 15. Best Practices
# -----------------------------
print("\n15. Best Practices:")
print("Avoid modifying list while iterating, use copies")

print("\n--- End of Loops Mastery File ---")
