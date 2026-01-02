"""
Leap Year Checker - Python Project 12
=====================================
Check if years are leap years and find leap years in ranges.

🎯 LEARNING OBJECTIVES:
- Implement leap year rules with conditional logic
- Work with modulo operator for divisibility
- Validate year inputs
- Find patterns in sequences
- Display formatted lists

📚 CONCEPTS COVERED:
- Modulo operator (%) for divisibility checks
- Complex boolean conditions (and, or)
- Range operations
- List filtering with comprehensions
- Calendar mathematics
"""

def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    Rules:
    1. Divisible by 4 → leap year
    2. UNLESS divisible by 100 → not leap year
    3. UNLESS divisible by 400 → leap year
    
    Examples:
    - 2020: divisible by 4 → LEAP
    - 1900: divisible by 100 but not 400 → NOT LEAP
    - 2000: divisible by 400 → LEAP
    
    LEARNING: Complex conditional logic with multiple rules
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def find_leap_years(start, end):
    """
    Find all leap years in a range.
    
    LEARNING: List comprehension with filtering
    """
    return [year for year in range(start, end + 1) if is_leap_year(year)]

def next_leap_year(year):
    """
    Find the next leap year after given year.
    
    LEARNING: While loop to find next occurrence
    """
    current = year + 1
    while not is_leap_year(current):
        current += 1
    return current

def previous_leap_year(year):
    """
    Find the previous leap year before given year.
    
    LEARNING: Counting backwards with negative step
    """
    current = year - 1
    while current > 0 and not is_leap_year(current):
        current -= 1
    return current if current > 0 else None

def days_in_year(year):
    """
    Return number of days in a year.
    
    LEARNING: Leap years have 366 days, regular years have 365
    """
    return 366 if is_leap_year(year) else 365

def days_in_month(month, year):
    """
    Return number of days in a specific month.
    
    LEARNING: February has 29 days in leap years
    """
    days_per_month = {
        1: 31,   # January
        2: 29 if is_leap_year(year) else 28,  # February
        3: 31,   # March
        4: 30,   # April
        5: 31,   # May
        6: 30,   # June
        7: 31,   # July
        8: 31,   # August
        9: 30,   # September
        10: 31,  # October
        11: 30,  # November
        12: 31   # December
    }
    return days_per_month.get(month, 0)

