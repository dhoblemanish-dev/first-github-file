"""
Simple Python Program to Add Two Numbers
This program demonstrates different ways to add two numbers
"""

# ============================================
# METHOD 1: Direct Addition
# ============================================
print("=" * 50)
print("METHOD 1: Direct Addition")
print("=" * 50)

num1 = 10
num2 = 20
sum_result = num1 + num2

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Sum: {sum_result}")


# ============================================
# METHOD 2: Addition with User Input
# ============================================
print("\n" + "=" * 50)
print("METHOD 2: User Input Addition")
print("=" * 50)

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    sum_result = num1 + num2
    print(f"\nThe sum of {num1} and {num2} is {sum_result}")
except ValueError:
    print("Error: Please enter valid numbers!")


# ============================================
# METHOD 3: Function to Add Numbers
# ============================================
print("\n" + "=" * 50)
print("METHOD 3: Using Function")
print("=" * 50)

def add_two_numbers(a, b):
    """
    Function to add two numbers
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b

result = add_two_numbers(25, 35)
print(f"Using function: {25} + {35} = {result}")


# ============================================
# METHOD 4: Function with Default Values
# ============================================
print("\n" + "=" * 50)
print("METHOD 4: Function with Default Values")
print("=" * 50)

def add_numbers_with_defaults(num1=5, num2=10):
    """Add two numbers with default values"""
    return num1 + num2

print(f"Default: 5 + 10 = {add_numbers_with_defaults()}")
print(f"Custom: 100 + 200 = {add_numbers_with_defaults(100, 200)}")


# ============================================
# METHOD 5: Class-based Approach
# ============================================
print("\n" + "=" * 50)
print("METHOD 5: Using Class")
print("=" * 50)

class Calculator:
    """A simple calculator class"""
    
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        """Add two numbers and store result"""
        self.result = a + b
        return self.result
    
    def display_result(self):
        """Display the stored result"""
        return f"Result: {self.result}"

calc = Calculator()
calc.add(50, 75)
print(f"50 + 75 = {calc.display_result()}")


# ============================================
# METHOD 6: Add Multiple Numbers
# ============================================
print("\n" + "=" * 50)
print("METHOD 6: Add Multiple Numbers")
print("=" * 50)

def add_multiple(*numbers):
    """Add any number of arguments"""
    total = sum(numbers)
    return total

print(f"10 + 20 + 30 = {add_multiple(10, 20, 30)}")
print(f"5 + 10 + 15 + 20 + 25 = {add_multiple(5, 10, 15, 20, 25)}")


# ============================================
# METHOD 7: Using Lambda Function
# ============================================
print("\n" + "=" * 50)
print("METHOD 7: Using Lambda Function")
print("=" * 50)

add = lambda x, y: x + y
print(f"Using lambda: 15 + 25 = {add(15, 25)}")


print("\n" + "=" * 50)
print("Program Completed Successfully!")
print("=" * 50)
