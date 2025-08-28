import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("🎲 Welcome to Dice Roller 🎲")

    while True:
        sides = input("\nEnter number of sides for the dice (default 6): ")
        if sides.strip() == "":
            sides = 6
        elif sides.isdigit() and int(sides) > 1:
            sides = int(sides)
        else:
            print("❌ Invalid input! Using 6 sides.")
            sides = 6

        result = roll_dice(sides)
        print(f"✅ You rolled a {result} on a {sides}-sided dice!")

        again = input("Roll again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
