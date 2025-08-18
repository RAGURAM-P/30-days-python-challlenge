from datetime import datetime, timedelta

class Library:
    def __init__(self, fine_per_day=5):
        self.records = []
        self.fine_per_day = fine_per_day

    def borrow_book(self, book_title, borrower, borrow_days=7):
        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=borrow_days)
        self.records.append({
            "book": book_title,
            "borrower": borrower,
            "borrow_date": borrow_date,
            "due_date": due_date
        })
        print(f"📚 {book_title} borrowed by {borrower}")
        print(f"   Due on: {due_date.strftime('%Y-%m-%d')}")

    def return_book(self, book_title, borrower):
        for record in self.records:
            if record["book"] == book_title and record["borrower"] == borrower:
                return_date = datetime.now()
                overdue_days = (return_date - record["due_date"]).days

                if overdue_days > 0:
                    fine = overdue_days * self.fine_per_day
                    print(f"⚠️ Book returned late by {overdue_days} days!")
                    print(f"Fine to pay: ₹{fine}")
                else:
                    print("✅ Book returned on time. No fine.")
                
                self.records.remove(record)
                return
        print("❌ No record found for this book and borrower.")

    def list_borrowed_books(self):
        if not self.records:
            print("No books are currently borrowed.")
            return
        print("\n📖 Borrowed Books:")
        for record in self.records:
            print(f"- {record['book']} (by {record['borrower']}, Due: {record['due_date'].strftime('%Y-%m-%d')})")

library = Library(fine_per_day=10)

library.borrow_book("Python Basics", "Ragul", borrow_days=5)
library.borrow_book("AI Revolution", "Roshini", borrow_days=3)

library.list_borrowed_books()

print("\n--- Returning Book ---")
library.return_book("Python Basics", "Alice")
