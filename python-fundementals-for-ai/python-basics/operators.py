"""
Python Operators - Complete Guide with Examples
Run this file to understand all operator concepts in Python
"""

# -----------------------------
# 1. Arithmetic Operators
# -----------------------------
a = 10
b = 3
print("1. Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# -----------------------------
# 2. Comparison Operators
# -----------------------------
print("\n2. Comparison Operators:")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# -----------------------------
# 3. Logical Operators
# -----------------------------
x = True
y = False
print("\n3. Logical Operators:")
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# -----------------------------
# 4. Assignment Operators
# -----------------------------
n = 5
print("\n4. Assignment Operators:")
n += 3
print("+=:", n)
n -= 2
print("-=:", n)
n *= 2
print("*=:", n)
n /= 2
print("/=:", n)
n //= 2
print("//=:", n)
n %= 2
print("%=:", n)
n **= 3
print("**=:", n)

# -----------------------------
# 5. Bitwise Operators
# -----------------------------
a = 5  # 0101
b = 3  # 0011
print("\n5. Bitwise Operators:")
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# -----------------------------
# 6. Membership Operators
# -----------------------------
nums = [1, 2, 3, 4]
print("\n6. Membership Operators:")
print(2 in nums)
print(5 not in nums)

# -----------------------------
# 7. Identity Operators
# -----------------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("\n7. Identity Operators:")
print(a is b)
print(a is c)
print(a is not c)

# -----------------------------
# 8. Operator Precedence
# -----------------------------
print("\n8. Operator Precedence:")
result = 10 + 5 * 2
print(result)  # Multiplication first

# -----------------------------
# 9. Ternary Operator
# -----------------------------
age = 18
print("\n9. Ternary Operator:")
status = "Adult" if age >= 18 else "Minor"
print(status)

# -----------------------------
# 10. Chained Comparisons
# -----------------------------
print("\n10. Chained Comparisons:")
print(1 < 5 < 10)

print("\n--- End of Operators Guide ---")
