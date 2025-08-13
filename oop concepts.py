#1.Bank Class

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")
        return f"Deposited ₹{amount}. Balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.history.append(f"Withdrew ₹{amount}")
        return f"Withdrew ₹{amount}. Balance: ₹{self.balance}"

    def show_history(self):
        return "\n".join(self.history)

acc = BankAccount("Raguram", 5000)
print(acc.deposit(1000))
print(acc.withdraw(3000))
print(acc.show_history())


#2.Book Class
print("Book Class")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # List to store Book objects
    
    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Added: {book}")
    
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"❌ Removed: {book}")
                return
        print(f"⚠️ Book '{title}' not found in the library.")
    
    def list_books(self):
        if not self.books:
            print("📂 No books available in the library.")
        else:
            print(f"📚 Books in {self.name}:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")


my_library = Library("City Central Library")

book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("Japanies", "Yuval Noah Harari")
book3 = Book("1984", "George Orwell")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.list_books()

my_library.remove_book("Sapiens")

my_library.list_books()

