"""
Password Generator - Python Project 06
======================================
Generate secure random passwords with customizable options.

🎯 LEARNING OBJECTIVES:
- Use the random module for secure password generation
- Work with string constants (ascii_letters, digits, punctuation)
- Implement password strength validation
- Create customizable password options
- Practice string manipulation and list operations

📚 CONCEPTS COVERED:
- random.choice() and random.shuffle()
- string module constants
- List comprehensions
- Password security best practices
"""

import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                     use_digits=True, use_special=True):
    """
    Generate a random password with specified criteria.
    
    Args:
        length (int): Password length
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_digits (bool): Include numbers
        use_special (bool): Include special characters
    
    Returns:
        str: Generated password
    
    LEARNING: Building character pools based on user preferences
    """
    # Build character pool
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase  # A-Z
    if use_lowercase:
        characters += string.ascii_lowercase  # a-z
    if use_digits:
        characters += string.digits  # 0-9
    if use_special:
        characters += string.punctuation  # !@#$%^&*()...
    
    # Validate that at least one character type is selected
    if not characters:
        return "Error: Select at least one character type!"
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def generate_strong_password(length=16):
    """
    Generate a guaranteed strong password with all character types.
    
    LEARNING: Ensuring password contains at least one of each type
    """
    # Ensure at least one of each type
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill remaining length with random characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_chars += [random.choice(all_chars) for _ in range(length - 4)]
    
    # Shuffle to avoid predictable pattern
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

def check_password_strength(password):
    """
    Evaluate password strength.
    
    Returns:
        tuple: (strength_score, feedback_message)
    
    LEARNING: Analyzing strings for specific character types
    """
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short (min 8 chars recommended)")
    
    # Character type checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if has_upper:
        score += 1
    else:
        feedback.append("⚠️ Add uppercase letters")
    
    if has_lower:
        score += 1
    else:
        feedback.append("⚠️ Add lowercase letters")
    
    if has_digit:
        score += 1
    else:
        feedback.append("⚠️ Add numbers")
    
    if has_special:
        score += 1
    else:
        feedback.append("⚠️ Add special characters")
    
    # Determine strength level
    if score >= 6:
        strength = "🟢 STRONG"
    elif score >= 4:
        strength = "🟡 MEDIUM"
    else:
        strength = "🔴 WEAK"
    
    return strength, feedback

def generate_multiple_passwords(count=5, length=12):
    """
    Generate multiple password options.
    
    LEARNING: Using loops to generate multiple items
    """
    print(f"\n🔐 Generated {count} password options:")
    print("="*60)
    
    for i in range(1, count + 1):
        pwd = generate_strong_password(length)
        strength, _ = check_password_strength(pwd)
        print(f"{i}. {pwd} - {strength}")
    
    print("="*60)

def main():
    """
    Main program with interactive menu.
    """
    print("\n" + "="*60)
    print("🔐 SECURE PASSWORD GENERATOR")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Generate quick strong password (recommended)")
        print("2. Customize password options")
        print("3. Generate multiple passwords")
        print("4. Check password strength")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            # Quick strong password
            length = input("\nPassword length (default 16): ").strip()
            length = int(length) if length.isdigit() else 16
            
            password = generate_strong_password(length)
            strength, feedback = check_password_strength(password)
            
            print("\n" + "="*60)
            print(f"🔑 Your password: {password}")
            print(f"💪 Strength: {strength}")
            print("="*60)
        
        elif choice == '2':
            # Custom password
            print("\n--- Password Customization ---")
            
            length = input("Length (8-128): ").strip()
            length = int(length) if length.isdigit() and 8 <= int(length) <= 128 else 12
            
            use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
            use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
            use_digits = input("Include numbers? (y/n): ").lower() == 'y'
            use_special = input("Include special chars? (y/n): ").lower() == 'y'
            
            password = generate_password(length, use_upper, use_lower, use_digits, use_special)
            
            if not password.startswith("Error"):
                strength, feedback = check_password_strength(password)
                print("\n" + "="*60)
                print(f"🔑 Your password: {password}")
                print(f"💪 Strength: {strength}")
                if feedback:
                    print("\nSuggestions:")
                    for msg in feedback:
                        print(f"  {msg}")
                print("="*60)
            else:
                print(f"\n{password}")
        
        elif choice == '3':
            # Multiple passwords
            count = input("\nHow many passwords? (1-20): ").strip()
            count = int(count) if count.isdigit() and 1 <= int(count) <= 20 else 5
            
            length = input("Password length (default 16): ").strip()
            length = int(length) if length.isdigit() else 16
            
            generate_multiple_passwords(count, length)
        
        elif choice == '4':
            # Check strength
            test_pwd = input("\nEnter password to check: ").strip()
            strength, feedback = check_password_strength(test_pwd)
            
            print("\n" + "="*60)
            print(f"Password: {test_pwd}")
            print(f"Strength: {strength}")
            print(f"Length: {len(test_pwd)} characters")
            
            if feedback:
                print("\nSuggestions for improvement:")
                for msg in feedback:
                    print(f"  {msg}")
            else:
                print("\n✅ Excellent password!")
            print("="*60)
        
        elif choice == '5':
            print("\n🔒 Stay secure! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

