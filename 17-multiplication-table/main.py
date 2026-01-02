"""
Multiplication Table Generator - Python Project 17
==================================================
Generate and display multiplication tables.

🎯 LEARNING OBJECTIVES:
- Use nested loops
- Format tables
- Work with range()
- Display aligned output

📚 CONCEPTS COVERED:
- Nested for loops
- String formatting with width
- Range operations
- Table generation
"""

def generate_table(number, up_to=10):
    """Generate multiplication table for a number."""
    table = []
    for i in range(1, up_to + 1):
        table.append((i, number * i))
    return table

def display_table(number, up_to=10):
    """Display multiplication table."""
    print("\n" + "="*40)
    print(f"MULTIPLICATION TABLE FOR {number}")
    print("="*40)
    
    for i in range(1, up_to + 1):
        result = number * i
        print(f"{number:>3} × {i:<2} = {result:>4}")
    
    print("="*40)

def display_grid(up_to=12):
    """Display multiplication grid."""
    print("\n" + "="*80)
    print("MULTIPLICATION GRID")
    print("="*80)
    
    # Header row
    print("   |", end="")
    for i in range(1, up_to + 1):
        print(f"{i:>4}", end="")
    print("\n" + "-"*80)
    
    # Table rows
    for i in range(1, up_to + 1):
        print(f"{i:>2} |", end="")
        for j in range(1, up_to + 1):
            print(f"{i*j:>4}", end="")
        print()
    
    print("="*80)

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("✖️  MULTIPLICATION TABLE GENERATOR")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Single table")
        print("2. Multiple tables")
        print("3. Multiplication grid")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            try:
                number = int(input("\nEnter number: "))
                up_to = int(input("Up to (default 10): ") or "10")
                display_table(number, up_to)
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '2':
            try:
                start = int(input("\nStart number: "))
                end = int(input("End number: "))
                up_to = int(input("Up to (default 10): ") or "10")
                
                for num in range(start, end + 1):
                    display_table(num, up_to)
                    input("\nPress Enter for next table...")
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '3':
            try:
                size = int(input("\nGrid size (default 12): ") or "12")
                display_grid(size)
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '4':
            print("\n👋 Happy multiplying!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

