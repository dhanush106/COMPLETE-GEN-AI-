"""
Python Sets - Complete Guide (All Operations + Tricky/Anomaly Cases)
Run this file to master sets for interviews and real-world usage
"""

# -----------------------------
# 1. Creating Sets
# -----------------------------
print("1. Creating Sets:")
s1 = {1, 2, 3}
s2 = set([1, 2, 2, 3])  # duplicates removed
empty_set = set()       # {} is dict, not set
print(s1)
print(s2)
print(empty_set)

# -----------------------------
# 2. Set Properties
# -----------------------------
print("\n2. Properties:")
print("Unique elements only:", {1,1,2,3})
# print({[1,2], 3})  # ❌ unhashable (lists not allowed)

# -----------------------------
# 3. Add Elements
# -----------------------------
print("\n3. Adding Elements:")
s = {1, 2}
s.add(3)
print("add:", s)
s.update([4, 5], {6, 7})
print("update:", s)

# -----------------------------
# 4. Remove Elements
# -----------------------------
print("\n4. Removing Elements:")
s.remove(7)  # error if not present
print("remove:", s)
s.discard(10)  # no error
print("discard (no error if absent):", s)
popped = s.pop()  # random element
print("pop (random):", popped, s)

# -----------------------------
# 5. Set Operations
# -----------------------------
print("\n5. Set Operations:")
a = {1,2,3}
b = {3,4,5}
print("union:", a | b, a.union(b))
print("intersection:", a & b, a.intersection(b))
print("difference a-b:", a - b, a.difference(b))
print("symmetric diff:", a ^ b, a.symmetric_difference(b))

# -----------------------------
# 6. Subset & Superset
# -----------------------------
print("\n6. Subset/Superset:")
a = {1,2}
b = {1,2,3}
print("a subset b:", a.issubset(b))
print("b superset a:", b.issuperset(a))
print("proper subset:", a < b)

# -----------------------------
# 7. Membership
# -----------------------------
print("\n7. Membership:")
print(2 in b)
print(10 not in b)

# -----------------------------
# 8. Iteration
# -----------------------------
print("\n8. Iteration:")
for x in {1,2,3}:
    print(x, end=" ")
print()

# -----------------------------
# 9. Copying
# -----------------------------
print("\n9. Copying:")
a = {1,2}
b = a.copy()
b.add(3)
print("original:", a)
print("copy:", b)

# -----------------------------
# 10. Frozen Set (Immutable Set)
# -----------------------------
print("\n10. Frozen Set:")
fs = frozenset([1,2,3])
print(fs)
# fs.add(4) ❌ not allowed

# -----------------------------
# 11. Built-in Functions
# -----------------------------
print("\n11. Built-ins:")
s = {5,2,9,1}
print("len:", len(s))
print("max:", max(s))
print("min:", min(s))
print("sum:", sum(s))

# -----------------------------
# 12. Set Comprehension
# -----------------------------
print("\n12. Set Comprehension:")
sq = {x*x for x in range(5)}
print(sq)

# -----------------------------
# 13. Important Tricky/Anomaly Cases
# -----------------------------
print("\n13. Tricky Cases:")

# Duplicate removal
data = [1,2,2,3,3]
print("Remove duplicates:", list(set(data)))

# Order not guaranteed
print("Order not preserved:", {3,1,2})

# Pop randomness
s = {10,20,30}
print("pop random element:", s.pop(), s)

# Mutable elements not allowed
# s = {[1,2]} ❌ TypeError

# Using tuple inside set
s = {(1,2), (3,4)}
print("tuple inside set:", s)

# Set vs list membership performance
print("Fast lookup in set vs list")

# Intersection trick
common = set([1,2,3]) & set([2,3,4])
print("common elements:", common)

# -----------------------------
# 14. Performance Insight
# -----------------------------
print("\n14. Performance Insight:")
print("Sets provide O(1) average time for lookup")

print("\n--- End of Set Mastery File ---")
