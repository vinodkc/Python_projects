"""
FizzBuzz Challenge - Python Project 23
======================================
Classic FizzBuzz with variations and analysis.

🎯 LEARNING OBJECTIVES:
- Implement modulo logic
- Use conditional statements
- Understand FizzBuzz rules
- Create variations

📚 CONCEPTS COVERED:
- Modulo operator
- Multiple conditions
- Pattern recognition
- Loop iteration
"""

def fizzbuzz(n):
    """Return FizzBuzz value for number n."""
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def fizzbuzz_range(start, end):
    """Generate FizzBuzz for a range."""
    results = []
    for i in range(start, end + 1):
        results.append((i, fizzbuzz(i)))
    return results

def count_fizzbuzz(start, end):
    """Count Fizz, Buzz, and FizzBuzz occurrences."""
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    
    for i in range(start, end + 1):
        result = fizzbuzz(i)
        if result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        elif result == "FizzBuzz":
            fizzbuzz_count += 1
    
    return fizz_count, buzz_count, fizzbuzz_count

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("🎯 FIZZBUZZ CHALLENGE")
    print("="*60)
    print("\nRules:")
    print("• Divisible by 3 → Fizz")
    print("• Divisible by 5 → Buzz")
    print("• Divisible by both → FizzBuzz")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. FizzBuzz for range")
        print("2. Check single number")
        print("3. Statistics")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            try:
                start = int(input("\nStart: "))
                end = int(input("End: "))
                
                results = fizzbuzz_range(start, end)
                
                print("\n" + "="*60)
                for num, result in results:
                    print(f"{num:>4}: {result}")
                print("="*60)
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '2':
            try:
                num = int(input("\nEnter number: "))
                result = fizzbuzz(num)
                print(f"\n{num} → {result}")
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '3':
            try:
                start = int(input("\nStart: "))
                end = int(input("End: "))
                
                fizz, buzz, fizzbuzz_count = count_fizzbuzz(start, end)
                
                print("\n" + "="*60)
                print(f"FIZZBUZZ STATISTICS [{start}-{end}]")
                print("="*60)
                print(f"Fizz:     {fizz}")
                print(f"Buzz:     {buzz}")
                print(f"FizzBuzz: {fizzbuzz_count}")
                print(f"Numbers:  {end - start + 1 - fizz - buzz - fizzbuzz_count}")
                print("="*60)
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '4':
            print("\n👋 Fizz you later!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

