"""
ASCII Art Generator - Python Project 21
=======================================
Generate ASCII art text banners and shapes.

🎯 LEARNING OBJECTIVES:
- Work with ASCII characters
- Create text-based art
- Use dictionaries for character mapping
- Build visual representations

📚 CONCEPTS COVERED:
- ASCII character sets
- Dictionary mapping
- String building
- Multi-line output
"""

def text_to_banner(text):
    """Convert text to ASCII art banner."""
    art = {
        'A': ['  A  ', ' A A ', 'AAAAA', 'A   A', 'A   A'],
        'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
        'C': [' CCC ', 'C   C', 'C    ', 'C   C', ' CCC '],
        'D': ['DDD  ', 'D  D ', 'D   D', 'D  D ', 'DDD  '],
        'E': ['EEEEE', 'E    ', 'EEEE ', 'E    ', 'EEEEE'],
        'F': ['FFFFF', 'F    ', 'FFFF ', 'F    ', 'F    '],
        'G': [' GGG ', 'G    ', 'G  GG', 'G   G', ' GGG '],
        'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
        'I': ['IIIII', '  I  ', '  I  ', '  I  ', 'IIIII'],
        'J': ['JJJJJ', '    J', '    J', 'J   J', ' JJJ '],
        'K': ['K   K', 'K  K ', 'KKK  ', 'K  K ', 'K   K'],
        'L': ['L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
        'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
        'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N'],
        'O': [' OOO ', 'O   O', 'O   O', 'O   O', ' OOO '],
        'P': ['PPPP ', 'P   P', 'PPPP ', 'P    ', 'P    '],
        'Q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q  QQ', ' QQQQ'],
        'R': ['RRRR ', 'R   R', 'RRRR ', 'R  R ', 'R   R'],
        'S': [' SSSS', 'S    ', ' SSS ', '    S', 'SSSS '],
        'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  '],
        'U': ['U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
        'V': ['V   V', 'V   V', 'V   V', ' V V ', '  V  '],
        'W': ['W   W', 'W   W', 'W W W', 'WW WW', 'W   W'],
        'X': ['X   X', ' X X ', '  X  ', ' X X ', 'X   X'],
        'Y': ['Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  '],
        'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'ZZZZZ'],
        ' ': ['     ', '     ', '     ', '     ', '     '],
        '!': ['  !  ', '  !  ', '  !  ', '     ', '  !  '],
        '?': [' ??? ', '?   ?', '   ? ', '  ?  ', '  ?  '],
    }
    
    lines = ['', '', '', '', '']
    
    for char in text.upper():
        if char in art:
            for i in range(5):
                lines[i] += art[char][i] + '  '
    
    return '\n'.join(lines)

def draw_box(text):
    """Draw text in a box."""
    width = len(text) + 4
    print('┌' + '─' * (width - 2) + '┐')
    print('│ ' + text + ' │')
    print('└' + '─' * (width - 2) + '┘')

def draw_banner(text):
    """Draw text with banner decoration."""
    width = len(text) + 4
    print('=' * width)
    print('| ' + text + ' |')
    print('=' * width)

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("🎨 ASCII ART GENERATOR")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. ASCII text banner")
        print("2. Box frame")
        print("3. Banner frame")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            text = input("\nEnter text (max 10 chars): ")[:10]
            print("\n" + text_to_banner(text))
        
        elif choice == '2':
            text = input("\nEnter text: ")
            print()
            draw_box(text)
        
        elif choice == '3':
            text = input("\nEnter text: ")
            print()
            draw_banner(text)
        
        elif choice == '4':
            print("\n🎨 Keep creating art!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

