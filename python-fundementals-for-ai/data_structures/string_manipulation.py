"""
Python String Manipulation - Complete Guide (All Methods + Tricky Cases)
Run this file to master string handling for interviews and real-world use
"""

# -----------------------------
# 1. Basic String Operations
# -----------------------------
print("1. Basic Operations:")
s = "hello"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

# -----------------------------
# 2. Searching & Counting
# -----------------------------
print("\n2. Searching:")
s = "hello world"
print(s.find("world"))
print(s.count("l"))
print(s.startswith("he"))
print(s.endswith("ld"))

# -----------------------------
# 3. Replace & Modify
# -----------------------------
print("\n3. Replace:")
s = "hello world"
print(s.replace("world", "Python"))

# -----------------------------
# 4. Split & Join
# -----------------------------
print("\n4. Split & Join:")
s = "a,b,c"
parts = s.split(",")
print(parts)
print("-".join(parts))

# -----------------------------
# 5. Strip Spaces
# -----------------------------
print("\n5. Strip:")
s = "  hello  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# -----------------------------
# 6. Check Methods
# -----------------------------
print("\n6. Check Methods:")
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
print(" ".isspace())

# -----------------------------
# 7. String Slicing Tricks
# -----------------------------
print("\n7. Slicing:")
s = "python"
print(s[::-1])  # reverse
print(s[::2])   # skip chars

# -----------------------------
# 8. Formatting Strings
# -----------------------------
print("\n8. Formatting:")
name = "Dhanush"
age = 20
print(f"My name is {name} and I am {age}")

# -----------------------------
# 9. Encoding & Decoding
# -----------------------------
print("\n9. Encoding:")
s = "hello"
enc = s.encode()
print(enc)
print(enc.decode())

# -----------------------------
# 10. Important Tricky Cases
# -----------------------------
print("\n10. Tricky Cases:")

# Strings are immutable
s = "hello"
# s[0] = 'H' ❌
print("Strings are immutable")

# Replace does not modify original
s = "hello"
s.replace("h", "H")
print("Original unchanged:", s)

# Join expects iterable of strings
try:
    print("-".join([1,2,3]))
except Exception as e:
    print("Error:", e)

# find vs index
print("find:", "abc".find("z"))  # -1
try:
    print("index:", "abc".index("z"))
except Exception as e:
    print("Error:", e)

# -----------------------------
# 11. Mini Problems
# -----------------------------
print("\n11. Mini Problems:")

# Reverse string
s = "python"
print("Reverse:", s[::-1])

# Palindrome check
s = "madam"
print("Palindrome:", s == s[::-1])

# Count vowels
s = "hello world"
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print("Vowels:", count)

# -----------------------------
# 12. Best Practices
# -----------------------------
print("\n12. Best Practices:")
print("Use built-in methods instead of manual loops for efficiency")

print("\n--- End of String Manipulation Mastery File ---")
