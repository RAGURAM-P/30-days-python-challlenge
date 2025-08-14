# Custom Exception
class FlightFullError(Exception):
    """Raised when trying to book a seat on a full flight."""
    pass


class Passenger:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self, flight_number, capacity):
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers = []

    def book_seat(self, passenger):
        if len(self.passengers) >= self.capacity:
            raise FlightFullError(f"Cannot book seat for {passenger.name}: Flight {self.flight_number} is FULL.")
        self.passengers.append(passenger)
        print(f"✅ Seat booked for {passenger.name} on Flight {self.flight_number}.")

    def show_passengers(self):
        if not self.passengers:
            print("No passengers booked yet.")
        else:
            print(f"Passengers on Flight {self.flight_number}:")
            for p in self.passengers:
                print(f" - {p.name}")

try:
    
    flight1 = Flight("AI101", 2)

    p1 = Passenger("Mathi")
    p2 = Passenger("Lima")
    p3 = Passenger("Robet")
                   
    flight1.book_seat(p1)
    flight1.book_seat(p2)

    flight1.book_seat(p3)

except FlightFullError as e:
    print(f"❌ ERROR: {e}")

flight1.show_passengers()
