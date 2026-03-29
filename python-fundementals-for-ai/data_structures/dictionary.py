"""
Python Dictionaries - Complete Guide (All Operations + Tricky/Anomaly Cases)
Run this file to master dictionaries for APIs, AI, and real-world projects
"""

# -----------------------------
# 1. Creating Dictionaries
# -----------------------------
print("1. Creating Dictionaries:")
d1 = {"name": "Dhanush", "age": 20}
d2 = dict(a=1, b=2)
empty = {}
print(d1)
print(d2)
print(empty)

# -----------------------------
# 2. Accessing Values
# -----------------------------
print("\n2. Accessing Values:")
print(d1["name"])  # KeyError if missing
print(d1.get("age"))
print(d1.get("city", "Not Found"))

# -----------------------------
# 3. Adding & Updating
# -----------------------------
print("\n3. Adding & Updating:")
d1["city"] = "Hyderabad"
print(d1)
d1.update({"age": 21, "country": "India"})
print(d1)

# -----------------------------
# 4. Removing Items
# -----------------------------
print("\n4. Removing Items:")
d = {"a":1, "b":2, "c":3}
print(d.pop("b"))
print(d)
d.popitem()  # removes last inserted
print(d)
del d["a"]
print(d)
d.clear()
print(d)

# -----------------------------
# 5. Looping
# -----------------------------
print("\n5. Looping:")
d = {"x":1, "y":2}
for key in d:
    print(key, d[key])

for k, v in d.items():
    print(k, v)

# -----------------------------
# 6. Dictionary Methods
# -----------------------------
print("\n6. Methods:")
d = {"a":1, "b":2}
print(d.keys())
print(d.values())
print(d.items())

# -----------------------------
# 7. Copying
# -----------------------------
print("\n7. Copying:")
d1 = {"a": [1,2]}
d2 = d1.copy()
d2["a"][0] = 99
print("Shallow copy:", d1)

# -----------------------------
# 8. Nested Dictionaries
# -----------------------------
print("\n8. Nested Dictionaries:")
student = {
    "name": "Dhanush",
    "marks": {"math": 90, "cs": 95}
}
print(student["marks"]["cs"])

# -----------------------------
# 9. Dictionary Comprehension
# -----------------------------
print("\n9. Comprehension:")
sq = {x: x*x for x in range(5)}
print(sq)

# -----------------------------
# 10. Membership
# -----------------------------
print("\n10. Membership:")
d = {"a":1, "b":2}
print("a" in d)
print(1 in d.values())

# -----------------------------
# 11. Built-in Functions
# -----------------------------
print("\n11. Built-ins:")
d = {"a":1, "b":2}
print(len(d))

# -----------------------------
# 12. Important Tricky/Anomaly Cases
# -----------------------------
print("\n12. Tricky Cases:")

# Mutable values issue
x = {"key": [1,2]}
y = x.copy()
y["key"][0] = 100
print("Shallow copy issue:", x)

# Default mutable argument trap
def add_item(val, my_dict={}):
    my_dict[val] = val
    return my_dict

print(add_item(1))
print(add_item(2))  # unexpected behavior

# Keys must be immutable
# d = {[1,2]: "value"} ❌ TypeError

# Using tuple as key
d = {(1,2): "valid"}
print(d)

# Overwriting keys
d = {"a":1, "a":2}
print("duplicate keys:", d)

# -----------------------------
# 13. Advanced Useful Methods
# -----------------------------
print("\n13. Advanced Methods:")
d = {"a":1}
print(d.setdefault("b", 10))
print(d)

# Merging dictionaries (Python 3.9+)
d1 = {"a":1}
d2 = {"b":2}
print(d1 | d2)

# -----------------------------
# 14. Performance Insight
# -----------------------------
print("\n14. Performance Insight:")
print("Dictionaries provide O(1) average lookup time")

print("\n--- End of Dictionary Mastery File ---")
