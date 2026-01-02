"""
Vowel Counter - Python Project 15
=================================
Count vowels in text with detailed analysis.

🎯 LEARNING OBJECTIVES:
- Iterate through strings
- Check character membership
- Count occurrences
- Analyze text patterns

📚 CONCEPTS COVERED:
- String iteration
- Character checking (in operator)
- Counting with dictionaries
- Case-insensitive comparison
"""

def count_vowels(text):
    """Count total vowels in text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def count_each_vowel(text):
    """Count each vowel separately."""
    counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
    return counts

def analyze_text(text):
    """Complete text analysis."""
    vowel_counts = count_each_vowel(text)
    total_vowels = sum(vowel_counts.values())
    total_chars = len(text)
    letters = sum(1 for c in text if c.isalpha())
    consonants = letters - total_vowels
    
    return {
        'vowels': vowel_counts,
        'total_vowels': total_vowels,
        'consonants': consonants,
        'total_chars': total_chars,
        'letters': letters
    }

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("🔤 VOWEL COUNTER")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Count vowels in text")
        print("2. Detailed analysis")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            text = input("\nEnter text: ")
            total = count_vowels(text)
            print(f"\nTotal vowels: {total}")
        
        elif choice == '2':
            text = input("\nEnter text: ")
            analysis = analyze_text(text)
            
            print("\n" + "="*60)
            print("TEXT ANALYSIS")
            print("="*60)
            print(f"Total characters: {analysis['total_chars']}")
            print(f"Letters:          {analysis['letters']}")
            print(f"Vowels:           {analysis['total_vowels']}")
            print(f"Consonants:       {analysis['consonants']}")
            print("\nVowel breakdown:")
            for vowel, count in sorted(analysis['vowels'].items()):
                bar = '█' * count
                print(f"  {vowel}: {bar} ({count})")
            print("="*60)
        
        elif choice == '3':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

