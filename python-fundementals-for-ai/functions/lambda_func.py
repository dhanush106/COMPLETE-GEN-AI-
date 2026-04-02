"""
Python Lambda, map(), filter() - Complete Guide (with Tricky Cases)
Run this file to master functional programming basics in Python
"""

# -----------------------------
# 1. Lambda Basics
# -----------------------------
print("1. Lambda Basics:")
square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(2, 3))

# -----------------------------
# 2. Lambda with Multiple Inputs
# -----------------------------
print("\n2. Multiple Inputs:")
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))

# -----------------------------
# 3. map() Function
# -----------------------------
print("\n3. map() Function:")
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print("Squares:", squares)

# map with multiple lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, l1, l2))
print("Sum of lists:", sums)

# -----------------------------
# 4. filter() Function
# -----------------------------
print("\n4. filter() Function:")
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)

# -----------------------------
# 5. map vs filter Combined
# -----------------------------
print("\n5. map + filter:")
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums)))
print("Square of evens:", result)

# -----------------------------
# 6. Using Lambda in Sorting
# -----------------------------
print("\n6. Sorting with Lambda:")
data = [(1, 3), (1, 2), (2, 1)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

# -----------------------------
# 7. Using Lambda in List Comprehension (Alternative)
# -----------------------------
print("\n7. Comparison with List Comprehension:")
nums = [1, 2, 3, 4]
map_result = list(map(lambda x: x*x, nums))
list_comp = [x*x for x in nums]
print("map:", map_result)
print("list comp:", list_comp)

# -----------------------------
# 8. Tricky / Anomaly Cases
# -----------------------------
print("\n8. Tricky Cases:")

# map returns iterator
nums = [1,2,3]
m = map(lambda x: x*2, nums)
print("map object:", m)
print("converted:", list(m))

# filter truthy behavior
vals = [0, 1, "", "hello", None]
f = list(filter(None, vals))
print("filter(None):", f)

# late binding issue
funcs = [lambda x: x*i for i in range(3)]
print([f(2) for f in funcs])  # unexpected

# correct way
funcs = [lambda x, i=i: x*i for i in range(3)]
print([f(2) for f in funcs])

# -----------------------------
# 9. Mini Problems
# -----------------------------
print("\n9. Mini Problems:")

# double all numbers
doubled = list(map(lambda x: x*2, [1,2,3]))
print(doubled)

# filter positive numbers
nums = [-2, -1, 0, 1, 2]
pos = list(filter(lambda x: x > 0, nums))
print(pos)

# -----------------------------
# 10. Best Practices
# -----------------------------
print("\n10. Best Practices:")
print("Use lambda for short operations, prefer list comprehension for readability")

print("\n--- End of Lambda/map/filter Mastery File ---")
