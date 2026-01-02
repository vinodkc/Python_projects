"""
Dice Rolling Simulator - Python Project 11
==========================================
Simulate rolling dice with multiple dice types and statistics tracking.

🎯 LEARNING OBJECTIVES:
- Use random.randint() for dice simulation
- Work with lists and tuples
- Track and display statistics
- Create interactive simulations
- Visualize dice faces with ASCII art

📚 CONCEPTS COVERED:
- Random number generation in ranges
- List operations and aggregation
- ASCII art for visualization
- Statistical analysis
- User interaction loops
"""

import random

def roll_dice(sides=6):
    """
    Roll a single die with specified number of sides.
    
    LEARNING: random.randint(a, b) returns random integer from a to b inclusive
    """
    return random.randint(1, sides)

def roll_multiple_dice(num_dice=1, sides=6):
    """
    Roll multiple dice and return results.
    
    Returns:
        list: Results of each die roll
    
    LEARNING: List comprehension for generating multiple values
    """
    return [roll_dice(sides) for _ in range(num_dice)]

def display_dice_face(value):
    """
    Display ASCII art representation of a die face (1-6).
    
    LEARNING: Multi-line strings and ASCII art
    """
    faces = {
        1: [
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"
        ],
        2: [
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"
        ],
        3: [
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"
        ],
        4: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        5: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        6: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"
        ]
    }
    
    return faces.get(value, ["Invalid die value"])

def display_multiple_dice(rolls):
    """
    Display multiple dice side by side.
    
    LEARNING: Printing multiple items horizontally using zip()
    """
    if not rolls:
        return
    
    # Get ASCII representation of each die
    dice_faces = [display_dice_face(roll) for roll in rolls]
    
    # Print dice side by side
    for row in zip(*dice_faces):
        print("  ".join(row))

def calculate_statistics(roll_history):
    """
    Calculate statistics from roll history.
    
    LEARNING: Aggregating data from lists
    """
    if not roll_history:
        return None
    
    all_rolls = [roll for rolls in roll_history for roll in rolls]
    
    return {
        'total_rolls': len(all_rolls),
        'sum': sum(all_rolls),
        'average': sum(all_rolls) / len(all_rolls),
        'min': min(all_rolls),
        'max': max(all_rolls),
        'most_common': max(set(all_rolls), key=all_rolls.count)
    }

def display_statistics(stats):
    """Display roll statistics."""
    print("\n" + "="*60)
    print("📊 ROLL STATISTICS")
    print("="*60)
    print(f"Total Rolls:       {stats['total_rolls']}")
    print(f"Sum of All Rolls:  {stats['sum']}")
    print(f"Average:           {stats['average']:.2f}")
    print(f"Minimum Roll:      {stats['min']}")
    print(f"Maximum Roll:      {stats['max']}")
    print(f"Most Common:       {stats['most_common']}")
    print("="*60)

def simulate_probability(sides=6, num_simulations=1000):
    """
    Simulate many rolls to show probability distribution.
    
    LEARNING: Law of large numbers - probabilities converge with more trials
    """
    results = {}
    
    for _ in range(num_simulations):
        roll = roll_dice(sides)
        results[roll] = results.get(roll, 0) + 1
    
    print("\n" + "="*60)
    print(f"📈 PROBABILITY DISTRIBUTION ({num_simulations} rolls)")
    print("="*60)
    
    for value in sorted(results.keys()):
        count = results[value]
        percentage = (count / num_simulations) * 100
        bar = "█" * int(percentage * 2)
        print(f"{value}: {bar} {count} ({percentage:.1f}%)")
    
    print("="*60)
    print(f"Expected: {100/sides:.1f}% for each number")

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("🎲 DICE ROLLING SIMULATOR")
    print("="*60)
    
    roll_history = []
    
    while True:
        print("\nOptions:")
        print("1. Roll standard die (6 sides)")
        print("2. Roll multiple dice")
        print("3. Roll custom die (choose sides)")
        print("4. View statistics")
        print("5. Probability simulation")
        print("6. Clear history")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == '1':
            # Single die roll
            result = roll_dice()
            roll_history.append([result])
            
            print("\n🎲 Rolling...")
            print()
            for line in display_dice_face(result):
                print(line)
            print(f"\nYou rolled: {result}")
        
        elif choice == '2':
            # Multiple dice
            try:
                num_dice = int(input("\nHow many dice? (1-10): "))
                if 1 <= num_dice <= 10:
                    sides = int(input("Sides per die (default 6): ") or "6")
                    
                    results = roll_multiple_dice(num_dice, sides)
                    roll_history.append(results)
                    
                    print(f"\n🎲 Rolling {num_dice} dice...")
                    print()
                    
                    if sides == 6 and num_dice <= 5:
                        display_multiple_dice(results)
                    else:
                        print(f"Results: {results}")
                    
                    print(f"\nTotal: {sum(results)}")
                else:
                    print("❌ Please enter 1-10 dice")
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '3':
            # Custom die
            try:
                sides = int(input("\nNumber of sides (4, 6, 8, 10, 12, 20): "))
                if sides in [4, 6, 8, 10, 12, 20]:
                    result = roll_dice(sides)
                    roll_history.append([result])
                    
                    print(f"\n🎲 Rolling d{sides}...")
                    print(f"\nYou rolled: {result}")
                else:
                    print("❌ Common dice: 4, 6, 8, 10, 12, 20 sides")
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '4':
            # Statistics
            if roll_history:
                stats = calculate_statistics(roll_history)
                display_statistics(stats)
            else:
                print("\n❌ No rolls yet!")
        
        elif choice == '5':
            # Probability simulation
            try:
                sides = int(input("\nDie sides (default 6): ") or "6")
                num_sims = int(input("Number of simulations (default 1000): ") or "1000")
                
                simulate_probability(sides, num_sims)
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '6':
            # Clear history
            roll_history.clear()
            print("\n✅ History cleared!")
        
        elif choice == '7':
            # Exit
            print("\n🎲 Thanks for rolling! Good luck!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

# ============================================================================
# DICE TYPES IN GAMES:
# ============================================================================
# d4:  Tetrahedron (4 sides) - used in D&D for small damage
# d6:  Cube (6 sides) - standard die, most common
# d8:  Octahedron (8 sides) - used in many RPGs
# d10: Pentagonal trapezohedron (10 sides) - percentile rolls
# d12: Dodecahedron (12 sides) - larger damage rolls
# d20: Icosahedron (20 sides) - D&D ability checks

