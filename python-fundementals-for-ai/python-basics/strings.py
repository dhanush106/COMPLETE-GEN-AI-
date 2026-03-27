# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:
print("Hello")
print('Hello')

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#or
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])
#looping through a string
for x in "banana":
  print(x)

#len of string
a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)


# Use it in an if statement:
# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

"""
Python Strings - Complete Important Methods Guide
Run this file to see examples of all commonly used string operations.
"""

# -----------------------------
# 1. Creating Strings
# -----------------------------
s1 = "Hello"
s2 = 'World'
s3 = """Multi-line
String"""
print("1. Creating Strings:", s1, s2, s3)

# -----------------------------
# 2. String Indexing & Slicing
# -----------------------------
text = "Python"
print("\n2. Indexing & Slicing:")
print(text[0])      # P
print(text[-1])     # n
print(text[0:4])    # Pyth
print(text[::-1])   # reverse

# -----------------------------
# 3. String Length
# -----------------------------
print("\n3. Length:", len(text))

# -----------------------------
# 4. Case Conversion
# -----------------------------
s = "hello world"
print("\n4. Case Conversion:")
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

# -----------------------------
# 5. Stripping Spaces
# -----------------------------
s = "  hello  "
print("\n5. Strip:")
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# -----------------------------
# 6. Searching Methods
# -----------------------------
s = "hello world"
print("\n6. Searching:")
print(s.find("world"))
print(s.index("hello"))
print(s.count("l"))

# -----------------------------
# 7. Checking Methods
# -----------------------------
print("\n7. Checking:")
print("hello".startswith("he"))
print("hello".endswith("lo"))
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
print(" ".isspace())

# -----------------------------
# 8. Replace & Modify
# -----------------------------
s = "hello world"
print("\n8. Replace:")
print(s.replace("world", "Python"))

# -----------------------------
# 9. Splitting & Joining
# -----------------------------
s = "a,b,c"
print("\n9. Split & Join:")
parts = s.split(",")
print(parts)
print("-".join(parts))

# -----------------------------
# 10. Formatting Strings
# -----------------------------
name = "Dhanush"
age = 20
print("\n10. Formatting:")
print("My name is {} and I am {}".format(name, age))
print(f"My name is {name} and I am {age}")

# -----------------------------
# 11. Encoding & Decoding
# -----------------------------
s = "hello"
print("\n11. Encoding:")
encoded = s.encode()
print(encoded)
print(encoded.decode())

# -----------------------------
# 12. Alignment Methods
# -----------------------------
s = "hi"
print("\n12. Alignment:")
print(s.center(10, '*'))
print(s.ljust(10, '-'))
print(s.rjust(10, '-'))

# -----------------------------
# 13. Removing Characters
# -----------------------------
s = "hello"
print("\n13. Removing Characters:")
print(s.removeprefix("he"))
print(s.removesuffix("lo"))

# -----------------------------
# 14. Partitioning
# -----------------------------
s = "hello-world-python"
print("\n14. Partition:")
print(s.partition("-"))
print(s.rpartition("-"))

# -----------------------------
# 15. Miscellaneous
# -----------------------------
print("\n15. Miscellaneous:")
print("hello\tworld".expandtabs(4))
print("42".zfill(5))

print("\n--- End of String Guide ---")
