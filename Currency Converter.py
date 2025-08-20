USD_RATE = 83   
EURO_RATE = 90

inr = float(input("Enter amount in INR: "))

usd = inr / USD_RATE
euro = inr / EURO_RATE

print(f"\n💰 {inr} INR is equal to:")
print(f"➡️ {usd:.2f} USD")
print(f"➡️ {euro:.2f} Euro")
