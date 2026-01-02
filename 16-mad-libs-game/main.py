"""
Mad Libs Game - Python Project 16
=================================
Interactive story generator using user inputs.

🎯 LEARNING OBJECTIVES:
- String formatting and replacement
- User input collection
- Template strings
- Creative text generation

📚 CONCEPTS COVERED:
- f-strings for interpolation
- String formatting
- Input prompts
- Story templates
"""

def story_1():
    """Adventure story template."""
    print("\n=== ADVENTURE STORY ===")
    adjective1 = input("Adjective: ")
    noun1 = input("Noun: ")
    verb1 = input("Verb (past tense): ")
    adjective2 = input("Another adjective: ")
    noun2 = input("Another noun: ")
    
    story = f"""
Once upon a time, in a {adjective1} land, there lived a brave {noun1}.
One day, they {verb1} through the forest and discovered a {adjective2} {noun2}.
It was the beginning of an incredible adventure!
    """
    print(story)

def story_2():
    """Funny story template."""
    print("\n=== FUNNY STORY ===")
    name = input("Person's name: ")
    place = input("A place: ")
    food = input("Type of food: ")
    animal = input("An animal: ")
    verb = input("Verb ending in -ing: ")
    
    story = f"""
{name} went to {place} to buy some {food}. Suddenly, a wild {animal} appeared!
It started {verb} right in front of everyone. What a day!
    """
    print(story)

def story_3():
    """Space adventure template."""
    print("\n=== SPACE ADVENTURE ===")
    adjective = input("Adjective: ")
    planet = input("Planet name: ")
    number = input("A number: ")
    noun = input("Noun (plural): ")
    verb = input("Verb: ")
    
    story = f"""
Captain's log: We've discovered a {adjective} new planet called {planet}.
It contains {number} different species of {noun}. They seem to {verb} peacefully.
This could change everything we know about the universe!
    """
    print(story)

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("📖 MAD LIBS GAME")
    print("="*60)
    print("\nCreate funny stories by filling in the blanks!")
    
    while True:
        print("\nChoose a story:")
        print("1. Adventure")
        print("2. Funny Story")
        print("3. Space Adventure")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            story_1()
        elif choice == '2':
            story_2()
        elif choice == '3':
            story_3()
        elif choice == '4':
            print("\n👋 Thanks for playing!")
            break
        else:
            print("❌ Invalid choice!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

