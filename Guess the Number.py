import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("🎯 Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

attempts = 0  # To count how many guesses

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"✅ You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("⚠ Please enter a valid number.")
