class Loan:
    def __init__(self, principal, annual_rate, years):
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years

    def calculate_emi(self):
        """Calculate EMI using the formula"""
        monthly_rate = self.annual_rate / 12 / 100  # convert % → decimal per month
        months = self.years * 12

        if monthly_rate == 0:  # Zero interest loan
            emi = self.principal / months
        else:
            emi = (self.principal * monthly_rate * (1 + monthly_rate) ** months) / \
                  ((1 + monthly_rate) ** months - 1)
        return emi

    def loan_summary(self):
        """Print loan details + EMI"""
        emi = self.calculate_emi()
        total_payment = emi * self.years * 12
        total_interest = total_payment - self.principal

        print("\n--- Loan Summary ---")
        print(f"Principal Amount : ₹{self.principal:,.2f}")
        print(f"Annual Interest  : {self.annual_rate}%")
        print(f"Tenure           : {self.years} years ({self.years*12} months)")
        print(f"Monthly EMI      : ₹{emi:,.2f}")
        print(f"Total Payment    : ₹{total_payment:,.2f}")
        print(f"Total Interest   : ₹{total_interest:,.2f}")



if __name__ == "__main__":
    print("🏦 Bank Loan EMI Calculator")
    principal = float(input("Enter loan amount (₹): "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter loan tenure (years): "))

    loan = Loan(principal, annual_rate, years)
    loan.loan_summary()
