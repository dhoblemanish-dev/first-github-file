"""
Python Program to Calculate Fixed Deposit (FD) Maturity Amount
This program calculates the maturity amount based on:
- Principal Amount (FD Amount)
- Interest Rate (Annual %)
- Time Period (Years)
"""

# ============================================
# METHOD 1: Simple Interest FD Calculation
# ============================================
print("=" * 70)
print("METHOD 1: Fixed Deposit - Simple Interest")
print("=" * 70)

try:
    principal = float(input("Enter FD Amount (Principal): ₹ "))
    rate = float(input("Enter Annual Interest Rate (%): "))
    time = float(input("Enter Time Period (Years): "))
    
    # Simple Interest Formula: A = P + (P × R × T / 100)
    simple_interest = (principal * rate * time) / 100
    maturity_amount = principal + simple_interest
    
    print("\n" + "-" * 70)
    print("CALCULATION DETAILS (Simple Interest):")
    print("-" * 70)
    print(f"Principal Amount (FD Amount):        ₹ {principal:,.2f}")
    print(f"Annual Interest Rate:                {rate}%")
    print(f"Time Period:                         {time} Years")
    print(f"Simple Interest Earned:              ₹ {simple_interest:,.2f}")
    print(f"Maturity Amount:                     ₹ {maturity_amount:,.2f}")
    print("=" * 70)
    
except ValueError:
    print("Error: Please enter valid numbers!")


# ============================================
# METHOD 2: Compound Interest FD Calculation
# ============================================
print("\n" + "=" * 70)
print("METHOD 2: Fixed Deposit - Compound Interest (Quarterly)")
print("=" * 70)

try:
    principal = float(input("\nEnter FD Amount (Principal): ₹ "))
    rate = float(input("Enter Annual Interest Rate (%): "))
    time = float(input("Enter Time Period (Years): "))
    
    # Compound Interest Formula: A = P × (1 + R/100)^T
    # For quarterly compounding: A = P × (1 + (R/4)/100)^(T×4)
    quarterly_rate = rate / 4 / 100
    num_quarters = time * 4
    
    maturity_amount = principal * ((1 + quarterly_rate) ** num_quarters)
    compound_interest = maturity_amount - principal
    
    print("\n" + "-" * 70)
    print("CALCULATION DETAILS (Compound Interest - Quarterly):")
    print("-" * 70)
    print(f"Principal Amount (FD Amount):        ₹ {principal:,.2f}")
    print(f"Annual Interest Rate:                {rate}%")
    print(f"Time Period:                         {time} Years")
    print(f"Compounding:                         Quarterly")
    print(f"Compound Interest Earned:            ₹ {compound_interest:,.2f}")
    print(f"Maturity Amount:                     ₹ {maturity_amount:,.2f}")
    print("=" * 70)
    
except ValueError:
    print("Error: Please enter valid numbers!")


# ============================================
# METHOD 3: Comparison of Interest Types
# ============================================
print("\n" + "=" * 70)
print("METHOD 3: Compare Simple vs Compound Interest")
print("=" * 70)

def calculate_simple_interest(principal, rate, time):
    """Calculate Simple Interest"""
    si = (principal * rate * time) / 100
    return principal + si

def calculate_compound_interest(principal, rate, time, compounds_per_year=1):
    """Calculate Compound Interest"""
    rate_decimal = rate / 100
    maturity = principal * ((1 + rate_decimal / compounds_per_year) ** (time * compounds_per_year))
    return maturity

try:
    principal = float(input("\nEnter FD Amount (Principal): ₹ "))
    rate = float(input("Enter Annual Interest Rate (%): "))
    time = float(input("Enter Time Period (Years): "))
    
    # Calculate all variations
    simple = calculate_simple_interest(principal, rate, time)
    compound_annual = calculate_compound_interest(principal, rate, time, 1)
    compound_half_yearly = calculate_compound_interest(principal, rate, time, 2)
    compound_quarterly = calculate_compound_interest(principal, rate, time, 4)
    compound_monthly = calculate_compound_interest(principal, rate, time, 12)
    
    print("\n" + "-" * 70)
    print("COMPARISON TABLE:")
    print("-" * 70)
    print(f"{'Interest Type':<30} {'Maturity Amount':<20} {'Interest Earned':<20}")
    print("-" * 70)
    print(f"{'Simple Interest':<30} ₹ {simple:>17,.2f} ₹ {simple - principal:>17,.2f}")
    print(f"{'Compound (Annual)':<30} ₹ {compound_annual:>17,.2f} ₹ {compound_annual - principal:>17,.2f}")
    print(f"{'Compound (Half-Yearly)':<30} ₹ {compound_half_yearly:>17,.2f} ₹ {compound_half_yearly - principal:>17,.2f}")
    print(f"{'Compound (Quarterly)':<30} ₹ {compound_quarterly:>17,.2f} ₹ {compound_quarterly - principal:>17,.2f}")
    print(f"{'Compound (Monthly)':<30} ₹ {compound_monthly:>17,.2f} ₹ {compound_monthly - principal:>17,.2f}")
    print("=" * 70)
    
