"""
Grade Calculator - Python Project 10
====================================
Calculate student grades, GPA, and provide detailed academic analysis.

🎯 LEARNING OBJECTIVES:
- Work with lists of numbers
- Calculate averages and statistics
- Implement grading systems
- Use conditional logic for grade assignment
- Format output as tables

📚 CONCEPTS COVERED:
- List operations and aggregation
- Statistical calculations (mean, min, max)
- Conditional grading logic
- Dictionary mapping for grades
- String formatting for tables
"""

def get_letter_grade(score):
    """
    Convert numerical score to letter grade.
    
    LEARNING: Conditional logic with multiple ranges
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def get_gpa(letter_grade):
    """
    Convert letter grade to GPA (4.0 scale).
    
    LEARNING: Dictionary mapping for conversions
    """
    gpa_scale = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return gpa_scale.get(letter_grade, 0.0)

def calculate_average(scores):
    """
    Calculate average of scores.
    
    LEARNING: sum() and len() functions
    """
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_grade_distribution(scores):
    """
    Calculate how many of each letter grade.
    
    LEARNING: Counting occurrences with dictionaries
    """
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    
    for score in scores:
        letter = get_letter_grade(score)
        distribution[letter] += 1
    
    return distribution

def display_grade_report(name, scores):
    """
    Display comprehensive grade report.
    
    LEARNING: Formatted output with statistics
    """
    print("\n" + "="*60)
    print(f"📊 GRADE REPORT FOR {name.upper()}")
    print("="*60)
    
    # Individual scores
    print("\nIndividual Scores:")
    print("-"*60)
    for i, score in enumerate(scores, 1):
        letter = get_letter_grade(score)
        print(f"Assignment {i}: {score:>6.2f}% - {letter}")
    
    # Statistics
    print("\n" + "-"*60)
    print("STATISTICS:")
    print("-"*60)
    
    average = calculate_average(scores)
    highest = max(scores)
    lowest = min(scores)
    letter_grade = get_letter_grade(average)
    gpa = get_gpa(letter_grade)
    
    print(f"Average Score:    {average:.2f}%")
    print(f"Letter Grade:     {letter_grade}")
    print(f"GPA:              {gpa:.2f}")
    print(f"Highest Score:    {highest:.2f}%")
    print(f"Lowest Score:     {lowest:.2f}%")
    print(f"Total Assignments: {len(scores)}")
    
    # Grade distribution
    distribution = get_grade_distribution(scores)
    print("\n" + "-"*60)
    print("GRADE DISTRIBUTION:")
    print("-"*60)
    for grade in ['A', 'B', 'C', 'D', 'F']:
        count = distribution[grade]
        bar = '█' * count
        print(f"{grade}: {bar} ({count})")
    
    print("="*60)

def calculate_weighted_grade(scores, weights):
    """
    Calculate weighted average.
    
    Args:
        scores (list): List of scores
        weights (list): List of weights (as percentages, must sum to 100)
    
    LEARNING: Weighted averages
    """
    if len(scores) != len(weights):
        return None
    
    if sum(weights) != 100:
        return None
    
    weighted_sum = sum(score * (weight / 100) for score, weight in zip(scores, weights))
    return weighted_sum

def calculate_class_statistics(all_students):
    """
    Calculate statistics for entire class.
    
    Args:
        all_students (dict): Dictionary mapping student names to score lists
    
    LEARNING: Working with nested data structures
    """
    print("\n" + "="*60)
    print("📊 CLASS STATISTICS")
    print("="*60)
    
    all_averages = []
    
    print(f"\n{'Student':<20} {'Average':<10} {'Grade':<5} {'GPA':<5}")
    print("-"*60)
    
    for name, scores in all_students.items():
        avg = calculate_average(scores)
        all_averages.append(avg)
        letter = get_letter_grade(avg)
        gpa = get_gpa(letter)
        print(f"{name:<20} {avg:>7.2f}%   {letter:<5} {gpa:<5.2f}")
    
    print("\n" + "-"*60)
    print("CLASS SUMMARY:")
    print("-"*60)
    print(f"Number of Students: {len(all_students)}")
    print(f"Class Average:      {calculate_average(all_averages):.2f}%")
    print(f"Highest Average:    {max(all_averages):.2f}%")
    print(f"Lowest Average:     {min(all_averages):.2f}%")
    print("="*60)

def main():
    """
    Main program loop.
    """
    print("\n" + "="*60)
    print("🎓 GRADE CALCULATOR")
    print("="*60)
    print("\nGrading Scale:")
    print("A: 90-100% (4.0 GPA)")
    print("B: 80-89%  (3.0 GPA)")
    print("C: 70-79%  (2.0 GPA)")
    print("D: 60-69%  (1.0 GPA)")
    print("F: 0-59%   (0.0 GPA)")
    print("="*60)
    
    all_students = {}
    
    while True:
        print("\nOptions:")
        print("1. Calculate single student grade")
        print("2. Calculate weighted grade")
        print("3. Add multiple students")
        print("4. View class statistics")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            # Single student
            name = input("\nEnter student name: ").strip()
            
            scores = []
            print("\nEnter scores (0-100). Type 'done' when finished:")
            
            while True:
                score_input = input(f"Score {len(scores) + 1}: ").strip().lower()
                
                if score_input == 'done':
                    break
                
                try:
                    score = float(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)
                    else:
                        print("❌ Score must be between 0 and 100!")
                except ValueError:
                    print("❌ Invalid input!")
            
            if scores:
                all_students[name] = scores
                display_grade_report(name, scores)
            else:
                print("❌ No scores entered!")
        
        elif choice == '2':
            # Weighted grade
            print("\n--- Weighted Grade Calculator ---")
            
            categories = []
            scores = []
            weights = []
            
            print("\nEnter categories. Type 'done' when finished:")
            
            while True:
                category = input("\nCategory name (or 'done'): ").strip()
                if category.lower() == 'done':
                    break
                
                try:
                    score = float(input(f"Score for {category} (0-100): "))
                    weight = float(input(f"Weight for {category} (percentage): "))
                    
                    if 0 <= score <= 100 and weight > 0:
                        categories.append(category)
                        scores.append(score)
                        weights.append(weight)
                    else:
                        print("❌ Invalid values!")
                except ValueError:
                    print("❌ Invalid input!")
            
            if scores and sum(weights) == 100:
                weighted_avg = calculate_weighted_grade(scores, weights)
                letter = get_letter_grade(weighted_avg)
                gpa = get_gpa(letter)
                
                print("\n" + "="*60)
                print("WEIGHTED GRADE REPORT")
                print("="*60)
                for cat, score, weight in zip(categories, scores, weights):
                    print(f"{cat:<20} {score:>6.2f}% (weight: {weight}%)")
                print("-"*60)
                print(f"Weighted Average: {weighted_avg:.2f}%")
                print(f"Letter Grade:     {letter}")
                print(f"GPA:              {gpa:.2f}")
                print("="*60)
            elif scores:
                print(f"❌ Weights must sum to 100% (currently {sum(weights)}%)")
            else:
                print("❌ No data entered!")
        
        elif choice == '3':
            # Multiple students
            num_students = input("\nHow many students? ").strip()
            
            try:
                num_students = int(num_students)
                
                for i in range(num_students):
                    print(f"\n--- Student {i + 1} ---")
                    name = input("Name: ").strip()
                    
                    scores = []
                    num_scores = input("Number of assignments: ").strip()
                    
                    try:
                        num_scores = int(num_scores)
                        
                        for j in range(num_scores):
                            score = float(input(f"Score {j + 1}: "))
                            if 0 <= score <= 100:
                                scores.append(score)
                        
                        if scores:
                            all_students[name] = scores
                            print(f"✅ Added {name}")
                    
                    except ValueError:
                        print("❌ Invalid input! Skipping student.")
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '4':
            # Class statistics
            if all_students:
                calculate_class_statistics(all_students)
            else:
                print("\n❌ No students added yet!")
        
        elif choice == '5':
            print("\n👋 Thanks for using Grade Calculator! Good luck!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

