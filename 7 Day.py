#1.Logging in Python

import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    number = int(input("Enter a number to divide 100: "))
    result = 100 / number
    print("Result:", result)
except Exception as e:
    logging.error("An error occurred: %s", e)
    print("An error occurred. Check errors.log file.")

#2.DateTime Manipulations

from datetime import datetime

date1_str = input("Enter first date (YYYY-MM-DD): ")
date2_str = input("Enter second date (YYYY-MM-DD): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

difference = abs((date2 - date1).days)

print(f"The difference between the two dates is {difference} days.")

#3.Inheritance & Method Overriding

# Parent Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def description(self):
        return f"{self.title} by {self.author}"

# Child Class 1
class Fiction(Book):
    def description(self):
        return f"Fiction Book: '{self.title}' by {self.author}"

# Child Class 2
class NonFiction(Book):
    def description(self):
        return f"Non-Fiction Book: '{self.title}' by {self.author} — based on real events."

# Using the classes
book1 = Fiction("The Hobbit", "J.R.R. Tolkien")
book2 = NonFiction("Sapiens", "Yuval Noah Harari")

print(book1.description())
print(book2.description())


