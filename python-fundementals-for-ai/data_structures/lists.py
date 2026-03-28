"""
Python Lists - Complete Guide (All Operations + Tricky Questions)
Run this file to master lists for interviews + real projects
"""

# -----------------------------
# 1. Creating Lists
# -----------------------------
print("1. Creating Lists:")
lst = [1, 2, 3, 4]
mixed = [1, "hello", 3.5, True]
print(lst)
print(mixed)

# -----------------------------
# 2. Access List Items
# -----------------------------
print("\n2. Accessing Elements:")
print(lst[0])
print(lst[-1])
print(lst[1:3])

# -----------------------------
# 3. Change List Items
# -----------------------------
print("\n3. Changing Elements:")
lst[1] = 10
print(lst)
lst[1:3] = [20, 30]
print(lst)

# -----------------------------
# 4. Add List Items
# -----------------------------
print("\n4. Adding Elements:")
lst.append(100)
print("append:", lst)
lst.insert(1, 50)
print("insert:", lst)
lst.extend([200, 300])
print("extend:", lst)

# -----------------------------
# 5. Remove List Items
# -----------------------------
print("\n5. Removing Elements:")
lst.remove(50)
print("remove:", lst)
popped = lst.pop()
print("pop:", lst, "removed:", popped)
del lst[0]
print("del:", lst)

# -----------------------------
# 6. Loop Lists
# -----------------------------
print("\n6. Looping:")
for i in lst:
    print(i, end=" ")
print()

# -----------------------------
# 7. List Comprehension
# -----------------------------
print("\n7. List Comprehension:")
squares = [x**2 for x in range(5)]
print(squares)

# -----------------------------
# 8. Sort Lists
# -----------------------------
print("\n8. Sorting:")
nums = [5, 2, 9, 1]
nums.sort()
print("ascending:", nums)
nums.sort(reverse=True)
print("descending:", nums)

# -----------------------------
# 9. Copy Lists
# -----------------------------
print("\n9. Copying:")
a = [1, 2, 3]
b = a.copy()
b.append(4)
print("original:", a)
print("copy:", b)

# -----------------------------
# 10. Join Lists
# -----------------------------
print("\n10. Joining:")
l1 = [1, 2]
l2 = [3, 4]
print(l1 + l2)
l1.extend(l2)
print(l1)

# -----------------------------
# 11. List Methods
# -----------------------------
print("\n11. List Methods:")
l = [1, 2, 2, 3]
print("count:", l.count(2))
print("index:", l.index(3))
l.reverse()
print("reverse:", l)
l.clear()
print("clear:", l)

# -----------------------------
# 12. Nested Lists
# -----------------------------
print("\n12. Nested Lists:")
nested = [[1, 2], [3, 4]]
print(nested[1][0])

# -----------------------------
# 13. Important Anomaly Questions
# -----------------------------
print("\n13. Tricky Questions:")

# Shallow Copy Issue
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][0] = 99
print("Shallow Copy:", a)  # changed!

# Multiplication Trap
lst = [[0]*3]*3
lst[0][0] = 1
print("Multiplication Trap:", lst)

# Remove vs Pop
lst = [1, 2, 3, 2]
lst.remove(2)
print("remove removes first occurrence:", lst)

# Sorting Strings
words = ["apple", "Banana", "cherry"]
words.sort()
print("Case sensitive sort:", words)

# List vs Tuple Mutability
l = [1, 2]
t = (l,)
l[0] = 99
print("Tuple containing list changed:", t)

# -----------------------------
# 14. Performance Tip
# -----------------------------
print("\n14. Performance Tip:")
# list comprehension faster than loop
nums = [i for i in range(1000)]

print("\n--- End of List Mastery File ---")