except ValueError:
    print("Error: Please enter valid numbers!")


# ============================================
# METHOD 4: Year-by-Year Breakdown
# ============================================
print("\n" + "=" * 70)
print("METHOD 4: Year-by-Year Maturity Breakdown")
print("=" * 70)

def year_by_year_breakdown(principal, rate, time):
    """Show maturity amount for each year"""
    print(f"\n{'Year':<10} {'Amount at End of Year':<30} {'Interest Earned':<20}")
    print("-" * 70)
    
    for year in range(1, int(time) + 1):
        # Compound Interest quarterly
        quarterly_rate = rate / 4 / 100
        num_quarters = year * 4
        amount = principal * ((1 + quarterly_rate) ** num_quarters)
        interest = amount - principal
        print(f"{year:<10} ₹ {amount:>27,.2f} ₹ {interest:>17,.2f}")

try:
    principal = float(input("\nEnter FD Amount (Principal): ₹ "))
    rate = float(input("Enter Annual Interest Rate (%): "))
    time = int(input("Enter Time Period (Years - Whole Numbers): "))
    
    year_by_year_breakdown(principal, rate, time)
    print("=" * 70)
    
except ValueError:
    print("Error: Please enter valid numbers!")


# ============================================
# METHOD 5: FD Calculator Class
# ============================================
print("\n" + "=" * 70)
print("METHOD 5: Complete FD Calculator Class")
print("=" * 70)

class FDCalculator:
    """A class to calculate FD maturity amounts"""
    
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time
    
    def simple_interest(self):
        """Calculate simple interest"""
        si = (self.principal * self.rate * self.time) / 100
        return self.principal + si
    
    def compound_interest(self, compounds_per_year=1):
        """Calculate compound interest"""
        rate_decimal = self.rate / 100
        amount = self.principal * ((1 + rate_decimal / compounds_per_year) ** (self.time * compounds_per_year))
        return amount
    
    def get_details(self, interest_type="compound"):
        """Get detailed FD information"""
        if interest_type.lower() == "simple":
            maturity = self.simple_interest()
            interest_earned = maturity - self.principal
            return {
                "principal": self.principal,
                "rate": self.rate,
                "time": self.time,
                "interest_earned": interest_earned,
                "maturity_amount": maturity,
                "interest_type": "Simple Interest"
            }
        else:
            maturity = self.compound_interest(4)  # Quarterly compounding
            interest_earned = maturity - self.principal
            return {
                "principal": self.principal,
                "rate": self.rate,
                "time": self.time,
                "interest_earned": interest_earned,
                "maturity_amount": maturity,
                "interest_type": "Compound Interest (Quarterly)"
            }
    
    def print_receipt(self):
        """Print FD receipt"""
        details = self.get_details("compound")
        print("\n" + "=" * 70)
        print("FIXED DEPOSIT (FD) RECEIPT")
        print("=" * 70)
        print(f"Principal Amount:                    ₹ {details['principal']:,.2f}")
        print(f"Annual Interest Rate:                {details['rate']}%")
        print(f"Tenure:                              {details['time']} Years")
        print(f"Interest Calculation Method:         {details['interest_type']}")
        print(f"Interest Earned:                     ₹ {details['interest_earned']:,.2f}")
        print("-" * 70)
        print(f"MATURITY AMOUNT:                     ₹ {details['maturity_amount']:,.2f}")
        print("=" * 70)

try:
    principal = float(input("\nEnter FD Amount (Principal): ₹ "))
    rate = float(input("Enter Annual Interest Rate (%): "))
    time = float(input("Enter Time Period (Years): "))
    
    fd = FDCalculator(principal, rate, time)
    fd.print_receipt()

except ValueError:
    print("Error: Please enter valid numbers!")


