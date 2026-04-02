"""
Python Functions - Complete Guide (args, kwargs, returns + tricky cases)
Run this file to master functions for real-world development
"""

# -----------------------------
# 1. Basic Function
# -----------------------------
print("1. Basic Function:")
def greet():
    print("Hello World")

greet()

# -----------------------------
# 2. Arguments (Positional)
# -----------------------------
print("\n2. Positional Arguments:")
def add(a, b):
    return a + b

print(add(2, 3))

# -----------------------------
# 3. Default Arguments
# -----------------------------
print("\n3. Default Arguments:")
def greet_user(name="Guest"):
    print("Hello", name)

greet_user()
greet_user("Dhanush")

# -----------------------------
# 4. Keyword Arguments
# -----------------------------
print("\n4. Keyword Arguments:")
def info(name, age):
    print(name, age)

info(age=20, name="Dhanush")

# -----------------------------
# 5. *args (Multiple Positional)
# -----------------------------
print("\n5. *args:")
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1,2,3,4))

# -----------------------------
# 6. **kwargs (Multiple Keyword)
# -----------------------------
print("\n6. **kwargs:")
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_info(name="Dhanush", age=20)

# -----------------------------
# 7. Return Values
# -----------------------------
print("\n7. Return Values:")
def square(x):
    return x * x

result = square(5)
print(result)

# Multiple return values
def get_values():
    return 1, 2, 3

a, b, c = get_values()
print(a, b, c)

# -----------------------------
# 8. Combining args and kwargs
# -----------------------------
print("\n8. Combining args & kwargs:")
def demo(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1,2,3,name="test")

# -----------------------------
# 9. Lambda Functions
# -----------------------------
print("\n9. Lambda Functions:")
square = lambda x: x*x
print(square(4))

# -----------------------------
# 10. Function as Object
# -----------------------------
print("\n10. Functions as Objects:")
def shout(text):
    return text.upper()

func = shout
print(func("hello"))

# -----------------------------
# 11. Nested Functions
# -----------------------------
print("\n11. Nested Functions:")
def outer():
    def inner():
        return "Inner function"
    return inner()

print(outer())

# -----------------------------
# 12. Recursion
# -----------------------------
print("\n12. Recursion:")
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# -----------------------------
# 13. Tricky / Anomaly Cases
# -----------------------------
print("\n13. Tricky Cases:")

# Mutable default argument trap
def add_item(x, lst=[]):
    lst.append(x)
    return lst

print(add_item(1))
print(add_item(2))  # unexpected behavior

# Correct way
def add_item_safe(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst

print(add_item_safe(1))
print(add_item_safe(2))

# args must come before kwargs
def order(a, *args, **kwargs):
    print(a, args, kwargs)

order(1,2,3,x=10)

# -----------------------------
# 14. Mini Problems
# -----------------------------
print("\n14. Mini Problems:")

# Sum using function
def sum_list(lst):
    return sum(lst)

print(sum_list([1,2,3]))

# Check palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))

# -----------------------------
# 15. Best Practices
# -----------------------------
print("\n15. Best Practices:")
print("Avoid mutable default args, keep functions small and reusable")

print("\n--- End of Functions Mastery File ---")
