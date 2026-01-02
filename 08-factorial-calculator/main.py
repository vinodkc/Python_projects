"""
Factorial Calculator - Python Project 08
========================================
Calculate factorials using recursion and iteration methods.

🎯 LEARNING OBJECTIVES:
- Understand recursion (function calling itself)
- Implement iterative solutions
- Compare different algorithmic approaches
- Handle large numbers in Python
- Validate numerical input

📚 CONCEPTS COVERED:
- Recursive functions
- Iterative loops
- Mathematical operations
- Base cases and edge conditions
- Big integers in Python
"""

import math
import time

def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    n! = n × (n-1) × (n-2) × ... × 2 × 1
    
    LEARNING: Recursion - function calls itself with smaller input
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """
    Calculate factorial using iteration (loop).
    
    LEARNING: Iterative approach - using loops instead of recursion
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_builtin(n):
    """
    Calculate factorial using Python's built-in math.factorial().
    
    LEARNING: Python has optimized built-in functions
    """
    return math.factorial(n)

def get_valid_number():
    """
    Get and validate user input.
    
    LEARNING: Input validation for non-negative integers
    """
    while True:
        try:
            num = int(input("\nEnter a non-negative integer: "))
            if num < 0:
                print("❌ Factorial is not defined for negative numbers!")
            else:
                return num
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.")

def display_factorial_table(n):
    """
    Display factorial values from 0! to n!
    
    LEARNING: Formatted table output
    """
    print("\n" + "="*50)
    print("📊 FACTORIAL TABLE")
    print("="*50)
    print(f"{'n':>5} | {'n!':>30}")
    print("-"*50)
    
    for i in range(n + 1):
        fact = factorial_iterative(i)
        print(f"{i:>5} | {fact:>30,}")
    
    print("="*50)

def compare_methods(n):
    """
    Compare execution time of different methods.
    
    LEARNING: Performance comparison and timing
    """
    print("\n" + "="*60)
    print("⏱️  PERFORMANCE COMPARISON")
    print("="*60)
    
    # Recursive method
    start = time.time()
    result_recursive = factorial_recursive(n)
    time_recursive = time.time() - start
    
    # Iterative method
    start = time.time()
    result_iterative = factorial_iterative(n)
    time_iterative = time.time() - start
    
    # Built-in method
    start = time.time()
    result_builtin = factorial_builtin(n)
    time_builtin = time.time() - start
    
    print(f"Number: {n}")
    print(f"Result: {result_recursive:,}")
    print("-"*60)
    print(f"Recursive method: {time_recursive:.6f} seconds")
    print(f"Iterative method: {time_iterative:.6f} seconds")
    print(f"Built-in method:  {time_builtin:.6f} seconds")
    print("="*60)
    
    # Determine fastest
    times = {
        'Recursive': time_recursive,
        'Iterative': time_iterative,
        'Built-in': time_builtin
    }
    fastest = min(times, key=times.get)
    print(f"\n🏆 Fastest method: {fastest}")

def factorial_facts(n):
    """
    Display interesting facts about the factorial.
    
    LEARNING: Mathematical properties and string formatting
    """
    fact = factorial_iterative(n)
    
    print("\n" + "="*60)
    print(f"📌 FACTS ABOUT {n}!")
    print("="*60)
    print(f"Value: {fact:,}")
    print(f"Number of digits: {len(str(fact))}")
    print(f"Trailing zeros: {count_trailing_zeros(n)}")
    
    # Calculate how many times certain primes divide the factorial
    if n >= 2:
        print(f"Times divisible by 2: {count_prime_factors(n, 2)}")
    if n >= 3:
        print(f"Times divisible by 3: {count_prime_factors(n, 3)}")
    if n >= 5:
        print(f"Times divisible by 5: {count_prime_factors(n, 5)}")
    
    print("="*60)

def count_trailing_zeros(n):
    """
    Count trailing zeros in n!
    
    LEARNING: Mathematical formula - zeros come from factors of 10 (2×5)
    Formula: count factors of 5 (since there are always more 2s than 5s)
    """
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count

def count_prime_factors(n, prime):
    """
    Count how many times prime divides n!
    
    LEARNING: Legendre's formula for prime factorization of factorials
    """
    count = 0
    power = prime
    while power <= n:
        count += n // power
        power *= prime
    return count

def main():
    """
    Main program loop.
    """
    print("\n" + "="*60)
    print("🔢 FACTORIAL CALCULATOR")
    print("="*60)
    print("\nFactorial (n!) = n × (n-1) × (n-2) × ... × 2 × 1")
    print("Example: 5! = 5 × 4 × 3 × 2 × 1 = 120")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Calculate factorial")
        print("2. Show factorial table (0! to n!)")
        print("3. Compare calculation methods")
        print("4. Factorial facts")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            # Calculate factorial
            n = get_valid_number()
            
            if n > 1000:
                print("\n⚠️ Large number! This may take time...")
            
            result = factorial_iterative(n)
            
            print("\n" + "="*60)
            print(f"Result: {n}! = {result:,}")
            print(f"Number of digits: {len(str(result))}")
            print("="*60)
        
        elif choice == '2':
            # Factorial table
            n = get_valid_number()
            
            if n > 20:
                print("\n⚠️ Large table! Limiting to 20 for readability.")
                n = 20
            
            display_factorial_table(n)
        
        elif choice == '3':
            # Compare methods
            n = get_valid_number()
            
            if n > 100:
                print("\n⚠️ Large number! Limiting to 100 for fair comparison.")
                print("(Recursion has stack limits in Python)")
                n = 100
            
            compare_methods(n)
        
        elif choice == '4':
            # Factorial facts
            n = get_valid_number()
            factorial_facts(n)
        
        elif choice == '5':
            print("\n👋 Thanks for calculating! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

# ============================================================================
# INTERESTING FACTORIAL FACTS:
# ============================================================================
# 0! = 1 (by definition)
# 1! = 1
# 10! = 3,628,800
# 20! = 2,432,902,008,176,640,000
# 100! has 158 digits!
# Factorials grow VERY fast (faster than exponential)