# ============================================
# METHOD 6: Interactive FD Calculator Menu
# ============================================
print("\n" + "=" * 70)
print("METHOD 6: Interactive FD Calculator Menu")
print("=" * 70)

def fd_calculator_menu():
    """Interactive menu for FD calculator"""
    print("\n" + "=" * 70)
    print("FIXED DEPOSIT CALCULATOR MENU")
    print("=" * 70)
    print("1. Calculate Simple Interest Maturity")
    print("2. Calculate Compound Interest Maturity (Quarterly)")
    print("3. Compare Different Interest Frequencies")
    print("4. Get Detailed FD Receipt")
    print("5. Exit")
    print("=" * 70)
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
        try:
            principal = float(input("\nEnter FD Amount (Principal): ₹ "))
            rate = float(input("Enter Annual Interest Rate (%): "))
            time = float(input("Enter Time Period (Years): "))
            
            si = (principal * rate * time) / 100
            maturity = principal + si
            
            print("\n" + "-" * 70)
            print(f"Principal:          ₹ {principal:,.2f}")
            print(f"Interest Rate:      {rate}%")
            print(f"Time Period:        {time} Years")
            print(f"Interest Earned:    ₹ {si:,.2f}")
            print(f"Maturity Amount:    ₹ {maturity:,.2f}")
            print("-" * 70)
        except ValueError:
            print("Error: Please enter valid numbers!")
    
    elif choice == "2":
        try:
            principal = float(input("\nEnter FD Amount (Principal): ₹ "))
            rate = float(input("Enter Annual Interest Rate (%): "))
            time = float(input("Enter Time Period (Years): "))
            
            fd = FDCalculator(principal, rate, time)
            fd.print_receipt()
        except ValueError:
            print("Error: Please enter valid numbers!")
    
    elif choice == "3":
        try:
            principal = float(input("\nEnter FD Amount (Principal): ₹ "))
            rate = float(input("Enter Annual Interest Rate (%): "))
            time = float(input("Enter Time Period (Years): "))
            
            fd = FDCalculator(principal, rate, time)
            
            print("\n" + "-" * 70)
            print("MATURITY AMOUNT COMPARISON:")
            print("-" * 70)
            print(f"{'Compounding Frequency':<30} {'Maturity Amount':<25} {'Interest Earned':<20}")
            print("-" * 70)
            
            frequencies = {"Annual": 1, "Semi-Annual": 2, "Quarterly": 4, "Monthly": 12}
            for freq_name, freq_value in frequencies.items():
                maturity = fd.compound_interest(freq_value)
                interest = maturity - principal
                print(f"{freq_name:<30} ₹ {maturity:>22,.2f} ₹ {interest:>17,.2f}")
            
            print("-" * 70)
        except ValueError:
            print("Error: Please enter valid numbers!")
    
    elif choice == "4":
        try:
            principal = float(input("\nEnter FD Amount (Principal): ₹ "))
            rate = float(input("Enter Annual Interest Rate (%): "))
            time = float(input("Enter Time Period (Years): "))
            
            fd = FDCalculator(principal, rate, time)
            fd.print_receipt()
        except ValueError:
            print("Error: Please enter valid numbers!")
    
    elif choice == "5":
        print("\nThank you for using FD Calculator!")
    
    else:
        print("Invalid choice! Please try again.")

try:
    fd_calculator_menu()
except ValueError:
    print("Error: Please enter valid numbers!")


# ============================================
# EXAMPLES
# ============================================
print("\n" + "=" * 70)
print("EXAMPLES - SAMPLE FD CALCULATIONS")
print("=" * 70)

examples = [
    {"principal": 100000, "rate": 6.5, "time": 1},
    {"principal": 100000, "rate": 6.5, "time": 3},
    {"principal": 100000, "rate": 6.5, "time": 5},
]

print("\nFor Principal: ₹100,000 | Interest Rate: 6.5% | Quarterly Compounding")
print("-" * 70)
print(f"{'Years':<15} {'Maturity Amount':<25} {'Interest Earned':<25}")
print("-" * 70)

for example in examples:
    fd = FDCalculator(example["principal"], example["rate"], example["time"])
    maturity = fd.compound_interest(4)
    interest = maturity - example["principal"]
    print(f"{example['time']:<15} ₹ {maturity:>22,.2f} ₹ {interest:>22,.2f}")

print("=" * 70)
print("\nProgram Completed!")
print("=" * 70)
