#1.Conditions (if, elif, else)

year = int(input("Enter a year: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is NOT a Leap Year")
    else:
        print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")


#2.Loops (for and while) + Functions

num = int(input("Enter a number: "))

print(f"\nMultiplication table of {num} using FOR loop:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#3. Exception Handling (Try/Except)

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("❌ Please enter valid numbers!")

except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

finally:
    print("✅ Calculation attempt complete.")