def leap_year_facts(year):
    """
    Display interesting facts about a year.
    """
    print("\n" + "="*60)
    print(f"📅 YEAR {year} FACTS")
    print("="*60)
    
    if is_leap_year(year):
        print(f"✅ {year} IS a leap year!")
    else:
        print(f"❌ {year} is NOT a leap year")
    
    print(f"\nDays in {year}: {days_in_year(year)}")
    print(f"Days in February {year}: {days_in_month(2, year)}")
    
    # Next and previous leap years
    next_leap = next_leap_year(year)
    prev_leap = previous_leap_year(year)
    
    if prev_leap:
        print(f"Previous leap year: {prev_leap} ({year - prev_leap} years ago)")
    print(f"Next leap year: {next_leap} ({next_leap - year} years away)")
    
    # Century information
    century = (year // 100) + 1
    print(f"\nCentury: {century}{'st' if century == 1 else 'nd' if century == 2 else 'rd' if century == 3 else 'th'}")
    
    # Divisibility checks
    print("\nDivisibility:")
    print(f"  Divisible by 4: {'Yes' if year % 4 == 0 else 'No'}")
    print(f"  Divisible by 100: {'Yes' if year % 100 == 0 else 'No'}")
    print(f"  Divisible by 400: {'Yes' if year % 400 == 0 else 'No'}")
    
    print("="*60)

def display_leap_years_table(leap_years):
    """
    Display leap years in a formatted table.
    
    LEARNING: Displaying lists in columns
    """
    print("\n" + "="*60)
    print("📅 LEAP YEARS")
    print("="*60)
    
    # Display 5 years per row
    for i in range(0, len(leap_years), 5):
        row = leap_years[i:i+5]
        print("  ".join(f"{year:>6}" for year in row))
    
    print("="*60)
    print(f"Total: {len(leap_years)} leap years")

def century_leap_years(century):
    """
    Find all leap years in a given century.
    
    Args:
        century (int): Century number (e.g., 21 for 2000-2099)
    
    LEARNING: Working with century ranges
    """
    start = (century - 1) * 100 + 1
    end = century * 100
    
    return find_leap_years(start, end)

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("📅 LEAP YEAR CHECKER")
    print("="*60)
    print("\nLeap Year Rules:")
    print("1. Divisible by 4 → leap year")
    print("2. UNLESS divisible by 100 → not leap year")
    print("3. UNLESS divisible by 400 → leap year")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Check a specific year")
        print("2. Find leap years in range")
        print("3. Next/Previous leap year")
        print("4. Leap years in a century")
        print("5. Year facts")
        print("6. Current year check")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == '1':
            # Check specific year
            try:
                year = int(input("\nEnter year: "))
                
                if is_leap_year(year):
                    print(f"\n✅ {year} IS a leap year! 🎉")
                    print(f"February {year} has 29 days.")
                else:
                    print(f"\n❌ {year} is NOT a leap year.")
                    print(f"February {year} has 28 days.")
            
            except ValueError:
                print("❌ Invalid year!")
        
        elif choice == '2':
            # Range of leap years
            try:
                start = int(input("\nStart year: "))
                end = int(input("End year: "))
                
                if start > end:
                    start, end = end, start
                
                leap_years = find_leap_years(start, end)
                
                if leap_years:
                    display_leap_years_table(leap_years)
                else:
                    print(f"\n❌ No leap years in range [{start}, {end}]")
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '3':
            # Next/Previous leap year
            try:
                year = int(input("\nEnter year: "))
                
                next_leap = next_leap_year(year)
                prev_leap = previous_leap_year(year)
                
                print(f"\nNext leap year after {year}: {next_leap}")
                if prev_leap:
                    print(f"Previous leap year before {year}: {prev_leap}")
            
            except ValueError:
                print("❌ Invalid year!")
        
        elif choice == '4':
            # Century leap years
            try:
                century = int(input("\nEnter century (e.g., 21 for 2000s): "))
                
                leap_years = century_leap_years(century)
                start = (century - 1) * 100 + 1
                end = century * 100
                
                print(f"\nLeap years in {century}{'st' if century == 1 else 'nd' if century == 2 else 'rd' if century == 3 else 'th'} century ({start}-{end}):")
                display_leap_years_table(leap_years)
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '5':
            # Year facts
            try:
                year = int(input("\nEnter year: "))
                leap_year_facts(year)
            except ValueError:
                print("❌ Invalid year!")
        
        elif choice == '6':
            # Current year
            import datetime
            current_year = datetime.datetime.now().year
            
            if is_leap_year(current_year):
                print(f"\n✅ {current_year} (this year) IS a leap year! 🎉")
            else:
                print(f"\n❌ {current_year} (this year) is NOT a leap year")
                next_leap = next_leap_year(current_year)
                print(f"Next leap year: {next_leap} ({next_leap - current_year} years away)")
        
        elif choice == '7':
            # Exit
            print("\n👋 Thanks for checking leap years! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

# ============================================================================
# INTERESTING LEAP YEAR FACTS:
# ============================================================================
# - Julius Caesar introduced leap years in 45 BCE
# - The Gregorian calendar (1582) added the 100/400 rule
# - Without leap years, seasons would drift (~6 hours/year)
# - 2000 was a leap year (divisible by 400)
# - 1900 was NOT a leap year (divisible by 100 but not 400)
# - Next year divisible by 400: 2400
# - Leap years occur roughly every 4 years (97 in 400 years)

