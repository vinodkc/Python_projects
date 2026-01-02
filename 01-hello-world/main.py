"""
============================================
PROJECT 1: HELLO WORLD & VARIABLES
============================================
Difficulty: Beginner
Concepts: Variables, Data Types, Print, Input, String Formatting

LEARNING OBJECTIVES:
- Understand Python syntax basics
- Learn about variables and data types
- Practice user input and output
- Explore string formatting methods
"""

# ============================================
# BASIC HELLO WORLD
# ============================================
print("Hello, World!")
print("Welcome to Python Programming!")

# ============================================
# VARIABLES AND DATA TYPES
# ============================================
# Integers
age = 25
year = 2024

# Floats
price = 19.99
temperature = 98.6

# Strings
name = "Python Learner"
message = "Learning Python is fun!"

# Boolean
is_learning = True
is_difficult = False

# Display variables
print(f"\nName: {name}")
print(f"Age: {age}")
print(f"Price: ${price}")
print(f"Is Learning: {is_learning}")

# ============================================
# USER INPUT
# ============================================
print("\n" + "="*50)
print("INTERACTIVE SECTION")
print("="*50)

user_name = input("What is your name? ")
user_age = input("How old are you? ")
favorite_color = input("What's your favorite color? ")

# ============================================
# STRING FORMATTING
# ============================================
# Method 1: f-strings (recommended)
print(f"\nHello, {user_name}!")
print(f"You are {user_age} years old.")
print(f"Your favorite color is {favorite_color}.")

# Method 2: .format()
print("\n{} is {} years old and loves {}.".format(user_name, user_age, favorite_color))

# Method 3: % operator (old style)
print("\nName: %s, Age: %s" % (user_name, user_age))

# ============================================
# CALCULATIONS
# ============================================
birth_year = 2024 - int(user_age)
print(f"\n{user_name} was born around {birth_year}")

# ============================================
# MULTIPLE VARIABLES
# ============================================
# Multiple assignment
x, y, z = 10, 20, 30
print(f"\nX: {x}, Y: {y}, Z: {z}")
print(f"Sum: {x + y + z}")

# Same value to multiple variables
a = b = c = 100
print(f"A: {a}, B: {b}, C: {c}")

# ============================================
# TYPE CHECKING
# ============================================
print("\n" + "="*50)
print("DATA TYPES")
print("="*50)
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of price: {type(price)}")
print(f"Type of is_learning: {type(is_learning)}")

# ============================================
# TYPE CONVERSION
# ============================================
# String to Integer
num_str = "42"
num_int = int(num_str)
print(f"\n'{num_str}' converted to integer: {num_int}")

# Integer to String
number = 100
number_str = str(number)
print(f"{number} converted to string: '{number_str}'")

# String to Float
price_str = "29.99"
price_float = float(price_str)
print(f"'{price_str}' converted to float: {price_float}")

print("\n" + "="*50)
print("Program completed successfully!")
print("="*50)

