class ContactBook:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contacts

    def add_contact(self, name, phone):
        if name in self.contacts:
            print(f"⚠ Contact '{name}' already exists. Use update option.")
        else:
            self.contacts[name] = phone
            print(f"✅ Contact added: {name} → {phone}")

    def update_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            print(f"🔄 Contact updated: {name} → {phone}")
        else:
            print(f"❌ Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"🗑 Contact deleted: {name}")
        else:
            print(f"❌ Contact '{name}' not found.")

    def view_contacts(self):
        if not self.contacts:
            print("📭 No contacts available!")
        else:
            print("\n📒 Contact List:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")


# ------------------------
# Main Program
# ------------------------
book = ContactBook()

while True:
    print("\n1. Add Contact\n2. Update Contact\n3. Delete Contact\n4. View Contacts\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        book.add_contact(name, phone)

    elif choice == "2":
        name = input("Enter name to update: ")
        phone = input("Enter new phone: ")
        book.update_contact(name, phone)

    elif choice == "3":
        name = input("Enter name to delete: ")
        book.delete_contact(name)

    elif choice == "4":
        book.view_contacts()

    elif choice == "5":
        print("👋 Exiting Contact Book. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Try again.")
