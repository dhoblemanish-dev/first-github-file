"""
Python Program to Find Factorial of a Number
This program demonstrates different ways to calculate factorial
Factorial of n (n!) = n × (n-1) × (n-2) × ... × 1
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""

import math

# ============================================
# METHOD 1: Using a Loop
# ============================================
print("=" * 60)
print("METHOD 1: Factorial Using Loop")
print("=" * 60)

def factorial_loop(n):
    """
    Calculate factorial using a for loop
    
    Args:
        n: A non-negative integer
    
    Returns:
        Factorial of n
    """
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

# Get input from user
try:
    num = int(input("Enter a number to find factorial (Loop method): "))
    result = factorial_loop(num)
    print(f"Factorial of {num} = {result}")
except ValueError:
    print("Error: Please enter a valid integer!")


# ============================================
# METHOD 2: Using Recursion
# ============================================
print("\n" + "=" * 60)
print("METHOD 2: Factorial Using Recursion")
print("=" * 60)

def factorial_recursion(n):
    """
    Calculate factorial using recursion
    
    Args:
        n: A non-negative integer
    
    Returns:
        Factorial of n
    """
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)

try:
    num = int(input("\nEnter a number to find factorial (Recursion method): "))
    result = factorial_recursion(num)
    print(f"Factorial of {num} = {result}")
except ValueError:
    print("Error: Please enter a valid integer!")
except RecursionError:
    print("Error: Number too large for recursion!")


# ============================================
# METHOD 3: Using math.factorial()
# ============================================
print("\n" + "=" * 60)
print("METHOD 3: Factorial Using math.factorial()")
print("=" * 60)

def factorial_math(n):
    """
    Calculate factorial using Python's built-in math.factorial()
    
    Args:
        n: A non-negative integer
    
    Returns:
        Factorial of n
    """
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    
    return math.factorial(n)

try:
    num = int(input("\nEnter a number to find factorial (Math module): "))
    result = factorial_math(num)
    print(f"Factorial of {num} = {result}")
except ValueError:
    print("Error: Please enter a valid integer!")


# ============================================
# METHOD 4: Using While Loop
# ============================================
print("\n" + "=" * 60)
print("METHOD 4: Factorial Using While Loop")
print("=" * 60)

def factorial_while(n):
    """
    Calculate factorial using a while loop
    
    Args:
        n: A non-negative integer
    
    Returns:
        Factorial of n
    """
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    
    return factorial

try:
    num = int(input("\nEnter a number to find factorial (While loop): "))
    result = factorial_while(num)
    print(f"Factorial of {num} = {result}")
except ValueError:
    print("Error: Please enter a valid integer!")


# ============================================
# METHOD 5: Complete Calculator with Menu
# ============================================
print("\n" + "=" * 60)
print("METHOD 5: Interactive Factorial Calculator")
print("=" * 60)

class FactorialCalculator:
    """A class to calculate factorial with multiple methods"""
    
    def __init__(self):
        self.last_result = None
    
    def calculate(self, n, method="loop"):
        """
        Calculate factorial using specified method
        
        Args:
            n: Number to find factorial of
            method: "loop", "recursion", or "math"
        
        Returns:
            Factorial of n
        """
        if n < 0:
            return "Error: Factorial not defined for negative numbers"
        
        if method == "loop":
            result = self._factorial_loop(n)
        elif method == "recursion":
            result = self._factorial_recursion(n)
        elif method == "math":
            result = self._factorial_math(n)
        else:
            return "Error: Unknown method"
        
        self.last_result = result
        return result
    
    @staticmethod
    def _factorial_loop(n):
        """Using loop"""
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    
    @staticmethod
    def _factorial_recursion(n):
        """Using recursion"""
        if n == 0 or n == 1:
            return 1
        return n * FactorialCalculator._factorial_recursion(n - 1)
    
    @staticmethod
    def _factorial_math(n):
        """Using math module"""
        return math.factorial(n)
    
    def display_last_result(self):
        """Display the last calculated result"""
        if self.last_result is not None:
            return f"Last Result: {self.last_result}"
        return "No calculation done yet"

# Interactive menu
calc = FactorialCalculator()

print("\nFactorial Calculator Menu:")
print("1. Loop method")
print("2. Recursion method")
print("3. Math module method")
print("4. Exit")

try:
    choice = input("\nChoose a method (1-4): ")
    
    if choice == "1":
        num = int(input("Enter a number: "))
        result = calc.calculate(num, "loop")
        print(f"Factorial of {num} = {result}")
    
    elif choice == "2":
        num = int(input("Enter a number: "))
        result = calc.calculate(num, "recursion")
        print(f"Factorial of {num} = {result}")
    
    elif choice == "3":
        num = int(input("Enter a number: "))
        result = calc.calculate(num, "math")
        print(f"Factorial of {num} = {result}")
    
    elif choice == "4":
        print("Thank you for using Factorial Calculator!")
    
    else:
        print("Invalid choice!")

except ValueError:
    print("Error: Please enter a valid integer!")


# ============================================
# EXAMPLES & DEMONSTRATION
# ============================================
print("\n" + "=" * 60)
print("EXAMPLES OF FACTORIAL CALCULATIONS")
print("=" * 60)

test_numbers = [0, 1, 5, 10, 15]

print("\nUsing Loop Method:")
for num in test_numbers:
    result = factorial_loop(num)
    print(f"  {num}! = {result}")

print("\nUsing Math Module:")
for num in test_numbers:
    result = factorial_math(num)
    print(f"  {num}! = {result}")


print("\n" + "=" * 60)
print("Program Completed!")
print("=" * 60)
