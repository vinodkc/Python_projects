"""
Prime Number Checker - Python Project 09
========================================
Check if numbers are prime and find prime numbers in ranges.

🎯 LEARNING OBJECTIVES:
- Understand prime numbers and their properties
- Implement efficient prime checking algorithms
- Optimize code with mathematical insights
- Work with loops and conditional logic
- Generate sequences of prime numbers

📚 CONCEPTS COVERED:
- Prime number definition and properties
- Loop optimization (checking up to sqrt(n))
- Boolean logic
- Range operations
- List comprehensions for filtering
"""

import math

def is_prime_basic(n):
    """
    Check if a number is prime using basic method.
    
    LEARNING: Basic prime check - divide by all numbers from 2 to n-1
    """
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def is_prime_optimized(n):
    """
    Check if a number is prime using optimized method.
    
    LEARNING: Only need to check up to sqrt(n)
    If n = a × b and a ≤ b, then a ≤ sqrt(n)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd numbers up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def find_prime_factors(n):
    """
    Find all prime factors of a number.
    
    LEARNING: Prime factorization
    """
    factors = []
    
    # Check for 2s
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check odd numbers from 3 onwards
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is still greater than 2, it's prime
    if n > 2:
        factors.append(n)
    
    return factors

def find_primes_in_range(start, end):
    """
    Find all prime numbers in a range.
    
    LEARNING: Applying prime check to multiple numbers
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime_optimized(num):
            primes.append(num)
    return primes

def sieve_of_eratosthenes(limit):
    """
    Find all primes up to limit using Sieve of Eratosthenes.
    
    LEARNING: Ancient algorithm (most efficient for finding many primes)
    """
    if limit < 2:
        return []
    
    # Create boolean array "prime[0..limit]" and initialize all as true
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    
    p = 2
    while p * p <= limit:
        # If prime[p] is not changed, it's prime
        if prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    
    # Collect all prime numbers
    return [num for num, is_prime in enumerate(prime) if is_prime]

def display_prime_table(primes):
    """
    Display primes in a formatted table.
    
    LEARNING: Formatting output in columns
    """
    print("\n" + "="*60)
    print("PRIME NUMBERS")
    print("="*60)
    
    # Display 10 primes per row
    for i in range(0, len(primes), 10):
        row = primes[i:i+10]
        print("  ".join(f"{p:>5}" for p in row))
    
    print("="*60)
    print(f"Total: {len(primes)} primes")

def prime_number_facts(n):
    """
    Display interesting facts about a prime number.
    """
    print("\n" + "="*60)
    print(f"📌 FACTS ABOUT {n}")
    print("="*60)
    
    if is_prime_optimized(n):
        print("✅ This IS a prime number!")
        
        # Find position among primes
        primes_up_to_n = sieve_of_eratosthenes(n)
        position = len(primes_up_to_n)
        print(f"Position: {position}th prime number")
        
        # Twin prime check
        if n > 2:
            if is_prime_optimized(n - 2):
                print(f"Twin prime with: {n-2} (lower twin)")
            if is_prime_optimized(n + 2):
                print(f"Twin prime with: {n+2} (upper twin)")
        
        # Special types
        if n > 2 and (n - 1) % 4 == 0:
            print("Type: Can be expressed as sum of two squares")
    else:
        print("❌ This is NOT a prime number")
        
        # Show factorization
        factors = find_prime_factors(n)
        print(f"Prime factorization: {' × '.join(map(str, factors))}")
        
        # Show all divisors
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        print(f"All divisors: {', '.join(map(str, divisors))}")
    
    print("="*60)

def main():
    """
    Main program loop.
    """
    print("\n" + "="*60)
    print("🔢 PRIME NUMBER CHECKER")
    print("="*60)
    print("\nA prime number is a natural number greater than 1")
    print("that has no positive divisors other than 1 and itself.")
    print("\nExamples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Check if a number is prime")
        print("2. Find primes in a range")
        print("3. Find prime factors")
        print("4. First N prime numbers")
        print("5. Prime number facts")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == '1':
            # Check single number
            try:
                num = int(input("\nEnter a number to check: "))
                
                if is_prime_optimized(num):
                    print(f"\n✅ {num} IS a prime number!")
                else:
                    print(f"\n❌ {num} is NOT a prime number")
                    if num > 1:
                        factors = find_prime_factors(num)
                        print(f"Prime factorization: {' × '.join(map(str, factors))}")
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '2':
            # Range of primes
            try:
                start = int(input("\nStart of range: "))
                end = int(input("End of range: "))
                
                if end - start > 10000:
                    print("\n⚠️ Large range! This may take time...")
                
                primes = find_primes_in_range(start, end)
                
                if primes:
                    display_prime_table(primes)
                else:
                    print(f"\n❌ No prime numbers in range [{start}, {end}]")
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '3':
            # Prime factors
            try:
                num = int(input("\nEnter a number to factorize: "))
                
                if num < 2:
                    print("❌ Prime factorization is only for numbers ≥ 2")
                else:
                    factors = find_prime_factors(num)
                    print(f"\n{num} = {' × '.join(map(str, factors))}")
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '4':
            # First N primes
            try:
                n = int(input("\nHow many primes to find? "))
                
                if n > 10000:
                    print("\n⚠️ Large number! Limiting to 10,000")
                    n = 10000
                
                # Find primes using sieve (estimate upper limit)
                limit = max(n * 15, 100)  # Approximation
                all_primes = sieve_of_eratosthenes(limit)
                
                while len(all_primes) < n:
                    limit *= 2
                    all_primes = sieve_of_eratosthenes(limit)
                
                primes = all_primes[:n]
                display_prime_table(primes)
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '5':
            # Prime facts
            try:
                num = int(input("\nEnter a number: "))
                prime_number_facts(num)
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '6':
            print("\n👋 Thanks for exploring prime numbers! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

# ============================================================================
# PRIME NUMBER FACTS:
# ============================================================================
# - 2 is the only even prime number
# - 1 is NOT prime (by definition)
# - There are infinitely many primes (Euclid's theorem)
# - Twin primes: pairs that differ by 2 (e.g., 11 and 13)
# - Mersenne primes: primes of form 2^p - 1
# - Largest known prime has over 24 million digits!

