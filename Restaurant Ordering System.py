# Restaurant Ordering System

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price:.2f}"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append(MenuItem(name, price))

    def show_menu(self):
        print("\n--- MENU ---")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item}")


class Order:
    def __init__(self):
        self.ordered_items = []

    def add_to_order(self, menu, choice):
        if 1 <= choice <= len(menu.items):
            self.ordered_items.append(menu.items[choice - 1])
            print(f"✅ {menu.items[choice - 1].name} added to your order!")
        else:
            print("❌ Invalid choice!")

    def show_order(self):
        if not self.ordered_items:
            print("Your order is empty.")
        else:
            print("\n--- Your Order ---")
            for item in self.ordered_items:
                print(f"- {item}")


class Bill:
    @staticmethod
    def generate(order):
        total = sum(item.price for item in order.ordered_items)
        print("\n--- BILL ---")
        for item in order.ordered_items:
            print(f"{item.name} - ₹{item.price:.2f}")
        print(f"Total: ₹{total:.2f}")
        return total


# ----------------------------
# Simulation
menu = Menu()
menu.add_item("Pizza", 250)
menu.add_item("Burger", 150)
menu.add_item("Pasta", 200)
menu.add_item("Coke", 50)

order = Order()

while True:
    menu.show_menu()
    choice = input("Enter item number to add (or 'done' to finish): ")

    if choice.lower() == "done":
        break
    elif choice.isdigit():
        order.add_to_order(menu, int(choice))
    else:
        print("❌ Please enter a valid number or 'done'.")

order.show_order()
Bill.generate(order)
