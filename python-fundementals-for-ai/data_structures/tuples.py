"""
Python Tuples - Complete Guide (All Concepts + Tricky Cases)
Run this file to master tuples for interviews and real-world use
"""

# -----------------------------
# 1. Creating Tuples
# -----------------------------
print("1. Creating Tuples:")
t1 = (1, 2, 3)
t2 = ("hello", 5.5, True)
t3 = (1,)  # single element tuple
print(t1)
print(t2)
print(t3)

# -----------------------------
# 2. Accessing Elements
# -----------------------------
print("\n2. Accessing Elements:")
print(t1[0])
print(t1[-1])
print(t1[0:2])

# -----------------------------
# 3. Tuple Immutability
# -----------------------------
print("\n3. Immutability:")
# t1[0] = 10  # ❌ This will give error
print("Tuples are immutable")

# -----------------------------
# 4. Looping Through Tuple
# -----------------------------
print("\n4. Looping:")
for i in t1:
    print(i, end=" ")
print()

# -----------------------------
# 5. Tuple Packing & Unpacking
# -----------------------------
print("\n5. Packing & Unpacking:")
packed = (1, 2, 3)
a, b, c = packed
print(a, b, c)

# Extended unpacking
a, *b = (1, 2, 3, 4)
print(a, b)

# -----------------------------
# 6. Tuple Methods
# -----------------------------
print("\n6. Tuple Methods:")
t = (1, 2, 2, 3)
print("count:", t.count(2))
print("index:", t.index(3))

# -----------------------------
# 7. Joining Tuples
# -----------------------------
print("\n7. Joining Tuples:")
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# -----------------------------
# 8. Repetition
# -----------------------------
print("\n8. Repetition:")
print((1, 2) * 3)

# -----------------------------
# 9. Nested Tuples
# -----------------------------
print("\n9. Nested Tuples:")
nested = ((1, 2), (3, 4))
print(nested[1][0])

# -----------------------------
# 10. Tuple Conversion
# -----------------------------
print("\n10. Conversion:")
lst = [1, 2, 3]
tpl = tuple(lst)
print(tpl)

# -----------------------------
# 11. Membership Test
# -----------------------------
print("\n11. Membership:")
print(2 in tpl)
print(5 not in tpl)

# -----------------------------
# 12. Length
# -----------------------------
print("\n12. Length:")
print(len(tpl))

# -----------------------------
# 13. Built-in Functions
# -----------------------------
print("\n13. Built-in Functions:")
nums = (5, 2, 9, 1)
print("max:", max(nums))
print("min:", min(nums))
print("sum:", sum(nums))

# -----------------------------
# 14. Important Tricky Cases
# -----------------------------
print("\n14. Tricky Cases:")

# Mutable inside tuple
t = ([1, 2], [3, 4])
t[0][0] = 99
print("Mutable inside tuple:", t)

# Comma matters
single = (5)
print(type(single))  # int
single_tuple = (5,)
print(type(single_tuple))  # tuple

# Tuple as dictionary key
d = {(1, 2): "value"}
print("Tuple as key:", d[(1, 2)])

# Sorting tuple of tuples
data = ((1, 3), (1, 2), (2, 1))
print("Sorted:", sorted(data))

# -----------------------------
# 15. Performance Insight
# -----------------------------
print("\n15. Performance Insight:")
print("Tuples are faster and use less memory than lists")

print("\n--- End of Tuple Mastery File ---")
