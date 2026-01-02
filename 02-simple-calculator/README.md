# 02 - Simple Calculator

## 🚀 Project Overview

Build a fully functional calculator that performs basic arithmetic operations. This project teaches you how to create functions, handle user input, implement error handling, and create an interactive menu system.

## 🎯 Learning Objectives

By completing this project, you will:
- Define and use functions with parameters and return values
- Handle different arithmetic operators (+, -, *, /, **, %)
- Implement try-except blocks for error handling
- Create interactive menu systems with loops
- Validate user input
- Work with conditional statements (if/elif/else)
- Understand division by zero errors
- Build a calculation history feature

## 📚 What You'll Learn

### **Core Concepts:**
- **Functions**: Modular, reusable code blocks
- **Parameters & Returns**: Passing data to/from functions
- **Operators**: +, -, *, /, ** (power), % (modulo)
- **Error Handling**: try-except blocks for robust code
- **Loops**: While loops for continuous operation
- **Input Validation**: Ensuring valid user input
- **Type Conversion**: Converting strings to numbers

### **Python Skills:**
- Function definition with `def`
- Return statements
- Exception handling (ZeroDivisionError, ValueError)
- User input with validation
- String formatting with f-strings
- List operations for history tracking

## 🔧 Implementation Explanation

The calculator is built with:

1. **Operation Functions**: Separate functions for each operation (add, subtract, multiply, divide, power, modulo)
2. **Menu System**: User-friendly menu with numbered options
3. **Input Validation**: Error handling for invalid inputs
4. **Calculation History**: Stores all calculations in a list
5. **Error Prevention**: Checks for division by zero
6. **Continuous Operation**: Loops until user chooses to exit

## ⚙️ How to Run

```bash
cd Python_projects/02-simple-calculator
python main.py
```

## 📖 Code Walkthrough

### **Functions (Lines 1-80)**
- Each arithmetic operation has its own function
- Functions accept two parameters and return the result
- Division and modulo functions include zero-check validation

### **Menu System (Lines 82-95)**
- `display_menu()`: Shows available operations
- Clean, formatted output with emojis

### **Input Validation (Lines 97-108)**
- `get_number()`: Ensures valid numeric input
- Uses try-except to catch ValueError
- Loops until valid input is received

### **Main Calculator Logic (Lines 110-180)**
- While loop for continuous operation
- Calculation history tracking
- Option to continue or exit after each calculation

## 🧠 Practice Exercises

1. **Add Square Root**: Implement a square root function using `math.sqrt()`

2. **Add Scientific Operations**:
   - Sine, cosine, tangent (use `math` module)
   - Logarithm and exponential

3. **Memory Feature**:
   - Store last result
   - Add "Use previous result" option
   - Implement MC (Memory Clear), MR (Memory Recall)

4. **Expression Parser**:
   - Allow input like "2 + 3 * 4"
   - Use `eval()` with safety checks
   - Implement proper order of operations

5. **Save History**:
   - Write calculation history to a text file
   - Add option to load previous session

6. **Advanced Features**:
   - Percentage calculations
   - Fraction support (using `fractions` module)
   - Complex number operations

7. **GUI Version**:
   - Create a graphical interface with Tkinter
   - Add buttons for numbers and operations

8. **Unit Converter**:
   - Add temperature conversion (C, F, K)
   - Length, weight, volume conversions

## 💡 Key Takeaways

- ✅ Functions make code modular and reusable
- ✅ Error handling prevents program crashes
- ✅ Input validation ensures data integrity
- ✅ Loops enable continuous program operation
- ✅ ZeroDivisionError must be handled for division/modulo
- ✅ Lists can store program history
- ✅ F-strings make output formatting easy

## 🔗 Related Concepts

- **Functions**: Building blocks of programs
- **Exception Handling**: Robust error management
- **Control Flow**: if/elif/else, while loops
- **Data Structures**: Lists for storing data
- **Operators**: Arithmetic and comparison

## 📖 Further Learning - W3Schools

- [Python Functions](https://www.w3schools.com/python/python_functions.asp)
- [Python Operators](https://www.w3schools.com/python/python_operators.asp)
- [Python Try Except](https://www.w3schools.com/python/python_try_except.asp)
- [Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
- [Python User Input](https://www.w3schools.com/python/python_user_input.asp)
- [Python Math Module](https://www.w3schools.com/python/module_math.asp)
- [Python Lists](https://www.w3schools.com/python/python_lists.asp)

## 🎓 What's Next?

After mastering this project, you're ready for:
- **Project 03**: Number Guessing Game - Random numbers and game logic
- **Project 04**: Temperature Converter - More functions practice
- Learn about the `math` module for advanced calculations
- Explore GUI programming with Tkinter

---

**Difficulty**: 🟢 Beginner  
**Estimated Time**: 45-60 minutes  
**Prerequisites**: Project 01 (variables and basic I/O)  
**Key Concepts**: Functions, Error Handling, Loops
