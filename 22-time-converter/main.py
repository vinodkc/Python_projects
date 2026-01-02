"""
Time Converter - Python Project 22
==================================
Convert between different time units and formats.

🎯 LEARNING OBJECTIVES:
- Convert between time units
- Work with datetime module
- Format time displays
- Perform time calculations

📚 CONCEPTS COVERED:
- Unit conversions
- Mathematical operations
- Time formatting
- datetime module basics
"""

import datetime

def seconds_to_time(seconds):
    """Convert seconds to hours:minutes:seconds."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return hours, minutes, secs

def time_to_seconds(hours, minutes, seconds):
    """Convert time to total seconds."""
    return hours * 3600 + minutes * 60 + seconds

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("⏰ TIME CONVERTER")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Seconds to H:M:S")
        print("2. H:M:S to seconds")
        print("3. Minutes converter")
        print("4. Hours converter")
        print("5. Current time info")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == '1':
            try:
                seconds = int(input("\nEnter seconds: "))
                h, m, s = seconds_to_time(seconds)
                print(f"\n{seconds} seconds = {h}h {m}m {s}s")
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '2':
            try:
                hours = int(input("\nHours: "))
                minutes = int(input("Minutes: "))
                seconds = int(input("Seconds: "))
                total = time_to_seconds(hours, minutes, seconds)
                print(f"\n{hours}h {minutes}m {seconds}s = {total} seconds")
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '3':
            try:
                minutes = float(input("\nEnter minutes: "))
                print(f"\n{minutes} minutes =")
                print(f"  {minutes * 60} seconds")
                print(f"  {minutes / 60:.2f} hours")
                print(f"  {minutes / 1440:.4f} days")
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '4':
            try:
                hours = float(input("\nEnter hours: "))
                print(f"\n{hours} hours =")
                print(f"  {hours * 60} minutes")
                print(f"  {hours * 3600} seconds")
                print(f"  {hours / 24:.4f} days")
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '5':
            now = datetime.datetime.now()
            print("\n" + "="*60)
            print("CURRENT TIME INFO")
            print("="*60)
            print(f"Date: {now.strftime('%Y-%m-%d')}")
            print(f"Time: {now.strftime('%H:%M:%S')}")
            print(f"Day of week: {now.strftime('%A')}")
            print(f"Day of year: {now.timetuple().tm_yday}")
            print("="*60)
        
        elif choice == '6':
            print("\n⏰ Time to go! Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

