"""
Lottery Number Generator - Python Project 20
============================================
Generate random lottery numbers with various game formats.

🎯 LEARNING OBJECTIVES:
- Generate random unique numbers
- Use sets to avoid duplicates
- Sort sequences
- Simulate lottery systems

📚 CONCEPTS COVERED:
- random.sample() for unique selection
- Set operations
- Sorting lists
- Range generation
"""

import random

def generate_lottery(count, min_num, max_num):
    """Generate unique lottery numbers."""
    return sorted(random.sample(range(min_num, max_num + 1), count))

def generate_powerball():
    """Standard Powerball: 5 numbers (1-69) + 1 powerball (1-26)."""
    main_numbers = sorted(random.sample(range(1, 70), 5))
    powerball = random.randint(1, 26)
    return main_numbers, powerball

def generate_mega_millions():
    """Mega Millions: 5 numbers (1-70) + 1 mega ball (1-25)."""
    main_numbers = sorted(random.sample(range(1, 71), 5))
    mega_ball = random.randint(1, 25)
    return main_numbers, mega_ball

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("🎰 LOTTERY NUMBER GENERATOR")
    print("="*60)
    
    while True:
        print("\nGame Types:")
        print("1. Custom lottery")
        print("2. Powerball")
        print("3. Mega Millions")
        print("4. Quick Pick (multiple)")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            try:
                count = int(input("\nHow many numbers? "))
                min_num = int(input("Minimum number: "))
                max_num = int(input("Maximum number: "))
                
                if count > (max_num - min_num + 1):
                    print("❌ Not enough unique numbers in range!")
                    continue
                
                numbers = generate_lottery(count, min_num, max_num)
                print(f"\n🎲 Your numbers: {' - '.join(map(str, numbers))}")
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '2':
            main_nums, powerball = generate_powerball()
            print("\n" + "="*60)
            print("POWERBALL NUMBERS")
            print("="*60)
            print(f"Main: {' - '.join(map(str, main_nums))}")
            print(f"Powerball: {powerball}")
            print("="*60)
        
        elif choice == '3':
            main_nums, mega = generate_mega_millions()
            print("\n" + "="*60)
            print("MEGA MILLIONS NUMBERS")
            print("="*60)
            print(f"Main: {' - '.join(map(str, main_nums))}")
            print(f"Mega Ball: {mega}")
            print("="*60)
        
        elif choice == '4':
            try:
                num_tickets = int(input("\nHow many tickets? (1-10): "))
                game = input("Game (powerball/mega): ").lower()
                
                print("\n" + "="*60)
                for i in range(1, min(num_tickets, 10) + 1):
                    if game == 'powerball':
                        main, special = generate_powerball()
                        print(f"#{i}: {' - '.join(map(str, main))} | PB: {special}")
                    elif game == 'mega':
                        main, special = generate_mega_millions()
                        print(f"#{i}: {' - '.join(map(str, main))} | MB: {special}")
                print("="*60)
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '5':
            print("\n🍀 Good luck!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

