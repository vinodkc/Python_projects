"""
Simple Interest Calculator - Python Project 14
==============================================
Calculate simple and compound interest with detailed breakdowns.

🎯 LEARNING OBJECTIVES:
- Implement financial formulas
- Work with floating-point calculations
- Format currency output
- Compare different interest types

📚 CONCEPTS COVERED:
- Mathematical formulas (SI = P × R × T / 100)
- Compound interest calculations
- Float formatting for money
- Comparative analysis
"""

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    Formula: SI = (P × R × T) / 100
    
    Args:
        principal: Initial amount
        rate: Interest rate per year (%)
        time: Time period in years
    """
    si = (principal * rate * time) / 100
    total = principal + si
    return si, total

def calculate_compound_interest(principal, rate, time, frequency=1):
    """
    Calculate compound interest.
    Formula: A = P(1 + r/n)^(nt)
    
    Args:
        principal: Initial amount
        rate: Annual interest rate (%)
        time: Time in years
        frequency: Compounding frequency per year (1=annually, 4=quarterly, 12=monthly)
    """
    r = rate / 100
    amount = principal * ((1 + r/frequency) ** (frequency * time))
    ci = amount - principal
    return ci, amount

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("💰 INTEREST CALCULATOR")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Compare Both")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice in ['1', '2', '3']:
            try:
                principal = float(input("\nPrincipal amount ($): "))
                rate = float(input("Interest rate (% per year): "))
                time = float(input("Time period (years): "))
                
                if choice == '1':
                    si, total = calculate_simple_interest(principal, rate, time)
                    print("\n" + "="*60)
                    print("SIMPLE INTEREST")
                    print("="*60)
                    print(f"Principal:        ${principal:,.2f}")
                    print(f"Rate:             {rate}% per year")
                    print(f"Time:             {time} years")
                    print(f"Interest Earned:  ${si:,.2f}")
                    print(f"Total Amount:     ${total:,.2f}")
                    print("="*60)
                
                elif choice == '2':
                    print("\nCompounding frequency:")
                    print("1. Annually (1x/year)")
                    print("2. Semi-annually (2x/year)")
                    print("3. Quarterly (4x/year)")
                    print("4. Monthly (12x/year)")
                    
                    freq_choice = input("Choose (1-4): ").strip()
                    frequencies = {'1': 1, '2': 2, '3': 4, '4': 12}
                    frequency = frequencies.get(freq_choice, 1)
                    
                    ci, total = calculate_compound_interest(principal, rate, time, frequency)
                    
                    freq_names = {1: "Annually", 2: "Semi-annually", 4: "Quarterly", 12: "Monthly"}
                    
                    print("\n" + "="*60)
                    print("COMPOUND INTEREST")
                    print("="*60)
                    print(f"Principal:        ${principal:,.2f}")
                    print(f"Rate:             {rate}% per year")
                    print(f"Time:             {time} years")
                    print(f"Compounding:      {freq_names[frequency]}")
                    print(f"Interest Earned:  ${ci:,.2f}")
                    print(f"Total Amount:     ${total:,.2f}")
                    print("="*60)
                
                elif choice == '3':
                    si, si_total = calculate_simple_interest(principal, rate, time)
                    ci, ci_total = calculate_compound_interest(principal, rate, time, 12)
                    
                    print("\n" + "="*60)
                    print("COMPARISON: SIMPLE vs COMPOUND")
                    print("="*60)
                    print(f"Principal: ${principal:,.2f} | Rate: {rate}% | Time: {time} years")
                    print("-"*60)
                    print(f"Simple Interest:   ${si:,.2f} → Total: ${si_total:,.2f}")
                    print(f"Compound (Monthly): ${ci:,.2f} → Total: ${ci_total:,.2f}")
                    print("-"*60)
                    print(f"Difference:        ${ci - si:,.2f}")
                    print(f"Compound earns {((ci/si - 1) * 100):.2f}% more!")
                    print("="*60)
            
            except ValueError:
                print("❌ Invalid input!")
        
        elif choice == '4':
            print("\n💰 Thanks for calculating! Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

