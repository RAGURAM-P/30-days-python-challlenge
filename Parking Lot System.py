import datetime

class Vehicle:
    def __init__(self, number, vehicle_type):
        self.number = number
        self.vehicle_type = vehicle_type
        self.entry_time = datetime.datetime.now()
        self.exit_time = None

    def exit(self):
        self.exit_time = datetime.datetime.now()

    def get_parking_duration(self):
        if self.exit_time:
            duration = self.exit_time - self.entry_time
            return duration.total_seconds() / 60  # in minutes
        return 0

    def calculate_fee(self):
        duration = self.get_parking_duration()
        if self.vehicle_type == "car":
            rate = 2   # ₹2 per minute
        else:
            rate = 1   # ₹1 per minute
        return round(duration * rate, 2)


# Parking Lot Manager
class ParkingLot:
    def __init__(self):
        self.vehicles = {}

    def park_vehicle(self, number, vehicle_type):
        if number in self.vehicles:
            print(f"🚨 Vehicle {number} is already parked!")
        else:
            vehicle = Vehicle(number, vehicle_type)
            self.vehicles[number] = vehicle
            print(f"✅ {vehicle_type.capitalize()} {number} parked at {vehicle.entry_time.strftime('%H:%M:%S')}")

    def remove_vehicle(self, number):
        if number in self.vehicles:
            vehicle = self.vehicles[number]
            vehicle.exit()
            fee = vehicle.calculate_fee()

            print(f"🚗 Vehicle {number} exited at {vehicle.exit_time.strftime('%H:%M:%S')}")
            print(f"🕒 Duration: {round(vehicle.get_parking_duration(),2)} mins | 💰 Fee: ₹{fee}")

            # Log to file
            with open("parking_log.txt", "a") as f:
                f.write(f"{vehicle.vehicle_type} {vehicle.number} | Entry: {vehicle.entry_time} | Exit: {vehicle.exit_time} | Fee: ₹{fee}\n")

            del self.vehicles[number]
        else:
            print(f"🚨 Vehicle {number} not found in parking!")

    def show_parked(self):
        if not self.vehicles:
            print("🅿️ Parking Lot is empty.")
        else:
            print("📌 Currently Parked Vehicles:")
            for number, vehicle in self.vehicles.items():
                print(f" - {vehicle.vehicle_type.capitalize()} {number} (since {vehicle.entry_time.strftime('%H:%M:%S')})")


lot = ParkingLot()

while True:
    print("\n===== Parking Lot Menu =====")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Show Parked Vehicles")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        num = input("Enter vehicle number: ")
        vtype = input("Enter type (car/bike): ").lower()
        lot.park_vehicle(num, vtype)

    elif choice == "2":
        num = input("Enter vehicle number to remove: ")
        lot.remove_vehicle(num)

    elif choice == "3":
        lot.show_parked()

    elif choice == "4":
        print("👋 Exiting Parking System...")
        break
    else:
        print("❌ Invalid choice. Try again!")
