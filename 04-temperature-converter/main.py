"""
Temperature Converter - Python Project 04
=========================================
Convert temperatures between Celsius, Fahrenheit, and Kelvin with validation.

🎯 LEARNING OBJECTIVES:
- Write conversion formulas as functions
- Validate temperature inputs (absolute zero check)
- Format output with proper decimal places
- Create a menu-driven program
- Handle edge cases and invalid inputs

📚 CONCEPTS COVERED:
- Mathematical formulas in code
- Function composition (calling functions from functions)
- Input validation with ranges
- Rounding and formatting numbers
- Scientific constants (absolute zero)
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    
    LEARNING: Converting mathematical formulas to code
    """
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """
    Convert Celsius to Kelvin.
    Formula: K = C + 273.15
    
    LEARNING: Kelvin is an absolute temperature scale (no negative values)
    """
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9
    
    LEARNING: Inverse of the C to F formula
    """
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin.
    
    LEARNING: Function composition - convert F→C then C→K
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    """
    Convert Kelvin to Celsius.
    Formula: C = K - 273.15
    """
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit.
    
    LEARNING: Chaining conversions K→C→F
    """
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def is_valid_temperature(temp, scale):
    """
    Check if temperature is physically possible (above absolute zero).
    
    Absolute Zero values:
    - Celsius: -273.15°C
    - Fahrenheit: -459.67°F
    - Kelvin: 0 K
    
    LEARNING: Validation based on scientific constraints
    """
    absolute_zero = {
        'C': -273.15,
        'F': -459.67,
        'K': 0
    }
    
    return temp >= absolute_zero[scale]

def get_temperature(scale_name, scale_code):
    """
    Get and validate temperature input from user.
    
    LEARNING: Combining input validation with domain-specific rules
    """
    while True:
        try:
            temp = float(input(f"\nEnter temperature in {scale_name}: "))
            
            if is_valid_temperature(temp, scale_code):
                return temp
            else:
                abs_zero = {
                    'C': "-273.15°C",
                    'F': "-459.67°F",
                    'K': "0 K"
                }
                print(f"❌ Temperature cannot be below absolute zero ({abs_zero[scale_code]})")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def display_menu():
    """
    Show conversion options.
    """
    print("\n" + "="*60)
    print("🌡️  TEMPERATURE CONVERTER")
    print("="*60)
    print("Choose conversion:")
    print("1. Celsius → Fahrenheit")
    print("2. Celsius → Kelvin")
    print("3. Fahrenheit → Celsius")
    print("4. Fahrenheit → Kelvin")
    print("5. Kelvin → Celsius")
    print("6. Kelvin → Fahrenheit")
    print("7. Convert to All Scales")
    print("8. Exit")
    print("="*60)

def convert_to_all(temp, from_scale):
    """
    Convert temperature to all other scales.
    
    LEARNING: Using dictionaries to store related data
    """
    results = {}
    
    if from_scale == 'C':
        results['Celsius'] = temp
        results['Fahrenheit'] = celsius_to_fahrenheit(temp)
        results['Kelvin'] = celsius_to_kelvin(temp)
    
    elif from_scale == 'F':
        results['Fahrenheit'] = temp
        results['Celsius'] = fahrenheit_to_celsius(temp)
        results['Kelvin'] = fahrenheit_to_kelvin(temp)
    
    elif from_scale == 'K':
        results['Kelvin'] = temp
        results['Celsius'] = kelvin_to_celsius(temp)
        results['Fahrenheit'] = kelvin_to_fahrenheit(temp)
    
    return results

def main():
    """
    Main program loop.
    """
    print("\n🌡️  Welcome to the Temperature Converter!")
    print("Learn to convert between Celsius, Fahrenheit, and Kelvin")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '8':
            print("\n👋 Thanks for using the Temperature Converter!")
            break
        
        if choice == '1':
            # Celsius to Fahrenheit
            temp = get_temperature("Celsius", 'C')
            result = celsius_to_fahrenheit(temp)
            print(f"\n✅ {temp}°C = {result:.2f}°F")
        
        elif choice == '2':
            # Celsius to Kelvin
            temp = get_temperature("Celsius", 'C')
            result = celsius_to_kelvin(temp)
            print(f"\n✅ {temp}°C = {result:.2f} K")
        
        elif choice == '3':
            # Fahrenheit to Celsius
            temp = get_temperature("Fahrenheit", 'F')
            result = fahrenheit_to_celsius(temp)
            print(f"\n✅ {temp}°F = {result:.2f}°C")
        
        elif choice == '4':
            # Fahrenheit to Kelvin
            temp = get_temperature("Fahrenheit", 'F')
            result = fahrenheit_to_kelvin(temp)
            print(f"\n✅ {temp}°F = {result:.2f} K")
        
        elif choice == '5':
            # Kelvin to Celsius
            temp = get_temperature("Kelvin", 'K')
            result = kelvin_to_celsius(temp)
            print(f"\n✅ {temp} K = {result:.2f}°C")
        
        elif choice == '6':
            # Kelvin to Fahrenheit
            temp = get_temperature("Kelvin", 'K')
            result = kelvin_to_fahrenheit(temp)
            print(f"\n✅ {temp} K = {result:.2f}°F")
        
        elif choice == '7':
            # Convert to all scales
            print("\nSelect input scale:")
            print("1. Celsius")
            print("2. Fahrenheit")
            print("3. Kelvin")
            
            scale_choice = input("Enter choice (1-3): ").strip()
            
            if scale_choice == '1':
                temp = get_temperature("Celsius", 'C')
                results = convert_to_all(temp, 'C')
            elif scale_choice == '2':
                temp = get_temperature("Fahrenheit", 'F')
                results = convert_to_all(temp, 'F')
            elif scale_choice == '3':
                temp = get_temperature("Kelvin", 'K')
                results = convert_to_all(temp, 'K')
            else:
                print("❌ Invalid choice!")
                continue
            
            print("\n" + "="*60)
            print("🌡️  CONVERSION RESULTS")
            print("="*60)
            print(f"Celsius:    {results['Celsius']:.2f}°C")
            print(f"Fahrenheit: {results['Fahrenheit']:.2f}°F")
            print(f"Kelvin:     {results['Kelvin']:.2f} K")
            print("="*60)
        
        else:
            print("❌ Invalid choice! Please select 1-8.")
        
        # Continue prompt
        cont = input("\nConvert another temperature? (y/n): ").strip().lower()
        if cont != 'y':
            print("\n👋 Thanks for using the Temperature Converter!")
            break

if __name__ == "__main__":
    main()

# ============================================================================
# INTERESTING TEMPERATURE FACTS (for testing):
# ============================================================================
# Water freezes: 0°C = 32°F = 273.15 K
# Water boils: 100°C = 212°F = 373.15 K
# Room temperature: ~20°C = 68°F = 293.15 K
# Body temperature: 37°C = 98.6°F = 310.15 K
# Absolute zero: -273.15°C = -459.67°F = 0 K
# Surface of Sun: ~5,500°C = ~9,932°F = ~5,773 K

