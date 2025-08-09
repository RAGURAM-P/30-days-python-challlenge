#1.List of names
print("list & files combo:")

names = ["Madhan", "Anita", "Keerthi", "Priya"]

#Write names to file
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

#Read and print names from file
with open("names.txt", "r") as file:
    print("Names in the file:")
    for line in file:
        print(line.strip())  

#2..importing Modulus
print("Importing Modules:")
import random
import math
import datetime

fruits = ["Apple", "Mango", "Banana", "Grapes"]
print("Random fruit:", random.choice(fruits))

radius = 5
area = math.pi * math.pow(radius, 2)
print(f"Area of circle with radius {radius} = {area:.2f}")

now = datetime.datetime.now()
print("Current date & time:", now.strftime("%Y-%m-%d %H:%M:%S"))

#3.oop concepts

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False  # Default state
        self.fuel = 100  # Fuel percentage

    def start(self):
        if self.fuel <= 0:
            print(f"{self.brand} {self.model} cannot start — fuel empty!")
        elif not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} is now starting...")
        else:
            print(f"{self.brand} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} is now stopping...")
        else:
            print(f"{self.brand} {self.model} is already stopped.")

    def refuel(self, amount):
        self.fuel = min(100, self.fuel + amount)
        print(f"{self.brand} {self.model} refueled. Fuel level: {self.fuel}%")

    def drive(self, distance):
        if not self.is_running:
            print(f"{self.brand} {self.model} can't drive — car is off.")
        elif self.fuel <= 0:
            print(f"{self.brand} {self.model} ran out of fuel!")
        else:
            fuel_used = distance * 0.5  # Example fuel consumption
            self.fuel = max(0, self.fuel - fuel_used)
            print(f"{self.brand} {self.model} drove {distance} km. Fuel left: {self.fuel}%")


print("🚗 Welcome to the Car Simulator 🚗")
car1 = Car("Toyota", "Corolla")

while True:
    print("\nChoose an action:")
    print("1. Start Car")
    print("2. Stop Car")
    print("3. Drive Car")
    print("4. Refuel Car")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        car1.start()
    elif choice == "2":
        car1.stop()
    elif choice == "3":
        km = float(input("Enter distance to drive (km): "))
        car1.drive(km)
    elif choice == "4":
        fuel_amount = float(input("Enter fuel amount to add: "))
        car1.refuel(fuel_amount)
    elif choice == "5":
        print("Goodbye! 🚗💨")
        break
    else:
        print("Invalid choice! Try again.")



