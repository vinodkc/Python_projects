"""
Case Converter - Python Project 24
==================================
Convert text between different cases and formats.

🎯 LEARNING OBJECTIVES:
- Use string methods for case conversion
- Understand different naming conventions
- Transform text formats
- Work with string manipulation

📚 CONCEPTS COVERED:
- String methods (upper, lower, title, capitalize)
- String splitting and joining
- Case conventions (camelCase, snake_case, etc.)
- Text transformation
"""

def to_snake_case(text):
    """Convert to snake_case."""
    return text.lower().replace(' ', '_')

def to_camel_case(text):
    """Convert to camelCase."""
    words = text.split()
    return words[0].lower() + ''.join(w.capitalize() for w in words[1:])

def to_pascal_case(text):
    """Convert to PascalCase."""
    return ''.join(w.capitalize() for w in text.split())

def to_kebab_case(text):
    """Convert to kebab-case."""
    return text.lower().replace(' ', '-')

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("🔤 CASE CONVERTER")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. UPPERCASE")
        print("2. lowercase")
        print("3. Title Case")
        print("4. Capitalize First")
        print("5. snake_case")
        print("6. camelCase")
        print("7. PascalCase")
        print("8. kebab-case")
        print("9. All formats")
        print("10. Exit")
        
        choice = input("\nEnter choice (1-10): ").strip()
        
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            text = input("\nEnter text: ")
            
            print("\n" + "="*60)
            
            if choice == '1':
                print(f"UPPERCASE: {text.upper()}")
            elif choice == '2':
                print(f"lowercase: {text.lower()}")
            elif choice == '3':
                print(f"Title Case: {text.title()}")
            elif choice == '4':
                print(f"Capitalized: {text.capitalize()}")
            elif choice == '5':
                print(f"snake_case: {to_snake_case(text)}")
            elif choice == '6':
                print(f"camelCase: {to_camel_case(text)}")
            elif choice == '7':
                print(f"PascalCase: {to_pascal_case(text)}")
            elif choice == '8':
                print(f"kebab-case: {to_kebab_case(text)}")
            elif choice == '9':
                print(f"Original:    {text}")
                print(f"UPPERCASE:   {text.upper()}")
                print(f"lowercase:   {text.lower()}")
                print(f"Title Case:  {text.title()}")
                print(f"Capitalized: {text.capitalize()}")
                print(f"snake_case:  {to_snake_case(text)}")
                print(f"camelCase:   {to_camel_case(text)}")
                print(f"PascalCase:  {to_pascal_case(text)}")
                print(f"kebab-case:  {to_kebab_case(text)}")
            
            print("="*60)
        
        elif choice == '10':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

