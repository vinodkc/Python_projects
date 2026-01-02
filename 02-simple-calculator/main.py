"""
Simple Calculator - Python Project 02
=====================================
A comprehensive calculator program demonstrating functions, operators,
error handling, and user input.

🎯 LEARNING OBJECTIVES:
- Define and use functions
- Handle different operators (+, -, *, /, **, %)
- Implement error handling with try-except
- Create a user-friendly menu system
- Use loops for continuous operation
- Validate user input

📚 CONCEPTS COVERED:
- Functions and parameters
- Arithmetic operators
- Error handling (ZeroDivisionError, ValueError)
- While loops
- Conditional statements (if/elif/else)
- String formatting
- Type conversion
"""

def add(x, y):
    """
    Add two numbers.
    
    Args:
        x (float): First number
        y (float): Second number
    
    Returns:
        float: Sum of x and y
    
    LEARNING: Basic arithmetic operation
    """
    return x + y

def subtract(x, y):
    """
    Subtract second number from first.
    
    Args:
        x (float): First number (minuend)
        y (float): Second number (subtrahend)
    
    Returns:
        float: Difference (x - y)
    
    LEARNING: Subtraction operator and order of operands
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers.
    
    Args:
        x (float): First number
        y (float): Second number
    
    Returns:
        float: Product of x and y
    
    LEARNING: Multiplication operator (*)
    """
    return x * y

def divide(x, y):
    """
    Divide first number by second.
    
    Args:
        x (float): Numerator
        y (float): Denominator
    
    Returns:
        float: Quotient (x / y)
    
    Raises:
        ZeroDivisionError: If y is zero
    
    LEARNING: Division operator and handling division by zero
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

def power(x, y):
    """
    Raise first number to the power of second.
    
    Args:
        x (float): Base
        y (float): Exponent
    
    Returns:
        float: x raised to the power of y
    
    LEARNING: Exponentiation operator (**)
    """
    return x ** y

def modulo(x, y):
    """
    Get remainder of division.
    
    Args:
        x (float): Dividend
        y (float): Divisor
    
    Returns:
        float: Remainder of x / y
    
    LEARNING: Modulo operator (%) - useful for checking even/odd, etc.
    """
    if y == 0:
        raise ZeroDivisionError("Cannot perform modulo with zero!")
    return x % y

def display_menu():
    """
    Display the calculator menu.
    
    LEARNING: Using print() for formatted output and creating user interfaces
    """
    print("\n" + "="*50)
    print("🔢 SIMPLE CALCULATOR")
    print("="*50)
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")
    print("6. Modulo (%)")
    print("7. Exit")
    print("="*50)

def get_number(prompt):
    """
    Get a valid number from user with error handling.
    
    Args:
        prompt (str): Message to display to user
    
    Returns:
        float: Valid number entered by user
    
    LEARNING: Input validation and error handling
    - Try-except blocks catch errors
    - Loops ensure valid input before continuing
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def calculate(choice, num1, num2):
    """
    Perform calculation based on user choice.
    
    Args:
        choice (str): Operation choice (1-6)
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float or None: Result of calculation or None if invalid choice
    
    LEARNING: Using if-elif chains and calling functions
    """
    try:
        if choice == '1':
            result = add(num1, num2)
            print(f"\n✅ {num1} + {num2} = {result}")
            return result
        
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\n✅ {num1} - {num2} = {result}")
            return result
        
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\n✅ {num1} × {num2} = {result}")
            return result
        
        elif choice == '4':
            result = divide(num1, num2)
            print(f"\n✅ {num1} ÷ {num2} = {result}")
            return result
        
        elif choice == '5':
            result = power(num1, num2)
            print(f"\n✅ {num1} ^ {num2} = {result}")
            return result
        
        elif choice == '6':
            result = modulo(num1, num2)
            print(f"\n✅ {num1} % {num2} = {result}")
            return result
        
        else:
            print("❌ Invalid choice! Please select 1-7.")
            return None
    
    except ZeroDivisionError as e:
        print(f"❌ Error: {e}")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return None

def main():
    """
    Main calculator loop.
    
    LEARNING: Program structure with main function
    - While True creates an infinite loop
    - break statement exits the loop
    - Good practice to have a main() function
    """
    print("\n🎓 Welcome to the Simple Calculator!")
    print("This calculator demonstrates functions, operators, and error handling.")
    
    # History feature to store calculations
    history = []
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '7':
            print("\n👋 Thank you for using the calculator!")
            if history:
                print("\n📜 Calculation History:")
                for i, calc in enumerate(history, 1):
                    print(f"  {i}. {calc}")
            print("Goodbye! 🎉\n")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            # Get numbers from user
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            # Perform calculation
            result = calculate(choice, num1, num2)
            
            # Store in history if successful
            if result is not None:
                operations = {
                    '1': f"{num1} + {num2} = {result}",
                    '2': f"{num1} - {num2} = {result}",
                    '3': f"{num1} × {num2} = {result}",
                    '4': f"{num1} ÷ {num2} = {result}",
                    '5': f"{num1} ^ {num2} = {result}",
                    '6': f"{num1} % {num2} = {result}"
                }
                history.append(operations[choice])
            
            # Ask if user wants to continue
            cont = input("\nPerform another calculation? (y/n): ").strip().lower()
            if cont != 'y':
                print("\n👋 Thank you for using the calculator!")
                if history:
                    print("\n📜 Calculation History:")
                    for i, calc in enumerate(history, 1):
                        print(f"  {i}. {calc}")
                print("Goodbye! 🎉\n")
                break
        else:
            print("❌ Invalid choice! Please select 1-7.")

# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    """
    LEARNING: This block runs only when the script is executed directly,
    not when imported as a module. This is a Python best practice.
    """
    main()

# ============================================================================
# PRACTICE EXERCISES:
# ============================================================================
# 1. Add a square root function (use math.sqrt)
# 2. Add a factorial function
# 3. Add memory feature (store and recall last result)
# 4. Add scientific operations (sin, cos, tan)
# 5. Add ability to chain calculations (use previous result)
# 6. Create a GUI version with tkinter
# 7. Add ability to evaluate expressions like "2 + 3 * 4"
# 8. Save calculation history to a file
