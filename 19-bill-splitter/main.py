"""
Bill Splitter - Python Project 19
=================================
Split bills among friends with tip calculation.

🎯 LEARNING OBJECTIVES:
- Perform financial calculations
- Divide amounts among people
- Calculate tips and totals
- Format currency output

📚 CONCEPTS COVERED:
- Division and rounding
- Percentage calculations
- Float formatting
- User-friendly output
"""

def calculate_split(total, num_people, tip_percent=0):
    """
    Calculate how much each person pays.
    
    Returns:
        tuple: (amount_per_person, tip_amount, grand_total)
    """
    tip_amount = total * (tip_percent / 100)
    grand_total = total + tip_amount
    per_person = grand_total / num_people
    
    return per_person, tip_amount, grand_total

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("💵 BILL SPLITTER")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Split bill")
        print("2. Split with custom amounts")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            try:
                total = float(input("\nTotal bill amount: $"))
                num_people = int(input("Number of people: "))
                
                if num_people <= 0:
                    print("❌ Must have at least 1 person!")
                    continue
                
                print("\nTip percentage:")
                print("1. No tip (0%)")
                print("2. Good (15%)")
                print("3. Great (18%)")
                print("4. Excellent (20%)")
                print("5. Custom")
                
                tip_choice = input("Choose (1-5): ").strip()
                
                tip_percent = 0
                if tip_choice == '2':
                    tip_percent = 15
                elif tip_choice == '3':
                    tip_percent = 18
                elif tip_choice == '4':
                    tip_percent = 20
                elif tip_choice == '5':
                    tip_percent = float(input("Enter tip %: "))
                
                per_person, tip_amount, grand_total = calculate_split(
                    total, num_people, tip_percent
                )
                
                print("\n" + "="*60)
                print("BILL SPLIT BREAKDOWN")
                print("="*60)
                print(f"Original Bill:    ${total:,.2f}")
                print(f"Tip ({tip_percent}%):        ${tip_amount:,.2f}")
                print(f"Grand Total:      ${grand_total:,.2f}")
                print(f"Number of People: {num_people}")
                print("-"*60)
                print(f"Each Person Pays: ${per_person:,.2f}")
                print("="*60)
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '2':
            try:
                num_people = int(input("\nNumber of people: "))
                amounts = []
                
                print("\nEnter what each person ordered:")
                for i in range(num_people):
                    name = input(f"Person {i+1} name: ")
                    amount = float(input(f"{name}'s amount: $"))
                    amounts.append((name, amount))
                
                tip_percent = float(input("\nTip percentage: "))
                
                total = sum(amt for _, amt in amounts)
                tip_amount = total * (tip_percent / 100)
                grand_total = total + tip_amount
                
                print("\n" + "="*60)
                print("ITEMIZED BILL SPLIT")
                print("="*60)
                
                for name, amount in amounts:
                    share_with_tip = amount * (1 + tip_percent/100)
                    print(f"{name:<15} ${amount:>7.2f} + tip = ${share_with_tip:>7.2f}")
                
                print("-"*60)
                print(f"Subtotal:  ${total:,.2f}")
                print(f"Tip:       ${tip_amount:,.2f}")
                print(f"Total:     ${grand_total:,.2f}")
                print("="*60)
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '3':
            print("\n💵 Happy splitting!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

