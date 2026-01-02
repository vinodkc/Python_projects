"""
Star Pattern Generator - Python Project 18
==========================================
Generate various star and shape patterns.

🎯 LEARNING OBJECTIVES:
- Create patterns with loops
- Use string multiplication
- Understand pattern logic
- Generate visual shapes

📚 CONCEPTS COVERED:
- Nested loops for patterns
- String repetition (* operator)
- Pattern mathematics
- ASCII art generation
"""

def right_triangle(n):
    """Right-angled triangle pattern."""
    print("\nRight Triangle:")
    for i in range(1, n + 1):
        print('*' * i)

def pyramid(n):
    """Pyramid pattern."""
    print("\nPyramid:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def diamond(n):
    """Diamond pattern."""
    print("\nDiamond:")
    # Upper half
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    # Lower half
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

def hollow_square(n):
    """Hollow square pattern."""
    print("\nHollow Square:")
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

def inverted_pyramid(n):
    """Inverted pyramid pattern."""
    print("\nInverted Pyramid:")
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

def number_pyramid(n):
    """Pyramid with numbers."""
    print("\nNumber Pyramid:")
    for i in range(1, n + 1):
        print(' ' * (n - i) + ' '.join(str(j) for j in range(1, i + 1)))

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("⭐ STAR PATTERN GENERATOR")
    print("="*60)
    
    while True:
        print("\nPatterns:")
        print("1. Right Triangle")
        print("2. Pyramid")
        print("3. Diamond")
        print("4. Hollow Square")
        print("5. Inverted Pyramid")
        print("6. Number Pyramid")
        print("7. All Patterns")
        print("8. Exit")
        
        choice = input("\nEnter choice (1-8): ").strip()
        
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                n = int(input("\nSize (3-20): "))
                if not 3 <= n <= 20:
                    print("❌ Size must be between 3 and 20")
                    continue
                
                if choice == '1':
                    right_triangle(n)
                elif choice == '2':
                    pyramid(n)
                elif choice == '3':
                    diamond(n)
                elif choice == '4':
                    hollow_square(n)
                elif choice == '5':
                    inverted_pyramid(n)
                elif choice == '6':
                    number_pyramid(n)
                elif choice == '7':
                    right_triangle(n)
                    pyramid(n)
                    diamond(n)
                    hollow_square(n)
                    inverted_pyramid(n)
                    number_pyramid(n)
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '8':
            print("\n⭐ Keep creating patterns!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

