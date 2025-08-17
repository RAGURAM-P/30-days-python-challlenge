import json
import os

# File to store inventory
FILE_NAME = "inventory.json"

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {"name": self.name, "quantity": self.quantity, "price": self.price}

class Inventory:
    def __init__(self):
        self.products = {}
        self.load_inventory()

    # Add new product
    def add_product(self, name, quantity, price):
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            self.products[name] = Product(name, quantity, price)
        self.save_inventory()
        print(f"✅ Added/Updated {name} ({quantity} units at ₹{price})")

    # Sell a product
    def sell_product(self, name, quantity):
        if name not in self.products:
            print(f"❌ {name} not found in inventory!")
            return
        if self.products[name].quantity < quantity:
            print(f"⚠️ Not enough stock for {name}. Available: {self.products[name].quantity}")
            return
        self.products[name].quantity -= quantity
        print(f"✅ Sold {quantity} of {name}. Remaining: {self.products[name].quantity}")
        self.save_inventory()

    # Show all products
    def show_inventory(self):
        if not self.products:
            print("⚠️ Inventory is empty.")
            return
        print("\n📦 Current Inventory:")
        for product in self.products.values():
            print(f"  {product.name} - {product.quantity} units @ ₹{product.price}")
        print()

    # Save inventory to file
    def save_inventory(self):
        data = {name: prod.to_dict() for name, prod in self.products.items()}
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    # Load inventory from file
    def load_inventory(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                data = json.load(f)
                for name, info in data.items():
                    self.products[name] = Product(info["name"], info["quantity"], info["price"])


# -----------------------------
# Demo Usage
# -----------------------------
inv = Inventory()

inv.add_product("Laptop", 10, 55000)
inv.add_product("Mouse", 50, 500)
inv.add_product("Keyboard", 20, 1500)

inv.sell_product("Mouse", 5)
inv.sell_product("Laptop", 2)

inv.show_inventory()
