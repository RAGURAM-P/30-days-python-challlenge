# Car Rental System

class Car:
    def __init__(self, brand, model, daily_rate):
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate
        self.is_available = True

    def rent_car(self, days):
        if self.is_available:
            self.is_available = False
            cost = self.calculate_bill(days)
            return f"✅ {self.brand} {self.model} rented for {days} days. Total cost = ₹{cost}"
        else:
            return f"❌ Sorry, {self.brand} {self.model} is already rented."

    def return_car(self):
        if not self.is_available:
            self.is_available = True
            return f"🚗 {self.brand} {self.model} has been returned."
        else:
            return f"⚠️ {self.brand} {self.model} was not rented."

    def calculate_bill(self, days):
        return days * self.daily_rate

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"{self.brand} {self.model} - ₹{self.daily_rate}/day ({status})"


# ---- Main Program ----
car1 = Car("Toyota", "Innova", 2000)
car2 = Car("Hyundai", "i20", 1500)

# Show available cars
print(car1)
print(car2)

# Renting cars
print(car1.rent_car(3))
print(car2.rent_car(2))

# Trying to rent again
print(car1.rent_car(1))

# Returning car
print(car1.return_car())

# Rent again after return
print(car1.rent_car(5))
