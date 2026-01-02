"""
Even/Odd Classifier - Python Project 13
=======================================
Classify numbers as even or odd with batch processing.

🎯 LEARNING OBJECTIVES:
- Use modulo operator to check even/odd
- Process lists of numbers
- Categorize and count values
- Display results in formatted output

📚 CONCEPTS COVERED:
- Modulo operator (% 2)
- List filtering and categorization
- Conditional classification
- Batch processing
"""

def is_even(n):
    """Check if number is even."""
    return n % 2 == 0

def is_odd(n):
    """Check if number is odd."""
    return n % 2 != 0

def classify_number(n):
    """Return 'Even' or 'Odd' for a number."""
    return "Even" if is_even(n) else "Odd"

def classify_list(numbers):
    """
    Classify a list of numbers.
    Returns dict with evens and odds lists.
    """
    evens = [n for n in numbers if is_even(n)]
    odds = [n for n in numbers if is_odd(n)]
    return {'evens': evens, 'odds': odds}

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("🔢 EVEN/ODD CLASSIFIER")
    print("="*60)
    print("\nEven numbers are divisible by 2 (remainder = 0)")
    print("Odd numbers have remainder 1 when divided by 2")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Check single number")
        print("2. Classify multiple numbers")
        print("3. Find evens/odds in range")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            try:
                num = int(input("\nEnter a number: "))
                result = classify_number(num)
                print(f"\n{num} is {result}")
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '2':
            numbers_str = input("\nEnter numbers (space-separated): ")
            try:
                numbers = [int(n) for n in numbers_str.split()]
                classified = classify_list(numbers)
                
                print("\n" + "="*60)
                print(f"Evens: {classified['evens']}")
                print(f"Odds:  {classified['odds']}")
                print(f"\nTotal evens: {len(classified['evens'])}")
                print(f"Total odds:  {len(classified['odds'])}")
                print("="*60)
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '3':
            try:
                start = int(input("\nStart: "))
                end = int(input("End: "))
                
                numbers = list(range(start, end + 1))
                classified = classify_list(numbers)
                
                print("\n" + "="*60)
                print(f"Range: [{start}, {end}]")
                print(f"Evens: {classified['evens'][:10]}{'...' if len(classified['evens']) > 10 else ''}")
                print(f"Odds:  {classified['odds'][:10]}{'...' if len(classified['odds']) > 10 else ''}")
                print(f"\nTotal evens: {len(classified['evens'])}")
                print(f"Total odds:  {len(classified['odds'])}")
                print("="*60)
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '4':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

