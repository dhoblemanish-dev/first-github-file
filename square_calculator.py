"""
Python Program to Calculate the Square of a Number
This program demonstrates:
- How to calculate the square of a number (number × number)
- Multiple methods and approaches
- Automatic examples with various numbers
"""

import math

# ============================================
# EXPLANATION: What is a Square?
# ============================================
print("=" * 70)
print("HOW TO CALCULATE THE SQUARE OF A NUMBER")
print("=" * 70)
print("\nDefinition: The square of a number is that number multiplied by itself.")
print("Formula: Square = n × n  OR  Square = n²")
print("\nExample:")
print("  If n = 5, then Square = 5 × 5 = 25")
print("  If n = 10, then Square = 10 × 10 = 100")
print("=" * 70)


# ============================================
# METHOD 1: Simple Multiplication
# ============================================
print("\n" + "=" * 70)
print("METHOD 1: Using Simple Multiplication (n × n)")
print("=" * 70)

def calculate_square_simple(number):
    """Calculate square using simple multiplication"""
    return number * number

# Automatic examples
print("\nAutomatic Examples:")
numbers = [1, 2, 3, 5, 10, 15, 20, -5, 3.5]

for num in numbers:
    square = calculate_square_simple(num)
    print(f"  {num}² = {num} × {num} = {square}")


# ============================================
# METHOD 2: Using Exponent Operator (**)
# ============================================
print("\n" + "=" * 70)
print("METHOD 2: Using Exponent Operator (**)")
print("=" * 70)

def calculate_square_exponent(number):
    """Calculate square using ** operator"""
    return number ** 2

print("\nAutomatic Examples:")
for num in numbers:
    square = calculate_square_exponent(num)
    print(f"  {num}² = {square}")


# ============================================
# METHOD 3: Using pow() Function
# ============================================
print("\n" + "=" * 70)
print("METHOD 3: Using pow() Function")
print("=" * 70)

def calculate_square_pow(number):
    """Calculate square using pow() function"""
    return pow(number, 2)

print("\nAutomatic Examples:")
for num in numbers:
    square = calculate_square_pow(num)
    print(f"  pow({num}, 2) = {square}")


# ============================================
# METHOD 4: User Interactive Input
# ============================================
print("\n" + "=" * 70)
print("METHOD 4: Interactive - Calculate Square of Your Number")
print("=" * 70)

try:
    user_number = float(input("\nEnter a number to calculate its square: "))
    
    square = user_number ** 2
    sqrt = math.sqrt(abs(user_number))
    
    print("\n" + "-" * 70)
    print("CALCULATION DETAILS:")
    print("-" * 70)
    print(f"Number:                              {user_number}")
    print(f"Square:                              {square}")
    print(f"Square Root (reverse):               ±{sqrt}")
    print("=" * 70)
    
except ValueError:
    print("Error: Please enter a valid number!")


# ============================================
# BONUS: Complete Square Reference Table
# ============================================
print("\n" + "=" * 70)
print("BONUS: SQUARES OF NUMBERS 1-20 (Reference Table)")
print("=" * 70)
print("\n{:<10} {:<10}".format("Number", "Square"))
print("-" * 20)

for i in range(1, 21):
    print("{:<10} {:<10}".format(i, i ** 2))

print("\n" + "=" * 70)
print("KEY POINTS TO REMEMBER:")
print("=" * 70)
print("✓ Square of any positive or negative number is always POSITIVE")
print("✓ Square of 0 is 0")
print("✓ Square of 1 is always 1")
print("✓ Square of decimals also works (e.g., 2.5² = 6.25)")
print("=" * 70)
